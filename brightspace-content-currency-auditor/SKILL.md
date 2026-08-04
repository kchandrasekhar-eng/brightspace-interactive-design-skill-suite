---
name: brightspace-content-currency-auditor
description: |
  Audits course content for outdated information, broken or stale links, expired statistics, superseded policies, and readings that are no longer accessible or relevant. Produces a flagged report with severity ratings and recommended fixes. Run before course copy or at the start of a new term. Triggers on phrases like "audit my course content", "check for outdated content", "broken links", "stale readings", "is my content current", "content review", "update my course materials", or any request to check whether course content is still accurate and accessible.
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

# Brightspace Content Currency Auditor

You audit course content for accuracy, accessibility, and relevance — and produce a prioritized fix list the instructor can act on before the course goes live.

## Skill Suite

This skill works closely with:
- **brightspace-course-copy-auditor** — run that skill first for structural issues (broken release conditions, hardcoded dates, absolute URLs); run this skill for content accuracy issues
- **brightspace-reading-list-builder** — stale or inaccessible readings flagged here can be replaced using the reading list builder
- **brightspace-html-builder** — outdated HTML Topic content can be rebuilt with this skill
- **brightspace-accessibility-auditor** — run after content fixes to confirm HTML Topics still meet accessibility standards
- **brightspace-student-experience-preview** — run after content fixes to check how updates affect student navigation
- **brightspace-course-outline-builder** — policy statements in the outline may also need updating
- **brightspace-session-debrief** — close out the audit session with a structured summary

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md`, `course-reading-list.md`, and `course-calendar.md` for content inventory
- Save the audit report as `content-currency-audit.md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Upload course materials for review: HTML Topic files, reading lists, course outline, slide decks
- The more content uploaded, the more thorough the audit

---

## Session Start — Scope the Audit

First, check what has been uploaded or is available in Project knowledge files. If materials are already present, acknowledge them:
> "I can see you've uploaded [list of files]. I'll use these as the basis for the audit."

Then ask:
> "What would you like me to audit? You can choose one or more:"
> 1. Reading list and assigned resources (links, access, relevance)
> 2. HTML Topic pages (statistics, dates, references, examples)
> 3. Course policies (AI policy, late policy, accessibility statement)
> 4. Course schedule (dates, exam periods, holiday references)
> 5. Video or media content (broken embeds, outdated platform links)
> 6. Everything you can upload

Also ask:
> "When was this course last substantially updated? (This helps me calibrate how urgently each flag needs attention. If you're not sure, I'll infer from content dates in the uploaded materials.)"

---

## Audit Categories

### Category 1 — Reading list and assigned resources

**Field calibration note:** Reading age is field-dependent. Flag age only in fields where currency matters (sciences, law, technology, medicine, social policy). Humanities, philosophy, history, and foundational theory readings may be decades old and still entirely appropriate — do not flag these on age alone.

For each reading or resource in the course:

| Check | Flag level | Action |
|---|---|---|
| URL is reachable and resolves correctly | 🔴 Critical | Replace or find new access path |
| Open-access link still points to the correct version | 🟡 Medium | Verify and update URL |
| Library permalink is still valid for this institution | 🟡 Medium | Instructor to verify with library |
| Reading is from more than 5 years ago in a fast-moving field (sciences, law, tech, medicine) | 🟡 Medium | Flag for instructor review — may still be appropriate |
| Reading is from more than 10 years ago in a fast-moving field | 🟠 High | Flag for instructor review — consider updating |
| Reading references superseded standards, legislation, or guidelines | 🔴 Critical | Replace or add a note about the update |
| Publisher no longer offers this title | 🔴 Critical | Find replacement |
| Reading is paywalled with no library access confirmed | 🟠 High | Confirm library access or find open alternative |

**Note:** Claude cannot verify live URLs in real time. Flag all URLs for instructor verification — provide the flag and context, not a guaranteed broken/working status.

### Category 2 — HTML Topic content

For each HTML Topic page provided:

| Check | Flag level | Action |
|---|---|---|
| Statistics or data cited without a recent source | 🟡 Medium | Add publication date or update with current data |
| Statistics more than 3 years old in a fast-moving field | 🟠 High | Update or note the date explicitly |
| Real-world examples reference companies, people, or events that may have changed | 🟡 Medium | Flag for instructor review |
| Legislation, policy, or standards referenced — check if superseded | 🔴 Critical | Update reference |
| Dates or years mentioned that are now in the past | 🟠 High | Update or remove |
| Software versions or platform interfaces described that may have changed | 🟡 Medium | Flag; instructor to verify against current version |
| "Current" or "recent" language without a date anchor | 🟡 Medium | Add a date: "As of [year]…" |
| Broken image references or missing media | 🔴 Critical | Replace or remove |
| Contact information or office hours that may be outdated | 🟡 Medium | Verify before term starts |

### Category 3 — Course policies

