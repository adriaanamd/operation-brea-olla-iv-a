# Operation Brea Olla IV-A — Academic Manuscript Specification

> **Purpose:** Specification for a research-like narrative report documenting the organized webinar held October 12, 2026.
>
> **Context:** This is an adapted CSC414A/L seminar report, not a thesis submission, oral-defense application, or degree-fulfillment document.
>
> **Output:** Markdown (`.md`). Do not generate DOCX or PDF unless separately requested.

## 0. Required skill routing

Every manuscript-writing, literature, citation, revision, or integrity task must use `$ars-codex:academic-research-suite` and one of its appropriate workflows. Chapter 3 computational analysis and Chapter 4 quantitative-result interpretation must also use `$data-analyst` practices for data inventory, quality validation, metric definitions, denominators, uncertainty, reproducibility, and limitations. Chapters 1 and 2 remain primarily source-based writing and synthesis unless a task explicitly includes dataset analysis.

## 1. Research-like narrative and IMRaD logic

The report should remain readable as a narrative account of the webinar while following IMRaD reasoning:

- **Introduction:** establish the context, problem, objectives, significance, scope, and terminology.
- **Methods:** document the activity, participants or respondents, instruments, evidence collection, and analysis procedures.
- **Results:** present observed implementation evidence, evaluation data, and coded feedback in research-question or objective order.
- **Discussion:** interpret the results against the literature, frameworks, context, and limitations.

Use retrospective tense for completed activities and label planned, reported, and directly observed information distinctly. Do not claim causal learning effects from post-event satisfaction data alone.

## 2. Required repository structure

Chapters 1–4 must be folders. Every substantive chapter part must be maintained in its own Markdown file; do not replace these files with one monolithic chapter file.

```text
README.md
INSTRUCTIONS.md
MANUSCRIPT-SPECS.md
REFERENCES.md
CHAPTER_1/
  01-background-of-the-study.md
  02-objectives-of-the-study-oots.md
  03-theoretical-and-conceptual-framework.md
  04-significance-of-the-study.md
  05-scope-and-delimitations.md
  06-definition-of-terms.md
CHAPTER_2/
  01-review-of-related-literature.md
  02-review-of-related-studies.md
  03-theoretical-framework.md
  04-conceptual-framework.md
  05-synthesis-and-research-gap.md
CHAPTER_3/
  01-research-design.md
  02-research-locale-and-context.md
  03-participants-and-sampling.md
  04-research-instruments.md
  05-data-gathering-procedure.md
  06-data-analysis.md
  07-ethical-considerations.md
CHAPTER_4/
  01-results-overview.md
  02-results-by-research-question.md
  03-discussion-of-findings.md
  04-implications.md
  05-limitations.md
ANALYSIS/
  README.md
  requirements.txt or pyproject.toml
  scripts/
  notebooks/
  data/raw/
  data/processed/
  outputs/tables/
  outputs/figures/
  logs/
```

“OOTS” means **Objectives of the Study**. It must be a separate file from the Background of the Study and Statement of the Problem.

If the approved activity requires an additional part, add it as a separately numbered Markdown file in the appropriate chapter and document its purpose here. Additional parts must not be used to merge existing parts.

## 3. Chapter specifications

### Chapter 1 — The Problem and Its Background

- `01-background-of-the-study.md`: explain the context of software testing, test-driven development, AI-assisted development, SDET responsibilities, and the educational webinar. Move from broad evidence to the specific problem. **Minimum: 30 distinct, relevant, verifiable sources cited in this file.**
- `02-objectives-of-the-study-oots.md`: state the general objective and specific objectives. Distinguish instructional objectives from evaluation objectives.
- `03-theoretical-and-conceptual-framework.md`: present the theoretical and conceptual framework for the report, linking TDD as an iterative verification practice, human-guided AI assistance, beginner learning, participant evaluation, and the input-process-output model. Do not present the framework as a validated causal model.
- `04-significance-of-the-study.md`: explain the evidence-based value for students, aspiring SDETs, faculty, organizers, and future training activities.
- `05-scope-and-delimitations.md`: define the webinar, setting, participants, evidence, time frame, exclusions, and boundaries of interpretation.
- `06-definition-of-terms.md`: define TDD, SDET, Red–Green–Refactor, Vitest, CI, AI coding agent, evaluation instrument, and other study-specific terms.

### Chapter 2 — Review of Related Literature

- `01-review-of-related-literature.md`: synthesize concepts, theories, patterns, and disagreements concerning TDD, software-testing education, AI-assisted coding, and webinar or training evaluation. **Minimum: 70 distinct, relevant, verifiable sources cited in this file alone.**
- `02-review-of-related-studies.md`: compare relevant empirical studies, contexts, methods, findings, and limitations.
- `03-theoretical-framework.md`: identify and justify the instructional or evaluation framework used by the study.
- `04-conceptual-framework.md`: describe the proposed model: inputs (topic, organizers, materials, platform) → process (planning, approval, delivery, demonstration, evaluation) → outputs (conducted webinar, documented feedback, and artifacts). Do not present it as a validated causal model.
- `05-synthesis-and-research-gap.md`: synthesize the evidence, state the precise gap, and explain how this report responds to it.

The 70-source minimum applies to `01-review-of-related-literature.md` by itself, not to the chapter by simple accumulation. Every source cited in Chapter 2 must also appear in `REFERENCES.md`.

### Chapter 3 — Research Methodology

