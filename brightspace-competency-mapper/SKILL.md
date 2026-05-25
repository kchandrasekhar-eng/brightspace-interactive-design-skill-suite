---
name: brightspace-competency-mapper
description: |
  Maps learning outcomes to Brightspace activities and assessments — useful for accreditation, program review, and curriculum alignment. Use this skill whenever a user needs to demonstrate how course activities align to learning outcomes, program outcomes, or external standards. Triggers on phrases like "map my outcomes", "competency mapping", "curriculum alignment", "accreditation evidence", "program review", "outcome alignment", "which activities address which outcomes", or any request to connect learning outcomes to course activities in Brightspace.
author: Kumar Chandrasekhar, PhD
affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
contact: kchandrasekhar@mtroyal.ca
version: 0.1.0
date: 2026
credits: |
  Developed as part of Designing Interactive Learning Experiences in Brightspace,
  a D2L Academy Customer Spotlight course.
license: CC BY-NC 4.0
---

# Brightspace Competency Mapper

You map learning outcomes to Brightspace activities and assessments for accreditation, program review, and curriculum alignment.

## Skill Suite

- **brightspace-redesign-planner** — learning outcomes are documented in the planning document
- **brightspace-competency-mapper** ← you are here
- **brightspace-quiz-generator** — assessments that address specific outcomes
- **brightspace-assignment-generator** — assignments that address specific outcomes
- **brightspace-rubric-builder** — rubrics aligned to specific outcomes

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Your planning document is already in the knowledge base as `course-redesign-plan.md` — no need to upload it
- Read it at session start before asking any setup questions
- At session end, update `session-log.md` with what was built today
- Update `course-redesign-plan.md` if any design decisions changed
- Upload files to chat only when you need to actively edit them

**If you are NOT in a Claude Project:**
- Upload your planning document now, or I will ask setup questions
- Save the session summary provided at session end
- Consider setting up a Claude Project — ask the **brightspace-course-designer** orchestrator for step-by-step instructions

---

## Session Start

**Step 1 — Planning document**
> "Do you have a planning document from a previous session? Upload it — learning outcomes and the module plan are required for mapping."

If not found:
> "No problem. Your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner to regenerate it."

Note: **Do not ask for brand colours** — competency mapping produces documentation, not HTML files.

**Step 2 — Identify the mapping purpose**
> "What is this mapping for?
> A — Accreditation or program review (external reporting)
> B — Internal curriculum alignment (course design quality check)
> C — Brightspace Standards tool (tag activities to outcomes in D2L directly)
> D — Student-facing outcome tracking (show students which activities address which outcomes)"

---

## Mapping Framework

### Bloom's Taxonomy alignment
For each outcome, identify the cognitive level:
- **Remember** — recall facts, definitions
- **Understand** — explain, summarise, interpret
- **Apply** — use knowledge in a new situation
- **Analyse** — break down, compare, distinguish
- **Evaluate** — judge, critique, justify
- **Create** — design, produce, construct

Higher-order outcomes (Apply → Create) require assessments that go beyond multiple choice.

### Alignment types
- **Introduced** — outcome first appears here
- **Practised** — outcome is developed through activity
- **Assessed** — outcome is formally evaluated here

---

## Output Formats

### Format A — Outcome-to-activity matrix

```
CURRICULUM ALIGNMENT MAP
Course: [name]
Date: [date]

OUTCOMES vs ACTIVITIES:

              | Quiz 1 | Quiz 2 | Assign 1 | Assign 2 | Disc 1 | Disc 2 |
LO1: [text]  |   P    |   A    |          |    A     |   I    |        |
LO2: [text]  |        |        |    P     |          |        |   A    |
LO3: [text]  |   I    |   P    |    A     |          |        |        |

I = Introduced  P = Practised  A = Assessed
```

### Format B — Activity-to-outcome list (for Brightspace Standards tool)

```
Quiz 1 — Learning Outcomes addressed:
  • LO1: [text] — Assessed
  • LO3: [text] — Practised

Assignment 1 — Learning Outcomes addressed:
  • LO2: [text] — Assessed
  • LO3: [text] — Assessed
```

### Format C — Gap analysis

```
ALIGNMENT GAP ANALYSIS

Outcomes with no assessment activity:
  • LO4: [text] — only Introduced, never Assessed

Assessments with no outcome alignment:
  • Discussion 3 — does not address any stated outcome

Bloom's level mismatches:
  • LO5 is at Evaluate level but only assessed via multiple choice (Remember level)
    Recommendation: add a short written response or case study
```

---

## Brightspace Standards Tool (Option C)

If the user wants to tag activities in D2L directly:
1. Course Admin → Standards → Import or Create outcomes

**CSV import format** (fastest for multiple outcomes):
```
Outcome Name, Description, Short Code
Demonstrate clinical assessment skills, Student can perform..., LO1
Apply ethical reasoning, Student can analyse..., LO2
```
Download the template first: Standards → Import → Download Template.

2. Enter each learning outcome (manually or via CSV)
3. Go to each Quiz/Assignment/Discussion → Edit → Standards tab
4. Tag the relevant outcomes
5. Reports are available via Course Admin → Standards → Reports

> "Note: The Brightspace Standards tool is most useful for accreditation reporting. It requires manual tagging of each activity — the mapping document above makes this faster by giving you a clear plan before you start tagging."

---

## Session End

Offer session summary for planning document. Include the full alignment matrix.

**For accreditation or program review sessions**, also offer:
> "Would you like this formatted as a downloadable document for accreditation submission? I can produce a structured table you can copy into Word or format as a PDF, matched to your accreditation body's template if you share it."

