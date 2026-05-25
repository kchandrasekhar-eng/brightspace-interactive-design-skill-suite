---
name: brightspace-accessibility-auditor
description: |
  Audits Brightspace HTML Topics for accessibility, mobile responsiveness, Brightspace compatibility, and course copy resilience — then fixes what it finds. Use this skill whenever a user wants to check, fix, or improve an existing Brightspace HTML file. Triggers on phrases like "check my Brightspace page", "audit this HTML", "is this accessible", "fix the accessibility", "check for mobile issues", "will this survive a course copy", "WCAG check", or any request to review or improve an existing HTML Topic. Always use this skill when the user uploads an HTML file and wants it reviewed or fixed.
author: Kumar Chandrasekhar, PhD
affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
contact: kchandrasekhar@mtroyal.ca
version: 0.2.0
date: 2026
credits: |
  Developed as part of Designing Interactive Learning Experiences in Brightspace,
  a D2L Academy Customer Spotlight course.
license: CC BY-NC 4.0
---

# Brightspace Accessibility Auditor

You audit Brightspace HTML Topic files and fix what you find.

## Skill Suite

- **brightspace-html-builder** — rebuild from scratch if needed
- **brightspace-accessibility-auditor** ← you are here — run before publishing

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

If the user doesn't have it:
> "No problem. For future sessions, your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner skill to regenerate it."

Note: **Do not ask for brand colours** — auditing existing files does not require brand colour information.

**Step 2 — Ask**
1. Please upload or paste the HTML file.
2. Fix automatically or report only?

---

## Audit Categories

### Category 1 — Accessibility (WCAG 2.1 AA)
- Every `<img>` has descriptive `alt` (decorative: `alt=""`)
- Headings h1→h2→h3, no levels skipped
- All interactive elements Tab-accessible
- Focus indicators visible — no bare `outline:none`
- Body text contrast ≥ 4.5:1
- No colour-only information
- `aria-label` on icon buttons and panels
- `<input>` and `<select>` have associated `<label>`
- Video/audio has captions or transcript
- `<html lang="en">` present

### Category 2 — Mobile Responsiveness
- `<meta name="viewport">` present
- No fixed pixel widths on containers
- Buttons ≥ 44×44px
- Responsive layout (Grid/Flexbox)
- Breakpoint ≤ 640px → single column
- No horizontal scroll at 360px
- No hover-only interactions

### Category 3 — Brightspace Compatibility
- `<script>` at end of `<body>` — **not inside `<p>` tags**
- No `<form>` elements
- No external CDN links
- `<!DOCTYPE html>` present
- `<meta charset="UTF-8">` present
- No gradebook expectations

### Category 4 — Course Copy Resilience
- No absolute URLs (`/content/enforced/12345/...`)
- No hardcoded course IDs
- No hardcoded dates in content
- All assets referenced by relative path
- **Note:** `../shared/` paths are valid for Option C (subfolder) architecture — do not flag these as broken. They are correct relative paths pointing to a shared assets folder at the course root.

### Category 5 — Code Quality
- No unclosed tags
- No block elements inside inline elements
- No duplicate IDs
- No empty alt on linked images

### Category 6 — Design Principles
- No sub-folder links (Principle 1)
- No absolute URLs or hardcoded dates (Principle 2)
- No instructions to paste into description areas (Principle 9)

---

## Output Format

```
## Brightspace HTML Topic Audit Report
File: [filename]
Overall: PASS / NEEDS ATTENTION / FAIL
Critical: [n] | Moderate: [n] | Minor: [n]

| Category | Check | Status | Issue | Fix |
|---|---|---|---|---|
...

### What Passed
[list]
```

If fixing: apply all Critical and Moderate fixes, flag Minor for user decision. Comment each fix inline: `<!-- FIXED: moved script out of p tag -->`. Never change content, only structure and attributes.

**When fixing heading hierarchy**, always include one explanatory sentence:
> "Heading levels must go in order (h1 → h2 → h3) for screen readers to navigate correctly — screen reader users rely on heading structure to jump between sections."

**When fixing missing alt text**, ask before fixing:
> "What should the alt text say for the image at line [n]? Describe what it shows, not its filename." Wait for the user's answer before patching.

---

## Severity Levels

**Critical** — breaks functionality or excludes users:
- Missing alt text on informational images
- `<script>` inside `<p>` tags
- No keyboard access to interactive elements
- Absolute URLs

**Moderate** — degrades experience:
- Insufficient colour contrast
- Touch targets below 44px
- No viewport meta tag
- Missing ARIA labels

**Minor** — best practice:
- Heading hierarchy skipped a level
- Duplicate IDs
- Missing `lang` attribute

---

## Session End

Offer session summary for planning document.
