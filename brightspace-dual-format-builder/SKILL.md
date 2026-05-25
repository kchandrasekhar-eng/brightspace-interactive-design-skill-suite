---
name: brightspace-dual-format-builder
description: |
  Builds a dual-format course system for Brightspace that lets instructors switch an entire course between Online Asynchronous and In-Person delivery with a single configuration change. Use this skill whenever a user needs a course that can run in two delivery modes, wants instructors to be able to toggle the format without editing code, or needs separate schedule configurations for each format. Triggers on phrases like "dual format course", "online and in-person switch", "toggle between async and in-person", "course format switch", "same course two delivery modes", or any request to build a Brightspace course that supports both delivery formats. Reference implementation: UGST 1001 (Effective Learning in the Undergraduate Context), Mount Royal University.
author: Kumar Chandrasekhar, PhD
affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
contact: kchandrasekhar@mtroyal.ca
version: 0.1.0
date: 2026
credits: |
  Developed as part of Designing Interactive Learning Experiences in Brightspace,
  a D2L Academy Customer Spotlight course. Reference implementation: UGST 1001
  (Effective Learning in the Undergraduate Context), Mount Royal University.
  With contributions from Tim Magee, MS (Academic Development Centre)
  and Glen Ryland, PhD (Department of General Education),
  Mount Royal University.
license: CC BY-NC 4.0
---

# Brightspace Dual-Format Course Builder

You build dual-format Brightspace course systems that allow instructors to switch an entire course between Online Asynchronous and In-Person delivery with a single configuration change — no code editing required.

## Reference Implementation

This skill is based on UGST 1001 (Effective Learning in the Undergraduate Context) at Mount Royal University — a course that runs in both online asynchronous and in-person sections using the same D2L shell, switching format via a single configuration file.

## Skill Suite

This skill is part of the **Brightspace Interactive Design Skill Suite**:
- **brightspace-redesign-planner** — start here for course-level planning; dual-format is a design decision documented in the planning document
- **brightspace-dual-format-builder** ← you are here
- **brightspace-html-builder** — builds individual session HTML Topic files
- **brightspace-accessibility-auditor** — audit all generated files before publishing

When a user's redesign plan includes both online and in-person delivery, suggest this skill automatically.

---

## How the System Works

The dual-format system has three layers:

**Layer 1 — Configuration**
A single source-of-truth file (`shared/course-config.js`) holds the current format:
```js
window.COURSE_FORMAT = "inperson"; // or "async"
```

**Layer 2 — Schedule configuration pages**
Two separate instructor-facing HTML pages (hidden from students via Release Conditions):
- `shared/course-schedule-inperson.html` — instructor enters two class dates per session
- `shared/course-schedule-async.html` — instructor enters one week range per session

**Layer 3 — Session pages**
Every student-facing session page reads `course-config.js` and renders format-appropriate content: in-person shows class dates, room, activities; async shows week range, online activities.

**Instructor workflow:**
- Edit one word in `course-config.js` via Manage Files → Edit File
- OR use the hidden admin page with a visible toggle button (no code editing)

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
> "Do you have a planning document from a previous session? Upload it to skip setup questions."

**Step 2 — Experience level**
> "How would you like to proceed?
> **A — Wizard** (recommended for first-timers): I walk you through every file one at a time with explanations.
> **B — Batch** (experienced users): I generate all files at once with setup instructions."

**Step 3 — Toggle mechanism**
> "How should instructors switch the course format?
> **Option 1 — course-config.js**: Instructor edits one word in a JS file via Manage Files. Simple, no extra page needed.
> **Option 2 — Admin page**: A hidden HTML page with a visible toggle button. No code editing at all — instructor clicks a button and saves. Requires Release Conditions to hide from students.
> **Option 3 — Both**: Generate both mechanisms. Admin page for day-to-day use, config file as a fallback."

**Step 4 — Collect course details**
1. Course name and code
2. Institution and brand colours
3. Number of sessions/weeks
4. Session naming convention (Session 1 / Week 1 / Module 1)
5. In-person: days of week, time, room
6. Async: week start/end days
7. Is there a reading break or other interruption?
8. What format-specific content differs between modes? (dates, activities, instructions)

---

## Architecture

Always show this folder structure before generating any files:

```
course-folder/
├── index.html                          ← course home (reads config)
├── session-01.html                     ← session page (reads config)
├── session-02.html
├── ...
└── shared/
    ├── course-config.js                ← THE SWITCH (one word to change)
    ├── course-schedule-inperson.html   ← instructor config (hidden from students)
    ├── course-schedule-async.html      ← instructor config (hidden from students)
    ├── admin/
    │   └── format-control.html         ← admin toggle page (Option 2/3 only)
    ├── css/
    │   └── styles.css
    └── js/
        └── course.js                   ← reads config, applies format
```

---

## Wizard Mode — Step by Step

Walk through these steps one at a time, waiting for confirmation before proceeding:

### Step W1 — course-config.js
Generate the configuration file. Explain:
> "This is the single switch for your entire course. Instructors change one word here — 'inperson' or 'async' — and every session page updates automatically."

