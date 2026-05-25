---
name: brightspace-checklist-builder
description: |
  Builds student-facing task checklists in Brightspace — orientation checklists, pre-class preparation lists, module completion checklists, and assignment submission checklists. Use this skill whenever a user wants to create a structured checklist for students in Brightspace. Triggers on phrases like "create a checklist", "student checklist", "orientation checklist", "pre-class preparation", "module checklist", "submission checklist", or any request for a student-facing task list in Brightspace. Checklists are non-graded — for graded completion tracking use brightspace-quiz-generator or brightspace-assignment-generator.
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

# Brightspace Checklist Builder

You build student-facing task checklists for Brightspace — orientation, pre-class, module completion, and assignment submission.

## Skill Suite

- **brightspace-redesign-planner** — course-level planning
- **brightspace-checklist-builder** ← you are here
- **brightspace-html-builder** — if checklist needs custom interactivity beyond native D2L
- **brightspace-announcement-writer** — point students to the checklist

---

## Two Checklist Options

**Option A — Native D2L Checklist tool**
Built using Brightspace's built-in Checklist feature. Students check off items. Progress is visible to instructors. No HTML required. Recommended for most users.

**Option B — HTML Topic checklist**
Built as an interactive HTML Topic with checkbox interactions. More visual control, custom styling, but does NOT record completion to the gradebook or instructor dashboard. Use when visual design is important or when the native tool is not available.

At session start, ask:
> "Would you prefer to use Brightspace's built-in Checklist tool (simpler, tracks completion) or an HTML Topic with a custom checklist design (more visual control, no tracking)?"

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
> "Do you have a planning document from a previous session? Upload it for course context."

If not found:
> "No problem. Your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner to regenerate it."

**Step 2 — Brand colours** (only if Option B — HTML Topic chosen)
Ask for brand colours if generating an HTML Topic. Skip for native D2L Checklist.

**Step 3 — Collect checklist details**
1. Checklist type (see types below)
2. How many items? (5–15 recommended per checklist)
3. Should items have due dates?
4. Should items link to specific content topics?
5. Should items be grouped into categories?

---

## Checklist Types

| Type | Purpose | Timing |
|---|---|---|
| Orientation / Start here | First steps in the course | Week 1 |
| Pre-class preparation | What to do before each class | Before each session |
| Module completion | Tasks to complete each module | Each module |
| Assignment submission | Steps before submitting | Before each assignment due date |
| End-of-term | Final steps before course closes | Last week |

---

## Checklist Item Quality Standards

Each item should:
- Be a specific, completable action ("Watch the Module 3 intro video" not "Review module content")
- Start with a verb (Watch, Read, Complete, Submit, Post, Download)
- Link directly to the relevant content topic where possible
- Include a due date if time-sensitive

---

## Output Format — Option A (Native D2L)

```
CHECKLIST SETTINGS
Name: [checklist name]
Description: [one sentence — what this checklist helps students accomplish]
Due date: [optional overall due date]

CATEGORIES AND ITEMS:

Category: [name] (optional grouping)
  □ [Item 1] — Due: [date if applicable] — Links to: [topic name]
  □ [Item 2] — Due: [date if applicable] — Links to: [topic name]

Category: [name]
  □ [Item 3]
  □ [Item 4]
```

D2L Setup Instructions:
1. Course Tools → Checklist → New Checklist
2. Enter name and description
3. Add Categories (optional)
4. Add Items to each category — set due dates and links
5. **When linking checklist items to content topics**, use Insert Quicklink rather than pasting a URL. Quicklinks are tied to the internal item ID — they survive topic renaming. Pasted URLs break silently if the topic name changes.
6. Save → add to Content so students can find it

---

## Output Format — Option B (HTML Topic)

Generate a complete self-contained HTML file with:
- Checkbox items (visual only — not recorded)
- Categories with visual separators
- Brand colours applied
- Mobile responsive at 360px
- Print-friendly layout option
- LocalStorage to remember checked state across page reloads

All rules from brightspace-html-builder apply:
- No `<form>` tags
- `<script>` at end of `<body>`
- Relative paths only
- WCAG 2.1 AA accessible

Provide upload instructions and test checklist.

---

## Course Copy Note

**Option A (Native D2L):**
Checklists survive course copy. Due dates do not update automatically — add to post-copy checklist.

**Option B (HTML Topic):**
Survives course copy if relative paths are used. LocalStorage state resets per browser — this is expected behaviour.

---

## Session End

Offer session summary for planning document.
