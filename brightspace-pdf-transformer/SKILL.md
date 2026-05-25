---
name: brightspace-pdf-transformer
description: |
  Transforms static PDF readings into interactive Brightspace HTML Topics with structured sections, expandable key terms, comprehension questions, and a before/after toggle. Use this skill whenever a user wants to convert a PDF, Word document, or static reading into an interactive Brightspace page. Triggers on phrases like "turn this PDF into a Brightspace page", "make this reading interactive", "PDF to HTML Topic", "transform this document", "interactive reading page", or any request to make a static document interactive in Brightspace.
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

# Brightspace PDF Transformer

You transform static PDF readings into interactive Brightspace HTML Topics.

## Skill Suite

- **brightspace-redesign-planner** — course-level planning
- **brightspace-html-builder** — custom HTML Topics
- **brightspace-pdf-transformer** ← you are here
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

**Step 1 — Check for planning document**
> "Do you have a planning document from a previous session? Upload it to skip setup questions."

If uploaded: extract brand colours, course context, architecture choice.

**Step 2 — Copyright check (mandatory gate)**

Before any other questions:
> "Before we begin — do you have the right to use this content in your course? This includes:
> ✓ Readings you wrote yourself
> ✓ Open-access articles
> ✓ Materials your library has licensed for course use
> ✗ Publisher textbook chapters (typically cannot be reproduced)
> ✗ Paywalled journal articles (check with your library first)
>
> Creating an interactive version does not change the copyright status. If you're unsure, check with your institution's library or copyright office before proceeding."

Do not proceed until confirmed.

**Step 3 — Architecture**
How many interactive readings across the course? Recommend architecture (same logic as other skills).

---

## Architecture Recommendation

| Reading count | Recommendation |
|---|---|
| 1–3 | Option A — HTML file + PDF in same folder |
| 4–10 | Option B — flat course folder, shared assets |
| 10+ | Option C — one subfolder per reading |

**Always show folder diagram:**

Option A:
```
course-folder/
├── week04-reading.html
└── week04-reading.pdf      ← same folder, relative link works
```

Option C:
```
course-folder/
├── week04/
│   ├── week04-reading.html
│   └── week04-reading.pdf
└── shared/
    ├── css/styles.css
    └── js/scripts.js
```

---

## Content Collection

Ask for:
1. Full text of the reading (paste or upload)
2. Course context (module name, how reading fits)
3. 3–5 main sections with one-sentence descriptions
4. 3–5 key terms with plain-language definitions
5. 1–2 comprehension questions (question, 4 choices, correct answer, feedback)
6. Include before/after toggle? (yes/no)

If user isn't sure about structure, suggest one based on the text provided.

---

## Output Features

Generate with:
- Reading title, author, course context
- Download link to original PDF (relative path, `download` attribute)
- Section navigation (jump links)
- Key terms highlighted inline — click/hover to reveal definition
- Comprehension questions with immediate feedback (formative only)
- Before/after toggle (if requested)
- WCAG 2.1 AA — keyboard accessible, alt text, contrast
- Mobile responsive at 360px

---

## Upload Instructions

Always include — **order matters**:

```
Step 1: Create the folder in Manage Files:
[course-folder]/
├── [topic]-reading.html
└── [topic]-reading.pdf     ← PDF and HTML must be in the same folder

Step 2: Upload the PDF file FIRST into [course-folder]/
Step 3: Upload the HTML file into the SAME folder
Step 4: In Content → Upload/Create → Create a File → browse to [topic]-reading.html
```

> ⚠️ Upload the PDF before the HTML. If you add the HTML Topic to Content first and the PDF isn't in the same folder yet, the download link will be broken when students first visit the page.

---

## Test Checklist

- [ ] Sections display correctly
- [ ] Key terms expand on click
- [ ] Comprehension question shows feedback
- [ ] PDF download link works
- [ ] Before/after toggle works (if included)
- [ ] Mobile layout correct

---

## Troubleshooting

| Problem | Fix |
|---|---|
| PDF link broken | PDF must be in same folder as HTML, exact filename |
| Question not working | Added via description editor — use Create a File |
| AI paraphrased the text | Split into two prompts: structure first, then paste full text |

---

## Session End

Offer session summary for planning document.
