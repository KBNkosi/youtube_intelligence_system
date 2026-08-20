# YouTube Intelligence System

## Project Execution & Validation Roadmap

**Project status:** Discovery → Hypothesis Definition → Technical Feasibility

**Current objective:** Establish exactly what the MVP needs to prove, determine whether the required evidence can be obtained, and only then design and build the prototype.

---

### 1. How to Use This Document

This is the project's control document.

It exists to answer five questions at any point in the project:

* Where am I?
* What am I trying to accomplish at this stage?
* What do I need to do?
* What evidence have I gathered?
* What must be true before I move forward?

Do not treat completing tasks as the goal.

The goal is to satisfy the exit criteria for each stage.

#### Core rule

Do not move to the next stage because the current stage feels complete. Move because its exit criteria have been satisfied with evidence.

---

### 2. Project Pipeline

```
STAGE 0
Project Context
    ↓
STAGE 1
Problem & Hypothesis
    ↓
STAGE 2
Validation & Evidence Design
    ↓
STAGE 3
Data & API Feasibility
    ↓
STAGE 4
MVP Definition
    ↓
STAGE 5
Architecture & Technical Design
    ↓
STAGE 6
Implementation Plan
    ↓
STAGE 7
Prototype Development
    ↓
STAGE 8
Real-World Evaluation
    ↓
STAGE 9
Decision & Next Iteration

```

The project should be considered stage-gated.

You may research ahead when useful, but do not allow downstream work to substitute for completing the current gate.

---

### 3. Current Project State

#### Current Stage

Stage 1 — Problem & Hypothesis

#### Status

🟡 In progress

#### Completed

* [x] Meeting with Danilo completed
* [x] Meeting transcript reviewed
* [x] Project context updated using meeting evidence
* [x] SEM's business context documented
* [x] Danilo's broader product vision documented
* [x] YouTube Intelligence MVP separated from SEM asset-review opportunity
* [x] Major technical uncertainty identified: performance/content alignment
* [x] Major API/access questions identified
* [x] Commercial assumptions identified as unvalidated
* [x] Project scope boundaries documented

#### Remaining

* [ ] Define the precise hypothesis
* [ ] Define what would constitute evidence for the hypothesis
* [ ] Define what would constitute evidence against it
* [ ] Define the minimum information required to test it
* [ ] Identify the specific analytical unit being investigated
* [ ] Define what "useful insight" means
* [ ] Define the intended decision/workflow the insight should support

#### Current gate

Do not begin architecture yet.

---

### 4. Stage 0 — Project Context

#### Purpose

Establish the project context, boundaries and known information before attempting to solve the problem.

#### Tasks

* [x] Review meeting transcript
* [x] Identify stakeholders
* [x] Document business context
* [x] Document current SEM workflow/problem
* [x] Separate current project from adjacent opportunities
* [x] Document original hypothesis
* [x] Document broader product vision
* [x] Identify commercial assumptions
* [x] Identify technical assumptions
* [x] Identify known uncertainties

#### Required Outputs

* Project Context document
* Meeting evidence
* Scope boundaries
* Initial assumptions/risks

#### Exit Criteria

Stage 0 is complete when:

* [x] The project can be explained without relying on memory
* [x] The current problem is documented
* [x] The larger product vision is separated from the MVP
* [x] Out-of-scope opportunities are explicitly recorded
* [x] Major assumptions and unknowns are visible

#### Status

🟢 **COMPLETE**

*Do not redo this work unless new evidence materially changes the project.*

---

### 5. Stage 1 — Problem & Hypothesis

#### Purpose

Determine exactly what the project is trying to investigate.

This stage prevents the project from becoming:

> "Build an AI system for YouTube analytics."

Instead, it should establish a falsifiable technical/product hypothesis.

#### Tasks

##### Problem