```js
// ═══════════════════════════════════════════════════════════
// [COURSE NAME] — COURSE FORMAT CONFIGURATION
// ═══════════════════════════════════════════════════════════
//
// This file controls whether students see the In-Person format
// or the Online Asynchronous format throughout the course.
//
// TO CHANGE THE FORMAT:
//   Change the word below to "inperson" OR "async"
//   Keep the quotation marks.
//   Save the file. The change takes effect immediately.
//
// DO NOT MODIFY ANYTHING ELSE IN THIS FILE.

window.COURSE_FORMAT = "inperson";
```

**How instructors edit it:**
1. Course Admin → Manage Files
2. Navigate to `shared/course-config.js`
3. Click the dropdown arrow → Edit File
4. Change `"inperson"` to `"async"` (or back)
5. Click Save

### Step W2 — course.js (shared JavaScript)
Generate the shared JS that reads the config and applies format:
- Reads `window.COURSE_FORMAT`
- Shows/hides format-specific elements using `data-format="inperson"` and `data-format="async"` attributes
- Displays a preview banner if no schedule is configured
- `Ctrl+Shift+F` keyboard shortcut — toggles format in instructor's browser only, no effect on students

### Step W3 — In-person schedule config page
Generate `course-schedule-inperson.html`:
- Instructor enters two class dates per session (e.g. Tue Sep 9 / Thu Sep 11)
- Stale-date detection — warns instructor if dates are from a previous term
- "Unconfigured" state with clear instructions when opened fresh
- Saves to `localStorage` so dates persist across sessions

### Step W4 — Async schedule config page
Generate `course-schedule-async.html`:
- Instructor enters one week range per session (e.g. Sep 8–12)
- Same stale-date detection and unconfigured state

### Step W5 — Admin page (if Option 2 or 3)
Generate `shared/admin/format-control.html`:
- Shows current format from `course-config.js`
- Large, clear toggle button — no code visible
- Instructor-only preview toggle (changes only their browser view)
- Step-by-step instructions for hiding from students via Release Conditions
- Verification checklist

### Step W6 — Session page template
Generate one complete session HTML file showing:
- Format-specific content blocks using `data-format` attributes
- In-person block: class 1 date, class 2 date, room, in-person activities
- Async block: week range, online activities, self-paced instructions
- Preview banner when schedule not configured
- Navigation (previous/next session)

### Step W7 — Release Conditions setup
Provide exact D2L instructions for hiding instructor pages from students:
1. Content → click the three-dot menu on the schedule/admin topic
2. Edit Properties → Add Release Condition
3. Condition type: Role → Instructor (or custom instructor role at the institution)
4. Save
5. Verify: open an incognito window and confirm the page is not visible

### Step W8 — Testing checklist
Provide a complete verification checklist before going live.

---

## Batch Mode

Generate all files at once in the correct folder structure. Include:
1. `shared/course-config.js`
2. `shared/js/course.js`
3. `shared/course-schedule-inperson.html`
4. `shared/course-schedule-async.html`
5. `shared/admin/format-control.html` (if Option 2 or 3)
6. One complete session page template with `data-format` blocks
7. Full setup instructions document
8. Release Conditions setup steps
9. Testing checklist

---

## Format-Specific Content Blocks

Use `data-format` attributes to show/hide content:

```html
<!-- In-person content -->
<div data-format="inperson">
  <p><strong>Class 1:</strong> <span class="session-date-1">TBD</span> — Room Y318</p>
  <p><strong>Class 2:</strong> <span class="session-date-2">TBD</span> — Room Y318</p>
</div>

<!-- Async content -->
<div data-format="async">
  <p><strong>Week:</strong> <span class="session-week">TBD</span></p>
  <p>Work through the materials below at your own pace this week.</p>
</div>
```

The shared `course.js` reads `window.COURSE_FORMAT` on page load and shows only the matching blocks.

---

## Preview Banner

When schedule is not yet configured, show this banner on session pages:

```html
<div class="preview-banner">
  📅 <strong>Preview mode</strong> — Schedule not yet configured for
  <span id="formatLabel">In-Person</span> format.
  <a href="../shared/course-schedule-inperson.html">Set up schedule →</a>
</div>
```

---

## Core Rules

All rules from **brightspace-html-builder** apply plus:
- `course-config.js` is the single source of truth — never hardcode the format in session pages
- All paths relative — no absolute Brightspace URLs
- Admin and schedule pages hidden from students via Release Conditions — never rely on obscurity alone
- `localStorage` for schedule data — no server-side storage
- `Ctrl+Shift+F` preview shortcut documented in instructor notes only — not visible to students
- Stale-date detection on all schedule pages — warn when dates are from a previous term

---

## Updating for a New Term

Provide these instructions at the end of every session:

**Each new term, the instructor needs to:**
1. Update dates in `course-schedule-inperson.html` and/or `course-schedule-async.html`
2. Set `window.COURSE_FORMAT` in `course-config.js` to the correct format for this section
3. Verify in an incognito window that students see the right format

**Mid-term format switch:**
If the format changes mid-semester (e.g. in-person section moves online):
> "Students currently viewing a session page will see the old format until they refresh their browser. Post an announcement explaining the change before switching the config — use the **brightspace-announcement-writer** skill to draft it quickly. Then switch the format. Students who refresh will immediately see the updated content." 

**Course copy note:** Because all paths are relative and no course IDs are hardcoded, the entire system survives a D2L Course Copy without breaking. Only the dates need updating.

---

## Session End

Offer session summary for planning document. Include:
- Which toggle mechanism was chosen
- Which files were generated
- Release Conditions steps completed
- What still needs to be done before publishing
