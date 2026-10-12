# Data-gathering procedure

The analysis began with the supplied desensitized CSV export. The raw file was read without overwriting it. The pipeline assigned stable row-order identifiers, selected fields by their export positions, parsed the five-point ratings, and separated the open-ended fields from the quantitative frame.

The procedure had four reproducible stages. First, structural and rating checks assessed row count, expected fields, missing rating cells, and out-of-range values. Second, the pipeline flagged rows in which all 13 primary items were recorded as `1` while both overall rating and satisfaction were at least `4`. Third, only the 13 primary items in those flagged rows were reverse-normalized with `6 - raw`; the summary questions were retained unchanged. Fourth, the normalized ratings and de-identified text fields were exported for descriptive summaries and thematic coding.

The final execution is intended for Google Colab through `ANALYSIS/src/main.ipynb`. The notebook installs analysis dependencies in the Colab runtime, imports the same reusable pipeline used by the script, writes outputs under `ANALYSIS/outputs/`, and displays the generated tables and figures. No local package installation is required for this project.
