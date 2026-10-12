# IMRADC Methods and Results Design

> **For agentic workers:** This design governs the Chapter 2 methodology and Chapter 3 results/discussion work. Use the project `AGENTS.md`, `INSTRUCTIONS.md`, and `MANUSCRIPT-SPECS.md` as higher-level repository instructions.

**Goal:** Complete the manuscript's methodology and results/discussion sections as a bounded convergent mixed-methods evaluation of the webinar, using the desensitized evaluation CSV and reproducible Python/Colab artifacts.

**Architecture:** Chapter 2 will document the methods: descriptive post-activity evaluation design, participants and sampling, instrument, data collection, quantitative normalization, thematic coding, integration, and ethics. Chapter 3 will report the normalized Likert results and thematic findings before integrating them into a cautious discussion. Raw data remain read-only; analysis outputs are generated under `ANALYSIS/`.

**Tech Stack:** Python 3, pandas, NumPy, SciPy where justified, matplotlib/seaborn, Jupyter/Google Colab, Markdown, and the existing CSV.

## Global Constraints

- Use the IMRADC chapter routing: Chapter 1 is the introduction/background; Chapter 2 is methodology; Chapter 3 is results and discussion.
- Treat the study as a convergent mixed-methods, nonexperimental, post-activity evaluation of one webinar.
- Use the 13 experience statements as the primary Likert item set; report overall rating and satisfaction separately.
- Preserve the raw CSV and create a separate normalized analysis copy.
- Reverse-normalize the two internally inconsistent respondent rows with `normalized = 6 - raw` for applicable 1–5 rating fields; preserve an audit record.
- Analyze open-ended responses thematically without treating theme frequency as proof of learning or generalizable opinion.
- Do not claim causal learning effects, objective competence, psychometric validation, or representative sampling from this dataset.
- Keep unresolved event details as `[TO VERIFY: ...]` and do not infer them from the CSV.
- Use `ANALYSIS/src/pipeline/` for reusable analysis modules and `ANALYSIS/src/themes/` for the thematic codebook and coding assets.

## Data flow

```text
ANALYSIS/data/raw CSV (read-only)
        ↓
ANALYSIS/src/pipeline/ load → validate → flag → normalize
        ↓                         ↘
ANALYSIS/outputs/tables/           ANALYSIS/src/themes/ codebook + coding table
ANALYSIS/outputs/figures/          ↘
        ↓                           mixed-methods evidence matrix
CHAPTER 3 results and discussion ← CHAPTER 2 method definitions
```

The pipeline will record input path, row and column counts, rating fields, excluded or unresolved values, normalization decisions, package versions, and output filenames. The themed coding table will use de-identified response identifiers and permit multiple codes per response.

## Methods design

Chapter 2 will contain separate files for research design, locale/context, participants/sampling, instruments, data-gathering procedure, data analysis, and ethical considerations. It will state that all 52 rows are treated as available evaluation responses for this bounded analysis, while the relationship between respondents and the full attendance population remains unresolved unless another artifact is supplied.

The quantitative method will define the Likert scale, valid range, respondent-level normalization, item-level descriptive statistics, separate single-item summaries, and missing/invalid-value handling. No inferential test is planned because there is no comparison group, pretest, posttest, or independent outcome measure.

The qualitative method will use an analyst-coded codebook for learning value, valued session features, clarity, demonstrations, TDD/testing, AI use, engagement, technical issues, requests for improvement, and non-substantive responses. Coding decisions will be stored separately from raw text, and manuscript quotations will be avoided or paraphrased to reduce identification risk.

## Results and discussion design

Chapter 3 will first present data quality and normalization, then the 13-item Likert distributions, separate overall-rating and satisfaction summaries, thematic findings, and an integration matrix. Discussion paragraphs will distinguish observed results from interpretation and implication. Positive ratings will be described as participant-reported experience, not as evidence that the webinar caused learning.

## Verification gates

- Run the pipeline from a clean working directory using relative paths.
- Confirm the raw CSV checksum is unchanged after analysis.
- Confirm exactly two respondent rows are flagged for the approved scale-direction correction, unless validation finds otherwise.
- Confirm normalized values remain within 1–5 and the audit maps raw to normalized values.
- Confirm every numeric value in Chapter 3 appears in a generated table or figure.
- Confirm thematic counts match the saved coding table.
- Run Markdown, citation, reference, and cross-chapter consistency checks before completion.