* [ ] Describe the problem independently of the proposed technology
* [ ] Describe how SEM currently addresses the problem
* [ ] Identify where current analysis relies on conjecture
* [ ] Identify what information is currently missing
* [ ] Identify who experiences the problem
* [ ] Identify what decision the missing information affects

##### Hypothesis

* [ ] Write the primary hypothesis
* [ ] Define the independent/content variables
* [ ] Define the dependent/performance variables
* [ ] Define the relationship being investigated
* [ ] Identify alternative explanations
* [ ] Define assumptions underlying the hypothesis

##### Falsification

* [ ] Define what evidence would support the hypothesis
* [ ] Define what evidence would weaken it
* [ ] Define what evidence would falsify it

##### Usefulness

* [ ] Define what constitutes an actionable insight
* [ ] Define who would use the insight
* [ ] Define what decision it would influence
* [ ] Define what would make the insight too obvious or unhelpful

#### Required Output

**Hypothesis & Validation Specification**

It should answer:

*What exactly are we trying to prove, for whom, and what would count as convincing evidence?*

#### Exit Criteria

Do not leave Stage 1 until:

* [ ] The hypothesis can be explained without mentioning the software
* [ ] The hypothesis is specific enough to test
* [ ] The required variables are identified conceptually
* [ ] Success and failure conditions are defined
* [ ] The intended user decision is clear
* [ ] The hypothesis could realistically be disproven

#### Gate

🟢 **GREEN when:** another technically competent person can understand exactly what experiment we are proposing without needing the original meeting transcript.

---

### 6. Stage 2 — Validation & Evidence Design

#### Purpose

Determine what evidence would actually be sufficient to answer the hypothesis.

This prevents collecting data simply because it is available.

#### Tasks

* [ ] Define the unit of analysis
* [ ] Determine whether analysis occurs per video, segment, channel, creator, or across creators
* [ ] Define the minimum performance metrics
* [ ] Define the minimum content characteristics
* [ ] Define required temporal resolution
* [ ] Define required historical period
* [ ] Determine minimum sample size conceptually
* [ ] Define comparison groups
* [ ] Define baseline/comparison methods
* [ ] Define how confounding factors will be handled
* [ ] Define how results will be evaluated
* [ ] Define what a useful output would look like

> **Important Question:**
> For example: If retention is available at a certain resolution, is that resolution sufficient to associate a retention change with a transcript/content event?
> *Do not assume the answer.*

#### Required Output

**Validation Plan** containing:

* Research question
* Data required
* Analysis unit
* Comparison method
* Evaluation criteria
* Limitations
* Evidence threshold

#### Exit Criteria

* [ ] We know what evidence is required
* [ ] We know what measurements are needed
* [ ] We know what comparisons are required
* [ ] We know what would constitute a meaningful result
* [ ] We are not collecting unnecessary data

#### Gate

🟢 **GREEN when:** you can state exactly what data would allow you to answer the hypothesis.

---

### 7. Stage 3 — Data & API Feasibility

#### Purpose

Determine whether the required evidence can actually be obtained.

This is the first major technical feasibility gate.

#### Tasks

##### YouTube APIs

* [ ] Identify relevant APIs
* [ ] Read official documentation
* [ ] Identify authentication requirements
* [ ] Identify OAuth scopes
* [ ] Identify quota limitations
* [ ] Identify rate limits
* [ ] Identify historical-data limitations
* [ ] Identify channel-level data
* [ ] Identify video-level data
* [ ] Identify analytics data
* [ ] Investigate retention data
* [ ] Investigate temporal resolution
* [ ] Investigate transcript availability
* [ ] Investigate thumbnail availability
* [ ] Investigate metadata availability
* [ ] Investigate Content Owner / CMS capabilities

##### SEM Access

* [ ] Determine how SEM currently accesses channels
* [ ] Determine whether SEM has Content Owner access
* [ ] Determine what permissions SEM can provide
* [ ] Determine whether Kenny can access required APIs
* [ ] Determine whether test access can be provided
* [ ] Determine which channels can be used
* [ ] Determine whether historical data can be accessed

