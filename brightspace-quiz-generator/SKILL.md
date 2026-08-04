---
name: brightspace-quiz-generator
description: |
  Generates Brightspace Quiz questions, question banks, and quiz settings — as a D2L-ready CSV file (default), QTI XML, or structured text for manual entry. Use this skill whenever a user wants to create quiz questions, a question bank, or configure a Brightspace Quiz. Triggers on phrases like "create quiz questions", "build a Brightspace quiz", "generate a question bank", "multiple choice questions for Brightspace", "CSV import", "QTI import", "quiz settings", or any request involving Brightspace Quiz creation or configuration. Always use this skill when the user needs graded questions or quiz settings in Brightspace — not HTML Topics, which cannot record grades.
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
- Consider setting up a Claude Project — ask the **brightspace-orchestrator** for step-by-step instructions

---

## Session Start

**Step 1 — Planning document**
> "Do you have a planning document? Upload it for course context."

**Note on inline rubrics for written response questions:**
When generating an inline rubric for a written response question, always inherit the per-question point value from Step 3 automatically. State:
> "This written response is worth [X] points — generating a [X]-point rubric."
Do not use generic point values that don't match the quiz structure.

**Step 2 — Output format and upload path**

Present all three options, then ask. Do not assume a format.

> "How would you like the questions delivered?
>
> **A — D2L CSV** *(recommended for most users)* — a ready-to-import CSV file in D2L's native format. Works for both upload paths:
> - Directly into a quiz: Add Existing → Upload a File → Import All
> - Into the Question Library: Course Admin → Question Library → Import
>
> **B — QTI XML** — imports into the Question Library only (via Manage Files + Import). Better for large question banks or when QTI interoperability with other platforms matters.
>
> **C — Structured text** — a formatted list you enter into Brightspace manually, question by question. Best for very small quizzes or users new to Brightspace who prefer to type directly into the editor.
>
> Which works best for you? If you're not sure, go with A."

**If the user chooses A — also ask:**
> "Are you uploading directly into a quiz, or into the Question Library? I'll give you the right import steps."

**CSV format limitations — check before generating:**
After the user confirms question types (Step 3, item 4), check this table. If any affected types are requested, flag the limitation before generating.

| Question type | CSV support | Limitation | Recommendation |
|---|---|---|---|
| Multiple Choice | ✅ Full | None | — |
| True/False | ✅ Full | None | — |
| Multi-Select | ✅ Full | Scoring method must be set in CSV (`AllOrNothing`, `RightAnswers`, `RightMinusWrong`) | Default to `RightAnswers` unless user specifies |
| Short Answer | ✅ Full | Answer percentage weighting works; `regexp` flag available for pattern matching | Confirm whether regex matching is needed |
| Written Response | ✅ Full | Answer key is instructor-facing only; pair with a rubric for grading | Offer brightspace-rubric-builder |
| Matching | ⚠️ Partial | Scoring defaults to `EquallyWeighted` — cannot be changed in CSV; must be updated manually after import | Inform user; confirm they're comfortable adjusting after import |
| Ordering | ⚠️ Partial | Scoring defaults to `RightMinusWrong` — cannot be changed in CSV; HTML flag column (`HTML`/`NOT HTML`) must be set per item | Inform user; default to `NOT HTML` unless rich text is needed |
| Fill in the Blanks | ❌ Not supported | D2L CSV does not support this question type | See below |

**Fill in the Blanks — if requested with CSV:**
> "Fill in the Blanks questions aren't supported in D2L's CSV format. Here are your options:
> 1. **Replace with Short Answer** — auto-graded, keyword matching, works well for single-word or short-phrase completions. Recommended if auto-grading matters.
> 2. **Replace with Multiple Choice** — convert the blank into answer choices. Recommended if you want reliable auto-grading with distractors.
> 3. **Receive these questions as structured text** — I'll generate Fill in the Blanks questions separately as formatted text for manual entry alongside your CSV.
>
> Which would you prefer?"

Generate whichever replacement or supplementary output the user chooses. If structured text is added as a supplement, label the two outputs clearly: `[CSV — import via Brightspace]` and `[Structured text — enter manually]`.

**Step 3 — Collect quiz details**
1. Course name and module/topic
2. Learning outcomes being assessed
3. Number of questions needed
4. Question types needed (see below) — **check CSV limitations table above before proceeding**
5. Point value per question (total and per question)
6. Should questions be shuffled?
7. Should answer choices be shuffled?
8. Graded or practice? — **skip if the user already made it clear in their opening message**. Only ask if ambiguous. If practice → suggest brightspace-html-builder instead.
9. Time limit? Attempts allowed?

---

## Question Types Supported

| Type | Brightspace name | CSV code | When to use |
|---|---|---|---|
| Multiple choice | Multiple Choice | `MC` | Single correct answer, 3–5 choices |
| Multi-select | Multi-Select | `MS` | More than one correct answer |
| True/False | True/False | `TF` | Simple factual check |
| Short answer | Short Answer | `SA` | Keyword matching, auto-graded |
| Written response | Written Response | `WR` | Manual grading — pair with rubric |
| Matching | Matching | `M` | Pair terms with definitions |
| Ordering | Ordering | `O` | Sequence steps or events |
| Fill in the blank | Fill in the Blanks | ❌ not in CSV | Complete a sentence — see CSV limitations above |

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

