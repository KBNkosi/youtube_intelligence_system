# Engineering & AI-Assisted Development Workflow

## Purpose

AI accelerates research, design and implementation, but Kenny remains
responsible for understanding and verifying the system.

> AI is an assistant, not the authority.

---

## Workflow

### 1. DEFINE

Before starting:

- What am I trying to accomplish?
- Why does it matter?
- What should the outcome be?
- What constraints exist?

**Done when:** The task/question is clearly defined.

### 2. RESEARCH

- Identify relevant concepts and existing approaches.
- Prefer official documentation and primary sources.
- Treat AI-generated claims as unverified until their sources are checked.

**Done when:** Relevant facts, assumptions and unknowns are identified.

### 3. VERIFY

Identify assumptions where being wrong could invalidate the work.

Verify using the appropriate method:

- Documentation → API/library behaviour
- Real test → External system/data behaviour
- Known-input test → Data transformations
- Experiment → Data/ML assumptions
- Real user/business feedback → Business assumptions

**Done when:** Critical assumptions have sufficient evidence.

### 4. PLAN

Define the smallest implementation:

- Inputs
- Processing
- Outputs
- Dependencies
- Failure cases
- Tests

**Done when:** The implementation approach is understood before coding.

### 5. IMPLEMENT

Build the smallest useful version first.

Do not expand the implementation before the current step works.

**Done when:** The implementation performs the defined task.

### 6. TEST

Check:

1. Does the code work?
2. Does it work with the real system/data?
3. Does the result actually mean what we think it means?

**Done when:** The result is supported by appropriate tests.

### 7. REVIEW

Before accepting significant work:

- What assumptions remain?
- What evidence supports the result?
- What could be wrong?
- What edge cases were missed?
- Are we confusing correlation with causation?
- What would make us reject this approach?

---

## Evidence Chain

For important decisions, maintain:

**Requirement → Assumption → Evidence → Decision → Implementation → Test → Result**

---

## AI Code Rule

Before accepting meaningful AI-generated code, understand:

- What it does
- Why it works
- What it assumes
- What can fail
- How it was verified

I do not need to write every line myself, but I must be able to defend
the behaviour of the system.

---

## Risk Rule

The higher the consequence of being wrong, the stronger the verification.

**Don't guess. Don't blindly trust AI. Verify critical assumptions before
building on them.**