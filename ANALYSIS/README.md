# Webinar evaluation analysis

This directory contains the reproducible analysis for the IMRADC manuscript. The raw CSV in `data/` is read-only. The preferred execution environment is the local Conda/Jupyter kernel selected in VS Code. Open [`src/main.ipynb`](src/main.ipynb) from this repository and run the cells in order; generated tables and figures will be written directly to `ANALYSIS/outputs/` and can then be committed with Git. The notebook verifies that the standard packages are available in the active environment and does not install packages into the local machine.

If a Colab kernel is selected instead, execution occurs on a remote Jupyter server and its `/content` files are separate from this local Git working tree. A Windows path such as `C:\\Users\\...` is valid only with the local Conda/Jupyter kernel. The setup cell detects the local project root from the working directory first; `LOCAL_PROJECT_ROOT` can be set manually if VS Code opened the notebook from another directory.

Colab remains a remote fallback. When no local project root is found, the setup cell can clone the public repository into temporary `/content` or accept a ZIP upload. Those remote outputs must be downloaded or otherwise transferred before they can be committed locally. No Google Drive mount is required, and no GitHub token or password belongs in the notebook.

The notebook expects the desensitized CSV at:

```text
ANALYSIS/data/CodeCrafters_ Tech Beyond the Screen – Day 1 Afternoon Session Evaluation.csv
```

For a compatible Python environment, the retained script entry point is:

```powershell
python -m ANALYSIS.src.pipeline.run_analysis
```

The pipeline uses the 13 experience statements as the primary Likert set. It reports overall rating and satisfaction separately. Two rows whose primary items are all raw `1` while both summary ratings are positive are flagged as likely reversed scale direction. The pipeline reverses only the 13 primary items for those rows with `6 - raw`; it keeps the summary ratings unchanged as consistency anchors. The raw values and every field-level correction are retained in `outputs/tables/normalization_audit.csv`.

Open-ended answers are coded with the codebook and de-identified coding decisions in `src/themes/`. Theme counts describe reported response patterns; they are not measures of objective learning.

The notebook is organized in CRISP-DM phases: business understanding, data understanding, data preparation, descriptive modeling/analysis, evaluation, and deployment. It produces additional auditable tables for data profiling, response coverage, bootstrap mean intervals, Wilson agreement intervals, item rankings, the normalized composite, institutional reach, speaker-clarity cross-tabs, normalization sensitivity, thematic counts by prompt, validation checks, and decision prompts. The notebook imports the same pipeline used by the command-line run so the manuscript numbers do not depend on a separate manual notebook calculation. No local package installation is required for this project.

The command-line pipeline also writes the reusable Chapter 3 figure set to `outputs/figures/`: item means with bootstrap intervals, item means with interquartile ranges, the five-point Likert distribution, summary-rating distributions, the respondent composite distribution, institution profile, speaker-clarity/overall-rating heatmap, coded-theme assignments, theme-by-prompt heatmap, normalization sensitivity, and agreement-versus-top-box scatterplot. These figures are descriptive and use the same normalized ratings and coded-theme tables consumed by the manuscript.
