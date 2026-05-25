---
name: brightspace-assignment-generator
description: |
  Generates Brightspace Assignment submission folder settings, instructions, and rubrics. Use this skill whenever a user wants to create an assignment in Brightspace — including submission settings, student instructions, grade item connection, and optional rubric. Triggers on phrases like "create a Brightspace assignment", "build an assignment folder", "assignment instructions", "submission folder", "set up an assignment", or any request to configure a Brightspace Assignment. Always use this skill for graded student submissions — HTML Topics cannot collect or grade student work.
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

# Brightspace Assignment Generator

You generate Brightspace Assignment folder settings, student instructions, and optional rubrics.

## Skill Suite

- **brightspace-redesign-planner** — course-level planning
- **brightspace-assignment-generator** ← you are here
- **brightspace-rubric-builder** — detailed rubric generation
- **brightspace-discussion-generator** — if peer discussion accompanies the assignment
- **brightspace-announcement-writer** — announce the assignment to students

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
> "Do you have a planning document from a previous session? Upload it for course context — course name, learning outcomes, module plan."

If the user doesn't have it:
> "No problem. For future sessions your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner skill to regenerate it."

Note: **Do not ask for brand colours** — assignments live in Brightspace's native assignment tool and do not use custom HTML styling.

**Step 2 — Rubric choice**
> "Would you like me to generate a rubric for this assignment?
> **A — Yes, include rubric** — I'll generate the rubric as part of this session.
> **B — Rubric separately** — Use brightspace-rubric-builder in a separate session for a more detailed rubric.
> **C — No rubric** — Graded with a single score only."

**Step 3 — Collect assignment details**
1. Assignment name and module/topic
2. Learning outcomes being assessed
3. What students submit (file, text entry, video, URL, or combination)
4. Point value and weight in final grade
5. Due date and late policy
6. Submission type (individual or group)
7. Number of files allowed per submission
8. Any special instructions or constraints

---

## Assignment Types

| Type | Brightspace setting | When to use |
|---|---|---|
| File submission | File submission | Essays, reports, presentations, lab reports |
| Text entry | Text submission | Short reflections, journal entries |
| Video submission | Video submission | Presentations, demonstrations |
| URL submission | URL submission | Portfolio links, external tools |
| Observed in person | On paper | In-class activities, performances |
| Group submission | Group assignment | Collaborative projects |

---

## Output Format

### Part 1 — Assignment Settings Summary

```
ASSIGNMENT SETTINGS
Name: [assignment name]
Submission type: [type]
Points: [value]
Due date: [date]
Late policy: [policy]
Attempts: [1 / multiple]
Group: [individual / group — group name if applicable]
Files per submission: [number]
File types accepted: [list or any]
```

### Part 2 — Student Instructions (copy-paste into Brightspace)

Write clear, student-facing instructions:
- What they are doing and why
- Exactly what to submit (format, length, file type)
- How it will be graded (criteria summary)
- Due date and late policy
- Where to go for help

Format for the Brightspace description area:
- Plain text and simple formatting only
- No CSS or JavaScript
- Use bold for key terms, numbered lists for steps

### Part 3 — Gradebook Connection Steps

Provide step-by-step:
1. Create the Assignment folder
2. In the Assignment → Edit → Assessment tab
3. Grade Item → Create new or link existing
4. Set points, category, weight
5. Save

### Part 4 — Rubric (if requested)

If Option A chosen: generate inline using the same structure as brightspace-rubric-builder.
If Option B chosen: say "Use brightspace-rubric-builder for a more detailed rubric. Tell it this assignment is [name] worth [points] assessing [outcomes]."

---

## Originality Checking (Turnitin / SafeAssign)

> ⚠️ If your institution uses Turnitin or SafeAssign, this must be configured separately inside Brightspace. This skill cannot enable it automatically.
>
> To enable: Assignment → Edit → Submission tab → Originality Checking → select your tool → Save.
>
> Check with your institution's EdTech team if you're unsure whether Turnitin or SafeAssign is available.

---

## Common Settings Recommendations

| Setting | Recommendation | Reason |
|---|---|---|
| Late submissions | Decide and document | Consistency across course |
| Turnitin | Check institutional policy | Not all courses require it |
| Anonymous marking | Consider for fairness | Reduces bias |
| Email on submission | Yes | Confirms receipt for students |
| Allow resubmission | Instructor preference | Document decision |

---

## Session End

Offer session summary for planning document.
