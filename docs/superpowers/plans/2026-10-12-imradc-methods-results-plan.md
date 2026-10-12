# IMRADC Methods and Results Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (\`- [ ]\`) syntax for tracking.

**Goal:** Complete Chapter 2 methodology and Chapter 3 results/discussion for a bounded convergent mixed-methods evaluation of the webinar.

**Architecture:** Chapter 2 documents the design, respondents, instrument, procedures, analysis, and ethics. A Python pipeline under \`ANALYSIS/src/pipeline/\` validates, normalizes, summarizes, and exports the Likert data. The codebook and de-identified thematic decisions live under \`ANALYSIS/src/themes/\`. Chapter 3 consumes only generated outputs and verified manuscript evidence.

**Tech Stack:** Python 3, pandas, NumPy, matplotlib, seaborn, Jupyter/Google Colab, JSON/CSV/Markdown, and PowerShell verification.

## Global Constraints

- Use IMRADC routing: Chapter 1 is introduction/background, Chapter 2 is methodology, and Chapter 3 is results and discussion.
- Treat the study as a convergent mixed-methods, nonexperimental, post-activity evaluation of one webinar.
- Use the 13 experience statements as the primary Likert item set; report overall rating and satisfaction separately.
- Preserve the raw CSV; write normalized and de-identified outputs separately.
- Reverse-normalize the two internally inconsistent respondent rows with \`normalized = 6 - raw\` for applicable 1–5 rating fields and preserve an audit record.
- Analyze open-ended responses thematically without treating theme frequency as proof of learning or generalizable opinion.
- Do not claim causal learning effects, objective competence, psychometric validation, or representative sampling.
- Keep unresolved event details as \`[TO VERIFY: ...]\`.
- Use \`ANALYSIS/src/pipeline/\` for reusable analysis code and \`ANALYSIS/src/themes/\` for thematic assets.

---

### Task 1: Align the repository contracts with IMRADC

**Files:**
- Modify: \`AGENTS.md\`
- Modify: \`INSTRUCTIONS.md\`
- Modify: \`MANUSCRIPT-SPECS.md\`
- Test: PowerShell routing checks

**Interfaces:**
- Consumes: \`docs/superpowers/specs/2026-10-12-imradc-methods-results-design.md\`
- Produces: consistent Chapter 2 methodology and Chapter 3 results/discussion rules

- [ ] **Step 1: Update chapter maps and analysis boundaries**

Replace outdated Chapter 2 literature-review and Chapter 3 methodology routing with the approved IMRADC structure. Preserve Chapter 1 and make Chapter 3 the only chapter that reports generated numeric results.

- [ ] **Step 2: Verify the contract**

Run:

\`\`\`powershell
rg -n "Chapter 2|Chapter 3|Methodology|Results and Discussion|Python is mandatory" AGENTS.md INSTRUCTIONS.md MANUSCRIPT-SPECS.md
\`\`\`

Expected: all three files route Chapter 2 to methodology, Chapter 3 to results/discussion, and Python to reproducible numeric work.

- [ ] **Step 3: Commit**

\`\`\`powershell
git add AGENTS.md INSTRUCTIONS.md MANUSCRIPT-SPECS.md
git commit -m "docs: align manuscript instructions with IMRADC chapters"
\`\`\`

### Task 2: Build the pipeline and data contract

**Files:**
- Create: \`ANALYSIS/README.md\`
- Create: \`ANALYSIS/requirements.txt\`
- Create: \`ANALYSIS/src/__init__.py\`
- Create: \`ANALYSIS/src/pipeline/__init__.py\`
- Create: \`ANALYSIS/src/pipeline/config.py\`
- Create: \`ANALYSIS/src/pipeline/io.py\`
- Create: \`ANALYSIS/src/pipeline/quality.py\`
- Create: \`ANALYSIS/src/pipeline/summary.py\`
- Create: \`ANALYSIS/src/pipeline/run_analysis.py\`
- Create: \`ANALYSIS/src/themes/README.md\`
- Create: \`ANALYSIS/src/themes/codebook.json\`
- Test: pipeline help and unit-level invariants

**Interfaces:**
- \`io.py\`: \`load_evaluation_csv(path: Path) -> pandas.DataFrame\`, \`extract_rating(value: object) -> int | pandas.NA\`.
- \`quality.py\`: \`validate_frame(df) -> dict\`, \`flag_scale_direction_rows(df, primary_columns, summary_columns) -> pandas.DataFrame\`, \`normalize_rating_frame(df, columns, flagged_ids) -> tuple[pandas.DataFrame, pandas.DataFrame]\`.
- \`summary.py\`: \`summarize_likert(df, columns) -> pandas.DataFrame\`, \`summarize_single_items(df, columns) -> pandas.DataFrame\`.
- \`run_analysis.py\`: CLI that writes only to \`ANALYSIS/outputs/\`.

- [ ] **Step 1: Add dependencies and package files**

Use \`pandas>=2.1,<3\`, \`numpy>=1.26,<3\`, \`matplotlib>=3.8,<4\`, \`seaborn>=0.13,<1\`, \`jupyter>=1.0,<2\`, and \`nbformat>=5.9,<6\`.

- [ ] **Step 2: Define exact CSV columns**

Store the exact 13 primary Likert headers, the overall-rating header, the satisfaction header, and the four open-ended headers in \`config.py\`. Exclude consent, institution, timestamp, and attendance-link fields from numeric analysis.

- [ ] **Step 3: Implement loading and parsing**

Load UTF-8 CSV text, preserve the raw frame in memory, add stable row-order IDs \`R001\`–\`R052\`, and parse leading 1–5 integers from values such as \`5 – Strongly Agree\`.

- [ ] **Step 4: Implement validation and normalization**

Validate required headers, row count, missingness, and rating range. Flag a respondent only when all 13 primary items are raw 1 and both summary ratings are at least 4. Apply \`6 - raw\` to applicable numeric rating fields and write a field-level normalization audit.

- [ ] **Step 5: Implement output tables and figures**

Write:

\`\`\`text
ANALYSIS/outputs/tables/data_quality_summary.csv
ANALYSIS/outputs/tables/normalization_audit.csv
ANALYSIS/outputs/tables/likert_item_summary.csv
ANALYSIS/outputs/tables/likert_distributions.csv
ANALYSIS/outputs/tables/overall_satisfaction_summary.csv
ANALYSIS/outputs/tables/thematic_counts.csv
ANALYSIS/outputs/tables/mixed_methods_evidence_matrix.csv
ANALYSIS/outputs/processed/normalized_ratings.csv
ANALYSIS/outputs/processed/deidentified_text_for_coding.csv
ANALYSIS/outputs/figures/likert_item_means.png
ANALYSIS/outputs/figures/likert_distribution.png
ANALYSIS/outputs/analysis_manifest.json
\`\`\`

- [ ] **Step 6: Run the smoke test**

\`\`\`powershell
python -m ANALYSIS.src.pipeline.run_analysis --help
\`\`\`

Expected: exit code 0 and help text with relative input/output arguments.

- [ ] **Step 7: Commit**

\`\`\`powershell
git add ANALYSIS/README.md ANALYSIS/requirements.txt ANALYSIS/src
git commit -m "feat: add reproducible webinar analysis pipeline"
\`\`\`

### Task 3: Complete thematic coding and mixed-methods integration

**Files:**
- Create: \`ANALYSIS/src/themes/coding_decisions.csv\`
- Create: \`ANALYSIS/src/themes/coding_protocol.md\`
- Modify: \`ANALYSIS/src/themes/codebook.json\`
- Modify: \`ANALYSIS/src/pipeline/run_analysis.py\`
- Test: coding/count consistency

**Interfaces:**
- Consumes: \`deidentified_text_for_coding.csv\`.
- Produces: de-identified response-field/code assignments and thematic counts consumed by Chapter 3.

- [ ] **Step 1: Define the codebook**

Use these IDs: \`LEARNING_TDD_TESTING\`, \`LEARNING_AI_USE\`, \`LEARNING_SOFTWARE_DEVELOPMENT\`, \`VALUED_DEMONSTRATION\`, \`VALUED_EXPLANATION\`, \`VALUED_PRACTICALITY\`, \`VALUED_SPEAKER\`, \`ENGAGEMENT_INTERACTIVITY\`, \`IMPROVEMENT_MORE_EXAMPLES\`, \`IMPROVEMENT_MORE_INTERACTION\`, \`IMPROVEMENT_TECHNICAL_QUALITY\`, \`IMPROVEMENT_MORE_DEPTH\`, \`NO_SUBSTANTIVE_RESPONSE\`, and \`OTHER_RELEVANT_FEEDBACK\`.

- [ ] **Step 2: Record decisions**

Create one row per coded response-field with \`respondent_id\`, \`source_field\`, \`code_id\`, and \`coding_note\`. Do not copy institutions, timestamps, links, or full participant text into the coding table.

- [ ] **Step 3: Document the protocol**

State the unit of analysis, multiple-code rule, treatment of “none/N/A”, analyst-coded status, de-identification rule, and the boundary that theme counts represent reported response patterns rather than learning outcomes.

- [ ] **Step 4: Verify coding**

\`\`\`powershell
python -c "import pandas as pd; c=pd.read_csv('ANALYSIS/src/themes/coding_decisions.csv'); assert c['respondent_id'].nunique() <= 52; assert c['code_id'].notna().all(); print('coding rows:', len(c), 'codes:', c['code_id'].nunique())"
\`\`\`

Expected: exit code 0 with no missing code IDs.

- [ ] **Step 5: Commit**

\`\`\`powershell
git add ANALYSIS/src/themes ANALYSIS/src/pipeline/run_analysis.py
git commit -m "feat: add thematic coding and mixed-methods outputs"
\`\`\`

### Task 4: Add the Colab notebook and execute the analysis

**Files:**
- Modify: \`ANALYSIS/src/main.ipynb\`
- Modify: \`ANALYSIS/README.md\`
- Create: \`ANALYSIS/logs/analysis_run.log\`
- Test: CLI execution and notebook execution when Jupyter is available

**Interfaces:**
- Consumes: pipeline CLI and thematic assets.
- Produces: a Colab-compatible notebook with environment, path, execution, output inspection, and limitations cells.

- [ ] **Step 1: Create notebook cells**

Include environment display, Colab installation guidance, relative path setup, pipeline execution, table/figure inspection, and limitations. Do not embed raw participant text.

- [ ] **Step 2: Run the CLI pipeline**

\`\`\`powershell
python -m ANALYSIS.src.pipeline.run_analysis --input "ANALYSIS/data/CodeCrafters_ Tech Beyond the Screen – Day 1 Afternoon Session Evaluation.csv" --output-dir ANALYSIS/outputs
\`\`\`

Expected: exit code 0, exactly two flagged respondents, normalized values in 1–5, and all listed outputs created.

- [ ] **Step 3: Execute the notebook if supported**

\`\`\`powershell
python -m jupyter nbconvert --to notebook --execute ANALYSIS/src/main.ipynb --output ANALYSIS/src/main.executed.ipynb --ExecutePreprocessor.timeout=120
\`\`\`

If Jupyter is unavailable, record that limitation and verify the CLI path instead.

- [ ] **Step 4: Commit**

\`\`\`powershell
git add ANALYSIS/src/main.ipynb ANALYSIS/README.md ANALYSIS/logs/analysis_run.log
git commit -m "docs: add Colab analysis notebook and run record"
\`\`\`

### Task 5: Write Chapter 2 methodology

**Files:**
- Create: \`CHAPTER 2/01-research-design.md\`
- Create: \`CHAPTER 2/02-research-locale-and-context.md\`
- Create: \`CHAPTER 2/03-participants-and-sampling.md\`
- Create: \`CHAPTER 2/04-research-instruments.md\`
- Create: \`CHAPTER 2/05-data-gathering-procedure.md\`
- Create: \`CHAPTER 2/06-data-analysis.md\`
- Create: \`CHAPTER 2/07-ethical-considerations.md\`

- [ ] **Step 1: Write design and context**

Describe the convergent mixed-methods, nonexperimental, post-activity evaluation and mark platform, venue, host, presenter, and schedule details as \`[TO VERIFY: ...]\` unless supplied by an artifact.

- [ ] **Step 2: Write respondents and instrument**

State that 52 available evaluation rows were analyzed, explain that the attendance denominator and response rate are unresolved, and document the 13 primary Likert statements, two single-item ratings, consent fields, and open-ended prompts. Do not claim psychometric validation.

- [ ] **Step 3: Write collection and ethics**

Document the timestamped post-event CSV, read-only raw-data policy, de-identification, removal of institutions/links from outputs, limited access assumption, and unresolved approval details.

- [ ] **Step 4: Write analysis procedures**

Link numeric results to generated tables/figures. Define the scale-direction correction, descriptive statistics, codebook, multiple coding, analyst-coded limitation, and evidence matrix. State that inferential tests and causal claims are out of scope.

- [ ] **Step 5: Verify file structure**

\`\`\`powershell
Get-ChildItem 'CHAPTER 2' -Filter '*.md' | Sort-Object Name | Select-Object -ExpandProperty Name
\`\`\`

Expected: seven separate methodology files.

- [ ] **Step 6: Commit**

\`\`\`powershell
git add 'CHAPTER 2'
git commit -m "docs: write mixed-methods methodology chapter"
\`\`\`

### Task 6: Write Chapter 3 results and discussion

**Files:**
- Create: \`CHAPTER 3/01-results-overview.md\`
- Create: \`CHAPTER 3/02-results-by-research-question.md\`
- Create: \`CHAPTER 3/03-discussion-of-findings.md\`
- Create: \`CHAPTER 3/04-implications.md\`
- Create: \`CHAPTER 3/05-limitations.md\`

- [ ] **Step 1: Write results overview**

Report the 52 analyzed rows, the two normalized scale-direction cases, the 13-item rating set, separate overall/satisfaction outcomes, and the open-ended response corpus. Link numeric statements to generated outputs.

- [ ] **Step 2: Write results by question**

Present item-level distributions and descriptive statistics, then thematic counts and paraphrased patterns. Keep participant perception separate from objective learning or performance.

- [ ] **Step 3: Write discussion**

Integrate quantitative and qualitative strands with the evidence matrix. Compare interpretation with current Chapter 1 sources on TDD, AI-assisted development, beginner instruction, and verification. Do not add unsupported event details or manual calculations.

- [ ] **Step 4: Write implications and limitations**

State practical implications for webinar design and evaluation documentation. State limitations involving one event, available-response sampling, uncertain attendance denominator, post-event self-report, scale correction, analyst-coded themes, missing technical artifacts, and inability to infer causation.

- [ ] **Step 5: Verify numeric traceability**

\`\`\`powershell
rg -n "[0-9]+\\.?[0-9]*|Table|Figure|outputs/" 'CHAPTER 3'
python -c "import json, pathlib; m=json.loads(pathlib.Path('ANALYSIS/outputs/analysis_manifest.json').read_text()); print(m['rows'], m['flagged_rows'], sorted(m['outputs']))"
\`\`\`

Expected: every reported number is in a generated output; the manifest reports 52 rows and two flagged rows.

- [ ] **Step 6: Commit**

\`\`\`powershell
git add 'CHAPTER 3'
git commit -m "docs: write mixed-methods results and discussion"
\`\`\`

### Task 7: Run the completion verification gate

**Files:**
- Verify: \`AGENTS.md\`, \`INSTRUCTIONS.md\`, \`MANUSCRIPT-SPECS.md\`, \`ANALYSIS/\`, \`CHAPTER 2/\`, \`CHAPTER 3/\`

- [ ] **Step 1: Re-run the full CLI pipeline**

Run the Task 4 command from the repository root and inspect the manifest and exit code.

- [ ] **Step 2: Verify raw data is unchanged**

\`\`\`powershell
git diff -- ANALYSIS/data
git status --short
\`\`\`

Expected: no diff under \`ANALYSIS/data\`; only intended files are changed.

- [ ] **Step 3: Verify output invariants**

\`\`\`powershell
python -c "import pandas as pd; a=pd.read_csv('ANALYSIS/outputs/tables/normalization_audit.csv'); n=pd.read_csv('ANALYSIS/outputs/processed/normalized_ratings.csv'); assert a['respondent_id'].nunique()==2; assert n.filter(regex='^rating_|^overall_|^satisfaction_').stack().between(1,5).all(); print('output invariants passed')"
\`\`\`

Expected: exit code 0 and \`output invariants passed\`.

- [ ] **Step 4: Run hygiene checks**

\`\`\`powershell
git diff --check
rg -n "TODO|TBD|lorem ipsum|test\\.only|describe\\.only|skip\\(" AGENTS.md INSTRUCTIONS.md MANUSCRIPT-SPECS.md 'CHAPTER 2' 'CHAPTER 3' ANALYSIS
\`\`\`

Expected: clean diff and no unintended prohibited patterns.

- [ ] **Step 5: Report exact verification state**

Record passed checks, unavailable checks, and remaining \`[TO VERIFY: ...]\` items. Do not claim completion without fresh verification output.

