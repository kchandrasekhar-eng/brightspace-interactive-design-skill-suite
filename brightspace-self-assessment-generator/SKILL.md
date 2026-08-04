---
name: brightspace-self-assessment-generator
description: |
  Builds self-assessment and reflection tools for Brightspace — structured rubric-based self-evaluations, metacognitive check-ins, learning journals, and pre/post activity reflections. Can be graded or ungraded. Connects to assignments, discussions, and the gradebook. Produces outputs as HTML Topic, Brightspace Quiz (for structured formats), Word, and Markdown. Triggers on phrases like "self-assessment", "student reflection", "metacognitive activity", "learning journal", "self-evaluation", "reflection prompt", "pre/post reflection", or any request to build a structured student self-evaluation tool in Brightspace.
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

# Brightspace Self-Assessment Generator

You build structured, pedagogically grounded self-assessment and reflection tools — from a quick metacognitive check-in to a full learning journal system.

## Skill Suite

This skill works closely with:
- **brightspace-course-outline-builder** — outcomes frame what students reflect on; also feeds into the "build last" outline workflow
- **brightspace-learning-outcomes-generator** — self-assessments should map to course CLOs
- **brightspace-assignment-generator** — self-assessment can be submitted as part of an assignment
- **brightspace-rubric-builder** — rubric-based self-assessment requires an existing rubric as the scaffold; build the rubric first
- **brightspace-quiz-generator** — structured Likert-scale or rating self-assessments can be built as ungraded Brightspace Quizzes
- **brightspace-group-project-setup** — group contribution self-report pairs with group project setup
- **brightspace-exam-wrapper-builder** — exam wrappers are a specialized form of self-assessment; use that skill for pre/post exam reflection

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for learning outcomes and course level
- Read `course-calendar.md` for placement of self-assessment activities
- Save completed self-assessment tools as `self-assessment-[title].md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Describe your course, the purpose of the self-assessment, and where it falls in the course
- Save the session summary at session end

---

## Session Start — Identify Type and Purpose

Ask if not clear from context:

> "What is the purpose of this self-assessment? Here are the most common types:"

| Type | Purpose | Typical timing |
|---|---|---|
| **Rubric-based self-evaluation** | Students rate their own work against the same criteria used for grading | At assignment submission |
| **Metacognitive check-in** | Students reflect on how they're learning, not just what they're learning | Mid-module or mid-term |
| **Learning journal** | Ongoing structured reflection across the course | Weekly or per module |
| **Pre/post reflection** | Students capture what they know before and after a topic | Before and after a module |
| **Skills inventory** | Students rate their confidence or competence in course skills | Start of term and end of term |
| **Group contribution self-report** | Students document their contribution to a group project | At project submission |

**Decision guide:**
- Pre/post reflection → for module-level learning (what did I know, what do I know now)
- Skills inventory → for course-level competence tracking (how confident am I across all course skills)
- These two are distinct: use reflection for learning events; use inventory for cumulative skill growth

**Boundary note:** For pre/post *exam* reflection specifically (what did I study, what went wrong, what will I change), use the **brightspace-exam-wrapper-builder** skill instead.

Also ask:
> "How many self-assessment activities do you need? I can build them in sequence."

---

## Information Collection

Collect before building. Skip questions already answered by `course-outline.md`.

### Group 1 — Context
1. Course name, code, and level
2. Self-assessment type (from the table above)
3. Which learning outcome(s) or skills does this self-assessment connect to?
4. Where in the course does this activity fall? (week, module, tied to an assignment)
5. Graded or ungraded?
   - If graded: what is the weight? What does good self-assessment look like for this course?
   - If ungraded: how will the instructor use the responses? (inform feedback, track growth, course analytics)

### Group 2 — Format preferences
1. Should students respond to structured prompts (fill-in, rating scale, rubric) or open-ended questions, or a combination?
2. Approximately how long should this activity take? (5 min / 10–15 min / 20–30 min)
3. Should responses be visible to the instructor only, or shared with peers?
4. Will this be repeated across the term? (If yes: build a template that can be reused)

---

## Self-Assessment Formats

### Format 1 — Rubric-based self-evaluation

Students rate their own submission against the same criteria used for instructor grading.

**Prerequisite:** This format requires an existing rubric. If the rubric hasn't been built yet, run **brightspace-rubric-builder** first — then return here to build the self-rating overlay on top of it.

**Design rules:**
- Mirror the same performance descriptors as the assignment rubric
- Add one column: "My self-rating" with the same performance levels as the rubric
- Add 1–2 open-ended questions: "What aspect of your work are you most confident about?" and "What would you change if you had more time?"
- Do not use self-rating to calculate the grade — use it as a calibration tool and conversation starter

**Brightspace delivery:** As a text entry assignment submitted alongside the main assignment, or as a separate reflection assignment due at the same time.

### Format 2 — Metacognitive check-in

Brief, structured prompts that ask students to step back from content and think about their learning process.

**Core prompts (choose 3–4):**
1. What concept from this module do you feel most confident about? Why?
2. What concept are you still uncertain about? What would help you understand it better?
3. How did you approach the reading/activities this week — and how effective was that approach?
4. On a scale of 1–5, how engaged did you feel in this module? What influenced that?
5. What question do you most want answered before the next assessment?

**Brightspace delivery options:**
- As a short text entry assignment (graded for completion, not quality)
- As an ungraded Brightspace Quiz with a combination of Likert items and written responses
- As a discussion post (if peer visibility is desired)

### Format 3 — Learning journal

An ongoing, structured reflection system across the course.

**Structure:**
- One entry per week or per module
- Consistent prompt structure across all entries (so growth can be tracked)
- Each entry: 150–300 words for undergraduate; 250–500 words for graduate

**Standard prompt set (used consistently each entry):**
1. **What I learned** — summarize the key idea in your own words (2–3 sentences)
2. **What surprised me** — something unexpected or that challenged your prior understanding
3. **What I'm still unclear about** — an honest gap
4. **How this connects** — to something outside the course, a previous module, or a lived experience

**Brightspace delivery:** As a recurring assignment with a consistent rubric, or as a discussion thread with one topic per week.

**Grading note:** Grade on engagement and honest reflection, not correctness. Never grade for "right answers."

**Concrete engagement indicators** — a strong journal entry:
- Names specific course concepts, readings, or activities (not vague references)
- Identifies a genuine gap, not a generic one ("I'm still unclear about X because Y" not "I found it confusing")
- Makes a specific connection outside the course (a real example, a personal experience, another course)
- Shows change or growth from a previous entry (for later entries in the course)

**Frequency note:** For a 12-week course, consider alternating graded and ungraded entries, or reducing to every other week after Week 4. Weekly graded journals for a full semester create marking load for the instructor and fatigue for students.

### Format 4 — Pre/post reflection

Students capture what they know before a module begins, then return after the module to update.

**Use this for:** Module-level learning (what did I know before, what do I know now).
**Use Skills Inventory instead for:** Course-level competence tracking across all outcomes.

**Pre-activity prompts:**
1. What do you already know about [topic]?
2. What do you expect to find confusing or challenging?
3. What question do you most want this module to answer?

**Post-activity prompts:**
1. What did you learn that confirmed what you already knew?
2. What surprised you or changed your thinking?
3. Was your key question answered? If not, what would it take to answer it?

**Brightspace delivery:**
- As two linked assignment submissions (pre and post in the same folder, two attempts)
- Or as a two-part text entry with both sections visible

### Format 5 — Skills inventory

Students rate their confidence or competence across course skills — typically at the start and end of term to show growth.

**Use this for:** Course-level competence tracking across all outcomes.
**Use Pre/post reflection instead for:** Module-level learning tied to a specific topic.

**Design:**
- List 6–10 specific skills drawn from course learning outcomes
- Rating scale: 1 (Not yet confident) → 5 (Highly confident)
- Add one open-ended item: "What is the one skill you most want to develop in this course?"
- End-of-term version: same items + "How has your confidence changed?" for each

**Brightspace delivery:** As an ungraded Brightspace Quiz (Likert items + written response). Use the **brightspace-quiz-generator** skill for the Quiz configuration.

### Format 6 — Group contribution self-report

Students document their specific contributions to a group project.

**Connection to Group Project Setup:** If you've used **brightspace-group-project-setup**, this self-report links directly to that project's submission folder and timeline. Confirm the project name and submission date with the group project configuration.

**Prompts:**
1. What specific tasks did you complete for this project? (Be concrete — "I wrote sections 2 and 4 of the report")
2. How would you rate your contribution to the group? (1–5) Why?
3. What did you contribute that isn't visible in the final product? (e.g., coordinating meetings, giving feedback)
4. What would you do differently in a future group project?
5. (Optional, instructor-only) Are there any concerns about group dynamics you'd like to share?

**Brightspace delivery:** As a private text entry assignment. Emphasize that responses are instructor-only unless the instructor specifies otherwise.

---

## Output Formats

### Format A — HTML Topic (for student-facing instructions and ungraded activities)
- Clear activity instructions with purpose statement
- Prompts formatted with adequate space/guidance
- Institutional branding if available; otherwise clean neutral styling
- WCAG 2.1 AA accessible, mobile responsive

### Format B — Brightspace Quiz configuration (for Likert-scale formats)
- Question-by-question settings for ungraded Quiz
- Likert items + written response items
- Pass to **brightspace-quiz-generator** for full configuration

### Format C — Assignment folder instructions (for submitted reflections)
- Submission instructions, prompt text, grading approach
- Pass to **brightspace-assignment-generator** for folder creation

### Format D — Word document
- Formatted for printing or distribution
- Activity instructions, prompts, and grading note in clearly labelled sections
- Header with course code, activity title, and date

### Format E — Markdown (for Project knowledge files and reuse)
```markdown
# [Self-Assessment Title] — [Course Name]