##### Practical Verification

*Do not rely solely on documentation.*

Where possible:

* [ ] Create/test API credentials
* [ ] Authenticate
* [ ] Retrieve a real test channel
* [ ] Retrieve real videos
* [ ] Retrieve available analytics
* [ ] Test historical data
* [ ] Test retention availability
* [ ] Test transcript workflow
* [ ] Record actual responses and limitations

#### Evidence Classification

Every finding should be classified as:

* **CONFIRMED**: Verified through documentation or actual API testing.
* **CONDITIONAL**: Possible only under certain permissions/access conditions.
* **UNKNOWN**: Not yet established.
* **UNAVAILABLE**: Confirmed to be inaccessible under the relevant conditions.

#### Required Output

**Data & API Feasibility Report**

#### Exit Criteria

You must be able to answer:

*Given SEM's actual access, what data can we reliably obtain for the experiment?*

And:

* [ ] Required data sources identified
* [ ] Access requirements known
* [ ] Retention feasibility established
* [ ] Temporal resolution established
* [ ] Historical availability established
* [ ] Transcript availability established
* [ ] Major API limitations documented
* [ ] SEM-specific access requirements identified
* [ ] Unknowns that materially affect architecture are resolved

#### Gate

* 🟢 **GREEN:** Required evidence is technically obtainable.
* 🟡 **YELLOW:** Some required evidence is unavailable, but the hypothesis can be tested through a modified experiment.
* 🔴 **RED:** The hypothesis cannot be meaningfully tested with the available data.

*A RED result is not failure. It means the hypothesis or experiment must change before development.*

---

### 8. Stage 4 — MVP Definition

#### Purpose

Convert the validated hypothesis and available data into the smallest credible system capable of producing evidence.

#### Tasks

* [ ] Define one primary MVP question
* [ ] Define MVP users
* [ ] Define inputs
* [ ] Define processing
* [ ] Define outputs
* [ ] Define workflow
* [ ] Define supported use case
* [ ] Define limitations
* [ ] Define non-goals
* [ ] Define MVP success criteria
* [ ] Remove unjustified features

##### Feature Test

For every proposed feature:

*Does this directly contribute to answering the MVP question?*

If no → **Defer it.**

##### Features to challenge aggressively

* Prediction
* Computer vision
* Audio analysis
* Automated recommendations
* Multi-channel dashboards
* Real-time monitoring
* Multi-tenant architecture
* Creator-facing SaaS
* Complex authentication
* Automated reporting

*None should enter V1 without justification.*

#### Required Output

**MVP Specification**

#### Exit Criteria

* [ ] MVP can be explained in one paragraph
* [ ] MVP answers one primary question
* [ ] Inputs are known
* [ ] Outputs are known
* [ ] Success criteria are measurable
* [ ] Non-goals are explicit
* [ ] Every included feature has a reason
* [ ] MVP is feasible with confirmed data

#### Gate

🟢 **GREEN when:** the MVP is the smallest credible experiment capable of producing useful evidence.

---

### 9. Stage 5 — Architecture & Technical Design

#### Purpose

Design the simplest system capable of implementing the MVP.

#### Tasks

* [ ] Define system boundaries
* [ ] Define data flow
* [ ] Define components
* [ ] Define storage
* [ ] Define ingestion pipeline
* [ ] Define processing pipeline
* [ ] Define analysis layer
* [ ] Define API/backend
* [ ] Define user interface if required
* [ ] Define external services
* [ ] Define AI/ML components
* [ ] Define authentication
* [ ] Define error handling
* [ ] Define logging/observability
* [ ] Define deployment requirements
* [ ] Identify security/privacy requirements

##### Architecture Rule

For every component ask:

*What MVP requirement forces this component to exist?*

If there isn't a good answer, challenge it.

#### Required Outputs

* System architecture diagram
* Data-flow diagram
* Data model
* API/interface specification
* Technical decision record
* Technology selection rationale
* Risk register

