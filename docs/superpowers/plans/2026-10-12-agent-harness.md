# Manuscript Agent Harness Implementation Plan

> **For agentic workers:** Use the root `AGENTS.md` as the operating contract for manuscript work.

**Goal:** Create a deterministic manuscript-agent workflow that captures the user's webinar narrative before drafting, routes computational work to Chapter 3, and prevents unsupported claims in Chapters 1, 2, and 4.

**Architecture:** A root `AGENTS.md` defines the session lifecycle, evidence states, chapter routing, citation gates, and stop conditions. `INSTRUCTIONS.md` and `MANUSCRIPT-SPECS.md` remain the manuscript-level rules; they are aligned so Chapter 3 owns computational analysis and Chapter 4 consumes its outputs.

**Tech Stack:** Markdown documentation, Python for Chapter 3 analysis, existing CSV evidence in `ANALYSIS/data/`.

## Global Constraints

- Preserve the separate Markdown file structure for Chapters 1–4.
- Do not invent event facts, participants, outcomes, quotations, statistics, citations, or references.
- Use at least 30 distinct verified sources for Chapter 1 Background and 70 for Chapter 2 Literature Review.
- Store Chapter 3 Python code and outputs under `ANALYSIS/`.
- Treat user narration as a source that must be labeled as user-reported until corroborated by an artifact.
- Activate `$ars-codex:academic-research-suite` for every manuscript task; add `$data-analyst` for Chapter 3 computation and Chapter 4 quantitative interpretation.

## Task 1: Create the root agent harness

**Files:**
- Create: `AGENTS.md`

- [ ] Add the intake protocol, fact ledger rules, chapter routing, analysis boundaries, citation gates, and completion checklist.
- [ ] Include explicit stop conditions for missing or contradictory evidence.

## Task 2: Align manuscript rules with chapter-specific analysis

**Files:**
- Modify: `INSTRUCTIONS.md`
- Modify: `MANUSCRIPT-SPECS.md`

- [ ] Clarify that Chapter 3 requires Python for data preparation, statistical analysis, and derived outputs.
- [ ] Clarify that Chapters 1, 2, and 4 do not require Python; Chapter 4 may only report or interpret verified Chapter 3 outputs.
- [ ] Preserve the citation thresholds and `REFERENCES.md` audit requirements.

## Task 3: Verify the harness

**Files:**
- Verify: `AGENTS.md`, `INSTRUCTIONS.md`, `MANUSCRIPT-SPECS.md`

- [ ] Confirm the harness names the narrative intake phase.
- [ ] Confirm it distinguishes user-reported, verified, observed, and unresolved facts.
- [ ] Confirm it routes Python work only to Chapter 3 and prevents unsupported Chapter 4 computations.
- [ ] Confirm required citation thresholds and reference-ledger rules remain present.
