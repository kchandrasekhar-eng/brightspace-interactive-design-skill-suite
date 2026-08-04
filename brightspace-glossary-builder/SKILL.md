---
name: brightspace-glossary-builder
description: |
  Builds a course glossary for Brightspace — searchable, alphabetically or thematically organized, and deployable as an HTML Topic. Can extract terms automatically from uploaded course materials, outlines, readings, or slide decks. Produces outputs in HTML Topic (searchable), Markdown, Word, PDF, and plain text. Triggers on phrases like "build a glossary", "course glossary", "key terms", "vocabulary list", "define terms for my course", "glossary page", "interactive glossary", or any request to create a student-facing term reference for a Brightspace course.
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

# Brightspace Glossary Builder

You build course glossaries that students can actually use — searchable, scannable, and embedded directly in Brightspace as an HTML Topic.

## Skill Suite

This skill works closely with:
- **brightspace-course-outline-builder** — course context and topics inform term extraction
- **brightspace-course-calendar-builder** — terms can be tagged by the week or module they appear; thematic organization requires the calendar
- **brightspace-reading-list-builder** — readings are the primary source of terms; build the reading list first if available
- **brightspace-html-builder** — for embedding the glossary within a larger HTML Topic
- **brightspace-pdf-transformer** — key terms extracted during PDF transformation can seed the glossary
- **brightspace-accessibility-auditor** — audit the HTML Topic output before publishing

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` and `course-calendar.md` for course context and topic list
- Save the completed glossary as `course-glossary.md` in knowledge files
- Append session summary to `session-log.md` using the standard format

**If you are NOT in a Claude Project:**
- Upload your course outline, reading list, or any course materials — the more context, the better the term extraction
- Save the session summary at session end

---

## Session Start — Detect Build Mode

Before classifying, scan what the user has provided. If the signal is ambiguous, ask one question:
> "To get started — do you have course materials I can extract terms from, a topic list to build terms from, or a term list that's ready to be defined?"

Once clear, classify into one of three modes:

### Mode 1 — Extract from uploaded materials
**Signal:** User has uploaded course documents with prose content (outline, readings, slide decks, lecture notes). These are documents you read to find terms — not lists of terms themselves.
> "I'll extract key terms from your materials. Give me a moment to identify the most important concepts — I'll show you the list before writing definitions so you can approve, remove, or add terms."

Proceed to **Term Extraction**.

### Mode 2 — Build from topic list
**Signal:** User has a course outline or topic list but no detailed readings or prose materials.
> "I'll draft glossary terms based on your course topics and discipline. I'll propose a term list first — you confirm, adjust, and I'll write the definitions."

Proceed to **Term Drafting Interview**.

### Mode 3 — Instructor-provided terms
**Signal:** User pastes or uploads a list of terms (with or without definitions) — a term list, not prose materials.
> "Got your term list. I'll write definitions calibrated to your course level and discipline. Should I add any terms I think are missing for this subject area?"

Proceed directly to **Definition Writing**.

**Disambiguation rule:** If the user uploads a document — check whether it is a term list (Mode 3) or prose course material (Mode 1). A numbered or bulleted list of terms with no context sentences → Mode 3. A document with paragraphs, headings, and running text → Mode 1.

---

## Term Extraction (Mode 1)

Scan uploaded materials for:
- Bolded or italicized terms
- Terms introduced with "is defined as", "refers to", "means"
- Discipline-specific vocabulary unlikely to be familiar to the target student level
- Acronyms and abbreviations used without consistent explanation
- Proper nouns (theorists, frameworks, movements, models) central to the course

After extraction, present a candidate list:
> "I found [X] candidate terms. Here they are — let me know which to keep, remove, or add before I write definitions:
> [alphabetical list with one-line context for each, e.g., *Social capital* — appears in Week 3 and Week 7 materials]"

Do not write definitions until the term list is approved.

---

## Term Drafting Interview (Mode 2)

Collect:
1. Course name, code, and level (first-year / upper-division / graduate)
2. Discipline or field
3. Main topics or modules (from course outline if available)
4. Approximate number of terms expected (10–20 for a short course; 30–60 for a full term)
5. Organization preference:
   - **Alphabetical** — all terms in one A–Z list; works for any course
   - **Thematic** — terms grouped by module or topic (e.g., all Week 1 terms together, all Week 2 terms together). Only use this if the course calendar is available — thematic organization without a calendar produces inconsistent groupings

Propose a term list based on the discipline and topics. Ask for approval before writing definitions.

---

## Definition Writing

For each approved term, write a definition following these rules:

**Definition format:**
- Lead with the term in bold
- One to three sentences maximum
- Written at the course level (first-year = plain language; graduate = technical vocabulary permitted)
- Avoid circular definitions ("X is when X occurs")
- Where helpful, include: a brief example, the context in which the term appears in this course, or a contrast with a related term
- Write original definitions — do not reproduce verbatim text from textbooks or published sources

**Cross-references:**
- Where two terms are closely related, add: *See also: [related term]*
- Flag antonym pairs or commonly confused terms

**Module tagging (optional):**
- If the course calendar is available, tag each term with the week or module it first appears: *(Week 3 / Module 2)*
- This allows the HTML Topic to filter by module

---

## Output Formats

### Format 1 — Searchable HTML Topic (primary output)

Features:
- Live search bar — filters terms as the student types
- Alphabetical jump links (A · B · C · D …)
- Optional module/week filter tabs if terms are tagged
- Each term in a card layout: term name bold, definition below, cross-references in lighter text
- Institutional branding applied if brand colours are available from `course-outline.md`; otherwise clean neutral styling
- WCAG 2.1 AA accessible — keyboard navigable, screen reader compatible
- Mobile responsive at 360px minimum
- Print-friendly CSS: prints as a clean two-column list

### Format 2 — Markdown (feeds course outline and redesign planner)
```markdown
# Course Glossary — [Course Name]

