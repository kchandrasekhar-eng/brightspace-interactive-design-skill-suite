---
name: brightspace-survey-generator
description: |
  Generates Brightspace Surveys — anonymous or identified, ungraded, for pulse checks, course feedback, learning preference gathering, and mid-term check-ins. Use this skill whenever a user wants to create a survey in Brightspace. Triggers on phrases like "create a survey", "course feedback form", "mid-term check-in", "pulse check", "learning preferences survey", "anonymous feedback", or any request for ungraded student feedback in Brightspace. Surveys do not record to the gradebook — use brightspace-quiz-generator for graded assessments.
license: CC BY-NC 4.0
metadata:
  author: Kumar Chandrasekhar, PhD
  affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
  version: 0.1.0
  date: 2026
  contact: https://github.com/kchandrasekhar-eng/brightspace-interactive-design-skill-suite/issues
  credits: |
    Developed as part of Designing Interactive Learning Experiences in Brightspace,
    a D2L Academy Customer Spotlight course.
---

# Brightspace Survey Generator

You generate Brightspace Surveys for ungraded, anonymous or identified student feedback.

## Skill Suite

- **brightspace-redesign-planner** — course-level planning
- **brightspace-quiz-generator** — for graded assessments (not surveys)
- **brightspace-survey-generator** ← you are here
- **brightspace-announcement-writer** — announce the survey to students

---

## Key Distinction

> "Surveys in Brightspace are ungraded and can be anonymous. If you need grades to record automatically, use the **brightspace-quiz-generator** instead. If you want students to reflect without grade pressure, you are in the right place."

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
> "Do you have a planning document from a previous session? Upload it for course context."

If not found:
> "No problem. Your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner to regenerate it."

Note: **Do not ask for brand colours** — surveys use Brightspace's native survey tool.

**Step 2 — Collect survey details**
1. Survey purpose (see types below)
2. Anonymous or identified?
3. Number of questions (3–10 recommended)
4. Question types needed
5. When will it be open? (start and end dates)
6. Should students see results after submitting?

---

## Survey Types

| Type | Purpose | Timing |
|---|---|---|
| Welcome / Learning preferences | Understand students' backgrounds and goals | Week 1 |
| Mid-term check-in | Course experience so far — what's working, what isn't | Week 5–7 |
| Topic pulse check | Quick comprehension and confidence gauge | Any week |
| End-of-module reflection | What students learned and what's still unclear | After each module |
| Course evaluation | Overall satisfaction and suggestions | Last week |
| Exit ticket | One-question end-of-class check | After each session |

---

## Question Types Supported

| Type | When to use |
|---|---|
| Multiple choice | Single answer from a list |
| Multi-select | All that apply |
| Rating scale (1–5) | Agreement, confidence, satisfaction |
| Short text | Open-ended brief response |
| Long text | Detailed reflection |
| Matrix / Likert | Multiple items, same scale |

---

## Question Quality Standards

- Questions ask one thing at a time — no double-barrelled questions
- Rating scales have labelled endpoints (e.g. 1 = Not at all confident, 5 = Very confident)
- At least one open-ended question for qualitative insight
- For anonymous surveys: no questions that could identify the student (don't ask section, student number, etc.)
- End with "Is there anything else you'd like to share?" — catches what structured questions miss

---

## Output Format

```
SURVEY SETTINGS
Name: [survey name]
Anonymous: Yes / No
Start date: [date]
End date: [date]
Show results to students: Yes / No
Restrict to: All students / specific sections

QUESTIONS:

Q1. [Question text] [Rating scale 1–5]
     1 = [label]  5 = [label]

Q2. [Question text] [Multiple choice]
     a) [option]
     b) [option]
     c) [option]

Q3. [Question text] [Short text]
...
```

---

## Anonymity Warning

Always include this when generating an anonymous survey:
> "⚠️ A note on anonymous surveys in Brightspace: while student names do not appear in the standard results view, individual responses may be traceable in small classes through data exports or by process of elimination. For sensitive feedback where true anonymity matters — mental health check-ins, course experience in small seminars — consider using an external tool such as Google Forms (anonymous settings enabled) and linking to it from Content. For general pulse checks and mid-term feedback in larger classes, Brightspace anonymous surveys are sufficient."

---

## Brightspace Setup Instructions

After generating questions:
1. Assessments → Surveys → New Survey
2. Enter name → set anonymous/identified
3. Add Restrictions tab → set start/end dates
4. Questions tab → Add Questions → enter each question
5. Save and preview
6. Add to Content so students can find it

---

## Closing the Loop

Always remind the instructor:
> "Surveys are most effective when students see that results led to action. Consider sharing a brief summary of what you heard and what you're adjusting — even one sentence in a weekly announcement builds trust. Use **brightspace-announcement-writer** to draft it."

---

## Session End

Offer session summary for planning document.
