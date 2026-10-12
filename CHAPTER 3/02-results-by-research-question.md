# Results by research question

The results are organized around the evaluation objectives: the perceived quality of the session, the respondent and institutional profile, the feedback participants reported in the open-ended prompts, and the way the two evidence streams relate. All quantitative values below were read from the Conda-generated outputs in `ANALYSIS/outputs/`.

## Evaluation of the session experience

The 13 primary statements were summarized on the normalized 1-5 Likert scale. The agreement rate uses the pre-specified threshold of 4 or 5. The top-box rate is the percentage selecting 5. The full metric file also contains bootstrap 95% intervals for item means and Wilson 95% intervals for agreement proportions.

| Primary item | Mean | SD | Agreement (4 or 5) | Top-box (5) |
| --- | ---: | ---: | ---: | ---: |
| Session objectives were clearly presented | 4.6923 | 0.5064 | 98.08% | 71.15% |
| Topics were relevant and informative | 4.6731 | 0.5134 | 98.08% | 69.23% |
| Content was easy to understand | 4.6346 | 0.5250 | 98.08% | 65.38% |
| Speakers explained the topics clearly | 4.5577 | 0.5744 | 96.15% | 59.62% |
| Presentation materials were clear and organized | 4.7308 | 0.4897 | 98.08% | 75.00% |
| Examples and discussions supported understanding | 4.6346 | 0.5611 | 96.15% | 67.31% |
| Session was engaging and interactive | 4.6154 | 0.6310 | 92.31% | 69.23% |
| Activities reinforced the topics | 4.6346 | 0.5611 | 96.15% | 67.31% |
| Knowledge was useful for studies or everyday life | 4.6346 | 0.5611 | 96.15% | 67.31% |
| Session encouraged critical thinking | 4.6731 | 0.5503 | 96.15% | 71.15% |
| Session was well-organized | 4.7115 | 0.4985 | 98.08% | 73.08% |
| Technical aspects were satisfactory | 4.6923 | 0.5064 | 98.08% | 71.15% |
| Session met expectations | 4.6923 | 0.5064 | 98.08% | 71.15% |

The item means ranged from 4.5577 to 4.7308. Presentation materials received the highest mean and top-box rate, while speaker clarity received the lowest mean and top-box rate. The engagement item had the lowest agreement rate at 92.31%, although it still had a high mean of 4.6154. These rankings identify relative differences within this respondent set; they do not establish meaningful population differences or a causal hierarchy among session components. The source table is [`crispdm_quantitative_metrics.csv`](../ANALYSIS/outputs/tables/crispdm_quantitative_metrics.csv), with the response distribution in [`likert_distributions.csv`](../ANALYSIS/outputs/tables/likert_distributions.csv).

The separate summary ratings were also favorable:

| Summary item | Mean | SD | Agreement (4 or 5) | Top-box (5) |
| --- | ---: | ---: | ---: | ---: |
| Overall session rating | 4.6154 | 0.5297 | 98.08% (51/52) | 63.46% (33/52) |
| Satisfaction | 4.6731 | 0.5134 | 98.08% (51/52) | 69.23% (36/52) |

The primary-item composite had a mean of 4.6598 (SD = 0.4390; median = 4.9231), and 94.23% of respondents had a composite score of at least 4. This composite is a descriptive summary of the 13 items, not a validated psychometric scale. The composite output is [`crispdm_composite_summary.csv`](../ANALYSIS/outputs/tables/crispdm_composite_summary.csv).

## Respondent and institutional profile

The analysis included 52 available evaluation responses. The institution field was retained as recorded for descriptive reporting. `Gordon College` appeared as the exact recorded value for 37 responses (71.15%). Fifteen other recorded categories appeared once each (1.92% per category), including capitalization and spelling variants of Gordon College, other institutions, one unspecified response, and one `Prefer not to say` response. Because institution labels were not harmonized in the pipeline, these values should not be added to produce an inferred institutional total. The complete output is [`crispdm_institution_summary.csv`](../ANALYSIS/outputs/tables/crispdm_institution_summary.csv).

The dataset contained no missing rating cells and no out-of-range rating cells. Two duplicate timestamp values were retained because timestamps were not used as respondent identifiers. The data-quality and manifest records are available in [`crispdm_validation_summary.csv`](../ANALYSIS/outputs/tables/crispdm_validation_summary.csv) and [`analysis_manifest.json`](../ANALYSIS/outputs/analysis_manifest.json).

