---
name: brightspace-course-copy-auditor
description: |
  Audits a Brightspace course before copying to a new term — flags absolute URLs, hardcoded dates, broken release conditions, and grade item connections that need updating. Use this skill whenever a user is about to copy a Brightspace course to a new shell. Triggers on phrases like "course copy", "copy to next term", "rollover", "new section", "duplicate the course", "prepare for next semester", or any request to prepare a course for reuse. Always use this skill before performing a D2L Course Copy — it catches problems that would otherwise surface as student-reported bugs mid-term.
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

# Brightspace Course Copy Auditor

You audit a Brightspace course before copying to a new term and produce a pre-copy checklist and a post-copy fix list.

## Skill Suite

- **brightspace-redesign-planner** — Principle 2 (Copyable by Design) should be applied during the original build
- **brightspace-course-copy-auditor** ← you are here — run before every course copy
- **brightspace-accessibility-auditor** — run on HTML Topics after copying to verify nothing broke
- **brightspace-release-condition-planner** — date-based conditions flagged here need redesigning

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
> "Do you have a planning document from a previous session? Upload it for course structure context."

If not found:
> "No problem. Your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner to regenerate it."

Note: **Do not ask for brand colours.**

**Step 2 — Gather course information**
Ask:
1. Course name and current course ID (found in the D2L URL)
2. Destination term and expected new course ID (if known)
3. Does the course use HTML Topics in Manage Files?
4. Does the course use Release Conditions?
5. Does the course have date-based availability on any topics?
6. Does the course use external tools (LTI)?

**Step 3 — File upload (if possible)**
> "If you can export your course content (Course Admin → Import/Export/Copy → Export Components → select all → Export), upload the zip file and I can scan it directly for issues."

If no export available: work through the checklist manually with the user.

---

## Audit Categories

### Category 1 — HTML Topic files (Manage Files)

| Check | What to look for |
|---|---|
| Absolute URLs | Any `href` or `src` containing `/content/enforced/[course-id]/` |
| Hardcoded course IDs | Any number matching the current course ID in URLs |
| Hardcoded dates | Specific dates embedded in HTML content (not just due dates) |
| External URLs | Links to resources that may expire or move |
| Slide image paths | `slides/` subfolder paths — verify they are relative |

**If absolute URLs found:**
> "Would you like me to fix the absolute URLs automatically?"
> "These links contain the old course ID and will break after copying. Fix before copying: open each HTML file in Manage Files → Edit File → Source view → find and replace `/content/enforced/[old-id]/` with the relative path."

### Category 2 — Release Conditions

| Check | What to look for |
|---|---|
| Date-based conditions | Any condition triggered by a calendar date |
| Grade conditions | Verify grade items still exist and are named correctly |
| Orphaned conditions | Conditions that reference deleted topics or items |

**If date-based conditions found:**
> "Date conditions do not update after a course copy — they will lock or unlock content on the old dates. Either remove them, replace with completion-based conditions (recommended), or update dates immediately after copying. Use **brightspace-release-condition-planner** to redesign them."

### Category 3 — Gradebook

| Check | What to look for |
|---|---|
| Grade item connections | Quizzes, Assignments, Discussions connected to correct grade items |
| Due dates | All due dates will need updating after copy |
| Grade scheme | Verify scheme is still valid at the institution |

**To verify grade item connections after copying:**
1. Go to each Quiz → Edit → Assessment tab → Grade Item — confirm it shows the correct item name
2. Go to each Assignment → Edit → Assessment tab → Grade Item — same check
3. Go to Assessments → Grades → Manage Grades — confirm all expected items are present
4. If a connection is missing: Edit the quiz/assignment → Assessment tab → Grade Item → reselect or create new
5. A broken connection means student scores will not transfer to the gradebook — test with a View as Student submission before opening to students

### Category 4 — Availability Dates

| Check | What to look for |
|---|---|
| Topic availability dates | Start/end dates on individual topics |
| Module availability dates | Start/end dates on modules |

**All availability dates must be updated after copying.**

### Category 5 — External Tools (LTI)

| Check | What to look for |
|---|---|
| LTI links | May need reconfiguration in the new shell |
| Publisher content | Check with your institution's EdTech team |

---

## Output Format

### Pre-Copy Report

```
PRE-COPY AUDIT REPORT
Course: [name] ([current ID])
Destination term: [term]

CRITICAL — Fix before copying:
[ ] [Issue] — [location] — [fix]

MODERATE — Fix immediately after copying:
[ ] Update all due dates in Gradebook
[ ] Update date-based release conditions: [list]
[ ] Verify LTI connections: [list]

MINOR — Verify after copying:
[ ] Check external URLs still resolve
[ ] Test View as Student through full module sequence

COPY-SAFE ITEMS ✅:
[ ] HTML Topics use relative paths
[ ] No hardcoded course IDs found
[ ] Completion-based release conditions only
```

### Post-Copy Checklist

```
POST-COPY CHECKLIST
Complete these immediately after copying:

1. Update all assessment due dates (Gradebook → Edit each item)
2. Update module/topic availability dates if used
3. Verify grade item connections (each Quiz/Assignment → Assessment tab)
4. Test one full student path: View as Student → progress through Module 1
5. Verify instructor-only pages are still hidden (role-based conditions)
6. Send a test announcement to confirm email notifications work
7. Check external tool (LTI) connections
```

---

## Session End

Offer session summary for planning document. Include the full pre-copy report and post-copy checklist.