#### Exit Criteria

* [ ] One complete data path can be traced end-to-end
* [ ] Every major component has a reason
* [ ] Technology choices are supported by requirements
* [ ] External dependencies are understood
* [ ] Major technical risks have mitigations
* [ ] Prototype can be implemented without major unanswered architectural questions

#### Gate

🟢 **GREEN when:** another developer could understand what needs to be built and why.

---

### 10. Stage 6 — Implementation Plan

#### Purpose

Turn the architecture into manageable implementation increments.

#### Tasks

* [ ] Break system into vertical slices
* [ ] Prioritise highest-risk components
* [ ] Define implementation order
* [ ] Define acceptance criteria
* [ ] Define test strategy
* [ ] Define development environment
* [ ] Define repository structure
* [ ] Define coding conventions
* [ ] Define AI-assisted development rules

#### Preferred Implementation Order

Where appropriate:

```
Data access
    ↓
Data ingestion
    ↓
Data storage
    ↓
Content processing
    ↓
Performance processing
    ↓
Analysis
    ↓
Insight generation
    ↓
Presentation

```

*Do not build an elaborate frontend before proving the analytical pipeline.*

#### Required Output

**Implementation Plan / Backlog**

Every task should have a testable definition of done.

#### Exit Criteria

* [ ] Implementation can be broken into small increments
* [ ] Highest-risk components are addressed early
* [ ] Each task has acceptance criteria
* [ ] Testing approach is defined
* [ ] No major product/architecture decisions remain unresolved

---

### 11. Stage 7 — Prototype Development

#### Purpose

Build the smallest working end-to-end system.

#### Development Loop

```
Implement → Test → Verify → Document → Commit

```

#### Principles

* Build vertically
* Keep components simple
* Test against real data as early as possible
* Do not polish prematurely
* Do not add features without updating the specification
* Do not silently change requirements
* Record important decisions

#### First Prototype Goal

The first meaningful milestone should ideally demonstrate:

```
Real YouTube data
       ↓
Ingestion
       ↓
Content analysis
       ↓
Performance analysis
       ↓
Relationship analysis
       ↓
Useful insight

```

*Not: "The dashboard looks good."*

#### Exit Criteria

* [ ] Real data can enter the system
* [ ] Data is processed correctly
* [ ] Analysis executes successfully
* [ ] Output is reproducible
* [ ] At least one complete workflow works end-to-end
* [ ] Known limitations are documented
* [ ] Prototype can be demonstrated

---

### 12. Stage 8 — Real-World Evaluation

#### Purpose

Determine whether the prototype produces useful information for SEM.

Technical functionality is not enough.

#### Technical Evaluation

* [ ] Data accuracy checked
* [ ] Data relationships verified
* [ ] Processing correctness verified
* [ ] Analysis reproducibility checked
* [ ] Errors identified
* [ ] Edge cases tested

#### Analytical Evaluation

* [ ] Patterns identified
* [ ] Patterns tested against data
* [ ] Alternative explanations considered
* [ ] False correlations investigated
* [ ] Sample-size limitations documented
* [ ] Results compared against baseline

#### Business Evaluation (With SEM)

* [ ] Would this insight change a decision?
* [ ] Is the insight new?
* [ ] Is it actionable?
* [ ] Is it sufficiently trustworthy?
* [ ] Does it improve an existing workflow?
* [ ] Would SEM actually use this repeatedly?

#### Required Output

**Prototype Evaluation Report** containing:

* What we expected
* What we tested
* What we found
* Evidence
* Interpretation
* Limitations
* SEM feedback
* Recommended next step

---

### 13. Stage 9 — Decision

Do not automatically continue development.

Choose the outcome supported by evidence.

* **Outcome A — Continue:** Evidence indicates meaningful value.
* *Next:* Improve reliability, expand dataset, expand functionality, test broader use cases.