## Speaker clarity and overall rating

The cross-tabulation below examines speaker clarity against the overall rating. It is descriptive and does not imply that clarity caused the overall rating.

| Speaker clarity response | *n* | Mean overall rating | Overall rating of 5 | Top-box rate |
| --- | ---: | ---: | ---: | ---: |
| 3 | 2 | 3.5000 | 0/2 | 0.00% |
| 4 | 19 | 4.3684 | 7/19 | 36.84% |
| 5 - Strongly agree | 31 | 4.8387 | 26/31 | 83.87% |

The ordinal association between speaker clarity and overall rating was Spearman rho = **0.5459** across 52 complete cases. This positive association is compatible with the idea that perceptions of delivery and overall evaluation moved together in this dataset, but the post-event design cannot distinguish association from confounding or response-style effects. The underlying tables are [`crispdm_speaker_clarity_overall_crosstab.csv`](../ANALYSIS/outputs/tables/crispdm_speaker_clarity_overall_crosstab.csv), [`crispdm_speaker_clarity_overall_summary.csv`](../ANALYSIS/outputs/tables/crispdm_speaker_clarity_overall_summary.csv), and [`crispdm_association_summary.csv`](../ANALYSIS/outputs/tables/crispdm_association_summary.csv).

## Open-ended feedback

The qualitative unit was one respondent answer to one open-ended prompt. Multiple codes could be assigned to one answer. The resulting counts are therefore coded assignments and respondent coverage, not mutually exclusive participant categories.

| Code | Description | Assignments | Respondents |
| --- | --- | ---: | ---: |
| `LEARNING_AI_USE` | AI use | 36 | 25 |
| `LEARNING_SOFTWARE_DEVELOPMENT` | Software development | 22 | 21 |
| `LEARNING_TDD_TESTING` | TDD or software testing | 21 | 17 |
| `VALUED_EXPLANATION` | Explanation and clarity | 17 | 17 |
| `VALUED_DEMONSTRATION` | Demonstration | 11 | 11 |
| `VALUED_PRACTICALITY` | Practical relevance | 11 | 9 |
| `OTHER_RELEVANT_FEEDBACK` | Other relevant feedback | 9 | 7 |
| `IMPROVEMENT_MORE_EXAMPLES` | More examples | 7 | 7 |
| `IMPROVEMENT_MORE_INTERACTION` | More interaction | 6 | 5 |
| `VALUED_SPEAKER` | Speaker | 5 | 5 |
| `IMPROVEMENT_MORE_DEPTH` | More depth | 4 | 4 |
| `IMPROVEMENT_TECHNICAL_QUALITY` | Technical quality | 2 | 2 |

AI use was the most frequent substantive code, followed by broader software-development comments and TDD or testing comments. Explanation and clarity was the most frequent valued-delivery code. Requests for more examples and more interaction were the most frequent improvement codes. Technical-quality comments were less frequent, with two assignments involving two respondents. The coding output with respondent denominators is [`crispdm_theme_counts_with_denominators.csv`](../ANALYSIS/outputs/tables/crispdm_theme_counts_with_denominators.csv).

The coding record also marked 99 assignments as `NO_SUBSTANTIVE_RESPONSE`, involving 47 respondents across the four prompts. These counts are not additional findings about satisfaction; they document the amount of non-substantive material in the qualitative stream. By prompt, the no-substantive code appeared 9 times for learning-value responses, 10 times for liked-most responses, 38 times for improvement responses, and 42 times for additional comments. The prompt-by-code table is [`crispdm_theme_by_prompt.csv`](../ANALYSIS/outputs/tables/crispdm_theme_by_prompt.csv).

## Integration of the two strands

The two evidence streams pointed in a broadly similar direction. Ratings were high across the 13 primary items, while the comments most often referred to AI use, software development, testing, clarity, demonstrations, and practical relevance. The qualitative material also added information that the rating averages could not show: some respondents wanted more examples, more interaction, more depth, or improved technical quality. The resulting interpretation is therefore positive but not unqualified. Participants generally reported a favorable experience, while the coded feedback identified concrete ways to increase practice and participation. The generated mixed-methods matrix is available in [`mixed_methods_evidence_matrix.csv`](../ANALYSIS/outputs/tables/mixed_methods_evidence_matrix.csv).
