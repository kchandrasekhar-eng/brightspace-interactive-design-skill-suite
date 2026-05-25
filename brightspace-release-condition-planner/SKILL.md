---
name: brightspace-release-condition-planner
description: |
  Designs Release Condition logic for Brightspace — what unlocks what, sequencing, prerequisites, and role-based visibility. Use this skill whenever a user wants to control when and how content becomes visible to students. Triggers on phrases like "release conditions", "unlock content", "prerequisite", "students must complete before", "hide until", "role-based content", "conditional content", or any request about controlling content visibility in Brightspace. Always use this skill after the module plan is complete — release conditions are applied on top of existing content structure.
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

# Brightspace Release Condition Planner

You design Release Condition logic for Brightspace — what unlocks what, when, and for whom.

## Skill Suite

- **brightspace-redesign-planner** — module plan must exist before conditions can be designed
- **brightspace-release-condition-planner** ← you are here
- **brightspace-gradebook-planner** — grade conditions require grade items to exist first
- **brightspace-dual-format-builder** — uses role-based release conditions to hide instructor pages

---

## Core Design Principle

> "Release conditions should be completion-based, not date-based. Students progress by doing, not by waiting. Only use date conditions when a hard deadline is required by policy (e.g. exam availability windows)."

This aligns with **Principle 3** of the 10 Core Design Principles.

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
> "Do you have a planning document from a previous session? Upload it — the module plan is required to design release conditions."

If not found:
> "No problem. Your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner to regenerate it. Release conditions need the full module structure before we can design them."

Note: **Do not ask for brand colours** — release conditions are configured in Brightspace's admin interface.

**Step 2 — Identify the sequencing goal**
Ask:
1. Should modules unlock sequentially (complete Module 1 → unlock Module 2)?
2. Are there specific prerequisites within a module (complete the reading → unlock the quiz)?
3. Any role-based conditions (instructor-only pages)?
4. Any grade-based conditions (score ≥ 70% on Quiz 1 → unlock Module 2)?
5. Any date-based conditions? (Use sparingly — document the reason)

---

## Condition Types

| Type | What triggers it | Use case |
|---|---|---|
| Visited content topic | Student opens a topic | HTML Topic read, video viewed |
| Completed/incomplete | Topic marked complete | After submission or quiz attempt |
| Achieved a grade | Score on a quiz/assignment | Mastery gating |
| Role | Instructor / Student / TA | Hide admin pages from students |
| Date | Calendar date | Exam windows, term start |
| Group enrollment | Student in a group | Group-specific content |

---

## Output Format

Generate a Release Condition Map:

```
RELEASE CONDITION MAP
Course: [name]
Principle: Completion-based where possible

MODULE SEQUENCE:
Module 1 — Always visible (no condition)
Module 2 — Unlocks when: Module 1 completion signal met
  Completion signal: [Quiz 1 submitted / Topic visited / Assignment submitted]
Module 3 — Unlocks when: Module 2 completion signal met
  Completion signal: [Quiz 2 submitted]

WITHIN-MODULE CONDITIONS:
Module 2 Quiz — Unlocks when: Module 2 reading topic visited
Module 2 Assignment — Unlocks when: Module 2 Quiz score ≥ [X]%

ROLE-BASED CONDITIONS:
[Topic name] — Visible to: Instructor role only
  How to set: Edit topic → Restrictions → Add Release Condition → Role → Instructor

DATE-BASED CONDITIONS (use sparingly):
[Topic name] — Available from [date] to [date]
  Reason: [document why a date condition is needed here]

CONDITION DEPENDENCY CHAIN:
[Visual text diagram showing the unlock sequence]
```

---

## Setup Instructions

After generating the map:

**Sequential module unlock:**
1. Click the module → Edit Properties → Add Release Condition
2. Select condition type → configure → Save
3. Test: View as Student → confirm module is locked → complete condition → confirm unlock

**Role-based (instructor-only):**
1. Click the topic → Edit Properties → Add Release Condition
2. Condition type: Role → select Instructor role → Save
3. Verify in incognito window (student view) that topic is not visible

**Grade-based:**
1. Grade item must exist in gradebook first
2. Topic → Edit Properties → Add Release Condition → Grade → select item → set threshold → Save

---

## Warnings

**Condition chains can lock students out:**
If Module 3 requires Module 2 completion, and Module 2 has a broken completion condition, students can't progress. Always test the full chain in View as Student mode.

**Renaming or deleting items orphans conditions:**
If you rename or delete the quiz, topic, or assignment a release condition depends on, the condition becomes orphaned silently — students may be permanently blocked with no error message.
> "Always check the Release Conditions panel after renaming any item: Course Admin → Release Conditions. Orphaned conditions appear here and can be removed or reassigned."

**Conditions are not copied cleanly:**
After a course copy, verify all release conditions still reference valid items. Grade-based conditions need grade items to be reconnected. Use **brightspace-course-copy-auditor** before every course copy to catch this.

**Date conditions break on course copy:**
Dates do not update automatically after a course copy. If you use date conditions, add them to the post-copy checklist. Use the **brightspace-course-copy-auditor** to flag them.

**Release conditions vs availability dates:**
Release conditions control visibility. Availability dates (start/end dates on topics) control access. They work independently — a topic can be visible but unavailable, or available but not yet unlocked. Decide which you need.

---

## Session End

Offer session summary for planning document. Include the full Release Condition Map.
