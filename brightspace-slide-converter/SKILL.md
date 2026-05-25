---
name: brightspace-slide-converter
description: |
  Converts PowerPoint slides into a complete interactive HTML Topic slide viewer for Brightspace. Use this skill whenever a user wants to turn a slide deck into a navigable Brightspace page. Triggers on phrases like "convert my slides", "make a slide viewer", "turn my PowerPoint into a Brightspace page", "PPTX to HTML", "slide viewer", "navigable slides", or any request to put lecture slides into a Brightspace HTML Topic.
author: Kumar Chandrasekhar, PhD
affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
contact: kchandrasekhar@mtroyal.ca
version: 0.2.0
date: 2026
credits: |
  Developed as part of Designing Interactive Learning Experiences in Brightspace,
  a D2L Academy Customer Spotlight course.
  With contributions from Tim Magee, MS (Academic Development Centre)
  and Glen Ryland, PhD (Department of General Education),
  Mount Royal University.
license: CC BY-NC 4.0
---

# Brightspace Slide Converter

You convert slide decks into complete interactive HTML Topic slide viewers for Brightspace.

## Skill Suite

- **brightspace-redesign-planner** — start here for course-level planning
- **brightspace-html-builder** — any custom HTML Topic
- **brightspace-slide-converter** ← you are here
- **brightspace-accessibility-auditor** — audit the output before publishing

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

**If planning document uploaded:** extract brand colours, course context, architecture choice.

**Otherwise ask:**
1. "Do you have a planning document from a previous session? Upload it to skip setup questions."
2. Brand colours (or neutral palette)
3. How many slide viewers across the course? (determines architecture)

---

## Architecture Recommendation

| Total slide viewers | Recommendation |
|---|---|
| 1–3 | Option A — each HTML file self-contained, `slides/` subfolder alongside |
| 4–10 | Option B — flat folder, shared `css/` and `js/` |
| 10+ | Option C — one subfolder per week/topic |

**Always show the folder diagram before generating the file:**

Option A example:
```
course-folder/
├── week03-slides.html
└── slides/
    ├── week03-slide-01.png
    └── week03-slide-02.png
```

Option C example:
```
course-folder/
├── week03/
│   ├── week03-slides.html
│   └── slides/
│       ├── week03-slide-01.png
│       └── week03-slide-02.png
└── shared/
    ├── css/styles.css
    └── js/scripts.js
```

---

## Filename Validation — Always Check

If the user provides filenames, check immediately:
- Uppercase letters → flag and correct
- Spaces → flag and correct
- Missing zero-padding → flag and correct

**If filenames are non-compliant**, provide a rename table:

| Original | Corrected |
|---|---|
| Week 3 Slide 1.PNG | week03-slide-01.png |
| Week 3 Slide 2.PNG | week03-slide-02.png |

> "I'll use the corrected names in the HTML. Please rename your files to match before uploading to Manage Files."

**Required naming pattern:** `[topic]-slide-[##].png`
- Lowercase only
- Hyphens not spaces
- Zero-padded two-digit slide numbers

---

## Export Instructions (if user hasn't exported yet)

**Windows PowerPoint:** File → Export → Change File Type → PNG → Save Every Slide

**Mac PowerPoint:** File → Export → Format: PNG → Export All

**Google Slides:** File → Download → PNG (current slide) — repeat per slide, or use a Google Apps Script

---

## Slide Data Collection

Ask for each slide:
- Filename (corrected if needed)
- Title (shown in caption and dropdown)
- One-sentence description (shown in caption)

Accept a table, list, or plain description — structure it yourself.

---

## Viewer Features

Generate with:
- Previous / Next buttons (disabled at boundaries)
- Jump dropdown with all slide titles
- Progress bar and slide counter ("Slide 3 of 8")
- Caption area (title + description)
- Keyboard arrow navigation (← →)
- Each image: `alt` = slide description
- `aria-live` on counter
- Mobile responsive at 360px
- 44×44px minimum button targets

---

## Upload Instructions

Always include specific steps with the exact paths for this course:

```
Step 1: In Manage Files, create this folder structure:
[course-folder]/
├── [topic]-slides.html     ← upload HTML file here
└── slides/                 ← create this subfolder
    ├── [topic]-slide-01.png
    └── [topic]-slide-02.png

Step 2: Upload the HTML file to [course-folder]/
Step 3: Create the slides/ subfolder inside [course-folder]/
Step 4: Upload all PNG files into [course-folder]/slides/
Step 5: In Content → Upload/Create → Create a File → browse to [topic]-slides.html
```

The `slides/` subfolder must be INSIDE the same folder as the HTML file — not at the course root. If the subfolder is in the wrong place, images will not load.

---

## Test Checklist

- [ ] All slide images load
- [ ] Previous disabled on slide 1, Next disabled on last
- [ ] Dropdown shows all titles
- [ ] Keyboard ← → navigate slides
- [ ] Caption correct per slide
- [ ] Mobile layout correct at 360px

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Images not loading | Filename case mismatch — check exact case |
| Buttons not working | File added via description editor — use Create a File |
| Wrong slide order | Provide correct order — regenerate slides array |

---

## Session End

Offer session summary for planning document.
