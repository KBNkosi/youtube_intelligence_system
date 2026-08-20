# Hypothesis & Validation Specification

## Stage 1 — Problem & Hypothesis

### Problem

YouTube provides performance data showing where viewer engagement changes,
but this does not necessarily explain what was happening in the content at
those points.

The investigation is whether analysing the underlying content alongside
performance data can identify recurring patterns associated with viewer
engagement or disengagement.

---

## Primary Hypothesis

> Content characteristics can be aligned with YouTube performance data at
> sufficient temporal resolution to identify recurring patterns associated
> with viewer engagement or disengagement.

The initial investigation should focus on **association**, not claim that a
content characteristic directly causes viewer behaviour.

---

## Content Variables

Potential variables to investigate:

- Hooks
- Sentence length
- Filler words
- Information density
- Pacing
- Transitions
- CTAs
- Content structure
- Conversational vs formal language
- Tone

Visual/body-language characteristics are currently **out of scope for the
initial investigation** unless the data experiment shows they are necessary.

These are hypotheses to test, not committed MVP features.

---

## Performance Variables

### Primary

- Audience retention
- Average View Duration
- Watch time

### Secondary

- Views
- Impressions
- CTR
- Traffic sources
- Likes/comments/shares
- Subscribers gained

Other YouTube metrics such as revenue and demographics may provide context
but are not currently central to the hypothesis.

---

## Relationship Being Investigated

The core question is:

> When viewer engagement changes at a particular point in a video, can the
> content occurring around that point be characterised, and do similar
> relationships appear across multiple videos?

Example:

```text
Retention drop
      ↓
Content at that point
      ↓
Identify characteristics
      ↓
Compare against other videos
      ↓
Recurring pattern?

## Alternative Explanations

Viewer behaviour may be influenced by factors not observable in the content, including:

* Viewer intent
* External distractions
* Audience composition
* Traffic source
* Topic relevance
* Thumbnail/title expectations
* Platform effects
* Individual viewer behaviour

*These factors must be considered when interpreting results.*

---

**Assumption**

The underlying assumption is:

> Observable characteristics of video content contain information that can help explain differences in viewer engagement.

*This assumption remains unvalidated.*

---

#Validation

##✅ Evidence Supporting the Hypothesis**

Evidence would include:
* Content can be reliably aligned with performance data.
* Engagement changes can be mapped to specific content segments.
* Similar content characteristics appear around engagement changes across multiple videos.
* The patterns are stronger than would reasonably be expected from isolated examples.
* The resulting patterns can inform a meaningful content decision.

##⚠️ Evidence Weakening the Hypothesis**

* Content cannot be aligned with sufficient accuracy.
* Identified patterns are inconsistent across videos.
* Patterns disappear when comparing different videos/creators.
* Performance differences are better explained by non-content factors.
* Results require too many subjective interpretations.

##🛑 Evidence Falsifying the Hypothesis**

The hypothesis is considered unsupported if:
> Content characteristics cannot be reliably aligned with engagement changes, or analysis across a meaningful sample fails to identify reproducible content-performance relationships.

---

##Usefulness**

##💡 Actionable Insight**

An insight is useful when it:
* Connects a measurable content characteristic to performance behaviour.
* Is supported by evidence across more than one example.
* Reveals something not directly provided by YouTube's existing metrics.
* Can inform a concrete production or content decision.

> **Example:** Videos in this content category consistently show retention declines following a particular structural pattern, suggesting that future videos should test an alternative structure.

##⚠️ Unhelpful Insight**

An insight is insufficient if:
* It simply repeats an existing YouTube metric.
* It has no connection to the underlying content.
* It is based on a single anecdotal example.
* It cannot inform a practical decision.
* The relationship is too weak or inconsistent to justify the conclusion.