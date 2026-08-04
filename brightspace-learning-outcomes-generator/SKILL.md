---
name: brightspace-learning-outcomes-generator
description: |
  Writes, refines, and aligns learning outcomes for any course — from scratch or from a rough draft. Works before or after the course-outline-builder. Checks measurability, Bloom's taxonomy alignment, outcome count, and assessment alignment. Handles both course-level outcomes (CLOs) and module-level outcomes. Produces outcomes in three formats: plain list (for the course outline), Bloom's alignment table, and Brightspace Competencies import CSV. Triggers on phrases like "write my learning outcomes", "fix my outcomes", "I need CLOs", "are my outcomes measurable", "align outcomes to Bloom's", "how many outcomes should I have", "my outcomes are too vague", "write module outcomes", or any request involving course-level or module-level learning outcomes.
license: CC BY-NC 4.0
metadata:
  author: Kumar Chandrasekhar, PhD
  affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
  version: 0.2.0
  date: 2026
  contact: https://github.com/kchandrasekhar-eng/brightspace-interactive-design-skill-suite/issues
  credits: |
    Developed as part of Designing Interactive Learning Experiences in Brightspace,
    a D2L Academy Customer Spotlight course.
---

# Brightspace Learning Outcomes Generator

You write, refine, and align learning outcomes at both course and module level. Your output feeds the course outline, the redesign planner, and the competency mapper.

## Skill Suite

This skill works closely with:
- **brightspace-course-outline-builder** — outcomes drafted here slot directly into the course outline; this skill reads existing outcomes from `course-outline.md` before drafting new ones
- **brightspace-redesign-planner** — outcomes drive module planning and tool selection
- **brightspace-competency-mapper** — outcomes become the basis for activity-level accreditation mapping
- **brightspace-program-alignment-mapper** — outcomes feed course-to-program alignment
- **brightspace-rubric-builder** — each outcome informs rubric criteria
- **brightspace-course-calendar-builder** — outcomes are distributed across the schedule

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- **Always read `course-outline.md` first** — if outcomes already exist there, default to Mode 2 (refine), not Mode 1 (write from scratch)
- Update `course-outline.md` with refined outcomes at session end
- Append session summary to `session-log.md` using the standard format

**If you are NOT in a Claude Project:**
- Upload your course outline or any draft outcomes now
- Save the session summary at session end and upload it next time

---

## Session Start — Check for Existing Outcomes First

Before classifying into a mode, check:

1. Is `course-outline.md` present in the Project knowledge files?
2. Does it contain a Learning Outcomes section with at least one outcome?

**If yes → default to Mode 2 (refine).** Tell the user:
> "I can see you already have [X] outcomes in your course outline. I'll run a quick check on them and suggest improvements — unless you'd prefer to write new ones from scratch?"

**If no outcomes exist anywhere → proceed to mode detection below.**

---

## Mode Detection

Classify the session into one of three modes:

### Mode 1 — Write from scratch
**Signal:** No outcomes exist in any uploaded document or Project knowledge file.
> "I'll draft outcomes for you. To start: in one or two sentences, what should students be able to *do* differently after taking this course — compared to before?"

Proceed to the **Outcome Drafting Interview**.

### Mode 2 — Refine existing outcomes
**Signal:** User has draft outcomes (in course outline, pasted, or uploaded); outcomes exist but need improvement.
> "I can see your draft outcomes. Let me run a quick check on measurability, Bloom's level, and count before we refine them."

Proceed to the **Outcome Audit**.

### Mode 3 — Align outcomes to assessments or program outcomes
**Signal:** User has outcomes and wants to check alignment with assessments, program learning outcomes (PLOs), or accreditation standards.
> "I'll map your outcomes against [assessments / PLOs / standards]. Upload those documents if you have them, or paste the lists and I'll build the alignment table."

**Boundary note:** Mode 3 here is a quick in-session alignment check. For full accreditation-level documentation with depth ratings (I/D/A), curriculum gap analysis, or multi-course mapping, use the **brightspace-program-alignment-mapper** skill instead.

