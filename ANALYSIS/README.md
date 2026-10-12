# Webinar evaluation analysis

This directory contains the reproducible analysis for the IMRADC manuscript. The raw CSV in `data/` is read-only. The intended execution environment is Google Colab, not the local Windows Python installation. Open [`src/main.ipynb`](src/main.ipynb) in Colab, upload or mount the repository, and run the cells in order. The notebook installs the analysis dependencies inside the temporary Colab runtime and imports the same reusable pipeline used by the script.

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

The `src/main.ipynb` notebook imports the same pipeline used by the command-line run so the manuscript numbers do not depend on a separate manual notebook calculation. No local package installation is required for this project.
