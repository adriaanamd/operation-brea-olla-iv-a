# Manuscript Agent Harness

This file is the operating contract for any agent working in this manuscript repository. Follow it together with `INSTRUCTIONS.md` and `MANUSCRIPT-SPECS.md`. The user's direct instructions take precedence when they explicitly change scope.

## 0. Mandatory skill routing

Use the following skills for every manuscript session. Do not treat them as optional suggestions:

1. **Manuscript writing, revision, literature review, citation work, research questions, abstracts, formatting, or integrity review:** activate `$ars-codex:academic-research-suite` first. Apply its router and select the narrowest suitable workflow rather than loading the whole suite. Typical routes are:
   - `ars/academic-paper/WORKFLOW.md` for drafting, outlining, revision, citation formatting, or manuscript parts;
   - `ars/deep-research/WORKFLOW.md` for source discovery, literature synthesis, and research-question refinement;
   - `ars/academic-pipeline/WORKFLOW.md` for an explicitly requested end-to-end research-to-paper run;
   - the ARS citation-check route for reference and citation audits.
2. **Manuscript prose humanization:** always activate `$humanizer` alongside ARS for drafting, revising, or reviewing manuscript text. Apply it after evidence and citation checks so that the prose remains natural without weakening claims, hedges, or uncertainty markers.
3. **Chapter 2 analysis methods or Chapter 3 quantitative results/discussion:** activate `$data-analyst` alongside ARS. Apply its analyst powers: establish the objective and decision context, inventory data and grain, validate quality and exclusions, define metrics and denominators, quantify uncertainty, preserve reproducibility, and report limitations and actionable implications.
4. **Pure narrative intake or Chapter 1 prose:** `$ars-codex:academic-research-suite` and `$humanizer` remain mandatory; `$data-analyst` is not required unless the task includes a dataset, metric, statistical claim, or quantitative interpretation.

Activation order is ARS first, then Data Analyst when data work applies. Announce the active skill and selected workflow in the progress update. If the runtime cannot literally invoke a named selector, follow the corresponding skill file and state that limitation; never silently skip the research or analyst controls.

## 1. Mission

Produce a research-like narrative report about the organized webinar while preserving the difference between:

- what the user narrates;
- what a supplied artifact proves;
- what the agent infers;
- what remains unknown.

The agent must never fill an evidence gap with a plausible detail. Missing information is recorded as `[TO VERIFY: ...]` or `[NOT PROVIDED: ...]` until the user supplies or verifies it.

## 2. Session lifecycle

### Phase 0 — Inspect before writing

1. Activate `$ars-codex:academic-research-suite` and select the appropriate workflow before manuscript drafting or revision. Activate `$data-analyst` as well when Chapter 2 analysis methods or Chapter 3 quantitative work applies.
2. Read `INSTRUCTIONS.md`, `MANUSCRIPT-SPECS.md`, and `REFERENCES.md`.
3. Inspect the relevant chapter folder and the `ANALYSIS/` directory.
4. Identify existing evidence files without changing or overwriting them.
5. Check whether the requested chapter part already exists and preserve unrelated user work.

### Phase 1 — Narrative intake

When the user begins narrating the webinar, do not immediately turn the narration into polished manuscript prose. First extract a fact ledger and event timeline.

Capture, in order where available:

1. event title, date, platform, and venue;
2. opening and closing times;
3. organizers, facilitator, presenter, and participant groups;
4. opening activities and stated objectives;
5. presentation sequence, demonstrations, questions, and transitions;
6. technical tools, repositories, tests, or code actually shown;
7. evaluation, feedback, attendance, and closing activities;
8. artifacts that support each claim;
9. contradictions, uncertainty, and details still to be verified.

Ask focused follow-up questions one at a time when a missing detail affects a chapter claim. If the detail does not affect the current chapter, record it as unresolved and continue.

### Phase 2 — Evidence freeze

Before drafting a chapter part, classify each factual statement as one of:

| Status | Meaning | Allowed manuscript treatment |
| --- | --- | --- |
| `VERIFIED` | Supported by an artifact or authoritative source | State as fact and cite or link the support |
| `USER-REPORTED` | Supplied directly by the user but not independently corroborated | Attribute or label carefully; do not strengthen the claim |
| `OBSERVED` | Directly visible in a supplied file, screenshot, dataset, or recording | Describe only what the artifact shows |
| `INFERRED` | Reasoned interpretation from verified evidence | Mark as interpretation and explain the basis |
| `UNRESOLVED` | Missing, contradictory, or not yet checked | Use `[TO VERIFY: ...]` or omit |

