# Manuscript Writing Instructions

## 1. Purpose and governing rule

This project produces a narrative report written in a research-like manner. The report must be evidence-based, transparent, reproducible, and organized according to `MANUSCRIPT-SPECS.md`.

These instructions apply to every chapter file. Preserve substantive draft ideas where possible, but reorganize the text and correct the documentation so that these rules are met.

For every manuscript-writing, literature-review, revision, citation, or integrity task, activate `$ars-codex:academic-research-suite` and select its narrowest applicable workflow. Always activate `$humanizer` alongside ARS for manuscript prose and apply it after evidence and citation checks. For Chapter 2 analysis methods and Chapter 3 quantitative results/discussion, also activate `$data-analyst` and apply its data-quality, metric-definition, uncertainty, reproducibility, and limitation checks. Pure Chapter 1 prose work does not require Data Analyst unless it includes dataset-based claims.

## 2. Required organization

Chapters 1–4 are folders, not single long Markdown files. Each substantive part of a chapter must have its own `.md` file. Do not combine Background of the Study, OOTS, or any other required part into a chapter-level file.

Use this layout and file naming convention:

```text
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
```

The names above are canonical. If the approved proposal requires another part, add a numbered file in the appropriate folder and document it in `MANUSCRIPT-SPECS.md`. Keep each file focused on one part and use headings inside the file for subsections only.

## 3. IMRaD logic for a narrative report

Although this is a narrative report, its reasoning must follow IMRaD:

- **Introduction:** establish context, problem, objectives, significance, scope, and key terms. Chapter 1 must move from broad context to the specific research problem.
- **Methods:** explain exactly how evidence was gathered, processed, and analyzed. Chapter 2 must be specific enough for another researcher to reproduce the work.
- **Results:** report what the data show before making broad claims. Chapter 3 must present findings in the same order as the research questions or objectives.
- **Discussion:** interpret findings in relation to the literature, framework, context, and limitations. Do not introduce uncited external claims or new data in the discussion.

Use a clear narrative voice, but do not replace evidence with anecdotes, unsupported opinion, promotional language, or fictional details. Separate observation, interpretation, and implication. Use cautious claims such as “the findings suggest” when the design does not support causal language.

## 4. Chapter-writing rules

1. Start every part with a short purpose-setting paragraph and end it with a transition or synthesis where appropriate.
2. Keep terminology, population labels, dates, variables, and research-question numbering consistent across all files.
3. Do not duplicate whole paragraphs across chapters. Cross-reference the relevant file instead.
4. Use Markdown headings, tables, and lists consistently. Store figures and tables with descriptive captions and stable filenames.
5. Every numeric result reported in Chapter 3 must be traceable to a Chapter 2 Python analysis and stored output in `ANALYSIS/`; narrative observations and interpretations must be traceable to the fact ledger or a cited source.
6. State limitations honestly. Never conceal missing data, contradictory findings, null findings, or methodological constraints.
7. Do not use placeholder citations, invented quotations, fabricated statistics, or references that cannot be verified.

## 5. Citation and reference requirements

Citation requirements are section-specific and are minimums, not targets to be met by padding:

- **Background of the Study:** at least 30 distinct, relevant, verifiable sources cited in the text.
- Chapter 2 is the methodology chapter under the approved IMRADC structure; it does not carry a 70-source literature-review minimum.
- Other sections must cite sources whenever they make a claim that depends on prior research, a standard, a policy, a dataset, or an external fact.

For every in-text citation:

1. The cited work must exist and must support the claim being made.
2. The complete bibliographic record must appear in the root `REFERENCES.md` file.
3. The author–date key, author names, year, title, and DOI or stable URL must agree between the manuscript and `REFERENCES.md`.
4. Count distinct works, not repeated mentions of the same work. Do not count a bibliography entry that is never cited.
5. Prefer peer-reviewed research, books from reputable academic publishers, official statistics, laws/policies, standards, and primary sources appropriate to the claim.
6. Use secondary sources only when they add genuine synthesis or are the authoritative source for the point being made.
7. Do not fabricate or “complete” missing bibliographic details. Mark unresolved records for correction before submission.
8. All citations used in the manuscript must be from 2022 or later. Do not use pre-2022 works as cited sources; replace them with current sources where support is needed.

Before completion, audit citation coverage and reference integrity. The audit must report the number of distinct sources in the Background file, uncited references, citations missing from `REFERENCES.md`, duplicate records, and records with missing identifiers or stable URLs. Methodology citations must still resolve accurately.

## 6. Chapter-specific analysis policy

Python is mandatory for Chapter 2 computational methods: data preparation, de-identification support, response coding, descriptive statistics, chart generation, and any derived numeric output reported in Chapter 3. Store the code and outputs under `ANALYSIS/`.

Chapter 1 is source-based. Chapter 2 documents the Python analysis and Chapter 3 consumes and interprets its verified outputs. Chapter 3 must not introduce undocumented spreadsheet calculations or manual statistics. If any chapter needs a new derived number, create or update the Chapter 2 Python artifact first.

Required Chapter 2 analysis practices:

- Keep scripts, notebooks, configuration, data dictionaries, logs, and generated outputs in clearly named `ANALYSIS/` subfolders.
- Prefer rerunnable `.py` scripts for the final pipeline. Notebooks may document exploration, but final reported results must be reproducible from a script or documented notebook run.
- Record the Python version, package dependencies, random seeds, input files, and output filenames.
- Keep raw data read-only. Never overwrite raw data with cleaned or derived data.
- Do not perform computational analysis manually in a spreadsheet or word processor and then paste unexplained results into the manuscript.
- Use relative paths so the analysis can run from a clean checkout. Do not commit passwords, tokens, personal identifiers, or other secrets.
- Save tables and figures used in the manuscript in `ANALYSIS/outputs/` and link each result to the chapter file that uses it.

## 7. Quality-control workflow

For each part:

1. Confirm that the file is in the correct chapter folder and has one clear purpose.
2. Check claims against the source and add or correct the corresponding `REFERENCES.md` record.
3. For Chapter 2 analysis or any numeric result reported in Chapter 3, run the relevant Python analysis and confirm that reported values match the generated outputs. For Chapter 1, run source, citation, and reference checks.
4. Check consistency with the research questions, frameworks, methods, and other chapter files.
5. Run the citation/reference audit and inspect Markdown links, tables, figures, and filenames.

Do not mark the manuscript complete while a required chapter part is missing, a cited source is unverified, a reference is absent from `REFERENCES.md`, a citation minimum is unmet, or a reported result cannot be reproduced from `ANALYSIS/`.