## Purpose
[one sentence]

## Instructions for students
[prompt text]

## Prompts
1. [prompt]
2. [prompt]

## Grading note
[how this is graded or why it is ungraded]
```

Ask which formats are needed before generating.

---

## Grading Self-Assessment Fairly

> **Important pedagogical note:** Self-assessments graded on accuracy (how close students are to the instructor's grade) undermine honesty and suppress the metacognitive benefit. Grade self-assessments on:
> - **Completion** — did the student engage with all prompts?
> - **Specificity** — are responses specific and reflective, not vague?
> - **Honesty** — does the student demonstrate awareness of both strengths and gaps?

Never penalize students for rating themselves lower than the instructor would. A student who accurately identifies their own weaknesses is demonstrating exactly the metacognitive skill you're trying to build.

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Self-assessment connects to at least one CLO or skill | Flag; ask what students should be reflecting on |
| Rubric-based format: rubric exists before building self-rating overlay | Flag; run brightspace-rubric-builder first |
| Prompts are open enough to allow honest response | Flag leading questions; rewrite |
| Activity length matches stated time budget | Trim prompts if too long; expand if too short |
| Graded self-assessments use engagement criteria, not accuracy | Flag if accuracy-based grading is planned; offer alternative |
| Repeated activities use consistent prompts | Flag inconsistency; offer to standardize |
| Learning journal frequency is sustainable | Flag if weekly graded for full term; suggest alternating schedule |
| Group contribution reports are private by default | Flag if set to peer-visible; advise on privacy implications |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Instructor wants to grade self-assessment on accuracy | Explain why this is counterproductive; suggest engagement-based criteria |
| Pre/post exam reflection requested | Refer to **brightspace-exam-wrapper-builder** |
| Instructor wants peer-visible contribution reports | Flag privacy concern; recommend instructor-only unless students consent |
| Self-assessment activities are very frequent (weekly graded) | Flag fatigue risk; suggest alternating graded/ungraded |
| No learning outcome provided | Ask what students should reflect on — open-ended reflection without an anchor tends to be vague |
| Rubric-based format requested but no rubric exists | Pause; run **brightspace-rubric-builder** first |

---

## Handoff

> "Your self-assessment tool is ready. Suggested next steps:
> 1. **Assignment Generator** — create the submission folder if this is a submitted reflection
> 2. **Quiz Generator** — configure the Brightspace Quiz if this uses a Likert-scale format
> 3. **Rubric Builder** — build the rubric if this is a rubric-based self-evaluation (run before returning to use this skill)
> 4. **Exam Wrapper Builder** — if you also need pre/post exam-specific reflection
> 5. **Course Outline Builder** — if building the outline at the end, self-assessment activities feed into the assessment structure automatically"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Self-Assessment Generator
Date: [date]
Course: [name and code]
Activities built: [count]
Types: [list]
Graded: [yes / no / mixed]
Timing: [list placements in course]
Learning outcomes addressed: [list]
Brightspace delivery: [Assignment / Quiz / Discussion / HTML Topic]
Output formats: [list]
Next recommended skill: [name]
---
```
