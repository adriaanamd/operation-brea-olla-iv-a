from __future__ import annotations

import pandas as pd


def _distribution(values: pd.Series) -> dict:
    counts = values.value_counts().reindex(range(1, 6), fill_value=0)
    n = int(values.notna().sum())
    return {
        **{f"count_{score}": int(counts[score]) for score in range(1, 6)},
        **{f"pct_{score}": round(float(counts[score] / n * 100), 2) if n else 0.0 for score in range(1, 6)},
    }


def summarize_likert(frame: pd.DataFrame, columns: list[str], labels: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    distributions = []
    for order, (column, label) in enumerate(zip(columns, labels), start=1):
        values = frame[column].astype("Float64")
        nonmissing = values.dropna()
        row = {
            "item_order": order,
            "item_key": column,
            "item_label": label,
            "n": int(nonmissing.size),
            "mean": round(float(nonmissing.mean()), 4),
            "median": float(nonmissing.median()),
            "sd": round(float(nonmissing.std(ddof=1)), 4),
            "min": int(nonmissing.min()),
            "max": int(nonmissing.max()),
            "q1": float(nonmissing.quantile(0.25)),
            "q3": float(nonmissing.quantile(0.75)),
            "agree_n": int((nonmissing >= 4).sum()),
            "agree_pct": round(float((nonmissing >= 4).mean() * 100), 2),
        }
        rows.append(row)
        distributions.append({"item_key": column, "item_label": label, **_distribution(values)})
    return pd.DataFrame(rows), pd.DataFrame(distributions)


def summarize_single_items(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    rows = []
    for column in columns:
        values = frame[column].astype("Float64").dropna()
        rows.append(
            {
                "item_key": column,
                "n": int(values.size),
                "mean": round(float(values.mean()), 4),
                "median": float(values.median()),
                "sd": round(float(values.std(ddof=1)), 4),
                "min": int(values.min()),
                "max": int(values.max()),
                "agree_n": int((values >= 4).sum()),
                "agree_pct": round(float((values >= 4).mean() * 100), 2),
                **_distribution(values),
            }
        )
    return pd.DataFrame(rows)