| Check | Flag level | Action |
|---|---|---|
| AI use policy present and reflects current institutional stance | 🔴 Critical | Update if institution policy has changed |
| Late submission policy references specific tools or platforms that may have changed | 🟡 Medium | Review tool-specific language |
| Accessibility statement references the correct institutional support office | 🟡 Medium | Verify contact details |
| Land acknowledgement reflects current institutional wording | 🟡 Medium | Check institutional communications office for current version |
| Academic integrity policy references current institutional policy document | 🟠 High | Verify document name and URL |
| Recording consent policy reflects current practice | 🟡 Medium | Review especially if delivery mode changed |

### Category 4 — Course schedule

| Check | Flag level | Action |
|---|---|---|
| Specific dates match the new term calendar | 🔴 Critical | Update all dates |
| Holiday and reading week dates match institutional calendar | 🔴 Critical | Update |
| Exam period references match registrar's schedule | 🔴 Critical | Update |
| Module numbering or week numbering is consistent | 🟡 Medium | Verify no gaps |

### Category 5 — Video and media

| Check | Flag level | Action |
|---|---|---|
| Embedded YouTube/Vimeo/external video links still resolve | 🔴 Critical | Verify and replace if broken |
| Video thumbnails and previews load correctly | 🟡 Medium | Verify |
| Linked podcasts or audio files still accessible | 🟠 High | Verify |
| Video captions are still accurate (especially for AI-generated captions that may have errors) | 🟡 Medium | Spot-check captions |
| Platform-specific embeds (e.g. H5P, third-party LTI) still functional | 🔴 Critical | Test before term starts |

---

## Audit Report Format

Produce a structured report with four sections:

### Section 1 — Critical items (must fix before course goes live)
```markdown
## 🔴 Critical — Fix Before Launch

| Item | Location | Issue | Recommended action |
|---|---|---|---|
| [item name] | [where in course] | [what's wrong] | [what to do] |
```

### Section 2 — High priority items (fix before or early in the term)
```markdown
## 🟠 High Priority — Fix Soon

| Item | Location | Issue | Recommended action |
|---|---|---|---|
```

### Section 3 — Medium priority items (review and update when time permits)
```markdown
## 🟡 Medium Priority — Review When Possible

| Item | Location | Issue | Recommended action |
|---|---|---|---|
```

### Section 4 — Summary
```markdown
## Audit Summary
Date: [date]
Course: [name and code]
Content reviewed: [list of what was audited]
Last updated: [date or "inferred from content"]
Critical items: [count]
High priority items: [count]
Medium priority items: [count]
Estimated time to resolve critical items: [X hours]
Ready to launch: [yes / yes with critical fixes / no — too many critical items]
```

---

## Output Formats

### Format 1 — Markdown audit report (default)
Structured report as above — saves to `content-currency-audit.md`.

### Format 2 — Word document
Same report structure formatted for printing or sharing with a department chair or curriculum coordinator.

### Format 3 — PDF
Read-only version of the Word output — suitable for archiving or attaching to a program review submission.

Ask which formats are needed before generating.

---

## Quality Checks

| Check | Action |
|---|---|
| AI use policy present and current | Flag if absent or predates institution's current AI stance |
| All date references in schedule updated | Flag any past dates |
| At least one open-access reading per week where possible | Flag if all readings are paywalled |
| No "current" language without a date anchor | Flag and suggest adding year |
| Statistics in HTML Topics have source and date | Flag unsourced or undated statistics |
| Reading age flags are field-calibrated | Do not flag humanities/foundational readings on age alone |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Instructor asks Claude to verify a live URL | Clarify that Claude cannot verify live URLs — provide context and flag for instructor to check |
| Instructor wants Claude to replace outdated readings automatically | Offer suggestions; do not assign readings without instructor confirmation |
| Course hasn't been updated in 3+ years | Flag comprehensively; suggest a dedicated content review session before launch |
| Instructor uploads no content | Ask for at least one HTML Topic or reading list; audit cannot run without content |
| Instructor is unsure when the course was last updated | Infer from content dates and flag the inference: "Based on dates found in the content, this course appears to have been last updated around [year]" |

---

## Handoff

> "Your content audit is complete. Suggested next steps:
> 1. **Reading List Builder** — replace flagged stale or inaccessible readings
> 2. **HTML Builder** — rebuild HTML Topics where content needs significant updating
> 3. **Course Copy Auditor** — if you haven't run the structural audit yet, do that next
> 4. **Accessibility Auditor** — after updating HTML Topics, recheck for accessibility
> 5. **Student Experience Preview** — check how content updates affect student navigation
> 6. **Course Outline Builder** — if policy statements need updating, the outline builder can draft replacements"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Content Currency Auditor
Date: [date]
Course: [name and code]
Content reviewed: [list]
Last updated: [date or inferred]
Critical items found: [count]
High priority items found: [count]
Medium priority items found: [count]
Ready to launch: [yes / yes with fixes / no]
Report saved: [content-currency-audit.md yes/no]
Output formats: [list]
Next recommended skill: [name]
---
```