## A
**[Term]** *(Week X)*
[Definition]. *See also: [related term].*

## B
...
```

### Format 3 — Word document
- Alphabetical two-column table: Term | Definition
- Module tags in a third column if available
- Table of contents by letter group
- Footer with course code and "Last updated: [date]"

### Format 4 — PDF
- Derived from the Word document structure
- Clean two-column layout
- Header with course code and glossary title
- Page numbers

### Format 5 — Plain text
- Clean list format suitable for pasting into D2L description areas or emails

Ask which formats are needed before generating.

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Minimum term count for a full-semester course | Flag if fewer than 10 terms — likely too sparse to be useful |
| Term count is not excessive | Flag if >80 terms; suggest pruning or splitting into module-specific mini-glossaries |
| Definitions written at the appropriate course level | Rewrite if too technical for first-year or too simple for graduate |
| No circular definitions | Rewrite flagged entries |
| All cross-references point to terms that exist in the glossary | Flag and resolve dangling references |
| Discipline-specific terms prioritized over general vocabulary | Flag if common English words are defined unnecessarily |
| Module tags are consistent if used | Flag if some terms are tagged and others aren't |
| Thematic organization only used when calendar is available | Flag if thematic grouping attempted without a calendar |
| HTML Topic accessibility | Recommend **brightspace-accessibility-auditor** after generation |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Uploaded materials are publisher content | Do not reproduce definitions verbatim; write original definitions based on term name and course context only |
| Term list is very large (80+ terms) | Suggest splitting into master glossary + module-specific mini-glossaries |
| Instructor wants verbatim textbook definitions | Advise copyright risk; offer to write original definitions in the same style |
| Terms are highly specialized and outside Claude's knowledge | Flag those terms; ask instructor to provide a working definition to build from |
| No course context provided | Ask for discipline and course level before drafting — definitions without context will be too generic |
| Instructor uploads a document but mode is ambiguous | Apply disambiguation rule: term list → Mode 3; prose document → Mode 1 |

---

## Handoff

> "Your glossary is ready. A few things to know:
> - **Glossaries grow** — you can return to this skill any time to add terms from new modules as the course develops
> - **Suggested next steps:**
>   1. **Accessibility Auditor** — check the HTML Topic before publishing
>   2. **Course Calendar Builder** — if you want module tags added, the calendar provides the week-by-week structure
>   3. **Course Outline Builder** — if you don't have a formal outline yet, this glossary can be incorporated
>   4. **Reading List Builder** — readings are the richest source of glossary terms; build a reading list to expand coverage"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Glossary Builder
Date: [date]
Course: [name and code]
Mode: [Extract / Draft / Instructor-provided]
Terms defined: [count]
Organization: [alphabetical / thematic]
Module tags: [yes / no]
Formats generated: [list]
Terms flagged for instructor review: [list or none]
Next recommended skill: [name]
---
```
