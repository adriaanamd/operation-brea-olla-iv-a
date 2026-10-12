# Results by research question

## Evaluation of the session experience

The 13 primary items were analyzed on the normalized 1–5 scale. The item-level results are generated in [`likert_item_summary.csv`](../ANALYSIS/outputs/tables/likert_item_summary.csv), with the corresponding response distributions in [`likert_distributions.csv`](../ANALYSIS/outputs/tables/likert_distributions.csv). The final Colab run should be used to replace the following controlled placeholders with the exact generated values:

| Result | Value | Source |
| --- | ---: | --- |
| Number of analyzed rows | 52 | `data_quality_summary.csv` |
| Flagged scale-direction rows | 2 | `scale_direction_flags.csv` |
| Primary Likert items | 13 | `likert_item_summary.csv` |
| Lowest item mean | [TO VERIFY: Colab output] | `likert_item_summary.csv` |
| Highest item mean | [TO VERIFY: Colab output] | `likert_item_summary.csv` |
| Overall rating mean | [TO VERIFY: Colab output] | `overall_satisfaction_summary.csv` |
| Satisfaction mean | [TO VERIFY: Colab output] | `overall_satisfaction_summary.csv` |

These values describe participants’ reported experience. They should not be described as objective learning scores, measured competence, or evidence that the webinar caused a change in performance.

## Open-ended feedback

The coded comments showed four broad patterns. First, respondents described learning related to AI-assisted coding, software development, code review, testing, and test-driven development. Second, demonstrations, explanations, practical examples, and speaker delivery were commonly valued. Third, the main improvement requests concerned more demonstrations or examples and more interactive or hands-on activities. Fourth, one response identified connection or microphone quality as a technical issue, while many other improvement and additional-comment fields were non-substantive.

The exact code-assignment counts are generated in [`thematic_counts.csv`](../ANALYSIS/outputs/tables/thematic_counts.csv). The principal codes and their Colab-derived counts are:

| Code | Description | Assignments | Respondents |
| --- | --- | ---: | ---: |
| `LEARNING_AI_USE` | AI use | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |
| `LEARNING_TDD_TESTING` | TDD or software testing | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |
| `LEARNING_SOFTWARE_DEVELOPMENT` | Software development | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |
| `VALUED_DEMONSTRATION` | Demonstration | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |
| `VALUED_EXPLANATION` | Explanation and clarity | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |
| `IMPROVEMENT_MORE_EXAMPLES` | More examples | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |
| `IMPROVEMENT_MORE_INTERACTION` | More interaction | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |
| `IMPROVEMENT_TECHNICAL_QUALITY` | Technical quality | [TO VERIFY: Colab output] | [TO VERIFY: Colab output] |

The theme counts allow multiple assignments per answer and therefore should not be added together as if they were mutually exclusive respondent categories. The evidence boundary is explicit: comments show what respondents reported, not whether their competence objectively increased.

## Integration of the two strands

The mixed-methods evidence matrix is stored in [`mixed_methods_evidence_matrix.csv`](../ANALYSIS/outputs/tables/mixed_methods_evidence_matrix.csv). A convergent reading would be supported if favorable normalized ratings and comments that value clarity, demonstrations, practical relevance, AI use, or testing point in the same direction. The qualitative requests for more examples and interaction would qualify the ratings by showing that favorable overall impressions can coexist with specific suggestions for improvement.
