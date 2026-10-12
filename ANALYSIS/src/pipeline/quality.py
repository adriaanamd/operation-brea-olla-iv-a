from __future__ import annotations

from typing import Iterable

import pandas as pd

from .config import PRIMARY_ITEM_KEYS, SUMMARY_KEYS


def validate_frame(raw: pd.DataFrame, ratings: pd.DataFrame) -> dict:
    required = set(["respondent_id", *PRIMARY_ITEM_KEYS, *SUMMARY_KEYS])
    missing_columns = sorted(required.difference(ratings.columns))
    rating_values = ratings[PRIMARY_ITEM_KEYS + SUMMARY_KEYS]
    invalid_cells = int(rating_values.isna().sum().sum())
    out_of_range = int(((rating_values < 1) | (rating_values > 5)).fillna(False).sum().sum())
    return {
        "rows": int(len(raw)),
        "raw_columns": int(len(raw.columns) - 1),
        "missing_analysis_columns": missing_columns,
        "invalid_rating_cells": invalid_cells,
        "out_of_range_cells": out_of_range,
    }


def flag_scale_direction_rows(ratings: pd.DataFrame) -> pd.DataFrame:
    primary = ratings[PRIMARY_ITEM_KEYS]
    summaries = ratings[SUMMARY_KEYS]
    all_primary_one = primary.eq(1).all(axis=1)
    summaries_high = summaries.ge(4).all(axis=1)
    flagged = all_primary_one & summaries_high
    return pd.DataFrame(
        {
            "respondent_id": ratings["respondent_id"],
            "all_primary_items_raw_one": all_primary_one,
            "summary_ratings_at_least_four": summaries_high,
            "flagged": flagged,
            "reason": flagged.map(
                lambda value: "Primary Likert scale direction appears reversed; summary ratings are positive"
                if value
                else ""
            ),
        }
    )


def normalize_rating_frame(
    ratings: pd.DataFrame, flagged_ids: Iterable[str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Reverse only primary Likert items; retain summary anchors unchanged."""
    normalized = ratings.copy()
    flagged_set = set(flagged_ids)
    audit_rows: list[dict] = []
    for respondent_id in flagged_set:
        mask = normalized["respondent_id"].eq(respondent_id)
        for key in PRIMARY_ITEM_KEYS:
            raw_value = normalized.loc[mask, key].iloc[0]
            new_value = 6 - int(raw_value)
            normalized.loc[mask, key] = new_value
            audit_rows.append(
                {
                    "respondent_id": respondent_id,
                    "field": key,
                    "raw_value": int(raw_value),
                    "normalized_value": new_value,
                    "reason": "Approved respondent-level Likert direction correction",
                }
            )
    return normalized, pd.DataFrame(audit_rows)
