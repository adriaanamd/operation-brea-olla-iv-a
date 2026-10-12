# Webinar evaluation analysis

This directory contains the reproducible analysis for the IMRADC manuscript. The raw CSV in `data/` is read-only. The intended execution environment is Google Colab, not the local Windows Python installation. Open [`src/main.ipynb`](src/main.ipynb) in Colab and run the cells in order. The notebook verifies that the standard analysis packages are available in the remote runtime; it does not install packages into the local machine.

Important: opening the notebook in VS Code does not make the local workspace visible to a Colab kernel. The editor is local, but execution happens on a remote Jupyter server. A Windows path such as `C:\\Users\\...` will therefore not work.

The setup cell avoids Google Drive. It clones the committed public repository into the temporary Colab runtime using the configured HTTPS URL and `master` branch. Push the current commit before running the notebook. If the repository is private or the commit has not been pushed, upload a ZIP containing `ANALYSIS/src` and the desensitized CSV when prompted. Never put a GitHub token or password in the notebook.

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
