from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .config import (
    DEFAULT_INPUT,
    DEFAULT_OUTPUT,
    PRIMARY_ITEM_KEYS,
    PRIMARY_ITEM_LABELS,
    SUMMARY_KEYS,
    THEME_CODEBOOK_PATH,
    THEME_DECISIONS_PATH,
)
from .io import build_rating_frame, build_text_frame, load_evaluation_csv
from .quality import flag_scale_direction_rows, normalize_rating_frame, validate_frame
from .reporting import (
    add_derived_plot_inputs,
    build_extended_tables,
    write_extended_figures,
    write_extended_tables,
)
from .summary import summarize_likert, summarize_single_items


def _ensure_dirs(output_dir: Path) -> dict[str, Path]:
    paths = {
        "tables": output_dir / "tables",
        "processed": output_dir / "processed",
        "figures": output_dir / "figures",
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def _theme_outputs(output_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    counts_path = output_dir / "tables" / "thematic_counts.csv"
    matrix_path = output_dir / "tables" / "mixed_methods_evidence_matrix.csv"
    if not THEME_DECISIONS_PATH.exists():
        empty = pd.DataFrame(columns=["code_id", "label", "n_assignments", "n_respondents"])
        empty.to_csv(counts_path, index=False)
        pd.DataFrame(columns=["evidence_stream", "measure", "value", "interpretive_boundary"]).to_csv(matrix_path, index=False)
        return empty, pd.DataFrame()

    decisions = pd.read_csv(THEME_DECISIONS_PATH)
    required = {"respondent_id", "source_field", "code_id", "coding_note"}
    missing = sorted(required.difference(decisions.columns))
    if missing:
        raise ValueError(f"Coding decisions are missing columns: {missing}")
    codebook = json.loads(THEME_CODEBOOK_PATH.read_text(encoding="utf-8"))
    labels = {row["code_id"]: row["label"] for row in codebook["codes"]}
    unknown_codes = sorted(set(decisions["code_id"]) - set(labels))
    if unknown_codes:
        raise ValueError(f"Coding decisions contain unknown code IDs: {unknown_codes}")
    counts = (
        decisions.groupby("code_id", as_index=False)
        .agg(n_assignments=("respondent_id", "size"), n_respondents=("respondent_id", "nunique"))
    )
    counts["label"] = counts["code_id"].map(labels).fillna("Unlisted code")
    counts = counts[["code_id", "label", "n_assignments", "n_respondents"]].sort_values(
        ["n_assignments", "code_id"], ascending=[False, True]
    )
    counts.to_csv(counts_path, index=False)
    return counts, decisions


def _write_evidence_matrix(
    output_dir: Path,
    item_summary: pd.DataFrame,
    single_summary: pd.DataFrame,
    theme_counts: pd.DataFrame,
) -> None:
    rows: list[dict] = []
    for row in item_summary.itertuples(index=False):
        rows.append(
            {
                "evidence_stream": "quantitative",
                "measure": "primary_likert_item_mean",
                "indicator": row.item_key,
                "value": row.mean,
                "denominator": row.n,
                "interpretive_boundary": "Post-event perception on a 1-5 response scale; not objective learning.",
            }
        )
    for row in single_summary.itertuples(index=False):
        rows.append(
            {
                "evidence_stream": "quantitative",
                "measure": row.item_key,
                "indicator": row.item_key,
                "value": row.mean,
                "denominator": row.n,
                "interpretive_boundary": "Single-item post-event perception; reported separately from the primary Likert set.",
            }
        )
    for row in theme_counts.itertuples(index=False):
        rows.append(
            {
                "evidence_stream": "qualitative",
                "measure": "coded_response_field_assignments",
                "indicator": row.code_id,
                "value": row.n_assignments,
                "denominator": row.n_respondents,
                "interpretive_boundary": "Analyst-coded reported feedback; frequency does not establish learning or generalizability.",
            }
        )
    pd.DataFrame(rows).to_csv(
        output_dir / "tables" / "mixed_methods_evidence_matrix.csv", index=False
    )


def _write_figures(summary: pd.DataFrame, distributions: pd.DataFrame, figure_dir: Path) -> None:
    sns.set_theme(style="whitegrid")
    means = summary.sort_values("mean")
    plt.figure(figsize=(10, 7))
    sns.barplot(data=means, x="mean", y="item_label", color="#2f6690")
    plt.xlim(1, 5)
    plt.xlabel("Mean normalized rating (1–5)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(figure_dir / "likert_item_means.png", dpi=180)
    plt.close()

    long = distributions.melt(
        id_vars=["item_key", "item_label"],
        value_vars=[f"pct_{score}" for score in range(1, 6)],
        var_name="rating",
        value_name="percent",
    )
    long["rating"] = long["rating"].str.replace("pct_", "", regex=False).astype(int)
    plt.figure(figsize=(11, 8))
    sns.barplot(data=long, x="percent", y="item_label", hue="rating", palette="viridis")
    plt.xlabel("Responses (%)")
    plt.ylabel("")
    plt.legend(title="Rating", ncol=5, loc="lower right")
    plt.tight_layout()
    plt.savefig(figure_dir / "likert_distribution.png", dpi=180)
    plt.close()


def run_analysis(input_path: Path = DEFAULT_INPUT, output_dir: Path = DEFAULT_OUTPUT) -> dict:
    paths = _ensure_dirs(output_dir)
    raw = load_evaluation_csv(input_path)
    ratings = build_rating_frame(raw)
    text = build_text_frame(raw)
    quality = validate_frame(raw, ratings)
    if quality["missing_analysis_columns"] or quality["invalid_rating_cells"] or quality["out_of_range_cells"]:
        raise ValueError(f"Input validation failed: {quality}")

    flags = flag_scale_direction_rows(ratings)
    flagged_ids = flags.loc[flags["flagged"], "respondent_id"].tolist()
    normalized, audit = normalize_rating_frame(ratings, flagged_ids)
    item_summary, distributions = summarize_likert(normalized, PRIMARY_ITEM_KEYS, PRIMARY_ITEM_LABELS)
    single_summary = summarize_single_items(normalized, SUMMARY_KEYS)

    normalized.to_csv(paths["processed"] / "normalized_ratings.csv", index=False)
    text.to_csv(paths["processed"] / "deidentified_text_for_coding.csv", index=False)
    flags.to_csv(paths["tables"] / "scale_direction_flags.csv", index=False)
    audit.to_csv(paths["tables"] / "normalization_audit.csv", index=False)
    item_summary.to_csv(paths["tables"] / "likert_item_summary.csv", index=False)
    distributions.to_csv(paths["tables"] / "likert_distributions.csv", index=False)
    single_summary.to_csv(paths["tables"] / "overall_satisfaction_summary.csv", index=False)
    pd.DataFrame([quality]).to_json(paths["tables"] / "data_quality_summary.json", orient="records", indent=2)
    pd.DataFrame([quality]).to_csv(paths["tables"] / "data_quality_summary.csv", index=False)
    theme_counts, theme_decisions = _theme_outputs(output_dir)
    _write_evidence_matrix(output_dir, item_summary, single_summary, theme_counts)
    extended_tables = build_extended_tables(
        raw,
        ratings,
        normalized,
        item_summary,
        distributions,
        single_summary,
        theme_counts,
        theme_decisions,
    )
    write_extended_tables(paths["tables"], extended_tables)
    extended_tables = add_derived_plot_inputs(extended_tables, normalized, distributions)
    write_extended_figures(extended_tables, paths["figures"])

    manifest = {
        "python": platform.python_version(),
        "pandas": pd.__version__,
        "input_file": str(input_path),
        "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
        "rows": int(len(raw)),
        "flagged_rows": len(flagged_ids),
        "flagged_respondent_ids": flagged_ids,
        "normalization_scope": "13 primary Likert items only; overall rating and satisfaction retained as anchors",
        "outputs": sorted(str(path.relative_to(output_dir)) for path in output_dir.rglob("*") if path.is_file()),
    }
    (output_dir / "analysis_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the webinar evaluation analysis pipeline.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    manifest = run_analysis(args.input, args.output_dir)
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
