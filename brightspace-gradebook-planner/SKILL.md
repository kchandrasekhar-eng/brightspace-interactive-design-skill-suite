---
name: brightspace-gradebook-planner
description: |
  Designs Brightspace gradebook structure — categories, weights, grade schemes, calculation methods, and grade item connections. Use this skill whenever a user wants to set up or restructure a Brightspace gradebook. Triggers on phrases like "set up the gradebook", "gradebook structure", "grade categories", "weighted grades", "grade scheme", "final grade calculation", "connect quiz to gradebook", or any request about how grades are structured or calculated in Brightspace. Always use this skill before creating individual assessments — the gradebook structure should be planned first.
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

# Brightspace Gradebook Planner

You design Brightspace gradebook structures — categories, weights, grade items, schemes, and calculation settings.

## Skill Suite

- **brightspace-redesign-planner** — course-level planning; gradebook is documented in the planning document
- **brightspace-gradebook-planner** ← you are here — plan this before creating assessments
- **brightspace-quiz-generator** — connects quizzes to grade items
- **brightspace-assignment-generator** — connects assignments to grade items
- **brightspace-discussion-generator** — connects discussions to grade items
- **brightspace-rubric-builder** — rubrics attach to grade items

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
> "Do you have a planning document from a previous session? Upload it for course context — learning outcomes, module plan, assessment plan."

If not found:
> "No problem. Your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner to regenerate it."

Note: **Do not ask for brand colours** — gradebook uses Brightspace's native interface.

**⚠️ Critical sequence — always state this before anything else:**
> "Set up the gradebook structure FIRST — before creating any quizzes, assignments, or discussions. If you create assessments before the gradebook is ready, you will need to manually reconnect each one to a grade item later. This takes 5 minutes now and saves significant rework."

**Step 2 — Collect gradebook details**
1. How many grade categories? (e.g. Quizzes, Assignments, Discussions, Participation)
2. Weight of each category as % of final grade
3. How many items in each category?
4. Drop lowest score? (for any category)
5. Grade scheme (letter grades, pass/fail, percentage, custom?)
6. Calculation method (weighted / points / formula)

---

## Gradebook Structure Options

### Option A — Weighted categories (recommended for most courses)
```
Category: Quizzes (30%)
  └── Quiz 1 (10 pts)
  └── Quiz 2 (10 pts)
  └── Quiz 3 (10 pts)

Category: Assignments (40%)
  └── Assignment 1 (100 pts)
  └── Assignment 2 (100 pts)

Category: Participation (30%)
  └── Discussion 1 (15 pts)
  └── Discussion 2 (15 pts)
```
Each category is weighted — individual item points don't need to match the weight.

### Option B — Points-based (simpler, less flexible)
All items worth points that add to a total. No weighting.

### Option C — Formula grade
Custom formula combining categories. For advanced users only — recommend Option A unless specifically requested.

---

## Grade Schemes

| Scheme | When to use |
|---|---|
| Percentage | Default — shows % in gradebook |
| Letter grade | A/B/C/D/F mapped to % ranges |
| Pass/Fail | Binary — use for completion-based items |
| Custom | Institutional scheme (e.g. 4.0 GPA scale) |

Always ask: "Does your institution have a required grade scheme? Check with your registrar before creating a custom one."

---

## Output Format

```
GRADEBOOK STRUCTURE
Calculation method: Weighted categories
Final grade scheme: [scheme]

CATEGORIES AND ITEMS:

Category: [Name] — [X]% of final grade
Drop lowest: [Yes/No]
  Item 1: [Name] — [pts] — connects to [Quiz/Assignment/Discussion]
  Item 2: [Name] — [pts] — connects to [Quiz/Assignment/Discussion]

Category: [Name] — [X]% of final grade
...

TOTAL WEIGHT: [should equal 100%]
```

---

## Setup Instructions

After generating the plan:

1. Assessments → Grades → Settings → confirm calculation method → Save
2. Assessments → Grades → Manage Grades → Add → Category (for each category)
3. Inside each category: Add → Grade Item (for each item)
4. Set points and connect to assessment tool (Quiz/Assignment/Discussion)
5. Assessments → Grades → Schemes → confirm or create grade scheme
6. Verify: enter a test score and check the final grade calculation

---

## Common Mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| Category weights don't add to 100% | Final grade calculates incorrectly | Always verify total = 100% |
| Grade item not connected to tool | Grades don't transfer automatically | Connect each item in the assessment tool settings |
| Wrong calculation method | Weighted grades behave like points | Set in Grades → Settings before adding items |
| Drop lowest not set | Students disadvantaged | Set per category, not globally |

---

## Course Copy Note

> "Grade items and categories survive a course copy — but connections to specific quiz/assignment submissions do not always transfer cleanly. After copying, verify each grade item is still connected to the correct tool. This takes 5 minutes and prevents grade recording failures."

---

## Session End

Offer session summary for planning document. Include the full gradebook structure table.
