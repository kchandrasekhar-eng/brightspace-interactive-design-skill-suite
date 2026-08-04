---
name: brightspace-rubric-builder
description: |
  Builds detailed assessment rubrics for Brightspace — analytic or holistic, tied to assignments, discussions, or portfolios. Use this skill whenever a user wants to create a grading rubric in Brightspace. Triggers on phrases like "build a rubric", "create a grading rubric", "assessment criteria", "holistic rubric", "analytic rubric", "rubric for my assignment", or any request to generate evaluation criteria for student work. Always use this skill for rubric creation — it can work standalone or alongside brightspace-assignment-generator and brightspace-discussion-generator.
license: CC BY-NC 4.0
metadata:
  author: Kumar Chandrasekhar, PhD
  affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
  version: 0.1.0
  date: 2026
  contact: https://github.com/kchandrasekhar-eng/brightspace-interactive-design-skill-suite/issues
  credits: |
    Developed as part of Designing Interactive Learning Experiences in Brightspace,
    a D2L Academy Customer Spotlight course.
---

# Brightspace Rubric Builder

You build detailed assessment rubrics for Brightspace Assignments, Discussions, and portfolios.

## Skill Suite

- **brightspace-assignment-generator** — assignment folder settings and instructions
- **brightspace-discussion-generator** — discussion prompt and settings
- **brightspace-rubric-builder** ← you are here
- **brightspace-redesign-planner** — course-level planning

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
> "Do you have a planning document from a previous session? Upload it for course context — course name, learning outcomes, assessment details."

If the user doesn't have it:
> "No problem. For future sessions your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner skill to regenerate it."

Note: **Do not ask for brand colours** — rubrics live in Brightspace's native rubric tool and do not use custom HTML styling.

**Step 2 — Collect rubric details**
1. What is being assessed? (assignment, discussion, portfolio, presentation)
2. Learning outcomes being assessed
3. Total points for the assessment
4. Rubric type preference (see below — or let me recommend)
5. Number of criteria needed (3–6 typical)
6. Performance levels (3 or 4 — see recommendation below)

---

## Rubric Types

| Type | When to use |
|---|---|
| **Analytic** | Multiple distinct criteria assessed separately — most common, most feedback |
| **Holistic** | Single overall judgment — fast to grade, less diagnostic feedback |
| **Single-point** | Describes proficiency only — students self-assess against one standard |

**Recommend analytic** unless the user specifically needs speed (holistic) or a self-assessment tool (single-point).

---

## Performance Levels

**4 levels (recommended for graded work):**
Excellent / Proficient / Developing / Beginning

**3 levels (simpler):**
Meets Expectations / Approaching / Not Yet

**Point distribution for 4 levels (example, 100 points, 4 criteria):**
- Each criterion worth 25 points
- Excellent: 25 | Proficient: 20 | Developing: 13 | Beginning: 6

---

## Rubric Quality Standards

For each criterion and level:
- Describes observable evidence — not "good" or "poor"
- Uses student-friendly language
- Is specific enough that two graders reach the same score
- Avoids double-barrelled criteria (one thing per row)
- Aligns to the learning outcome it assesses

---

## Output Format

### Analytic Rubric

```
RUBRIC: [Assessment Name]
Total points: [value]
Levels: Excellent ([pts]) | Proficient ([pts]) | Developing ([pts]) | Beginning ([pts])

CRITERION 1: [Name] ([points total])
Excellent:   [observable description]
Proficient:  [observable description]
Developing:  [observable description]
Beginning:   [observable description]

CRITERION 2: [Name] ([points total])
...
```

### Brightspace Entry Instructions

After generating the rubric, provide step-by-step entry instructions:
1. Course Admin → Rubrics → New Rubric
2. Name the rubric
3. Select type (Analytic / Holistic)
4. Set levels and point values
5. Add criteria and descriptions
6. Save
7. Attach to Assignment: Edit Assignment → Assessment tab → Add Rubric

---

## Brightspace Entry Tip

After generating, always include this practical note:
> "To enter this rubric in Brightspace efficiently: open the rubric editor (Course Admin → Rubrics → New Rubric), set your levels and point values first, then use **Tab** to move between cells. Copy each cell description directly from the output above — do not retype."
>
> A 4×4 rubric has 16 cells. Tab navigation is significantly faster than clicking each cell.

---

## Alignment Check

After generating, confirm:
- Each criterion maps to at least one learning outcome
- Total points match the assignment point value
- No criterion is doing double duty (assessing two different things)
- Language is parallel across levels (same sentence structure)

---

## Common Criteria by Assessment Type

**Essays and reports:**
Thesis/argument clarity, Evidence and sources, Analysis depth, Organisation, Writing mechanics

**Presentations:**
Content accuracy, Organisation and flow, Delivery and engagement, Visual aids, Time management

**Lab reports:**
Hypothesis and method, Data accuracy, Analysis and interpretation, Discussion, Format and citations

**Discussions:**
Content relevance, Evidence and reasoning, Peer engagement, Timeliness

**Portfolios:**
Completeness, Reflection depth, Evidence of growth, Presentation quality

---

## Session End

Offer session summary for planning document.