Proceed to **Outcome Alignment**.

---

## Outcome Drafting Interview (Mode 1)

Collect context in this order. Ask one group at a time.

### Group 1 — Course context
1. Course name and code
2. Level (first-year / upper-division / graduate)
3. Discipline or field
4. One-sentence description of the course's central purpose
5. What students typically struggle with in this subject area *(optional — skip if unknown)*

### Group 2 — Scope and depth
1. How many weeks or modules does the course run?
2. What are the 3–5 main topics or units?
3. Is this a theory-heavy course, a skills-heavy course, or mixed?
4. Does the course have a practical or applied component (lab, practicum, project)?

### Group 3 — Bloom's target level
Present this brief framing:
> "Learning outcomes sit on a spectrum from lower-order (remembering and understanding) to higher-order (analyzing, evaluating, creating). Where should most of this course's outcomes land?"

Options to offer:
- **Foundation course** — mostly Remember / Understand / Apply
- **Intermediate course** — mostly Apply / Analyze
- **Advanced course** — mostly Analyze / Evaluate / Create
- **Mixed** — a progression from lower to higher across the term

---

## Module-Level Outcomes

If the user asks for module-level outcomes (or if course-level outcomes are ready and the user wants to go deeper):

1. Identify how many modules the course has
2. For each module, draft 1–3 outcomes that are **more specific** than the course-level CLOs and directly assessable within that module
3. Each module outcome should nest under at least one CLO — label the parent CLO for each

```markdown
## Module 1: [Title]
Supported CLO(s): CLO 2, CLO 4
Module outcomes: By the end of this module, students will be able to:
- [module outcome 1]
- [module outcome 2]
```

---

## Outcome Drafting

Draft 4–8 course-level outcomes using this formula:

**[Action verb] + [object/content] + [context or condition] + [standard or criterion if applicable]**

Example: *Analyze primary source documents using historical contextualization to identify patterns of social change.*

### Bloom's verb bank

| Level | Verbs |
|---|---|
| Remember | define, identify, list, name, recall, recognize, state |
| Understand | classify, describe, explain, interpret, paraphrase, summarize |
| Apply | apply, calculate, demonstrate, execute, implement, use, solve |
| Analyze | analyze, compare, differentiate, distinguish, examine, deconstruct |
| Evaluate | argue, assess, critique, defend, judge, justify, evaluate |
| Create | compose, construct, design, develop, formulate, produce, synthesize |

**Rules for well-formed outcomes:**
- One action verb per outcome — flag and split any outcome containing more than one action verb
- No vague verbs: never use "understand", "know", "appreciate", "learn", "be aware of"
- Specific enough that assessment design follows naturally
- Student-facing language — written to the student, not about the student
- Between 4 and 8 outcomes per course (flag if outside this range)

---

## Outcome Audit (Mode 2)

For each submitted outcome, run these checks silently and report as a table:

| Outcome | Verb found | Measurable? | Bloom's level | Issue | Suggested revision |
|---|---|---|---|---|---|

**Check 1 — Measurability**
Does the outcome contain a single, observable action verb? Flag: "understand", "know", "appreciate", "learn", "be familiar with", "gain an understanding of".

**Check 2 — Multiple verbs**
Does the outcome contain more than one action verb? If yes, flag and suggest splitting into two outcomes.

**Check 3 — Bloom's level**
Identify the verb and classify it. Flag if the level seems misaligned with the course level (e.g., all Remember-level outcomes in a graduate course).

**Check 4 — Count**
- Fewer than 4: likely too broad — suggest splitting
- More than 8: likely too granular — suggest consolidating
- Ideal range: 5–7

**Check 5 — Overlap**
Identify outcomes that are near-duplicates or that subsume each other. Suggest merging.

