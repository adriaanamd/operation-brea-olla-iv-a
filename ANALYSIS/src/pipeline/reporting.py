from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from .config import PRIMARY_ITEM_KEYS, PRIMARY_ITEM_LABELS, SUMMARY_KEYS, TEXT_KEYS


BOOTSTRAP_SEED = 20261012
BOOTSTRAP_REPS = 2000


def _wilson_interval(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total == 0:
        return 0.0, 0.0
    p = successes / total
    denominator = 1 + z**2 / total
    centre = (p + z**2 / (2 * total)) / denominator
    margin = z * np.sqrt((p * (1 - p) + z**2 / (4 * total)) / total) / denominator
    return (max(0.0, centre - margin) * 100, min(1.0, centre + margin) * 100)


def _bootstrap_mean_interval(values: pd.Series, rng: np.random.Generator) -> tuple[float, float]:
    numeric = pd.to_numeric(values, errors="coerce").dropna().to_numpy(dtype=float)
    if numeric.size < 2:
        mean = float(numeric.mean()) if numeric.size else np.nan
        return mean, mean
    sample = rng.choice(numeric, size=(BOOTSTRAP_REPS, numeric.size), replace=True).mean(axis=1)
    return tuple(np.quantile(sample, [0.025, 0.975]).tolist())


def _metric_rows(
    normalized: pd.DataFrame,
    columns: list[str],
    labels: list[str],
    source: str,
) -> pd.DataFrame:
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    rows: list[dict] = []
    for key, label in zip(columns, labels):
        values = pd.to_numeric(normalized[key], errors="coerce").dropna()
        n = int(values.size)
        agree_n = int((values >= 4).sum())
        top_box_n = int((values == 5).sum())
        mean_low, mean_high = _bootstrap_mean_interval(values, rng)
        agree_low, agree_high = _wilson_interval(agree_n, n)
        rows.append(
            {
                "source": source,
                "item_key": key,
                "item_label": label,
                "n": n,
                "mean": round(float(values.mean()), 4),
                "median": float(values.median()),
                "sd": round(float(values.std(ddof=1)), 4),
                "q1": round(float(values.quantile(0.25)), 4),
                "q3": round(float(values.quantile(0.75)), 4),
                "min": int(values.min()),
                "max": int(values.max()),
                "agree_n": agree_n,
                "agree_pct": round(agree_n / n * 100, 2),
                "agree_ci_low": round(agree_low, 2),
                "agree_ci_high": round(agree_high, 2),
                "top_box_n": top_box_n,
                "top_box_pct": round(top_box_n / n * 100, 2),
                "mean_ci_low": round(float(mean_low), 4),
                "mean_ci_high": round(float(mean_high), 4),
            }
        )
    return pd.DataFrame(rows)


def _composite_summary(normalized: pd.DataFrame) -> pd.DataFrame:
    composite = normalized[PRIMARY_ITEM_KEYS].astype(float).mean(axis=1)
    return pd.DataFrame(
        [
            {
                "metric": "13-item normalized experience composite",
                "n": int(composite.notna().sum()),
                "mean": round(float(composite.mean()), 4),
                "median": round(float(composite.median()), 4),
                "sd": round(float(composite.std(ddof=1)), 4),
                "min": round(float(composite.min()), 4),
                "max": round(float(composite.max()), 4),
                "agree_composite_pct": round(float((composite >= 4).mean() * 100), 2),
            }
        ]
    )


def _institution_summary(raw: pd.DataFrame) -> pd.DataFrame:
    # The institution field is the fifth source column; respondent_id was inserted at 0.
    institution = raw.iloc[:, 5].fillna("Unspecified/NA").astype(str).str.strip()
    institution = institution.replace({"": "Unspecified/NA", "nan": "Unspecified/NA"})
    counts = institution.value_counts(dropna=False).rename_axis("institution").reset_index(name="n")
    counts["pct"] = (counts["n"] / len(institution) * 100).round(2)
    return counts


def _speaker_tables(normalized: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    cross = pd.crosstab(normalized["item_04"], normalized["overall_rating"]).reindex(
        index=range(1, 6), columns=range(1, 6), fill_value=0
    )
    clarity_labels = {1: "1 - Strongly disagree", 2: "2", 3: "3", 4: "4", 5: "5 - Strongly agree"}
    cross.index = [clarity_labels[i] for i in cross.index]
    cross.index.name = None
    summary = (
        normalized.groupby("item_04", dropna=False)
        .agg(
            n=("overall_rating", "size"),
            mean_overall=("overall_rating", "mean"),
            top_box_n=("overall_rating", lambda values: int((values == 5).sum())),
        )
        .reset_index()
    )
    summary["top_box_pct"] = (summary["top_box_n"] / summary["n"] * 100).round(2)
    summary["clarity_label"] = summary["item_04"].map(clarity_labels)
    rho = normalized[["item_04", "overall_rating"]].corr(method="spearman").iloc[0, 1]
    association = pd.DataFrame(
        [
            {
                "comparison": "speaker clarity vs overall rating",
                "n": int(len(normalized)),
                "spearman_rho": round(float(rho), 4),
                "interpretation": "Descriptive ordinal association; not causal.",
            }
        ]
    )
    return cross, summary, association


def _theme_tables(theme_counts: pd.DataFrame, decisions: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, pd.DataFrame]]:
    if theme_counts.empty or decisions.empty:
        empty = pd.DataFrame(columns=["source_field", "code_id", "label", "n_assignments"])
        return theme_counts.copy(), {"wide": empty, "long": empty}
    extended = theme_counts.copy()
    respondents = decisions["respondent_id"].nunique()
    assignments = len(decisions)
    extended["respondent_coverage_pct"] = (extended["n_respondents"] / respondents * 100).round(2)
    extended["assignment_share_pct"] = (extended["n_assignments"] / assignments * 100).round(2)
    by_prompt = pd.crosstab(decisions["source_field"], decisions["code_id"])
    by_prompt = by_prompt.reindex(sorted(by_prompt.columns), axis=1)
    labels = extended[["code_id", "label"]].drop_duplicates()
    long = decisions.groupby(["source_field", "code_id"], as_index=False).size().rename(columns={"size": "n_assignments"})
    long = long.merge(labels, on="code_id", how="left")
    return extended, {"wide": by_prompt, "long": long[["source_field", "code_id", "label", "n_assignments"]]}


def build_extended_tables(
    raw: pd.DataFrame,
    ratings: pd.DataFrame,
    normalized: pd.DataFrame,
    item_summary: pd.DataFrame,
    distributions: pd.DataFrame,
    single_summary: pd.DataFrame,
    theme_counts: pd.DataFrame,
    theme_decisions: pd.DataFrame,
) -> dict[str, pd.DataFrame]:
    del item_summary, distributions, single_summary
    labels = PRIMARY_ITEM_LABELS + ["Overall Rating", "Satisfaction"]
    metrics = _metric_rows(normalized, PRIMARY_ITEM_KEYS + SUMMARY_KEYS, labels, "normalized ratings")
    composite = _composite_summary(normalized)
    institutions = _institution_summary(raw)
    speaker_cross, speaker_summary, association = _speaker_tables(normalized)
    themes, theme_by_prompt = _theme_tables(theme_counts, theme_decisions)
    raw_means = ratings[PRIMARY_ITEM_KEYS].astype(float).mean()
    normalized_means = normalized[PRIMARY_ITEM_KEYS].astype(float).mean()
    sensitivity = pd.DataFrame(
        {
            "item_key": PRIMARY_ITEM_KEYS,
            "item_label": PRIMARY_ITEM_LABELS,
            "raw_mean": [raw_means[key] for key in PRIMARY_ITEM_KEYS],
            "normalized_mean": [normalized_means[key] for key in PRIMARY_ITEM_KEYS],
        }
    )
    sensitivity["mean_change"] = sensitivity["normalized_mean"] - sensitivity["raw_mean"]
    sensitivity = sensitivity.round(4)
    return {
        "quantitative_metrics": metrics,
        "composite_summary": composite,
        "institution_summary": institutions,
        "speaker_cross": speaker_cross,
        "speaker_summary": speaker_summary,
        "association_summary": association,
        "theme_counts": themes,
        "theme_by_prompt": theme_by_prompt["wide"],
        "theme_by_prompt_long": theme_by_prompt["long"],
        "normalization_sensitivity": sensitivity,
        "composite_values": pd.DataFrame({"composite": normalized[PRIMARY_ITEM_KEYS].astype(float).mean(axis=1)}),
    }


def write_extended_tables(tables_dir: Path, tables: dict[str, pd.DataFrame]) -> None:
    filenames = {
        "quantitative_metrics": "crispdm_quantitative_metrics.csv",
        "composite_summary": "crispdm_composite_summary.csv",
        "institution_summary": "crispdm_institution_summary.csv",
        "speaker_cross": "crispdm_speaker_clarity_overall_crosstab.csv",
        "speaker_summary": "crispdm_speaker_clarity_overall_summary.csv",
        "association_summary": "crispdm_association_summary.csv",
        "theme_counts": "crispdm_theme_counts_with_denominators.csv",
        "theme_by_prompt": "crispdm_theme_by_prompt.csv",
        "normalization_sensitivity": "crispdm_normalization_sensitivity.csv",
    }
    for key, filename in filenames.items():
        if key == "quantitative_metrics":
            frame = tables[key].rename(
                columns={
                    "source": "stream",
                    "agree_n": "agree_n_4_or_5",
                    "agree_pct": "agree_pct_4_or_5",
                    "agree_ci_low": "agree_ci95_low",
                    "agree_ci_high": "agree_ci95_high",
                    "top_box_n": "top_box_n_5",
                    "top_box_pct": "top_box_pct_5",
                    "mean_ci_low": "mean_bootstrap_ci95_low",
                    "mean_ci_high": "mean_bootstrap_ci95_high",
                }
            ).copy()
            frame["stream"] = frame["stream"].replace({"normalized ratings": "primary_likert"})
            frame.loc[frame["item_key"].isin(SUMMARY_KEYS), "stream"] = "summary_rating"
            frame = frame.drop(columns=["q1", "q3"], errors="ignore")
            frame = frame[["stream", "item_key", "item_label", "n", "mean", "median", "sd", "min", "max", "agree_n_4_or_5", "agree_pct_4_or_5", "agree_ci95_low", "agree_ci95_high", "top_box_n_5", "top_box_pct_5", "mean_bootstrap_ci95_low", "mean_bootstrap_ci95_high"]]
        elif key == "theme_by_prompt":
            frame = tables[key]
            frame.to_csv(tables_dir / filename)
            continue
        elif key == "speaker_cross":
            frame = tables[key]
            frame.to_csv(tables_dir / filename)
            continue
        elif key == "normalization_sensitivity":
            frame = tables[key][["item_key", "raw_mean", "normalized_mean", "mean_change"]]
        else:
            frame = tables[key]
        frame.to_csv(tables_dir / filename, index=False)


def _save(fig: plt.Figure, figure_dir: Path, filename: str) -> None:
    fig.tight_layout()
    fig.savefig(figure_dir / filename, dpi=180, bbox_inches="tight")
    plt.close(fig)


def write_extended_figures(tables: dict[str, pd.DataFrame], figure_dir: Path) -> None:
    sns.set_theme(style="whitegrid", context="notebook")
    metrics = tables["quantitative_metrics"]
    primary = metrics[metrics["item_key"].isin(PRIMARY_ITEM_KEYS)].copy()
    primary = primary.sort_values("mean")

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.errorbar(primary["mean"], primary["item_label"], xerr=[primary["mean"] - primary["mean_ci_low"], primary["mean_ci_high"] - primary["mean"]], fmt="o", color="#2f6690", ecolor="#8fb8d4", capsize=3)
    ax.set_xlim(1, 5)
    ax.set_xlabel("Mean normalized rating (1-5), with 95% bootstrap interval")
    ax.set_ylabel("")
    _save(fig, figure_dir, "likert_item_means.png")

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.hlines(primary["item_label"], primary["q1"] if "q1" in primary else primary["mean"], primary["q3"] if "q3" in primary else primary["mean"], color="#8fb8d4")
    ax.scatter(primary["mean"], primary["item_label"], color="#2f6690", zorder=3)
    ax.set_xlim(1, 5)
    ax.set_xlabel("Mean normalized rating (1-5); point with interquartile range")
    ax.set_ylabel("")
    _save(fig, figure_dir, "likert_item_means_iqr.png")

    dist = tables["distributions"].copy() if "distributions" in tables else None
    if dist is not None:
        long = dist.melt(id_vars=["item_key", "item_label"], value_vars=[f"pct_{i}" for i in range(1, 6)], var_name="rating", value_name="percent")
        long["rating"] = long["rating"].str.replace("pct_", "", regex=False).astype(int)
        pivot = long.pivot(index="item_label", columns="rating", values="percent").reindex(primary["item_label"])
        fig, ax = plt.subplots(figsize=(11, 8))
        pivot.plot.barh(stacked=True, ax=ax, colormap="viridis", width=0.8)
        ax.set_xlabel("Responses (%)")
        ax.set_ylabel("")
        ax.legend(title="Rating", ncol=5, loc="lower right")
        _save(fig, figure_dir, "likert_distribution.png")

    summary = metrics[metrics["item_key"].isin(SUMMARY_KEYS)].copy()
    summary["item_label"] = summary["item_key"].map({"overall_rating": "Overall session rating", "satisfaction": "Overall satisfaction"})
    fig, ax = plt.subplots(figsize=(9, 4))
    summary_plot = summary.set_index("item_label")[[f"{col}_{score}" for col in ("count",) for score in range(1, 6)]] if all(f"count_{score}" in summary for score in range(1, 6)) else None
    if summary_plot is None:
        # Counts are derived from the corresponding normalized rows for the two summary items.
        values = tables["summary_values"]
        summary_plot = values.groupby("item_label")["rating"].value_counts().unstack(fill_value=0).reindex(columns=range(1, 6), fill_value=0)
    summary_plot.div(summary_plot.sum(axis=1), axis=0).mul(100).plot.barh(stacked=True, ax=ax, colormap="viridis")
    ax.set_xlabel("Responses (%)")
    ax.set_ylabel("")
    ax.legend(title="Rating", ncol=5, loc="lower right")
    _save(fig, figure_dir, "summary_rating_distribution.png")

    composite = tables["composite_values"]["composite"].dropna()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(composite, bins=np.arange(2.75, 5.26, 0.25), color="#2f6690", edgecolor="white")
    ax.axvline(composite.mean(), color="#d1495b", linestyle="--", label=f"Mean = {composite.mean():.2f}")
    ax.axvline(composite.median(), color="#edae49", linestyle=":", label=f"Median = {composite.median():.2f}")
    ax.set_xlabel("Respondent-level normalized 13-item mean")
    ax.set_ylabel("Respondents")
    ax.legend()
    _save(fig, figure_dir, "composite_distribution.png")

    cross = tables["speaker_cross"].copy()
    if "speaker_clarity" in cross.columns:
        cross = cross.set_index("speaker_clarity")
    cross = cross.reindex(columns=range(1, 6), fill_value=0)
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(cross, annot=True, fmt="g", cmap="Blues", cbar=False, ax=ax)
    ax.set_xlabel("Overall session rating")
    ax.set_ylabel("Speaker clarity rating")
    _save(fig, figure_dir, "speaker_clarity_overall_heatmap.png")

    institutions = tables["institution_summary"].sort_values("n")
    fig, ax = plt.subplots(figsize=(10, max(5, len(institutions) * 0.35)))
    ax.barh(institutions["institution"], institutions["n"], color="#4c956c")
    ax.set_xlabel("Respondents")
    ax.set_ylabel("")
    _save(fig, figure_dir, "institution_profile.png")

    themes = tables["theme_counts"]
    themes = themes[themes["code_id"] != "NO_SUBSTANTIVE_RESPONSE"].sort_values("n_assignments")
    if not themes.empty:
        fig, ax = plt.subplots(figsize=(10, max(5, len(themes) * 0.35)))
        ax.barh(themes["label"], themes["n_assignments"], color="#6c5b7b")
        ax.set_xlabel("Coded assignments")
        ax.set_ylabel("")
        _save(fig, figure_dir, "theme_assignments.png")

        prompt = tables["theme_by_prompt_long"]
        prompt = prompt[prompt["code_id"] != "NO_SUBSTANTIVE_RESPONSE"]
        matrix = prompt.pivot_table(index="label", columns="source_field", values="n_assignments", fill_value=0)
        fig, ax = plt.subplots(figsize=(9, max(5, len(matrix) * 0.35)))
        sns.heatmap(matrix, annot=True, fmt="g", cmap="Purples", cbar=False, ax=ax)
        ax.set_xlabel("Open-ended prompt")
        ax.set_ylabel("")
        _save(fig, figure_dir, "theme_by_prompt_heatmap.png")

    sensitivity = tables["normalization_sensitivity"].sort_values("mean_change")
    fig, ax = plt.subplots(figsize=(10, 7))
    y = np.arange(len(sensitivity))
    ax.scatter(sensitivity["raw_mean"], y, label="Raw mean", color="#999999")
    ax.scatter(sensitivity["normalized_mean"], y, label="Normalized mean", color="#2f6690")
    for raw_mean, normalized_mean, yy in zip(sensitivity["raw_mean"], sensitivity["normalized_mean"], y):
        ax.plot([raw_mean, normalized_mean], [yy, yy], color="#d1495b", linewidth=1)
    ax.set_yticks(y, sensitivity["item_label"])
    ax.set_xlim(1, 5)
    ax.set_xlabel("Mean rating (1-5)")
    ax.set_ylabel("")
    ax.legend()
    _save(fig, figure_dir, "normalization_sensitivity.png")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(primary["agree_pct"], primary["top_box_pct"], color="#2f6690")
    for row in primary.itertuples(index=False):
        ax.annotate(row.item_key.replace("item_", ""), (row.agree_pct, row.top_box_pct), xytext=(4, 3), textcoords="offset points", fontsize=8)
    ax.set_xlabel("Agreement (ratings 4-5), %")
    ax.set_ylabel("Top-box (rating 5), %")
    ax.set_xlim(85, 101)
    ax.set_ylim(0, 101)
    _save(fig, figure_dir, "agreement_topbox_scatter.png")


def add_derived_plot_inputs(
    tables: dict[str, pd.DataFrame], normalized: pd.DataFrame, distributions: pd.DataFrame
) -> dict[str, pd.DataFrame]:
    tables = dict(tables)
    tables["distributions"] = distributions
    tables["summary_values"] = pd.concat(
        [
            normalized[["overall_rating"]].rename(columns={"overall_rating": "rating"}).assign(item_label="Overall session rating"),
            normalized[["satisfaction"]].rename(columns={"satisfaction": "rating"}).assign(item_label="Overall satisfaction"),
        ],
        ignore_index=True,
    )
    return tables