- `01-research-design.md`: describe the descriptive, nonexperimental post-activity evaluation design if supported by the evidence.
- `02-research-locale-and-context.md`: describe the online platform, hosting institution, and delivery setting; mark unverified details.
- `03-participants-and-sampling.md`: describe the population, eligibility, sample, sampling method, recruitment, and available attendance evidence.
- `04-research-instruments.md`: describe registration or attendance records, evaluation forms, structured and open-ended items, presentation materials, and technical evidence. Do not claim psychometric validation without proof.
- `05-data-gathering-procedure.md`: document approvals, registration, event delivery, post-webinar evaluation, screenshots, and links with dates and responsible parties when verified.
- `06-data-analysis.md`: document the analysis plan and link every reported analysis to a Python artifact in `ANALYSIS/`.
- `07-ethical-considerations.md`: document consent, privacy, confidentiality, de-identification, data handling, risks, and approvals.

Any technical demonstration evaluation must describe actual presentation flow, TDD steps, test execution, repository artifacts, and evidence limitations. Do not automatically import thesis-template sections such as “Algorithm Process Evaluation” when they do not fit a webinar.

### Chapter 4 — Presentation, Analysis, Interpretation, and Implications

- `01-results-overview.md`: describe the analyzed dataset or evidence corpus and the order of presentation.
- `02-results-by-research-question.md`: present implementation evidence, attendance or respondent characteristics, evaluation distributions, descriptive statistics, open-ended themes, technical evidence, and objective-to-evidence mapping as supported by the data.
- `03-discussion-of-findings.md`: interpret the findings against the literature and frameworks, separating results from interpretation.
- `04-implications.md`: state practical, theoretical, or policy implications supported by the design and evidence.
- `05-limitations.md`: state limitations affecting validity, transferability, reliability, missingness, or interpretation.

If a conclusion or recommendation section is required by the approved report outline, add it as a separate numbered file in Chapter 4 rather than appending it to another part.

## 4. Citation and reference specification

`REFERENCES.md` is the authoritative reference ledger. It must contain a complete, accurate entry for every work cited anywhere in the manuscript. Do not invent authors, titles, publication details, DOIs, URLs, access dates, quotations, or statistics.

| Section | Minimum distinct, verifiable sources | Counting rule |
| --- | ---: | --- |
| Chapter 1 — Background of the Study | 30 | Count distinct works cited in `CHAPTER_1/01-background-of-the-study.md` |
| Chapter 2 — Review of Related Literature | 70 | Count distinct works cited in `CHAPTER_2/01-review-of-related-literature.md` alone |

Repeated mentions do not increase a section's count. A source may support more than one section, but it is counted only once per section and must have one consistent record in `REFERENCES.md`.

Each reference record should include, as applicable: authors, year, title, journal or publisher, volume/issue, pages, DOI, stable URL, and access date for time-sensitive web material. Use consistent APA 7 formatting unless an approved alternative is documented.

Before sign-off, the citation audit must verify:

1. Every in-text citation resolves to a record in `REFERENCES.md`.
2. Every reference record is cited at least once.
3. The Background file has at least 30 distinct sources.
4. The Literature Review file has at least 70 distinct sources.
5. Duplicate or conflicting records are resolved.
6. Bibliographic details, DOI links, and stable URLs are valid or explicitly marked for manual review.

## 5. Chapter-specific Python analysis specification

Python is mandatory for Chapter 3 computational work: data preparation, de-identification support, response coding, descriptive statistics, statistical tests, modeling, chart generation, and any derived numeric output. Store the code and outputs under `ANALYSIS/`.

Chapters 1 and 2 use source reading, citation management, and prose synthesis; they do not require Python analysis. Chapter 4 consumes and interprets verified Chapter 3 outputs. It must not introduce undocumented spreadsheet calculations or manual statistics. If a Chapter 1, 2, or 4 task needs a new derived number, route that computation through a Python artifact in `ANALYSIS/` before reporting it.

Required Chapter 3 practices:

- Keep rerunnable `.py` scripts, notebooks, configuration, data dictionaries, logs, and generated outputs in clearly named `ANALYSIS/` subfolders.
- Prefer a rerunnable Python script for the final pipeline. Notebooks may document exploration, but final reported results must be reproducible from a script or documented notebook run.
- Record the Python version, package dependencies, random seeds, input files, output filenames, and expected exclusions.
- Keep raw data read-only. Store cleaned and derived data separately.
- Do not perform computational analysis manually in a spreadsheet or word processor and paste unexplained results into the manuscript.
- Use relative paths. Do not commit passwords, tokens, or unnecessary participant identifiers.
- Save manuscript tables and figures in `ANALYSIS/outputs/` and link each result to the chapter file that uses it.

## 6. Source evidence and appendices

Use verified evidence for the following where available:

- Topic proposal and faculty approval
- Organizing committee, responsibilities, and official program
- Publicity, registration, and attendance evidence
- Final slides, presenter script, and webinar content outline
- GitHub repositories, demo code, and test execution evidence
- Anonymized evaluation instrument and data
- Analysis tables, methods, screenshots, certificates, and other supporting documentation

Use `[TO VERIFY: ...]` for missing details. Remove or anonymize participant-identifying information. Do not include thesis-only oral-defense forms, degree-fulfillment declarations, Business Model Canvas, application manuals, ACM articles, or CVs unless genuinely relevant and specifically requested.

## 7. Acceptance criteria

The manuscript is ready for review only when:

1. Chapters 1–4 use separate part files as specified or as explicitly documented additions.
2. The prose follows IMRaD logic while retaining an appropriate narrative voice.
3. The Background of the Study contains at least 30 distinct, verifiable citations.
4. The Review of Related Literature contains at least 70 distinct, verifiable citations by itself.
5. Every citation is represented accurately in `REFERENCES.md`.
6. Every Chapter 3 computational result is reproducible using Python artifacts in `ANALYSIS/`, and Chapter 4 numeric claims match those outputs.
7. Results, tables, figures, and claims are internally consistent across chapter files.
8. Limitations, ethical safeguards, missingness, and uncertainty are reported honestly.