Do not silently convert `USER-REPORTED`, `INFERRED`, or `UNRESOLVED` material into verified fact.

### Phase 3 — Chapter routing

Work on one chapter part file at a time. Keep each part separate inside its chapter folder.

#### Chapter 1 — Introduction and literature review

Write the background, objectives/OOTS, problem, significance, scope, terms, and separate literature review as evidence-based narrative. Use scholarly and authoritative sources for general claims. Do not perform computational analysis here. The Background file must reach at least 30 distinct verified sources. The literature-review file must synthesize the existing source ledger and state the bounded research gap without inventing coverage.

#### Chapter 2 — Methodology

Document the convergent mixed-methods, nonexperimental, post-activity evaluation design; context; respondents and sampling; instruments; data gathering; quantitative normalization; thematic coding; integration; and ethics. Use Python for data preparation, de-identification support, response coding, descriptive statistics, and generated tables or figures. Store scripts, notebooks, configuration, logs, and outputs under `ANALYSIS/`. Document the actual method used; never claim a procedure that did not occur.

#### Chapter 3 — Results and Discussion

Report and interpret the evidence produced by the webinar and the Chapter 2 methods. Do not create new spreadsheet calculations or undocumented manual statistics in Chapter 3. Use verified Python outputs from `ANALYSIS/` for numeric results. Integrate Likert summaries and thematic findings while distinguishing participant perception from objective learning or causal effects.

## 4. Analysis boundary

The rule is chapter-specific:

- Python is mandatory for Chapter 2 computational methods and for every numeric result reported in Chapter 3.
- Chapter 1 remains source-based; Chapter 2 documents the analysis pipeline; Chapter 3 consumes verified outputs and does not introduce unsupported calculations.
- If any chapter unexpectedly requires a derived numeric result, stop and route that computation through a Python artifact in `ANALYSIS/` before reporting it.

Raw data must remain read-only. Use relative paths, record package versions and random seeds, and do not commit secrets or unnecessary personal identifiers.

## 5. Citation and reference gates

Before a chapter is considered ready:

1. Every external claim has an appropriate citation or verified source link.
2. Every in-text citation has a complete record in `REFERENCES.md`.
3. The Chapter 1 Background file contains at least 30 distinct, verifiable sources.
4. Chapter 2 methodology citations are complete and accurate where used; Chapter 2 is not a literature-review chapter under the approved IMRADC structure.
5. No invented source, DOI, URL, quotation, author, title, or publication detail appears anywhere.
6. Repeated mentions of the same work are not counted as additional sources.
7. All citations used in the manuscript must be from 2022 or later. Older sources may be discussed only as uncited historical context or replaced with a current source that supports the same claim.

Do not pad citation counts with irrelevant sources. Flag missing or conflicting reference records instead of guessing.

## 6. Writing and evidence rules

- Use retrospective tense for completed webinar events.
- Separate observation, result, interpretation, implication, and recommendation.
- Distinguish satisfaction, self-reported understanding, and objectively measured learning.
- Do not imply causal learning effects from a post-event evaluation without a suitable design.
- Do not report attendance, ratings, timing, participant identity, technical performance, or outcomes unless supported by the fact ledger.
- Anonymize participant information in manuscript text, tables, excerpts, and outputs.
- Preserve the user's narrative meaning while improving structure, grammar, and research clarity.

## 7. Stop conditions

Pause and ask the user for direction when:

- two supplied sources contradict one another on a material fact;
- a required result depends on data that are not present;
- a citation cannot be verified;
- a proposed claim would require causal, psychometric, or generalizable evidence that the study design does not provide;
- a requested edit would merge chapter parts or violate the Python-analysis boundary;
- a file contains unrelated user changes that would be overwritten by the requested work.

Do not resolve these conditions by inventing details, weakening the acceptance criteria, or silently changing the study design.

## 8. Completion checklist

Before declaring a manuscript task complete, verify:

- [ ] The requested part is in the correct chapter folder and remains a separate `.md` file.
- [ ] The fact ledger supports every event-specific claim.
- [ ] Chapter 2 analysis methods and Chapter 3 numeric work are reproducible from Python artifacts in `ANALYSIS/`.
- [ ] Chapter 3 numeric claims match the stored analysis outputs.
- [ ] Chapter 1 citation minimum is satisfied; Chapter 2 methodology citations are complete and accurate.
- [ ] All citations are recorded accurately in `REFERENCES.md`.
- [ ] Unverified details, limitations, missingness, and uncertainty are visible.
- [ ] No participant-identifying information or secrets were added.
- [ ] Markdown structure, links, tables, figures, and cross-references are valid.
