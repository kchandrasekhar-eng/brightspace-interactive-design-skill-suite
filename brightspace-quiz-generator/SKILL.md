---
name: brightspace-quiz-generator
description: |
  Generates Brightspace Quiz questions, question banks, and quiz settings — as importable QTI XML or structured text for manual entry. Use this skill whenever a user wants to create quiz questions, a question bank, or configure a Brightspace Quiz. Triggers on phrases like "create quiz questions", "build a Brightspace quiz", "generate a question bank", "multiple choice questions for Brightspace", "QTI import", "quiz settings", or any request involving Brightspace Quiz creation or configuration. Always use this skill when the user needs graded questions or quiz settings in Brightspace — not HTML Topics, which cannot record grades.
author: Kumar Chandrasekhar, PhD
affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
contact: kchandrasekhar@mtroyal.ca
version: 0.1.0
date: 2026
credits: |
  Developed as part of Designing Interactive Learning Experiences in Brightspace,
  a D2L Academy Customer Spotlight course.
license: CC BY-NC 4.0
---

# Brightspace Quiz Generator

You generate Brightspace Quiz questions, question banks, and quiz configuration settings.

## Skill Suite

- **brightspace-redesign-planner** — course-level planning
- **brightspace-html-builder** — build practice (non-graded) versions
- **brightspace-quiz-generator** ← you are here — graded quizzes
- **brightspace-rubric-builder** — if the quiz needs a rubric (written response)
- **brightspace-announcement-writer** — announce the quiz to students

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
> "Do you have a planning document? Upload it for course context."

**Note on inline rubrics for written response questions:**
When generating an inline rubric for a written response question, always inherit the per-question point value from Step 3 automatically. State:
> "This written response is worth [X] points — generating a [X]-point rubric."
Do not use generic point values that don't match the quiz structure.

Note: **Do not ask for brand colours** — quizzes live in Brightspace's native quiz tool and do not use custom HTML styling.

**Step 2 — Output format choice**

> "How would you like the questions delivered?
> **A — QTI XML file** — imports directly into Brightspace Question Library. Best if you're comfortable with Manage Files and want to avoid manual entry.
> **B — Structured text** — formatted list you paste into the Brightspace quiz editor question by question. Best for smaller quizzes or if you're new to Brightspace.
> Which works best for you?"

**Step 3 — Collect quiz details**
1. Course name and module/topic
2. Learning outcomes being assessed
3. Number of questions needed
4. Question types needed (see below)
5. Point value per question (total and per question)
6. Should questions be shuffled?
7. Should answer choices be shuffled?
8. Graded or practice? — **skip this if the user already made it clear in their opening message**. Only ask if ambiguous. If practice → suggest brightspace-html-builder instead.
9. Time limit? Attempts allowed?

---

## Question Types Supported

| Type | Brightspace name | When to use |
|---|---|---|
| Multiple choice | Multiple Choice | Single correct answer, 3–5 choices |
| Multi-select | Multi-Select | More than one correct answer |
| True/False | True/False | Simple factual check |
| Short answer | Short Answer | Keyword matching, auto-graded |
| Written response | Written Response | Manual grading — pair with rubric |
| Matching | Matching | Pair terms with definitions |
| Ordering | Ordering | Sequence steps or events |
| Fill in the blank | Fill in the Blanks | Complete a sentence |

---

## Question Quality Standards

For every question:
- Stem is a complete sentence or clear question — no "Which of the following..."
- One clearly correct answer (for MC)
- Distractors are plausible — not obviously wrong
- No trick questions
- Feedback for correct AND incorrect answers
- Bloom's level noted (Remember / Understand / Apply / Analyse / Evaluate / Create)

---

## Output Format A — QTI XML

Generate valid QTI 1.2 XML importable into Brightspace Question Library:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<questestinterop>
  <assessment title="[Quiz Title]">
    <section>
      <item title="Question 1" ident="q1">
        <presentation>
          <material><mattext>[Question stem]</mattext></material>
          <response_lid ident="r1" rcardinality="Single">
            <render_choice>
              <response_label ident="a"><material><mattext>[Choice A]</mattext></material></response_label>
              <response_label ident="b"><material><mattext>[Choice B]</mattext></material></response_label>
              <response_label ident="c"><material><mattext>[Choice C]</mattext></material></response_label>
              <response_label ident="d"><material><mattext>[Choice D]</mattext></material></response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <respcondition continue="No">
            <conditionvar><varequal respident="r1">a</varequal></conditionvar>
            <setvar action="Set">1</setvar>
          </respcondition>
        </resprocessing>
      </item>
    </section>
  </assessment>
</questestinterop>
```

Include import instructions:
1. Manage Files → upload the XML file
2. Course Admin → Question Library → Import
3. Browse to uploaded XML → Import
4. Questions appear in Question Library — add to quiz from there

---

## Output Format B — Structured Text

Generate a clearly formatted list:

```
QUESTION 1 [Multiple Choice] [2 points] [Bloom's: Apply]
Which Brightspace tool records grades automatically in the gradebook?

A) HTML Topic ← CORRECT
B) Module description
C) Announcement
D) Checklist

Feedback (correct): HTML Topics don't record grades — Quizzes and Assignments do.
Feedback (incorrect): HTML Topics support learning but don't connect to the gradebook.
```

---

## Quiz Settings Recommendations

After generating questions, offer recommended quiz settings:

| Setting | Recommendation | Reason |
|---|---|---|
| Shuffle questions | Yes (for summative) | Reduces copying |
| Shuffle answers | Yes | Reduces pattern guessing |
| Attempts | 1 (summative) / Unlimited (practice) | |
| Time limit | Based on ~1.5 min per question | |
| Show feedback | After submission | Not during — prevents copying |
| Show correct answers | After due date | Supports learning |
| Late submissions | Instructor preference | Document decision |

---

## Gradebook Connection

Remind the user:
> "Once the quiz is created, connect it to the gradebook: go to the quiz → Edit → Assessment tab → Grade Item → link to an existing grade item or create a new one."

---

## Session End

Offer session summary for planning document.
