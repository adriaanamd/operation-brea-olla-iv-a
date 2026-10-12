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
3. **Chapter 3 data work or Chapter 4 quantitative-result interpretation:** activate `$data-analyst` alongside ARS. Apply its analyst powers: establish the objective and decision context, inventory data and grain, validate quality and exclusions, define metrics and denominators, quantify uncertainty, preserve reproducibility, and report limitations and actionable implications.
4. **Pure narrative intake, Chapter 1 prose, or Chapter 2 prose synthesis:** `$ars-codex:academic-research-suite` and `$humanizer` remain mandatory; `$data-analyst` is not required unless the task includes a dataset, metric, statistical claim, or quantitative interpretation.

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

1. Activate `$ars-codex:academic-research-suite` and select the appropriate workflow before manuscript drafting or revision. Activate `$data-analyst` as well when Chapter 3 or Chapter 4 quantitative work applies.
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

#### Chapter 1 — Introduction

Write the background, objectives/OOTS, problem, significance, scope, and terms as evidence-based narrative. Use scholarly and authoritative sources for general claims. Do not perform computational analysis here. The Background file must reach at least 30 distinct verified sources.

#### Chapter 2 — Literature Review

Synthesize the literature, related studies, frameworks, and research gap. Do not write a citation list disguised as synthesis. Do not perform webinar-data analysis here. The Literature Review file must reach at least 70 distinct verified sources by itself, and every source must be recorded in `REFERENCES.md`.

#### Chapter 3 — Methodology

This is the computational-analysis chapter. Use Python for data preparation, de-identification support, response coding, descriptive statistics, statistical tests, and derived tables or figures. Store scripts, notebooks, configuration, logs, and outputs under `ANALYSIS/`. Document the actual method used; never claim a procedure that did not occur.

#### Chapter 4 — Results and Discussion

Report and interpret the evidence produced by the webinar and Chapter 3. Do not create new spreadsheet calculations or undocumented manual statistics in Chapter 4. Use the verified Python outputs from `ANALYSIS/` for numeric results. Narrative interpretation, comparison with Chapter 2, implications, and limitations do not require Python, but they must remain traceable to evidence.

## 4. Analysis boundary

The rule is chapter-specific:

- Python is mandatory for Chapter 3 computational work and for any numeric result that will be reported later.
- Chapters 1 and 2 use source reading, citation management, and prose synthesis; they do not require Python analysis.
- Chapter 4 consumes and interprets Chapter 3 outputs; it does not introduce unsupported calculations.
- If a Chapter 1, 2, or 4 task unexpectedly requires a derived numeric result, stop and route that computation through a Python artifact in `ANALYSIS/` before reporting it.

Raw data must remain read-only. Use relative paths, record package versions and random seeds, and do not commit secrets or unnecessary personal identifiers.

## 5. Citation and reference gates

Before a chapter is considered ready:

1. Every external claim has an appropriate citation or verified source link.
2. Every in-text citation has a complete record in `REFERENCES.md`.
3. The Chapter 1 Background file contains at least 30 distinct, verifiable sources.
4. The Chapter 2 Literature Review file contains at least 70 distinct, verifiable sources on its own.
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
- [ ] Chapter 3 numeric work is reproducible from Python artifacts in `ANALYSIS/`.
- [ ] Chapter 4 numeric claims match the stored Chapter 3 outputs.
- [ ] Chapter 1 and Chapter 2 citation minimums are satisfied when those sections are complete.
- [ ] All citations are recorded accurately in `REFERENCES.md`.
- [ ] Unverified details, limitations, missingness, and uncertainty are visible.
- [ ] No participant-identifying information or secrets were added.
- [ ] Markdown structure, links, tables, figures, and cross-references are valid.
