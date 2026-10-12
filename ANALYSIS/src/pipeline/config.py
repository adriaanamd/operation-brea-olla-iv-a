from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
ANALYSIS_ROOT = REPO_ROOT / "ANALYSIS"
DEFAULT_INPUT = ANALYSIS_ROOT / "data" / "CodeCrafters_ Tech Beyond the Screen – Day 1 Afternoon Session Evaluation.csv"
DEFAULT_OUTPUT = ANALYSIS_ROOT / "outputs"

# These indices are stable for the supplied export: timestamp, three consent
# fields, institution, 13 experience items, overall rating, satisfaction, and
# four open-ended fields. Headers are intentionally selected by position so
# trailing spaces and spreadsheet line breaks cannot change the mapping.
PRIMARY_ITEM_KEYS = [f"item_{i:02d}" for i in range(1, 14)]
PRIMARY_ITEM_LABELS = [
    "Session objectives were clearly presented",
    "Topics were relevant and informative",
    "Content was easy to understand",
    "Speakers explained the topics clearly",
    "Presentation materials were clear and organized",
    "Examples and discussions supported understanding",
    "Session was engaging and interactive",
    "Activities reinforced the topics",
    "Knowledge was useful for studies or everyday life",
    "Session encouraged critical thinking",
    "Session was well-organized",
    "Technical aspects were satisfactory",
    "Session met expectations",
]
PRIMARY_COLUMN_INDICES = list(range(5, 18))
SUMMARY_KEYS = ["overall_rating", "satisfaction"]
SUMMARY_COLUMN_INDICES = [18, 19]
TEXT_KEYS = ["learning_value", "liked_most", "improvements", "additional_comments"]
TEXT_COLUMN_INDICES = [20, 21, 22, 23]
ALL_RATING_KEYS = PRIMARY_ITEM_KEYS + SUMMARY_KEYS

THEME_CODEBOOK_PATH = ANALYSIS_ROOT / "src" / "themes" / "codebook.json"
THEME_DECISIONS_PATH = ANALYSIS_ROOT / "src" / "themes" / "coding_decisions.csv"
