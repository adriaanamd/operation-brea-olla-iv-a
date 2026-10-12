# Operation Brea Olla IV-A — Academic Manuscript Specification

> **Purpose:** Specification for a research-like narrative report documenting the organized webinar held October 12, 2026.
>
> **Context:** This is an adapted CSC414A/L seminar report, not a thesis submission, oral-defense application, or degree-fulfillment document.
>
> **Output:** Markdown (`.md`). Do not generate DOCX or PDF unless separately requested.

## 0. Required skill routing

Every manuscript-writing, literature, citation, revision, or integrity task must use `$ars-codex:academic-research-suite` and one of its appropriate workflows. Chapter 2 analysis methods and Chapter 3 quantitative results/discussion must also use `$data-analyst` practices for data inventory, quality validation, metric definitions, denominators, uncertainty, reproducibility, and limitations. Chapter 1 remains primarily source-based writing and synthesis.

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
  07-review-of-related-literature.md
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
- `07-review-of-related-literature.md`: synthesize current literature on software quality and testing, TDD, AI-assisted software development, novice computing education, and responsible AI use. Keep the synthesis distinct from the event-specific background and from Chapter 2 methodology.

### Chapter 2 — Research Methodology

- `01-research-design.md`: describe the convergent mixed-methods, nonexperimental post-activity evaluation design.
- `02-research-locale-and-context.md`: describe the online delivery context and mark unavailable details as unresolved.
- `03-participants-and-sampling.md`: describe the 52 available evaluation responses, sampling basis, and unresolved attendance denominator.
- `04-research-instruments.md`: describe the 13 Likert items, separate overall/satisfaction items, consent fields, and open-ended prompts.
- `05-data-gathering-procedure.md`: document the timestamped evaluation export and evidence-handling procedure.
- `06-data-analysis.md`: document Python validation, two-row scale normalization, descriptive statistics, thematic coding, and mixed-methods integration.
- `07-ethical-considerations.md`: document consent, privacy, confidentiality, de-identification, and unresolved approval details.

### Chapter 3 — Results and Discussion

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

Repeated mentions do not increase a section's count. A source may support more than one section, but it is counted only once per section and must have one consistent record in `REFERENCES.md`.

Each reference record should include, as applicable: authors, year, title, journal or publisher, volume/issue, pages, DOI, stable URL, and access date for time-sensitive web material. Use consistent APA 7 formatting unless an approved alternative is documented.

Before sign-off, the citation audit must verify:

1. Every in-text citation resolves to a record in `REFERENCES.md`.
2. Every reference record is cited at least once.
3. The Background file has at least 30 distinct sources.
4. Chapter 2 methodology citations are complete and accurate where used.
5. Duplicate or conflicting records are resolved.
6. Bibliographic details, DOI links, and stable URLs are valid or explicitly marked for manual review.

## 5. Chapter-specific Python analysis specification

Python is mandatory for Chapter 2 computational methods and all derived numeric output reported in Chapter 3. Store the code and outputs under `ANALYSIS/`.

Chapter 1 is source-based. Chapter 2 documents the Python analysis and Chapter 3 consumes and interprets verified outputs. Chapter 3 must not introduce undocumented spreadsheet calculations or manual statistics. If any chapter needs a new derived number, route that computation through a Python artifact in `ANALYSIS/` before reporting it.

Required Chapter 2 analysis practices:

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

1. Chapters 1–3 use separate part files as specified or as explicitly documented additions.
2. The prose follows IMRaD logic while retaining an appropriate narrative voice.
3. The Background of the Study contains at least 30 distinct, verifiable citations.
4. Chapter 2 methodology citations are complete and verifiable where used.
5. Every citation is represented accurately in `REFERENCES.md`.
6. Every Chapter 3 computational result is reproducible using Python artifacts in `ANALYSIS/`.
7. Results, tables, figures, and claims are internally consistent across chapter files.
8. Limitations, ethical safeguards, missingness, and uncertainty are reported honestly.
