---
name: brightspace-exam-wrapper-builder
description: |
  Builds pre- and post-exam metacognitive reflection activities (exam wrappers) for Brightspace. Pre-wrappers help students plan their study approach; post-wrappers guide students through analyzing their exam performance, identifying error patterns, and adjusting their study habits. Graded or ungraded. Based on Lovett's (2013) exam wrapper framework. Produces outputs as HTML Topic, Brightspace Assignment, and Markdown. Triggers on phrases like "exam wrapper", "pre-exam reflection", "post-exam reflection", "exam debrief", "study habit reflection", "exam analysis activity", or any request to help students reflect on exam preparation or performance.
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

# Brightspace Exam Wrapper Builder

You build exam wrappers — structured metacognitive activities that help students reflect on how they prepared for an exam and what they will do differently next time. Based on the Lovett (2013) exam wrapper framework.

> **Reference:** Lovett, M. C. (2013). Make exams worth more than the grade: Using exam wrappers to promote metacognition. In M. Kaplan, N. Silver, D. LaVaque-Manty, & D. Meizlish (Eds.), *Using reflection and metacognition to improve student learning*. Stylus Publishing.

## Skill Suite

This skill works closely with:
- **brightspace-self-assessment-generator** — for non-exam reflection activities (learning journals, check-ins, skills inventories); this skill handles exam-specific reflection only
- **brightspace-quiz-generator** — exam/quiz configuration
- **brightspace-assignment-generator** — wrapper submission folder creation
- **brightspace-course-calendar-builder** — placement of wrapper activities before and after exams
- **brightspace-course-outline-builder** — exam wrapper details feed into the "build last" outline workflow

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for assessment structure and exam timing
- Read `course-calendar.md` for exam dates and surrounding weeks
- Save completed wrappers as `exam-wrapper-[exam-name].md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Describe the exam type, course level, and what you want students to reflect on
- Save the session summary at session end

---

## Session Start — Collect Context

Ask if not available from course outline:

1. Course name, code, and level
2. Which exam is this wrapper for? (midterm, final, quiz series, lab practical)
3. What format is the exam? (multiple choice, short answer, essay, problem-solving, mixed)
4. When is the exam — and when will grades be returned to students?
5. Is this a pre-wrapper, post-wrapper, or both?
6. Graded or ungraded?
   - If graded: what is the weight? (typically 1–3%)
   - If ungraded: how will students access their returned wrapper after the exam?
7. Will the instructor review wrapper responses before returning exams?
8. How many exam wrappers are needed for this course? (I can build a matched pre/post set for each exam in sequence)

**Multi-wrapper session:** If the instructor needs wrappers for multiple exams, collect context for all of them at session start, then build each matched pair in sequence. Keep the course context loaded throughout.

---

## Exam Wrapper Design

### The Exam Wrapper Cycle

```
PRE-WRAPPER                    EXAM                    POST-WRAPPER
(before studying)         (submitted)            (after grades returned)
      ↓                        ↓                         ↓
How will I study?        Performance              What happened?
What do I expect?        captured               What will I change?
      ↓                                                   ↓
                    Student reviews both wrappers
                    together with graded exam
                    (optional: instructor-facilitated debrief)