* **Outcome B — Refine:** Interesting evidence exists but is insufficient.
* *Next:* Modify hypothesis, collect additional data, change analytical approach, run another experiment.


* **Outcome C — Pivot:** Technical approach works but doesn't solve the valuable problem.
* *Next:* Revisit user problem, reconsider output, investigate adjacent opportunity.


* **Outcome D — Stop:** Evidence does not support the underlying hypothesis.
* *Document:* What was tested, what was learned, why it did not work, what future work might still be worthwhile.



*Stopping a weak direction is a successful engineering decision.*

---

### 14. Evidence & Knowledge Log

This should be maintained throughout the project. **Never rely on memory.**

| ID | Question / Claim | Source | Evidence | Status | Date | Impact |
| --- | --- | --- | --- | --- | --- | --- |
| **E-001** | Retention data availability | YouTube API docs | TBD | Unknown |  | Critical |
| **E-002** | SEM Content Owner access | Danilo / SEM | TBD | Unknown |  | Critical |
| **E-003** | Transcript availability | API/test | TBD | Unknown |  | High |

#### Status values

`Confirmed` | `Conditional` | `Unknown` | `Contradicted` | `Rejected` | `Needs verification`

---

### 15. Decision Log

Record decisions that materially affect the project.

| ID | Decision | Evidence | Reason | Date | Revisit |
| --- | --- | --- | --- | --- | --- |
| **D-001** | Do not include asset review in YouTube MVP | Meeting | Separate SEM opportunity |  | Never unless scope changes |
| **D-002** | Do not assume prediction is MVP goal | Project hypothesis | Not yet validated |  | After evaluation |

*The purpose is to prevent repeatedly reconsidering decisions that have already been resolved.*

---

### 16. Assumption & Risk Register

| ID | Assumption / Risk | Importance | Status | Evidence | Next Action |
| --- | --- | --- | --- | --- | --- |
| **R-001** | Retention data is accessible | Critical | Unknown |  | Verify API |
| **R-002** | Retention resolution is sufficient | Critical | Unknown |  | Test |
| **R-003** | SEM can provide required access | Critical | Unknown |  | Confirm with Danilo |
| **R-004** | Transcript can be reliably obtained | High | Unknown |  | Verify |
| **R-005** | Content characteristics correlate meaningfully with performance | Critical | Unknown |  | Experiment |
| **R-006** | SEM finds resulting insights useful | Critical | Unknown |  | Prototype evaluation |

#### Risk rule

Work on the highest-impact unresolved uncertainty before working on lower-impact technical details.

---

### 17. Research Rules

Research must have a purpose.

Before starting research, write:

1. **Question:** What am I trying to determine?
2. **Relevance:** Why does this matter to the current stage?
3. *Execute research.*
4. **Record:** Finding → Evidence → Decision → Impact

*Do not accumulate bookmarks, articles, tutorials or notes without converting them into project knowledge.*

#### Research stopping rule

Stop researching when:

* The question has been answered sufficiently for the current decision
* Remaining uncertainty does not block the current stage
* Further research is unlikely to materially change the decision

---

### 18. AI-Assisted Development Rules

AI can accelerate implementation, but it must not replace project understanding.

For significant AI-generated work:

* Understand what was generated
* Verify assumptions
* Test behaviour
* Review dependencies
* Check security implications
* Check whether it matches the specification
* Record important architectural decisions

#### Rule

AI may accelerate execution. It does not determine requirements.

---

### 19. Progress Dashboard

Update this section regularly.

| Stage | Status | Exit Criteria |
| --- | --- | --- |
| **0. Project Context** | 🟢 Complete | Context established |
| **1. Problem & Hypothesis** | 🟡 Current | Hypothesis defined and testable |
| **2. Evidence Design** | ⚪ Not started | Required evidence defined |
| **3. Data/API Feasibility** | ⚪ Not started | Required data proven accessible |
| **4. MVP Definition** | ⚪ Not started | Smallest useful experiment defined |
| **5. Architecture** | ⚪ Not started | Technical design justified |
| **6. Implementation Plan** | ⚪ Not started | Build broken into verifiable increments |
| **7. Prototype** | ⚪ Not started | End-to-end workflow works |
| **8. Evaluation** | ⚪ Not started | Real-world usefulness assessed |
| **9. Decision** | ⚪ Not started | Evidence-based next step chosen |

