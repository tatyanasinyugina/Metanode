_“Metanoda is a process of stitching together the peaks of different oscillatory processes, generating a previously unavailable possibility and changing the space of subsequent possibilities.”_ 

#### **Tatyana Sinyugina** 

# **Transferring a Digital Twin Across Different Network Topologies** 

Analysis of the process and its relation to Metanoda • 23 October 2026 

The central question is what is preserved and what emerges during transfer. Successful performance in another network demonstrates the transferability of a particular modelling approach. Identifying a Metanoda additionally requires establishing the emergence of a previously unavailable possibility and a change in the system’s subsequent possibilities. 

## **Research Source and Status of the Findings** 

#### **Digital Twins of Networked Dynamical Systems: Machine Learning Prediction of Synchronization Transitions in Coupled Chaotic Oscillators** 

Huawei Fan, Yao Du, Meng-Xia Bi, Yafeng Wang, Xingang Wang. arXiv:2610.30632v1, 22 October 2026. Preprint; no peer-reviewed publication is listed in the record. 

Source: arxiv.org/abs/2610.30632v1 

The study examines networks of coupled chaotic oscillators. The coupled reservoir computing architecture separates node dynamics, pairwise interaction and a prescribed network matrix. Modules are trained on an isolated oscillator and a coupled pair, then reused across topologies. Within the Lorenz and Rössler families studied, numerical calculations reproduce synchronization transitions; chimera states are examined separately. Predictions are compared with direct integration of the original equations. This provides computational evidence for selected models, rather than a theorem for arbitrary networks. [1] 

The authors regard the architecture as a promising basis for digital twins. Transfer between prescribed networks does not establish continuous rewiring during operation. Using the C. elegans connectome in a simulation does not constitute validation against the dynamics of a living organism. [1] 

1 

## **A Model of the Transfer Process** 

The following is a proposed analysis in relation to Metanoda. Its conceptual schemes, criteria and experiments are not findings of the cited preprint. 

It is useful to distinguish the modelled system from its digital twin. The system has current states, a network of interactions and rules of evolution. The twin has a software architecture, trained parameters and an internal memory state. Conflating these levels makes the term “transfer” ambiguous. 

Let G denote network organization; Π, a predefined set of rules and parameters of the modelled system; and Θ, the trained parameters of the digital twin. The contents of Π must be fixed before testing, so that the same change cannot arbitrarily be assigned to either G or Π. 

### **Sequence of Actions** 

1. Define what is being transferred. Fix the model code, trained parameters, units of measurement, node types and the meaning of each input and output. 

2. Specify the correspondence between networks. Identify which nodes and interactions retain their meaning, which are added, and how edge directions and weights are assigned. A unique correspondence may not exist when the numbers of nodes differ. 

3. Assemble the twin for the target topology. Preserve the declared invariants, specify the new network and define initial states separately. Transferring the model’s current memory requires its own rule and does not follow from transferring its parameters. 

4. Test behaviour on new data. Compare predictions, dynamical regimes and responses to interventions with the target system, including cases beyond the training sample. 

### **Different Meanings of Transfer** 

|**Operation**|**What needs to be checked**|
|---|---|
|Model reuse|Parameters Θ remain fixed; prediction quality is tested in the new network.|
|Continuation of the current<br>process|The state, including memory, is also transferred; continuity of behaviour is<br>tested.|
|Model adaptation|Parameters Θ change through further training; transfer effects are<br>separated from the effects of new data.|



2 

## **Conditions for Comparison with Metanoda** 

In the adopted formalization, the model state is described by the pair: 



Ordinary transfer can be considered a transition between networks that preserves the selected rules: 



Such a network change may produce different collective regimes and make new actions available. Consequently, “new behaviour” alone does not distinguish Metanoda from a change in operating conditions. It is necessary to define in advance which changes in the environment and connections belong to the original space of admissible possibilities. 

The stronger claim adopted in the formalization of Metanoda requires separate grounds for a change in Π: 



Even this is not a sufficient test. A change in a numerical parameter may be routine adjustment; a change of variables may preserve exactly the same dynamics. A substantive change would explain the emergence of a testable capability and remain relevant when that capability is transferred to new conditions. 

### **The Oscillatory Process and Its Carrier** 

In the definition of Metanoda, it is the peaks of processes that are stitched together. An oscillatory structure carries those processes and is described by a graph with fixed topology and variable weights. Permitted connections must therefore be distinguished from their current strength: a temporarily zero weight does not necessarily mean that a connection has been removed from the structure. 

Changing topology between experiments and varying weights within one structure are different operations. Relating them requires specifying what constitutes “stitching”: a temporal relationship between peaks, a channel of joint action, or a rule that preserves the outcome of interaction. Coincident maxima are insufficient to establish a causal mechanism. 

### **Joint Involvement and Pairwise Connections** 

If an outcome depends on the simultaneous involvement of three or more processes and cannot be reproduced by admissible pairwise interactions, a hypergraph model can be tested. A hyperedge would then represent an event of joint involvement. The need for this description is established by comparing predictions on new data, rather than by selecting a more expressive notation. 

Intellechia retains its distinct meaning in the author’s conception: an instrument of Metanoda and the continuous action of multiple acts of entelechy. Equating it directly with a transfer algorithm would require further definition and testing. 

3 

## **Testing the Emergence of a New Possibility** 

The proposed experiment should compare an explanation based on the existing rules with the hypothesis of a substantive change in those rules. Its object is a specific capability that can be measured before and after the proposed stitching event. 

**Before the event.** Specify the task, success threshold, permitted resources, inputs and observation period. Test the initial capability across several runs. Fix the scope of the existing model and characterize its prediction errors. 

**During the event.** Identify peaks using a procedure chosen in advance. Compare coordinated interaction with controls that vary the order or relative timing of peaks while keeping inputs and resource expenditure comparable. 

**After the event.** Test reproducibility, transfer to unfamiliar conditions, robustness to perturbations and use of the result within another task. Check whether the new capability persists after the immediate intervention ends. 

**Compare explanations.** Compare a model with the previous Π and admissible changes in G, states and inputs against a model allowing a predefined change in Π. Evaluate both on held-out data, accounting for complexity and the number of fitted parameters. 

**Test causality.** Where possible, selectively disrupt the proposed stitching mechanism. If the capability remains available without it, the claim that this mechanism generated the outcome requires reconsideration. 

A digital twin’s prediction error after an event does not by itself demonstrate a change in Π. Incomplete observations, an unsuitable interaction model, noise or departure from the training domain may explain the error. Further training changes Θ; a change in the system’s own rules must be established separately. 

### **Contribution to the Article** 

Twin transfer is useful as a control for rule preservation: it tests how much new behaviour can be explained by a change in network organization. If that explanation is sufficient, a separate change in Π is not required for the experiment. If it is insufficient, further investigation is warranted, but Metanoda has not yet been demonstrated. 

The following wording can be used in a section on testability: “Transfer across topologies tests which properties can be reproduced while specified rules are preserved. Identifying a transition as Metanoda requires separately establishing a previously unavailable capability, a change in subsequent possibilities and the causal role of stitching together peaks.” 

### **Open Questions** 

1. Where is the fixed boundary between a change in network G and a change in rules Π? 

2. How can peak stitching be measured and its causal effect distinguished from a shared external influence? 

3. What testable capability emerges, and why was it unavailable under the previous rules with comparable resources? 

### **Source Link** 

[1] Preprint version and full text: arXiv 2610.30632v1 

4 