```

The key pedagogical move: students complete the PRE-wrapper *before the exam* and cannot revise it. They see it again only when they receive their graded exam alongside the POST-wrapper. Comparing predictions to performance is what generates metacognitive insight.

**In Brightspace, "sealing" the pre-wrapper means:** set the pre-wrapper assignment's due date to the exam start time. After the due date passes, students can view their submission but cannot edit it. This is the Brightspace equivalent of sealing.

### Brightspace delivery options

**Option A — Two separate assignments (recommended)**
- Pre-wrapper: text entry assignment, due date = exam start time
- Post-wrapper: text entry assignment, due 3–5 days after grades are returned
- Students open both assignments simultaneously when completing the post-wrapper to compare responses

**Option B — Single assignment with two attempts**
- First attempt = pre-wrapper (closes at exam start time)
- Second attempt = post-wrapper (opens after grade return)
- **Important caveat:** Brightspace Assignment tool does not show previous attempt text to students by default. Students must have saved their pre-wrapper response separately to reference it during the post-wrapper. For most instructors, Option A is more reliable.

**Option C — Ungraded HTML Topic with printed submission**
- Students complete on paper; instructor collects before exam, returns with graded exam
- Lower friction for in-person courses; less trackable in Brightspace

---

## Pre-Wrapper Content

**Purpose:** Help students plan their exam preparation — not just review, but think about *how* they will study.

### Standard pre-wrapper prompts

**Section 1 — Study planning**
1. How many hours do you plan to study for this exam in total?
2. What study strategies will you use? (Choose all that apply — type the numbers)
   1. Re-reading notes or slides
   2. Making summaries or concept maps
   3. Practice problems or past exams
   4. Flashcards or spaced repetition
   5. Study group or peer discussion
   6. Other: ___

   > **Delivery note:** If using Brightspace text entry, present this as a numbered list students type their selections from — HTML checkboxes do not render in Brightspace text entry submissions.

3. Which topics do you feel most prepared for? Why?
4. Which topics are you least confident about? What will you do about that?

**Section 2 — Prediction**
5. What grade do you expect to earn on this exam? (%)
6. What would that grade tell you about your understanding of the course material?

**Section 3 — Mindset (optional — for courses where exam anxiety is a concern)**
7. How are you feeling about this exam right now? (1 = very anxious → 5 = very confident)
8. What is one thing you can do before the exam to feel more prepared?

---

## Post-Wrapper Content

**Purpose:** Guide students through analyzing *why* they performed as they did — not just what they got wrong, but what study strategies led to that result.

### Standard post-wrapper prompts

**Section 1 — Performance analysis**
1. What grade did you earn on this exam? (%)
2. How does this compare to what you predicted in your pre-wrapper?
3. Were there specific topics or question types where you performed worse than expected? List them.
4. Were there specific topics where you performed better than expected? List them.

**Section 2 — Error analysis**

For each topic or question type where you lost marks, identify the most likely reason. Rate how much each applied (1 = not at all, 3 = somewhat, 5 = very much):

1. Didn't know the material — the topic wasn't covered in my studying
2. Knew it but forgot under pressure — I studied it but blanked during the exam
3. Misread or misunderstood the question — I answered a different question than what was asked
4. Ran out of time — I knew it but didn't get to it
5. Calculation or process error — I knew the concept but made a mechanical mistake
6. Conceptual misunderstanding — I thought I understood it, but my model was wrong

> **Delivery note for text entry:** Present as a numbered rating list (1–6 above) — HTML tables do not render in Brightspace text entry submissions. Students type a number 1–5 next to each error type. For HTML Topic delivery, the table format works well.

5. Which error type had the highest rating for you on this exam?

**Section 3 — Study strategy reflection**
6. Looking back at your pre-wrapper: which study strategies did you actually use?
7. Which strategies were most effective? Which were least effective?
8. Was there a mismatch between how you studied and what the exam actually tested?

**Section 4 — Plan for next time**
9. What is one specific thing you will do differently when preparing for the next exam?
10. What support do you need? (Office hours, study group, tutoring, different resources)

---

## Instructor Debrief Option

After collecting post-wrappers, offer the instructor a facilitation guide:

> "Would you like a short class debrief guide? A 10-minute debrief can turn aggregate wrapper patterns into a teaching moment without identifying individual students."

**Offer this proactively** when the instructor confirms they will review wrapper responses — don't wait for them to ask.

**Suggested debrief structure:**
1. Share aggregate error type ratings: "The most common issue was [X] — here's what that means for how you study"
2. Address the study strategy mismatch: "Many of you said you re-read notes — here's why that's less effective than [alternative]"
3. Close with two or three specific strategies for the next exam

**Facilitation guide format:** A one-page Markdown or Word document with talking points, timing (10 min), and suggested discussion questions.

---

## Output Formats

### Format 1 — Brightspace assignment folder instructions

**Pre-wrapper assignment:**
- Name: [Exam name] — Pre-Wrapper
- Submission type: Text entry
- Due date: Set to exam start time (this "seals" the pre-wrapper)
- Grade item: [weight]% or ungraded
- Instructions: [pre-wrapper prompts, formatted as numbered list for text entry]

**Post-wrapper assignment:**
- Name: [Exam name] — Post-Wrapper
- Submission type: Text entry
- Available from: Date grades are returned
- Due: 3–5 days after grades returned
- Grade item: [weight]% or ungraded
- Instructions: [post-wrapper prompts + instruction to open pre-wrapper submission in a separate tab for reference]

Pass to **brightspace-assignment-generator** for folder creation.

### Format 2 — HTML Topic (student-facing)
- Clear explanation of what an exam wrapper is and why it matters
- Pre-wrapper prompts with adequate response space
- Post-wrapper prompts with error analysis table (table renders correctly in HTML Topic)
- Institutional branding if available; otherwise clean neutral styling
- WCAG 2.1 AA accessible, mobile responsive

### Format 3 — Markdown (for Project knowledge files)
```markdown
# Exam Wrapper — [Exam Name]
## Course: [name and code]

