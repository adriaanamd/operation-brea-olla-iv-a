# Theoretical and Conceptual Framework

This section presents the framework used to organize the report on "CodeCrafters: Tech Beyond the Screen." It connects the instructional logic of test-driven development (TDD), the responsible use of AI-assisted programming tools, and the interpretation of participant-evaluation evidence. The framework guides the description of the webinar and the analysis of its available records; it is not presented as a validated causal model of learning.

## Theoretical framework

### TDD as an iterative learning and verification process

The first part of the framework treats TDD as an iterative process that links requirements, executable tests, implementation, and revision. In a simplified form, the learner first expresses an expected behavior as a test, writes or modifies the smallest amount of code needed to address that expectation, observes the result, and then improves the implementation without changing the intended behavior. The red-green-refactor sequence therefore makes feedback visible at several points in the development process.

Recent research supports using TDD as a structured learning object while cautioning against presenting it as a guaranteed solution. Studies have associated TDD with questions of program design, software quality, developer experience, and affective response, but they also report differences in how learners or developers experience the practice and identify challenges related to people, software, and process (Agha et al., 2023; Baldassarre et al., 2022; Calais & Franzini, 2023; Staegemann et al., 2022). The framework consequently treats TDD as a disciplined feedback routine that beginners can inspect and practice, not as an automatic cause of better performance.

### AI assistance as human-guided support

The second part of the framework treats an AI coding assistant as support within the development process rather than as an autonomous authority. AI tools may generate, explain, complete, repair, or test code, but the developer remains responsible for clarifying the requirement, checking the output, running relevant tests, and deciding whether the result is acceptable. Research on code-generation tools describes both their usefulness as starting points and the difficulty users may face when understanding, editing, debugging, or securing generated code (Barke et al., 2023; Pearce et al., 2022; Vaithilingam et al., 2022). Research on AI-assisted software engineering likewise shows that performance depends on the task, repository context, evaluation procedure, and interaction design (Hou et al., 2024; Jimenez et al., 2024; Yang et al., 2024; Zhang et al., 2023).

This human-guided view is also consistent with current risk-management guidance. The NIST AI Risk Management Framework and its generative-AI profile emphasize evaluation, oversight, and the management of risks across the AI lifecycle (Autio et al., 2024; Tabassi, 2023). UNESCO's guidance similarly calls for human-centred use, attention to privacy, and the capacity to evaluate whether generative-AI applications are appropriate in educational settings (Miao & Holmes, 2023). In this report, AI assistance is therefore understood as an input to a verification process. A generated suggestion is treated as provisional until it has been inspected against the requirement and checked through appropriate tests.

### Beginner learning and responsible digital delivery

The third part of the framework concerns the audience and delivery context. Contemporary computing education includes software development, artificial intelligence, professional practice, and responsible computing, but a short webinar cannot substitute for a complete programming course or professional certification pathway (Kumar et al., 2023). Studies of introductory programming also show that AI code generators can create opportunities for novice learners while introducing new instructional and assessment challenges (Becker et al., 2023; Denny et al., 2024; Kazemitabaar et al., 2023). The webinar is therefore framed as an introductory learning activity that should make the reasoning behind tests and code changes visible to beginners.

Online delivery adds another layer to the framework. Digital education depends not only on the tool being used but also on the teaching practice, assessment approach, institutional arrangements, and people who give the activity meaning (OECD, 2023). The report consequently considers the webinar as a coordinated activity involving a topic, organizers, materials, a delivery setting, a demonstration or explanation, participant interaction, and an evaluation process. Details that are not established by the supplied records remain explicitly unresolved.

### Participant evaluation as bounded evidence

The final part of the theoretical framework concerns interpretation. Participant ratings and open-ended comments can document how respondents perceived the objectives, relevance, clarity, interaction, organization, technical delivery, usefulness, and overall experience of the session. They can also identify reported learning value and suggestions for improvement. These records do not, by themselves, establish objective learning, durable competence, improved programming performance, or a causal effect of the webinar. The framework therefore separates participant perception from measured learning and treats the evaluation as evidence about the reported experience of the activity.

## Conceptual framework

The conceptual framework organizes the report through an input-process-output structure. It describes how the available elements of the webinar are connected for documentation and evaluation. The arrows indicate the order of the reporting process, not a tested causal relationship.

```text
Inputs
  topic and intended audience
  TDD and AI-assisted programming content
  organizers, objectives, materials, and delivery setting
  evaluation instrument, consent records, and attendance evidence
        ↓
Process
  planning and preparation
  approval and coordination [TO VERIFY where not documented]
  webinar delivery and explanation or demonstration
  participant interaction and post-webinar evaluation
  de-identification, coding, and descriptive analysis
        ↓
Outputs
  conducted webinar
  participant ratings and written feedback
  attendance or documentation artifacts [TO VERIFY where unavailable]
  evidence-based account of implementation and participant perception
        ↓
Interpretive boundary
  conclusions remain limited to the available records
  positive evaluation is not treated as proof of learning or causation
```

### Inputs

The inputs include the webinar topic, the intended beginner audience, the instructional focus on AI-assisted TDD, the planned objectives, the organizers and facilitators, the learning materials, the delivery platform or setting, and the evaluation instrument. The supplied CSV verifies the existence and general structure of a participant-evaluation instrument, including rating items, open-ended feedback, consent fields, and an attendance-evidence field. The exact organizer roles, platform, presenter, final materials, and technical demonstration artifacts remain **[TO VERIFY: obtain the official program, presentation materials, or other authoritative records]**.

### Process

The process covers the activity from preparation through evaluation: planning the webinar, coordinating or approving the activity, presenting the content, demonstrating or explaining the relationship between AI assistance and testing, engaging participants, collecting evaluation responses, protecting personal information, and analyzing the available records. The later methodology chapter will distinguish documented procedures from steps that remain unverified. Any numeric analysis of the evaluation data will be produced through the designated Python artifacts in `ANALYSIS/`.

### Outputs

The expected outputs are a documented account of the conducted webinar, anonymized participant-evaluation results, summarized open-ended feedback, and the artifacts available to support implementation claims. The outputs describe what the records show. They do not automatically demonstrate that participants acquired TDD competence, changed their programming behavior, or became able to evaluate AI-generated code independently.

### Framework use in the report

The framework will guide the succeeding chapters in three ways. First, it will keep the instructional topic separate from the evidence used to evaluate the session. Second, it will connect the webinar's planning and delivery elements to the participant records without treating missing artifacts as completed activities. Third, it will provide a consistent boundary for interpretation: the report may describe documented implementation and participant perceptions, but claims about learning effects or generalizable outcomes require evidence beyond the supplied post-event evaluation.

