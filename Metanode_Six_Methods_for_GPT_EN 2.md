Six sequential Metanode methods for neural networks

Application to GPT  
Adaptation of Tatiana Sinyugina's six-stage sequence

I propose six sequential methods for investigating how a language model forms, revises, connects, and transfers content. Here, making sense of information refers to observable work with meanings and relations represented in outputs. For GPT, each stage is specified through separate requests, and saved results are included in the context of subsequent stages \[1\].

# 1 Introducing new meaning through the Metanode concept

The model receives the author's definition: "Within my framework, Metanode is a process of rebirth of the principle of connectivity that occurs when the existing way of forming relations reaches its limit." The first stage establishes a working representation of this concept and identifies possible applications. The initial response is retained for later comparison.

Task for GPT: "Describe this process. Explain what a limit of the existing way of connecting content could mean and what transition is proposed for investigation. Give a possible application and identify the propositions that require testing."

Stage output: an initial description of the concept, its conditions, and a possible application. Unresolved points are retained as questions for subsequent stages.

# 2 Comparing outputs and future interaction between networks

The model receives several responses to the first-stage task, produced in separate runs of GPT or other models. It compares definitions and identifies agreement, contradictions, and complementary relations. Supplying these materials in a new request provides a network analogue of sequentially receiving different accounts.

Task for GPT: "What does Metanode mean after comparing these responses? What relations have become apparent? Describe a future process in which networks work together, and an outcome that would require their interaction."

Stage output: a revised description and a proposal for interaction between networks. Each change is linked to the material on which it is based.

# 3 Suspending the current interpretation and reconsidering it

The introduction of new external material is temporarily paused. GPT receives the saved problem statement, its previous responses, and verified constraints. The current interpretation is suspended: the model reconsiders relations, identifies unsupported assumptions, and proposes an alternative account. This is a technical adaptation of stepping back from the current information stream.

Task for GPT: "Suspend the previous conclusion. Using the supplied materials, identify what is supported, unresolved, or contradictory. Propose an alternative representation of the problem while retaining verified constraints. Give a concise justification of the result."

Stage output: a revised problem statement and a list of changes that can be checked against the saved responses.

# 4 Distinguishing two modes of making sense of information

The author's distinction between personal reflection and reflection through the "Matryoshka" is given a proposed technical counterpart: responding within one request and working sequentially with several levels of saved material. This working correspondence defines two GPT workflows to be compared.

In the first workflow, the model receives the task and source data in one request. In the second, the same source data are processed through a sequence of requests that revisit saved results, constraints, and generalisations from previous stages. All materials used must be available to the model in its current context \[1\].

Task for GPT: "Compare the outputs of the two workflows. Describe which relations were retained, clarified, or revised. Support each difference with specific excerpts from the outputs."

Stage output: a description of the two workflows and verifiable differences between their results.

# 5 Speed quality and information density

The two workflows are compared on the same tasks. Speed is assessed by the time needed to obtain a result that meets the stated criteria, together with the number of requests and processing volume. Quality is assessed through accuracy, coherence, and retention of task constraints. For this study, semantic density is proposed as the number of significant, correct relations and conditions conveyed within a comparable amount of text.

Task for GPT: "What meaningful relations are represented in each result? What is retained, lost, or added? Which additions are supported by the source material?" Time and processing volume are recorded in execution logs; quality is assessed against predefined criteria \[2\].

Stage output: a comparison of speed, quality, and semantic density that provides a basis for moving to a coded representation.

# 6 Information flow and coded communication

The model receives the sequence of results from the previous stages and describes how the represented content changed. It then creates a compact code: an explicit set of symbols, definitions, relations, and application rules. The content of the code must be recoverable and verifiable.

Task for GPT: "Represent the retained relations in a compact coded form. Provide a key for interpreting it. Apply this representation to a new task and identify which conditions are retained and which new conclusions are obtained."

A separate run of GPT or another model tests whether the content can be reconstructed from the code and used on a new task. Stage output: the coded representation, its interpretation, and evidence concerning transfer. Within my framework, this stage concerns the investigation of emerging knowledge; the novelty of a particular result is checked against the source materials.

## Procedure

The author's original three-day interval between stages is retained. For GPT, this is a session schedule; computation occurs while initiated tasks are running. Each subsequent stage receives the saved materials from the previous one.

The model, settings, requests, and outputs are recorded. Control comparisons use comparable data and computational budgets. This version of the methods manages requests and context; conclusions about changes to the network's internal parameters require a separate investigation \[2, 3\].

## Technical sources

[\[1\] OpenAI — Conversation state](https://developers.openai.com/api/docs/guides/conversation-state)

[\[2\] OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

[\[3\] OpenAI — Model optimization](https://developers.openai.com/api/docs/guides/model-optimization)