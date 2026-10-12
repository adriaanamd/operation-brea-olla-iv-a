from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from .config import (
    PRIMARY_COLUMN_INDICES,
    PRIMARY_ITEM_KEYS,
    SUMMARY_COLUMN_INDICES,
    SUMMARY_KEYS,
    TEXT_COLUMN_INDICES,
    TEXT_KEYS,
)


def load_evaluation_csv(path: Path) -> pd.DataFrame:
    """Load the raw export without modifying or overwriting it."""
    frame = pd.read_csv(path, encoding="utf-8")
    frame.insert(0, "respondent_id", [f"R{i:03d}" for i in range(1, len(frame) + 1)])
    return frame


def extract_rating(value: object) -> int | pd.NA:
    """Parse the first valid 1–5 rating from a spreadsheet cell."""
    if pd.isna(value):
        return pd.NA
    if isinstance(value, (int, float)) and float(value).is_integer() and 1 <= int(value) <= 5:
        return int(value)
    match = re.search(r"(?<!\d)([1-5])(?!\d)", str(value))
    return int(match.group(1)) if match else pd.NA


def _parsed_series(frame: pd.DataFrame, source_index: int) -> pd.Series:
    return frame.iloc[:, source_index + 1].map(extract_rating).astype("Int64")


def build_rating_frame(raw: pd.DataFrame) -> pd.DataFrame:
    """Create stable analysis names for the 13 items and two summaries."""
    result = pd.DataFrame({"respondent_id": raw["respondent_id"]})
    for key, source_index in zip(PRIMARY_ITEM_KEYS, PRIMARY_COLUMN_INDICES):
        result[key] = _parsed_series(raw, source_index)
    for key, source_index in zip(SUMMARY_KEYS, SUMMARY_COLUMN_INDICES):
        result[key] = _parsed_series(raw, source_index)
    return result


def build_text_frame(raw: pd.DataFrame) -> pd.DataFrame:
    """Extract open-ended fields with stable names and de-identified row IDs."""
    result = pd.DataFrame({"respondent_id": raw["respondent_id"]})
    for key, source_index in zip(TEXT_KEYS, TEXT_COLUMN_INDICES):
        result[key] = raw.iloc[:, source_index + 1].fillna("").astype(str).str.strip()
    return result
