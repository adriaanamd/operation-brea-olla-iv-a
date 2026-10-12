# Data analysis

## Quantitative analysis

The quantitative analysis was implemented in Python and is executed in Google Colab through `ANALYSIS/src/main.ipynb`. The pipeline uses pandas for tabular preparation and descriptive summaries and matplotlib/seaborn for figures. The input CSV remains read-only. The generated manifest records the Python version, pandas version, input-file hash, row count, flagged-row count, normalization scope, and output paths.

For the 13 primary Likert items, the pipeline reports the number of nonmissing responses, mean, median, sample standard deviation, minimum, maximum, first and third quartiles, and the number and percentage of responses at or above 4. Distribution tables report counts and percentages for each value from 1 to 5. Overall rating and satisfaction receive the same descriptive treatment in a separate table. The analysis is descriptive; no inferential test, reliability estimate, or causal model is used.

The scale-direction rule was specified before reporting the normalized results. A respondent was flagged only when all 13 primary items equaled raw `1` and both summary ratings were at least `4`. For a flagged row, each primary item was transformed as `normalized = 6 - raw`, changing the all-1 pattern to all-5 while preserving the summary fields. The field-level audit records the respondent ID, field, raw value, normalized value, and correction reason. This correction is a data-quality adjustment based on an internal response-pattern inconsistency; it is not evidence that the respondent actually learned more or less.

## Qualitative analysis

Open-ended answers were analyzed with the codebook in `ANALYSIS/src/themes/codebook.json`. The unit of analysis was one respondent answer to one prompt, and multiple codes were allowed when a response contained separate ideas. The codebook included learning themes (TDD/testing, AI use, and software development), valued session features (demonstration, explanation, practical relevance, speaker, and engagement), requested improvements (more examples, more interaction, technical quality, and more depth), a non-substantive-response code, and an other-feedback code.

The de-identified coding decisions are stored in `ANALYSIS/src/themes/coding_decisions.csv`, with no full response text or institution fields. The protocol identifies the coding as analyst-coded and records the absence of a second coder or inter-rater agreement estimate. Theme frequencies are therefore descriptive indicators of reported feedback, not measures of objective learning or generalizable opinion.

## Mixed-methods integration

The evidence matrix joins quantitative indicators and thematic codes at the level of interpretation. It places primary-item means and single-item summaries beside coded response-field counts and states the boundary for each evidence stream. Agreement between high ratings and positive comments is treated as convergence of reported experience. A mismatch is treated as a finding about measurement or response interpretation, not resolved by selecting whichever strand appears more favorable.
