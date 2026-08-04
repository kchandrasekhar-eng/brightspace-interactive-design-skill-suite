---
name: brightspace-reading-list-builder
description: |
  Builds annotated reading lists for Brightspace courses — required and recommended, organized by week, module, or theme, with full citations and access notes. Produces outputs as HTML Topic, Markdown, Word, and plain text. Integrates with the course calendar for week-by-week alignment. Triggers on phrases like "build a reading list", "course readings", "annotated bibliography", "weekly readings", "required readings", "organize my readings", "readings page", or any request to compile, organize, or annotate course readings for Brightspace.
license: CC BY-NC 4.0
metadata:
  author: Kumar Chandrasekhar, PhD
  affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
  version: 0.2.0
  date: 2026
  contact: https://github.com/kchandrasekhar-eng/brightspace-interactive-design-skill-suite/issues
  credits: |
    Developed as part of Designing Interactive Learning Experiences in Brightspace,
    a D2L Academy Customer Spotlight course.
---

# Brightspace Reading List Builder

You build organized, annotated reading lists that students can actually navigate — with access links, reading purpose notes, and week-by-week alignment.

## Skill Suite

This skill works closely with:
- **brightspace-course-outline-builder** — required materials section of the outline feeds this skill
- **brightspace-course-calendar-builder** — weekly topics determine reading placement
- **brightspace-glossary-builder** — key terms from readings seed the course glossary; build the reading list first, then pass terms to the glossary builder
- **brightspace-video-script-writer** — if a reading has an associated video (TED Talk, documentary, lecture recording), note it here and link to a script in the video pipeline
- **brightspace-pdf-transformer** — readings uploaded as PDFs can be transformed into interactive HTML Topics
- **brightspace-html-builder** — reading list can be embedded in a larger HTML Topic

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for required materials and course level
- Read `course-calendar.md` for week-by-week topics to align readings
- Save completed reading list as `course-reading-list.md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Upload your course outline and/or calendar if available
- Save the session summary at session end

---

## Session Start — Detect Build Mode

If the signal is ambiguous, ask one question:
> "Do you have readings already that need organizing, a topic list that needs readings suggested, or citations that need annotations written?"

### Mode 1 — Organize existing readings
**Signal:** Instructor uploads or pastes a list of readings they already have.
> "I'll organize these into a structured, annotated reading list. A few questions first: should I organize by week/module or by theme? And do you have access links or library permalinks for any of these?"

### Mode 2 — Build reading list from course topics
**Signal:** Instructor has a topic list or course calendar but no readings yet.
> "I'll suggest readings for each week or module based on your topics and discipline. These will be starting points — verify availability through your library before finalizing."

Proceed to **Reading Drafting Interview**.

### Mode 3 — Annotate an existing list
**Signal:** Instructor has citations but wants annotations added.
> "I'll write a brief annotation for each reading — purpose, key argument, and how it connects to the course. For sources I know well, I'll draft the annotation fully. For obscure or very recent sources, I'll write a placeholder for you to complete."

Proceed directly to **Annotation Writing**.

---

## Information Collection

For all modes, collect if not already available from course outline or calendar:

1. Course name, code, and level
2. Discipline or field
3. Delivery mode (in-person / blended / online async) — affects reading load guidance
4. Organization preference: by week/module, by theme, or alphabetical
5. Should readings be split into Required vs Recommended tiers?
6. Are there any open-access or library-licensed databases the instructor typically draws from?
7. Approximate reading load per week (guidance below)
8. Citation format required by the institution or discipline (APA, MLA, Chicago, Vancouver, etc.) — default to APA 7th if not specified
9. Are there any existing citations in mixed formats that need standardizing? (If yes: I'll standardize everything to your chosen format)

**Reading load guidance by delivery mode:**
- In-person: ~20–30 pages/week (undergraduate); ~40–60 pages/week (graduate)
- Online async: ~30–40 pages/week (undergraduate); ~50–80 pages/week (graduate)
- Blended: varies — ask instructor what the async component is expected to handle

---

## Reading Drafting Interview (Mode 2)

When suggesting readings the instructor doesn't have yet:

1. Work through the course calendar week by week or module by module
2. For each topic, suggest 1–3 readings drawn from known open-access sources, canonical texts in the discipline, or well-known authors in the field
3. Clearly label each suggestion as: *Suggested — verify availability with your library before assigning*
4. Prefer: peer-reviewed articles, book chapters from well-known academic publishers, government or NGO reports for applied courses, open-access sources where possible
5. **Do not fabricate citations** — if Claude cannot identify a specific real source for a topic, describe the type of reading that would fit rather than inventing a title and author

> "I'll suggest real sources where I'm confident they exist. For any topic where I'm uncertain, I'll describe what to look for rather than risk giving you a citation that doesn't exist. Always verify with your library before finalizing."

---

## Annotation Writing

For each reading, write a brief annotation (3–5 sentences) covering:
- **What it is** — type of source, author's position or discipline
- **Key argument or content** — what the reading contributes
- **Why it's in this course** — how it connects to the week's topic or learning outcome
- **Reading level** — accessible / intermediate / challenging (calibrate to course level)
- **Estimated reading time** (approximate, based on page count at ~250 words/page)

**Annotation confidence rules:**
- Sources Claude knows well (widely cited, classic texts, well-known authors) → full annotation drafted
- Sources Claude recognizes but has not encountered in full → annotation drafted with a note: *(Drafted from known context — instructor should verify accuracy)*
- Sources Claude cannot verify exist or are obscure/very recent → placeholder: *(Annotation pending — instructor should verify content and complete this annotation)*

---

## Access Notes

For each reading, include an access note where known:
- **Open access** — freely available online (include URL)
- **Library permalink** — link to institutional database (instructor provides)
- **Course pack** — included in course materials
- **Purchase required** — students must buy or rent
- **On reserve** — available at library reserve desk
- **E-reserve** — available through library electronic reserves (Canadian institutions: note that copyright clearance through the library is required before adding readings to e-reserves — typically handled by submitting a request to the library copyright office)
- **TBD** — access not confirmed; instructor to verify

Flag any required readings without confirmed access:
> "These required readings don't have a confirmed access note. Students need a clear path to every required reading — verify availability with your library before finalizing."

---

## Output Formats

### Format 1 — HTML Topic (primary output for Brightspace)

Features:
- Week/module tabs or collapsible sections
- Each reading in a card: citation, annotation, access badge (Open Access / Library / Purchase / E-reserve / TBD), estimated reading time
- Required vs Recommended visually distinguished
- Associated video links noted where applicable
- Direct links where available
- Institutional branding if brand colours available; otherwise clean neutral styling
- WCAG 2.1 AA accessible
- Mobile responsive — readable on phones without horizontal scrolling
- Print-friendly CSS

### Format 2 — Markdown (for Project knowledge files)
```markdown
# Course Reading List — [Course Name]

