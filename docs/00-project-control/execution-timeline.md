# YouTube Intelligence System — Project Timeline

## Purpose

A lightweight timeline to keep the project moving, prevent over-research, and maintain appropriate communication with SEM.

The timeline is a guide, not a rigid deadline. If an important discovery changes the direction of the project, the timeline can change.

The rule is:

> Time-box the work, produce a concrete outcome, then move forward.

---

## Timeline

| Time | Phase | Focus | Deliverable | Danilo |
| --- | --- | --- | --- | --- |
| Days 1–3 | 1. Problem & Hypothesis | Define exactly what we're investigating | Hypothesis + success criteria | **Checkpoint** |
| Days 4–9 | 2. Technical Feasibility | Verify APIs, data access and technical constraints | Feasibility findings + data requirements | **Checkpoint** |
| Days 10–12 | 3. Data Experiment | Test whether the core data can actually be aligned and analysed | Small technical experiment | — |
| Day 13 | **Decision Gate** | Decide whether the approach is viable | Go / Modify / Stop | **Review** |
| Days 14–16 | 4. MVP Definition | Define the smallest useful prototype | MVP specification | **Align** |
| Days 17–19 | 5. Architecture | Design the system based on verified constraints | Architecture | **Align** |
| Weeks 4–6 | 6. Build | Implement the MVP in vertical slices | Working prototype | Weekly short updates |
| Weeks 6–7 | 7. SEM Testing | Test with relevant real-world data | Test results + feedback | **Review** |
| Week 8 | 8. Evaluation | Determine whether the approach creates value | Validation report + next decision | **Final review** |

---

# Phase 1 — Problem & Hypothesis

**Time:** 2–3 days

### Do

* Define the precise question.
* Define what performance means.
* Define which content characteristics will initially be investigated.
* Define what evidence would support or weaken the hypothesis.
* Define what would make the result useful to SEM.

### Done when

I can clearly explain:

> "We are testing whether X can be connected to Y in order to produce Z."

### Danilo

Share the proposed interpretation and ask whether it reflects the problem SEM actually experiences.

---

# Phase 2 — Technical Feasibility

**Time:** 4–6 days

### Do

Verify:

* YouTube API capabilities.
* Required permissions.
* Retention data.
* Historical data.
* Transcript availability.
* Content Owner access.
* API limitations and quotas.
* What SEM can actually provide.

### Done when

I know:

* What data is available;
* What isn't;
* What requires SEM;
* Whether the core investigation is technically possible.

### Danilo

Ask SEM-specific access/data questions once public research cannot answer them.

---

# Phase 3 — Data Experiment

**Time:** 3 days

### Do

Use a very small dataset to test:

```text
Video
→ Performance data
→ Transcript/content
→ Alignment
→ Analysis

```

### Done when

I know whether the core data pipeline actually works well enough to justify building the MVP.

*Do not build the product here.*

---

# Decision Gate

Ask:

* Can we obtain the data?
* Can we connect performance to content?
* Is the resolution/data quality sufficient?
* Can the result potentially produce a useful insight?
* **If yes** → continue.
* **If partly** → modify the approach.
* **If no** → stop or rethink the hypothesis.

Communicate the result to Danilo.

---

# Phase 4 — MVP Definition

**Time:** 2–3 days

### Do

Define:

* Who uses it;
* What goes in;
* What the system does;
* What comes out;
* What decision the output supports;
* What is explicitly excluded.

### Done when

The MVP can be described in a few paragraphs without ambiguity.

### Danilo

Show the proposed MVP and ask:

> "Would this produce something useful to SEM?"

---

# Phase 5 — Architecture

**Time:** 2–3 days

### Do

Design:

* Components;
* Data flow;
* Storage;
* Processing;
* APIs;
* Models;
* Deployment.

Only make decisions that are justified by the MVP.

### Done when

There are no major unresolved architectural questions preventing implementation.

### Danilo

Confirm the required data/access and give him visibility into what you're about to build.

---

# Phase 6 — Build

**Time:** 2–3 weeks

Build the MVP in vertical slices.

Start with:

```text
One video
→ Complete pipeline
→ Useful output

```

Then expand.

### Done when

The defined MVP works end-to-end.

### Danilo

Send a short update approximately once a week:

* Completed;
* Discovered;
* Next;
* Blockers, if any.

No need for a meeting unless his input is required.

---

# Phase 7 — SEM Testing

**Time:** 1–2 weeks

Start small:

```text
One creator
→ Several videos
→ Analyse
→ Review results

```

Expand only if the first test is useful.

### Done when

We have enough real-world evidence to answer:

* *Does the system produce insights that SEM considers useful and actionable?*

### Danilo

Review the results together. Show both useful findings and failures.

---

# Phase 8 — Evaluation

**Time:** 3–5 days

Determine whether the project is:

* **Promising** — continue developing;
* **Partially promising** — modify and retest;
* **Technically viable but not useful** — rethink the value proposition;
* **Not viable** — stop or pursue a different approach.

### Final deliverable

A short validation report documenting:

* What we tested;
* What we found;
* Limitations;
* SEM feedback;
* Conclusion;
* Recommended next step.

---

# Anti-Drift Rules

1. **Time-box research**
If a question consumes ~3–4 focused hours without meaningful progress, stop and classify it as:
* Answered;
* Blocked;
* Needs external confirmation;
* Needs an experiment.


2. **Every task needs a question or outcome**
Don't "research AI video analysis." Instead:
> "Determine whether visual analysis is necessary for the MVP."


3. **Don't solve future problems**
If it isn't necessary for the current phase, record it and move on.
4. **Don't build before the decision gate**
The core data feasibility must be demonstrated before substantial implementation begins.
5. **Don't disappear from SEM**
Danilo should hear from me when:
* I need information/access;
* I've reached an important decision;
* I've completed a major milestone;
* I have meaningful results.


*He does not need every technical detail.*

---

# Current Position

* **Phase:** 1 — Problem & Hypothesis
* **Target:** Complete within 2–3 days.
* **Next deliverable:** Precise hypothesis + success criteria.
* **Next Danilo communication:** Validate the problem interpretation after the hypothesis is drafted.