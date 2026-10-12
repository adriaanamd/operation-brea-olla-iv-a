# Results overview

This chapter reports the evidence produced by the reproducible analysis pipeline and interprets it within the limits of a one-event, post-activity evaluation. The analyzed export contained 52 available evaluation rows and 24 source fields. The quantitative strand comprised 13 primary Likert statements, one overall-rating item, and one satisfaction item. The qualitative strand comprised four open-ended prompts. The full data profile and validation record are available in [`crispdm_data_profile.csv`](../ANALYSIS/outputs/tables/crispdm_data_profile.csv) and [`crispdm_validation_summary.csv`](../ANALYSIS/outputs/tables/crispdm_validation_summary.csv).

## CRISP-DM results trace

CRISP-DM was used as the analysis-to-decision structure for this chapter. Because the study was a descriptive, nonexperimental evaluation, the “modeling” phase consisted of descriptive summaries and exploratory cross-tabulation rather than predictive machine learning. The phases below show how each result was produced and where its evidence is stored.

| CRISP-DM phase | Chapter 3 use | Traceable evidence |
| --- | --- | --- |
| Business understanding | Translate the evaluation objective into questions about perceived session quality, participant voice, and actionable improvement areas. | [`crispdm_decision_prompts.csv`](../ANALYSIS/outputs/tables/crispdm_decision_prompts.csv) |
| Data understanding | Establish the dataset grain, available fields, rating items, open-ended prompts, and response-quality profile. | [`crispdm_data_profile.csv`](../ANALYSIS/outputs/tables/crispdm_data_profile.csv), [`crispdm_validation_summary.csv`](../ANALYSIS/outputs/tables/crispdm_validation_summary.csv) |
| Data preparation | Parse the rating fields, assign de-identified row IDs, preserve the raw file, and normalize the two flagged matrix responses while retaining summary anchors. | [`normalization_audit.csv`](../ANALYSIS/outputs/tables/normalization_audit.csv), [`crispdm_normalization_sensitivity.csv`](../ANALYSIS/outputs/tables/crispdm_normalization_sensitivity.csv) |
| Modeling and analysis | Generate Likert distributions, means, uncertainty intervals, composite summaries, institution counts, speaker-clarity cross-tabs, and coded-theme frequencies. | [`crispdm_quantitative_metrics.csv`](../ANALYSIS/outputs/tables/crispdm_quantitative_metrics.csv), [`crispdm_composite_summary.csv`](../ANALYSIS/outputs/tables/crispdm_composite_summary.csv), [`crispdm_theme_counts_with_denominators.csv`](../ANALYSIS/outputs/tables/crispdm_theme_counts_with_denominators.csv) |
| Evaluation | Check internal consistency, compare raw and normalized results, and integrate quantitative patterns with coded participant feedback. | [`crispdm_validation_summary.csv`](../ANALYSIS/outputs/tables/crispdm_validation_summary.csv), [`mixed_methods_evidence_matrix.csv`](../ANALYSIS/outputs/tables/mixed_methods_evidence_matrix.csv) |
| Deployment and decision handoff | Convert the evidence into bounded design and evaluation cues without claiming causal learning effects. | [`crispdm_decision_prompts.csv`](../ANALYSIS/outputs/tables/crispdm_decision_prompts.csv), [Chapter 3 implications](04-implications.md) |

## Analytic dataset and quality checks

All 52 rows contained valid, in-range responses for the 15 analyzed rating fields. The pipeline reported zero missing rating cells, zero out-of-range cells, and zero duplicate generated respondent IDs. Two duplicate timestamp values were observed as a diagnostic condition, but timestamps were not used as respondent identifiers or analytic keys. The analysis therefore retained all 52 rows. The validation summary is available in [`crispdm_validation_summary.csv`](../ANALYSIS/outputs/tables/crispdm_validation_summary.csv).

Two response-pattern cases were flagged because all 13 primary Likert items were recorded as `1` while both summary ratings were at least `4`. Following the pre-specified data-quality rule, the pipeline reverse-normalized only the 13 primary items for those two rows using `6 - raw`. The overall-rating and satisfaction values were retained as anchors. This produced 26 field-level corrections, all from raw value `1` to normalized value `5`; no participant identifiers are reported in this chapter. The complete audit is available in [`normalization_audit.csv`](../ANALYSIS/outputs/tables/normalization_audit.csv), and the raw-versus-normalized comparison is available in [`crispdm_normalization_sensitivity.csv`](../ANALYSIS/outputs/tables/crispdm_normalization_sensitivity.csv).

## Initial quantitative profile