## Pre-Wrapper (due: exam start time — [date/time])
[prompt text as numbered list]

## Post-Wrapper (due: [date] — 3–5 days after grade return)
[prompt text as numbered list]

## Grading approach
[notes]
```

Ask which formats are needed before generating.

---

## Grading Exam Wrappers

Exam wrappers should be graded on **completion and genuine engagement**, not accuracy.

**Recommended approach:**
- Full marks: all prompts answered with specific, honest responses
- Partial marks: some prompts answered or responses are very brief
- No marks: not submitted or clearly not engaged (e.g., "N/A" for all responses)

**Do not:**
- Grade based on whether the student's predicted grade matched actual grade
- Penalize students who performed poorly on the exam and honestly report it
- Require students to identify a "correct" explanation for their errors

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Pre-wrapper due date set to exam start time | Flag — must close before exam begins |
| Post-wrapper available only after grades are returned | Flag — students cannot complete post-wrapper without seeing their grade |
| Error analysis format matches delivery method | Use numbered list for text entry; table for HTML Topic |
| Study strategy list formatted as numbered list for text entry | Flag if checkboxes used — they don't render in text entry |
| Option B caveat communicated if chosen | Warn instructor about previous attempt visibility |
| Grading is engagement-based, not accuracy-based | Flag if accuracy grading planned; offer alternative |
| Wrapper weight is 1–3% | Flag if very high — undermines honest reflection |
| Pre and post wrappers designed as matched pair | Flag if only one built without reason |
| Debrief guide offered when instructor will review responses | Offer proactively |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Instructor wants post-wrapper to justify grade changes | Advise against — conflates reflection with grade appeal |
| Exam grades not returned when post-wrapper is due | Adjust post-wrapper available date |
| Instructor wants only a post-wrapper | Build it; note prediction comparison is lost but post-only still has value |
| Course has no exams, only assignments | Recommend **brightspace-self-assessment-generator** instead |
| Large class (200+ students) | Suggest ungraded or completion-graded; offer aggregate summary template for debrief |
| Instructor chooses Option B | Flag caveat about previous attempt visibility; recommend Option A |

---

## Handoff

> "Your exam wrapper is ready. Suggested next steps:
> 1. **Assignment Generator** — create the pre-wrapper and post-wrapper submission folders
> 2. **Course Calendar Builder** — place wrapper due dates around the exam in your schedule
> 3. **Self-Assessment Generator** — if you also want ongoing reflection activities between exams
> 4. **Course Outline Builder** — if building the outline at the end, exam wrapper details feed into the assessment structure"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Exam Wrapper Builder
Date: [date]
Course: [name and code]
Wrappers built: [count]
Exams:
  - Exam: [name] | Format: [MCQ/essay/mixed] | Wrapper type: [Pre/Post/Both] | Due dates: [pre date, post date]
  - [repeat per exam]
Graded: [yes — weight% / no]
Brightspace delivery: [Option A / B / C]
Debrief guide generated: [yes / no]
Output formats: [list]
Next recommended skill: [name]
---
```
