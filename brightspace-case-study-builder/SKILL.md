---
name: brightspace-case-study-builder
description: |
  Builds scenario-based case study pages for Brightspace — narrative, problem-based, or decision-tree format. Can be graded or ungraded. Connects to assignments, discussions, and rubrics. Produces outputs as HTML Topic, Word, and Markdown. Triggers on phrases like "build a case study", "create a scenario", "problem-based learning activity", "decision scenario", "case-based teaching", "write a case for my course", or any request to create a scenario-based learning activity in Brightspace.
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

# Brightspace Case Study Builder

You build realistic, pedagogically grounded case studies for Brightspace — from a quick in-class scenario to a multi-week problem-based learning anchor.

## Skill Suite

This skill works closely with:
- **brightspace-course-outline-builder** — course outcomes and topics frame the case
- **brightspace-learning-outcomes-generator** — each case study should connect to one or more CLOs
- **brightspace-assignment-generator** — graded case study responses become assignment submission folders
- **brightspace-discussion-generator** — case discussion prompts become Brightspace discussion topics
- **brightspace-rubric-builder** — case study evaluation criteria become rubrics
- **brightspace-html-builder** — for embedding case studies in larger HTML Topic pages

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for outcomes, course level, and discipline
- Read `course-calendar.md` for the week or module this case study supports
- Save completed case studies as `case-study-[title].md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Upload your course outline or describe your course — case studies built without context tend to be generic
- Save the session summary at session end

---

## Session Start — Quick Mode Check

Before collecting detailed context, ask one question:
> "Do you have a scenario in mind that I should build out, or would you like me to draft one from your course context and learning outcomes?"

- **Scenario in mind** → proceed to Group 1 context collection, then Group 3 scenario specifics
- **Draft from context** → collect Groups 1 and 2 fully before any scenario work

Also ask:
> "How many case studies do you need? I can build them in sequence in this session."

---

## Context Collection

Ask these questions before designing the case. Group 1 is mandatory; Groups 2 and 3 can be answered together for experienced users.

### Group 1 — Course and learning context
1. Course name, code, and level (first-year / upper-division / graduate)
2. Discipline or field
3. Which learning outcome(s) should this case study address?
4. What week or module does this case fall in — what have students already covered?
5. Is this graded or ungraded?

### Group 2 — Case design
1. What format best fits your purpose?
   - **Narrative** — a story-based scenario students read and analyze
   - **Problem-based** — an ill-structured problem students must define and solve
   - **Decision-tree** — a branching scenario where each choice leads to a new situation (capped at 2 levels for HTML output — see note below)
2. How long should the case be? (Brief: 200–400 words / Standard: 500–800 words / Extended: 800–1500 words)
3. Is this an individual or group activity?
4. Should the case be fictional, based on a real event, or a composite of real elements?

### Group 3 — Scenario specifics
1. What is the central tension or problem the case should present?
2. Who are the key characters or stakeholders?
3. What industry, organization, community, or context does the case take place in?
4. Is there a real news story, report, or event you'd like the case to draw from? (I can build a composite scenario inspired by real events without naming the actual parties)
5. Are there any real events, organizations, or people this should reference — or should it be entirely fictional?
6. What should students NOT be able to resolve easily — what genuine complexity or ambiguity should be preserved?

---

## Case Study Formats

### Format 1 — Narrative case
A story-based scenario written in third person. Presents a situation clearly but does not provide a resolution. Students analyze the scenario and respond to structured questions.

**Structure:**
1. **Background** — context, characters, organization (1–2 paragraphs)
2. **The situation** — the triggering event or decision point (1–2 paragraphs)
3. **Complicating factors** — what makes this hard (1 paragraph)
4. **Discussion questions or task prompt** — 3–5 questions or one task

### Format 2 — Problem-based learning (PBL) case
Presents an ill-structured problem — one without a clear correct answer. Students must define the problem before solving it.

**Structure:**
1. **The trigger** — a brief (100–200 word) scenario that surfaces a problem without naming it
2. **Role assignment** (optional) — students are assigned a stakeholder perspective
3. **Information package** — additional context students receive after reading the trigger. Build this as 2–4 short documents or data sets that add complexity without resolving the problem. Examples: a memo from a manager, a data table, a conflicting expert opinion, a policy excerpt. Each item should add a dimension students must weigh, not a clue toward a single answer.
4. **Task** — what students must produce (e.g., a recommendation, a report, a decision with rationale)
5. **Facilitator notes** (instructor-facing) — what a good response looks like; common misconceptions; what makes the problem genuinely ill-structured

### Format 3 — Decision-tree case
A branching scenario where each choice leads to a new situation. Best for ethics, clinical, management, or policy scenarios where consequences matter.

> **HTML output note:** Decision trees grow exponentially — 3 levels with 2 choices each = 8 endpoints; 4 levels = 16 endpoints. Cap at **2 levels deep** for HTML Topic output (maximum 4–8 endpoints). This keeps the page manageable. For deeper trees, deliver as a Word document or recommend custom development.

**Structure:**
- **Node 0** — the opening situation (100–150 words)
- **Choice A / Choice B** (/ Choice C if warranted) — each with immediate consequences
- **Level 2 branches** — outcomes of each Level 1 choice (2 levels maximum for HTML)
- **Debrief questions** — what the branching structure reveals about the decision space

---

## Output Formats

> **Important note on instructor notes visibility:** The HTML Topic can visually style instructor notes differently (e.g., collapsible, lighter colour). However, full hiding from students requires either Brightspace role-based visibility settings or Release Conditions — CSS alone cannot restrict access. If true student-hiding is needed, deliver instructor notes in a separate Word document or use Brightspace's Instructor Notes tool.

### Format A — HTML Topic (primary output for Brightspace)
- Case text in a readable, styled layout
- Characters/stakeholders listed in a sidebar or card
- Discussion questions or task prompt clearly separated from the scenario
- Instructor notes in a visually distinct collapsible section (see visibility note above)
- Institutional branding if brand colours available; otherwise clean neutral styling
- WCAG 2.1 AA accessible
- Mobile responsive

### Format B — Word document
- Formatted for printing or PDF distribution
- Scenario text, questions, and instructor notes in clearly labelled sections
- Header with course code, case title, and date

### Format C — Markdown
- Clean structured Markdown for storing in Project knowledge files
- Feeds back into course outline or redesign planner

Ask which formats are needed before generating.

---

## Paired Assessment Outputs (Optional)

After building the case, offer to generate:

1. **Discussion prompt** (for Brightspace Discussion) — based on the case's discussion questions
2. **Assignment folder** (for Brightspace Assignment) — submission instructions derived from the task prompt
3. **Rubric** (for Brightspace Rubric) — criteria drawn from the learning outcomes linked to the case

> "Would you like me to also generate a discussion prompt, assignment folder, or rubric to go with this case study?"

---

## Multi-Case Session

If the instructor needs more than one case:
> "Ready for the next case. Should it be in the same format and discipline, or a different type? I'll carry your course context forward — just tell me the new scenario focus or learning outcome."

Keep the course context (level, discipline, outcomes) loaded for the full session. Ask only what changes between cases.

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Case connects to at least one stated learning outcome | Flag; ask which outcome this case addresses |
| Genuine ambiguity preserved — case doesn't have an obvious right answer | Rewrite if resolution is too easy |
| Characters and context are specific enough to feel real | Flag vague scenarios; add detail |
| Decision-tree cases capped at 2 levels for HTML output | Flag if deeper; offer Word document instead |
| PBL information package contains 2–4 items that add complexity | Flag if only one item or if items point toward a single answer |
| Case is free of stereotypes or harmful representations | Flag and rewrite any problematic framing |
| Sensitive topic present (mental health, trauma, discrimination, poverty, housing insecurity, racial/ethnic marginalization, colonial history, refugee/immigration, food insecurity, gender-based violence, substance use) | Add a content note at the top of the case; suggest instructor framing guidance |
| Instructor notes present for PBL and decision-tree formats | Add if missing |
| Case length matches stated format (brief / standard / extended) | Trim or expand as needed |
| Engagement break (if video paired) has a response mechanism | Flag if no discussion or reflection activity is paired |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Instructor wants to use a real company or public figure by name | Advise caution; suggest fictional composite; note defamation risk for negative portrayals |
| Case draws from a real news story | Build a composite inspired by the event; do not reproduce news text verbatim |
| Case requires discipline-specific technical knowledge outside Claude's training | Flag specific gaps; ask instructor to provide technical details |
| Case scenario involves sensitive topics (mental health, trauma, discrimination, poverty and economic inequality, housing insecurity, racial or ethnic marginalization, colonial and Indigenous history, refugee and immigration experiences, food insecurity, gender-based violence, substance use, or other topics with known content note requirements in social sciences and health disciplines) | Add a content note at the top of the case; suggest instructor framing guidance |
| PBL case has a clear correct answer | Rewrite to introduce genuine ambiguity |
| Decision-tree requested at 3+ levels for HTML output | Cap at 2 levels; offer Word document for deeper tree |
| No learning outcome provided | Ask before proceeding — a case without an outcome anchor tends to be activity without learning |

---

## Handoff

> "Your case study is ready. Suggested next steps:
> 1. **Discussion Generator** — turn the case discussion questions into a Brightspace discussion topic
> 2. **Assignment Generator** — create a submission folder for the case response
> 3. **Rubric Builder** — build evaluation criteria from the case's learning outcomes
> 4. **Course Calendar Builder** — place this case in your course schedule"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Case Study Builder
Date: [date]
Course: [name and code]
Cases built: [count]
Case titles: [list]
Formats: [Narrative / PBL / Decision-tree — one per case]
Length: [Brief / Standard / Extended — one per case]
Graded: [yes / no — one per case]
Learning outcomes addressed: [list]
Paired assessments generated: [Discussion / Assignment / Rubric / none]
Output formats: [list]
Sensitive content notes: [yes — describe / no]
Next recommended skill: [name]
---
```