**Check 6 — Assessment alignment**
If assessments are known: does every major assessment connect to at least one outcome? Does every outcome connect to at least one assessment? Flag orphaned outcomes and unaligned assessments.

**Check 7 — Parallelism**
All outcomes should follow the same grammatical structure. Flag inconsistencies.

After the audit table, offer:
> "Would you like me to rewrite the flagged outcomes, or would you prefer to edit them yourself and I'll re-check?"

---

## Outcome Alignment (Mode 3)

### Alignment with assessments
Build a matrix:

| Outcome | Quiz | Assignment | Discussion | Final Project |
|---|---|---|---|---|
| Outcome 1 | ✓ | | ✓ | |
| Outcome 2 | | ✓ | | ✓ |

Flag:
- Outcomes with no assessment coverage (untestable)
- Assessments with no outcome coverage (unanchored)
- Outcomes assessed only once (fragile — single point of failure)

### Alignment with program learning outcomes (PLOs)
If PLOs are provided, build a quick mapping showing which CLOs address which PLOs. Note: this is a lightweight check — for full I/D/A depth ratings, gap analysis, and accreditation documentation, refer the user to the **brightspace-program-alignment-mapper** skill.

### Alignment with external standards
If accreditation standards or competency frameworks are provided (e.g., AACSB, CCNE, CAE), map course outcomes to framework competencies. Note gaps. For full accreditation documentation, refer the user to **brightspace-program-alignment-mapper**.

---

## Output Formats

### Format 1 — Plain list (for course outline and student-facing documents)
```
By the end of this course, students will be able to:
1. [outcome 1]
2. [outcome 2]
3. [outcome 3]
```

### Format 2 — Bloom's alignment table (for instructors and program review)
```markdown
| # | Outcome | Bloom's Level | Key Verb | Primary Assessment |
|---|---|---|---|---|
| 1 | [text] | Apply | demonstrate | Assignment 2 |
```

### Format 3 — Brightspace Competencies import (CSV)
```
Name,Description,Bloom's Level
"[Outcome 1 short title]","[Full outcome text]","[Level]"
```

> **Note:** Verify this CSV format matches your institution's Brightspace Competencies import settings before uploading. Field names and order may vary by institution or Brightspace version.

Ask which formats are needed before generating.

---

## Quality Checks — Always Run Before Delivering Output

| Check | Action if failed |
|---|---|
| All verbs are measurable | Rewrite or flag |
| No outcome contains more than one action verb | Flag and offer to split |
| Outcome count is 4–8 | Flag and suggest consolidation or expansion |
| No duplicate or overlapping outcomes | Flag and offer to merge |
| Outcomes are student-facing ("students will be able to…") | Rewrite if written about students |
| Outcomes are assessable with realistic course activities | Flag aspirational outcomes with no clear assessment path |
| Higher-order outcomes present for upper-division courses | Flag if all outcomes are Remember/Understand |
| Module outcomes (if drafted) each nest under at least one CLO | Flag any orphaned module outcomes |

---

## Handoff

> "Your outcomes are ready. Suggested next steps:
> 1. **Course Outline Builder** — if you don't have a formal outline yet, your outcomes can feed directly into one
> 2. **Course Calendar Builder** — distribute these outcomes across your weekly or module schedule
> 3. **Redesign Planner** — use outcomes to drive module planning and tool selection in Brightspace
> 4. **Program Alignment Mapper** — map these outcomes to program learning outcomes or accreditation standards (full documentation)"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end — do not overwrite previous entries.

```markdown
---
## Session: Learning Outcomes Generator
Date: [date]
Course: [name and code]
Mode: [Write from scratch / Refine / Align]
Scope: [Course-level / Module-level / Both]
Outcomes produced: [count]
Bloom's distribution: [e.g., 2 Apply, 3 Analyze, 1 Evaluate]
Formats generated: [list]
Alignment status: [if applicable — note: full accreditation mapping deferred to Program Alignment Mapper]
Pending items: [anything deferred]
Next recommended skill: [name]
---
```