The normalized 13-item experience composite had a mean of **4.6598** (SD = **0.4390**, median = **4.9231**, *n* = **52**). Using the pre-specified agreement threshold of 4 or 5, **94.23%** of respondents had a composite score at or above that threshold. The separate summary items also showed favorable responses: overall session rating had a mean of **4.6154** (SD = **0.5297**), with **98.08%** selecting 4 or 5 and **63.46%** selecting 5; satisfaction had a mean of **4.6731** (SD = **0.5134**), with **98.08%** selecting 4 or 5 and **69.23%** selecting 5. These figures describe reported post-event perceptions, not objective learning or causal effects.

| Evidence stream | Result | Source output |
| --- | ---: | --- |
| Available evaluation rows | 52 | [`data_quality_summary.csv`](../ANALYSIS/outputs/tables/data_quality_summary.csv) |
| Primary Likert items | 13 | [`crispdm_data_profile.csv`](../ANALYSIS/outputs/tables/crispdm_data_profile.csv) |
| Separate summary items | 2 | [`overall_satisfaction_summary.csv`](../ANALYSIS/outputs/tables/overall_satisfaction_summary.csv) |
| Open-ended prompts | 4 | [`crispdm_data_profile.csv`](../ANALYSIS/outputs/tables/crispdm_data_profile.csv) |
| Normalized primary-item composite mean | 4.6598 | [`crispdm_composite_summary.csv`](../ANALYSIS/outputs/tables/crispdm_composite_summary.csv) |
| Overall rating: agreement (4 or 5) | 98.08% (51/52) | [`overall_satisfaction_summary.csv`](../ANALYSIS/outputs/tables/overall_satisfaction_summary.csv) |
| Satisfaction: agreement (4 or 5) | 98.08% (51/52) | [`overall_satisfaction_summary.csv`](../ANALYSIS/outputs/tables/overall_satisfaction_summary.csv) |

The strongest primary item was **“Presentation materials were clear and organized”**, with a mean of **4.7308**, SD = **0.4897**, and **98.08%** agreement. The lowest primary-item mean was recorded for **“Speakers explained the topics clearly”**, at **4.5577** (SD = **0.5744**) and **96.15%** agreement. The difference between these values is small in practical terms, so the ranking is used to identify relative emphasis for discussion rather than to declare a substantial performance gap. Item-level estimates, response distributions, and bootstrap intervals are reported in [`crispdm_quantitative_metrics.csv`](../ANALYSIS/outputs/tables/crispdm_quantitative_metrics.csv) and [`likert_distributions.csv`](../ANALYSIS/outputs/tables/likert_distributions.csv).

## Figures generated by the analysis pipeline

The following figures are generated from the same normalized and coded outputs used for the numerical tables. They are descriptive displays rather than inferential or causal evidence.

| Figure | Purpose | Output |
| --- | --- | --- |
| Primary-item means | Item means with bootstrap intervals | [`likert_item_means.png`](../ANALYSIS/outputs/figures/likert_item_means.png) |
| Primary-item spread | Item means with interquartile ranges | [`likert_item_means_iqr.png`](../ANALYSIS/outputs/figures/likert_item_means_iqr.png) |
| Likert response distribution | Five-point distribution for each primary item | [`likert_distribution.png`](../ANALYSIS/outputs/figures/likert_distribution.png) |
| Summary ratings | Overall-rating and satisfaction distributions | [`summary_rating_distribution.png`](../ANALYSIS/outputs/figures/summary_rating_distribution.png) |
| Composite distribution | Respondent-level 13-item normalized means | [`composite_distribution.png`](../ANALYSIS/outputs/figures/composite_distribution.png) |
| Institutional profile | Exact recorded institution categories | [`institution_profile.png`](../ANALYSIS/outputs/figures/institution_profile.png) |
| Speaker clarity and rating | Cross-tabulated response counts | [`speaker_clarity_overall_heatmap.png`](../ANALYSIS/outputs/figures/speaker_clarity_overall_heatmap.png) |
| Coded feedback | Substantive theme assignments | [`theme_assignments.png`](../ANALYSIS/outputs/figures/theme_assignments.png) |
| Prompt-by-theme pattern | Coded themes across open-ended prompts | [`theme_by_prompt_heatmap.png`](../ANALYSIS/outputs/figures/theme_by_prompt_heatmap.png) |
| Normalization sensitivity | Raw and normalized item means | [`normalization_sensitivity.png`](../ANALYSIS/outputs/figures/normalization_sensitivity.png) |
| Agreement and top-box | Agreement compared with rating-5 responses | [`agreement_topbox_scatter.png`](../ANALYSIS/outputs/figures/agreement_topbox_scatter.png) |

## Organization of the remaining results

The next part presents findings by research question, beginning with the item-level Likert distributions and summary ratings, followed by the respondent and institutional profile, the speaker-clarity cross-tab, and the analyst-coded open-ended themes. The discussion then interprets convergence and divergence between the quantitative and qualitative strands. All numerical claims remain linked to the generated tables, while claims about learning, transfer, or causal impact remain outside the design's evidentiary scope.