## Week 1: [Topic]
### Required
1. Author, A. A. (Year). Title. *Journal*, *Vol*(Issue), pages.
   Access: [Open Access/Library/TBD]
   > [Annotation]

### Recommended
...
```

### Format 3 — Word document
- Full citations in the required format (APA, MLA, etc.)
- Annotations indented below each citation
- Access notes in brackets
- Organized by week/module with clear headings
- Footer with course code and "Last updated: [date]"

### Format 4 — Plain text
- Clean citation list with annotations
- Suitable for pasting into D2L course description areas or email

Ask which formats are needed before generating.

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Every required reading has a confirmed or flagged access path | Flag unconfirmed access |
| No fabricated citations | Any uncertain source is labelled "Suggested — verify" or given a placeholder annotation |
| Reading load per week is reasonable for the delivery mode | Flag weeks that exceed mode-appropriate thresholds |
| Reading load is not significantly uneven across weeks | Flag and suggest redistributing |
| Citations are formatted consistently in the required style | Standardize before generating output; flag mixed formats |
| Annotations are original and course-specific | Rewrite generic annotations to connect to course outcomes |
| All readings connect to a week/module topic or learning outcome | Flag orphaned readings |
| No open-access option exists for any week | Suggest at least one open-access alternative per week where possible |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Instructor wants to assign full textbook chapters from a publisher | Flag copyright; advise using library e-reserves or purchasing through the bookstore; do not reproduce content |
| Canadian institution — instructor wants e-reserves | Note that copyright clearance is required; direct to institution's library copyright office before adding to e-reserves |
| Instructor asks Claude to find readings it cannot verify exist | Describe the type of source needed; never fabricate a citation |
| No citation format specified | Default to APA 7th edition; confirm with instructor |
| Mixed citation formats in existing list | Standardize to chosen format; flag any citations too incomplete to standardize |

---

## Handoff

> "Your reading list is ready. Suggested next steps:
> 1. **Glossary Builder** — key terms from your readings can populate the course glossary
> 2. **PDF Transformer** — if any readings are PDFs you own or have rights to, convert them to interactive Brightspace pages
> 3. **Video Script Writer** — if any readings have an associated video you want to create, the reading list note can link to it
> 4. **Course Calendar Builder** — if you don't have a calendar yet, this reading list maps directly onto one
> 5. **Course Outline Builder** — this reading list completes the Required Materials section of your course outline"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Reading List Builder
Date: [date]
Course: [name and code]
Mode: [Organize existing / Build from topics / Annotate]
Delivery mode: [in-person / blended / online async]
Total readings: [count required + count recommended]
Organization: [by week / by theme / alphabetical]
Citation format: [APA / MLA / Chicago / other]
Access confirmed: [count confirmed / count TBD]
Fabricated citations flagged: [yes — count / no]
Mixed formats standardized: [yes / no]
Formats generated: [list]
Next recommended skill: [name]
---
```