#### Status Definitions

* 🟢 **Complete** — Exit criteria satisfied with evidence.
* 🟡 **In Progress** — Actively working on it.
* 🔴 **Blocked** — Cannot progress without resolving a dependency.
* ⚪ **Not Started** — Future stage.
* 🔵 **Revisit** — Previously completed but new evidence requires reconsideration.

---

### 20. Current Work Queue

#### Highest Priority

1. **Define the hypothesis**
* *Deliverable:* Hypothesis & Validation Specification
* *Questions to answer:*
* What exactly are we testing?
* What is the unit of analysis?
* What performance behaviour matters?
* What content characteristics are being investigated?
* What would support the hypothesis?
* What would weaken/falsify it?
* What would constitute a useful insight?




2. **Define required evidence**
* *Deliverable:* Validation Plan
* Determine the minimum data required to test the hypothesis.


3. **Begin API/data feasibility research**
* *Note:* Only after the above is sufficiently defined.
* *Deliverable:* Data & API Feasibility Report



---

### 21. What Not To Work On Yet

Until the MVP and data feasibility gates are passed, avoid:

* Building the production backend
* Building a frontend/dashboard
* Choosing the final tech stack
* Designing multi-tenant architecture
* Building authentication
* Building sophisticated AI agents
* Training prediction models
* Computer vision
* Audio intelligence
* Automated recommendations
* Commercial pricing
* Full SaaS architecture
* SEM asset-review system
* Building for all 45 Jungle Collective creators

*These may eventually become relevant. They are currently unproven downstream work.*

---

### 22. Definition of Progress

Progress is **not**:

* More code
* More documentation
* More research papers
* More API endpoints discovered
* More features designed
* More architecture diagrams
* More AI-generated code

Progress **is**:

* **Reducing important uncertainty.**

#### Examples:

> **Before:** We think retention data might be accessible.
> **After:** We verified that SEM's access allows X retention data at Y resolution for Z historical period.
> *That is progress.*

> **Before:** We think transcript characteristics might explain retention.
> **After:** We defined exactly which characteristics will be measured and what evidence would support or reject the relationship.
> *That is progress.*

> **Before:** We could build a platform for 45 creators.
> **After:** We determined that one creator and N videos are sufficient for the first experiment.
> *That is progress.*

---

### 23. The Ultimate Gate

The project is ready to enter serious development only when all of the following are true:

* [ ] The problem is clearly defined
* [ ] The hypothesis is testable
* [ ] Evidence requirements are defined
* [ ] Required data is known
* [ ] Data access has been verified
* [ ] Major API limitations are understood
* [ ] The MVP question is narrow
* [ ] MVP inputs and outputs are defined
* [ ] MVP success criteria are defined
* [ ] Architecture follows from those requirements
* [ ] Major technical risks have mitigations
* [ ] Implementation tasks have acceptance criteria

*At that point, you are no longer "figuring out what to build." You are implementing a justified experiment.*

---

### 24. Operating Principle

The entire project can be reduced to this loop:

```
QUESTION
   ↓
INVESTIGATE
   ↓
EVIDENCE
   ↓
DECISION
   ↓
SPECIFICATION
   ↓
IMPLEMENT
   ↓
TEST
   ↓
REAL-WORLD EVIDENCE
   ↓
REVISE
   ↺

```

The goal is not to execute the original plan perfectly.

The goal is to continuously replace assumptions with evidence until you either:

1. Prove enough value to justify building further, or
2. Prove that the direction should change.

*That is what disciplined delivery looks like for this project.*