## Output Format A — D2L CSV

Generate a valid UTF-8 CSV file using D2L's native import format. Save as CSV UTF-8.

**Required fields per question type:**

```
NewQuestion,[type code]
ID,[optional — leave blank to auto-assign]
Title,[question name / short description]
QuestionText,[full question stem]
Points,[integer]
```

**Per-type rows (append after required fields):**

```
// MULTIPLE CHOICE (MC)
Option,[100=correct / 0=incorrect / partial %],[answer text],,[per-option feedback]
// Repeat Option rows for each choice

// TRUE/FALSE (TF)
TRUE,[100 or 0],[feedback for True]
FALSE,[100 or 0],[feedback for False]

// MULTI-SELECT (MS)
Scoring,[AllOrNothing / RightAnswers / RightMinusWrong]
Option,[1=correct / 0=incorrect],[answer text],,[per-option feedback]
// Repeat Option rows for each choice

// SHORT ANSWER (SA)
InputBox,[rows],[character width]
Answer,[% credit],[answer text],[regexp if pattern matching — otherwise blank]
// Repeat Answer rows for each accepted answer

// WRITTEN RESPONSE (WR)
InitialText,[starter text for student — leave blank if none]
AnswerKey,[instructor-facing answer key]

// MATCHING (M)
Scoring,EquallyWeighted    // only supported value in CSV
Choice,[number],[choice text]
// Repeat Choice rows
Match,[choice number it matches],[match text]
// Repeat Match rows

// ORDERING (O)
Scoring,[RightMinusWrong / EquallyWeighted / AllOrNothing]
Item,[item text],[HTML or NOT HTML],[per-item feedback]
// Repeat Item rows in correct order
```

**Common optional fields (all types):**
```
Hint,[hint text]
Feedback,[overall question feedback shown after submission]
Difficulty,[1–10 — being deprecated; omit unless required]
Image,[path to image in course Manage Files — e.g. images/filename.jpg]
```

**Full CSV example — Mixed question set:**

```csv
NewQuestion,MC
Title,Gradebook tool identification
QuestionText,Which Brightspace tool automatically records grades in the gradebook?
Points,2
Option,100,Quiz,,Correct — Quizzes connect directly to the gradebook.
Option,0,HTML Topic,,HTML Topics support learning but do not record grades.
Option,0,Announcement,,Announcements are for communication only.
Option,0,Checklist,,Checklists track completion but do not record grades.
Feedback,Quizzes and Assignments are the two tools that connect to the Brightspace gradebook.

NewQuestion,TF
Title,Release condition behaviour
QuestionText,Release conditions in Brightspace can be set to unlock content after a student views a specific page.
Points,1
TRUE,100,Correct — viewing a content topic is a valid release condition trigger.
FALSE,0,Viewing a page is one of several available release condition types.
Feedback,Release conditions support a range of triggers including content views, quiz attempts, and grade thresholds.

NewQuestion,SA
Title,LMS abbreviation
QuestionText,What does LMS stand for?
Points,1
InputBox,1,40
Answer,100,Learning Management System
Answer,100,learning management system
Feedback,LMS stands for Learning Management System — software platforms like Brightspace used to deliver and manage online learning.

NewQuestion,WR
Title,Gradebook design rationale
QuestionText,Explain why gradebook structure should be set up before creating individual grade items in Brightspace.
Points,5
AnswerKey,Students expect look for: calculation method chosen before items are added; category weights established first; grade scheme applied at the category or course level before items inherit it.
Feedback,Your response has been submitted. Feedback will be provided after grading.
```

**Import instructions — context-aware:**

Provide the path matching what the user confirmed in Step 2.

*If uploading directly into a quiz:*
1. Open the quiz → Edit
2. In the question area → Add Existing → Upload a File
3. Browse Files → select your CSV → Import All
4. Questions are added to the quiz directly

*If uploading into the Question Library:*
1. Course Admin → Question Library → Import
2. Browse Files → select your CSV → Import
3. Questions appear in Question Library — add to any quiz from there

*Note on encoding:* Save the CSV as **UTF-8** (not UTF-16 or default Excel encoding). In Excel: Save As → CSV UTF-8 (Comma delimited). In Google Sheets: File → Download → CSV.

---

## Output Format B — QTI XML

Generate valid QTI 1.2 XML importable into Brightspace Question Library. Use when the user needs QTI interoperability or is building a large question bank for reuse across courses.

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

Import instructions:
1. Manage Files → upload the XML file to your course files
2. Course Admin → Question Library → Import
3. Browse to the uploaded XML → Import
4. Questions appear in Question Library — add to any quiz from there

---

## Output Format C — Structured Text

Use for very small quizzes or when the user prefers to type questions directly into the Brightspace editor. No file to upload.

```
QUESTION 1 [Multiple Choice] [2 points] [Bloom's: Apply]
Which Brightspace tool records grades automatically in the gradebook?

A) HTML Topic
B) Module description
C) Quiz ← CORRECT
D) Checklist

Feedback (correct): Quizzes connect directly to the gradebook — HTML Topics do not.
Feedback (incorrect): Quizzes and Assignments are the two tools that record grades in the Brightspace gradebook.
```

Manual entry path: Quiz → Edit → Create New → New Question → select question type → paste content.

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
