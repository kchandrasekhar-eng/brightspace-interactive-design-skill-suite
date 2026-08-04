---
name: brightspace-student-experience-preview
description: |
  Simulates what a student sees when they enter a Brightspace course — identifying navigation gaps, confusing instructions, orphaned content, missing context, and accessibility issues before students encounter them. Produces a student-perspective audit report with prioritized fixes. Triggers on phrases like "what does a student see", "student view", "preview my course", "check my course navigation", "is my course easy to follow", "student experience", "course walkthrough", or any request to evaluate a course from the student's perspective.
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

# Brightspace Student Experience Preview

You walk through a course as a student would — identifying what's confusing, what's missing, and what would cause a student to post "where do I find X?" in the first week.

## Skill Suite

This skill works closely with:
- **brightspace-redesign-planner** — course structure decisions affect student navigation
- **brightspace-html-builder** — confusing or incomplete HTML Topics can be rebuilt
- **brightspace-accessibility-auditor** — accessibility issues found here can be fixed there
- **brightspace-content-currency-auditor** — outdated content flagged here can be audited in depth there
- **brightspace-course-copy-auditor** — structural issues (broken links, release conditions) are handled there
- **brightspace-announcement-writer** — a well-written Week 1 announcement can address many navigation questions proactively
- **brightspace-session-debrief** — close out the preview session with a structured summary

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md`, `course-calendar.md`, and any uploaded HTML Topic files
- Save the preview report as `student-experience-report.md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Upload what you have: HTML Topic files, course outline, schedule, assignment instructions
- The more content uploaded, the more the preview can simulate

---

## Session Start — Establish the Student Profile

Before walking through the course, establish who the student is:

> "To simulate the student experience accurately, tell me about your typical student:"

1. Year level (first-year / second-year / upper-division / graduate)
2. Prior experience with online or blended learning (first time / some experience / experienced)
3. Likely device (desktop + mobile / mostly mobile / desktop only)
4. Any accessibility considerations typical for this course population? (e.g., ESL students, students with disclosed disabilities)
5. Is this a required course or elective? (affects motivation and baseline anxiety level)

---

## The Student Walkthrough

Simulate the student experience in this order — the same sequence a real student follows on Day 1.

### Step 1 — Course landing page

What does the student see when they first enter the course?

Check:
- Is there a welcome message, announcement, or orientation page? If not → flag: students will not know where to start
- Is the course title and instructor name clearly visible?
- Is the navigation bar labelled clearly? (Modules vs Content vs Week 1 — ambiguous labels confuse first-time users)
- Is there a "Start here" or "Course orientation" item? If not → flag
- Is the first thing visible an assessment or activity? (Students should encounter context before tasks)

### Step 2 — Orientation / Start here

Check:
- Does the orientation explain: how the course is structured, how to navigate, what tools are used, where to find help?
- Is the course outline or syllabus linked and easy to find?
- Are technical requirements stated? (browser, software, accounts needed)
- Is the instructor's contact info and office hours visible without hunting?
- Is there a course schedule or calendar visible? If not → flag

### Step 3 — Module 1 (or Week 1)

Simulate entering the first module as a student who has never seen the content:

Check:
- Is there a module overview that tells the student what they'll do and why?
- Are learning outcomes stated in student-friendly language?
- Is the sequence of activities clear? (read this → watch that → submit here)
- Are all links functional? (Claude cannot verify live links — flag all external links for instructor to check)
- Do activity instructions tell the student: what to do, how long it will take, where to submit, when it's due?
- Is there a clear path from reading/content to the graded activity?
- Are discussion prompts specific enough that a student knows what a good post looks like?

### Step 4 — Assessment instructions

Check each major assessment:
- Does the student know what to produce? (format, length, components)
- Does the student know how it will be graded? (rubric linked or criteria stated)
- Does the student know where to submit and by when?
- Is the late policy visible near the assessment, not only in the course outline?
- For group work: does the student know how groups are formed and when?
- Is there an example or model answer available? (flag if absent for major assessments)
- If there are timed quizzes or exams: is there a clear process stated for what to do if a student misses a timed activity?

### Step 5 — Navigation from a mobile device

Simulate on a narrow mobile screen (375px iPhone SE or 390px iPhone 14 — give both as reference points):

Check:
- Does the navigation bar collapse to a usable mobile menu?
- Are buttons and links large enough to tap? (minimum 44×44px)
- Do tables in HTML Topics reflow or require horizontal scrolling?
- Do video embeds render at the correct size on mobile?
- Are PDF links labelled clearly? (PDFs are difficult on mobile — flag if assigned without an alternative)

### Step 6 — "I'm lost" scenario

Simulate a student who can't find something:

Check:
- Is there a clearly labelled help or FAQ page?
- Is the instructor's email or contact method visible from every module?
- Is there a discussion forum for course questions (not just content discussions)?
- If a student misses Week 1, can they catch up independently? Is everything they need available asynchronously?
- If a student misses a timed quiz or exam, is there a clear process stated for what to do next?

---

## Finding Categories and Severity

### 🔴 Critical — Students will be unable to proceed or will submit incorrectly
- No "Start here" or orientation content
- Module 1 has no instructions — student doesn't know what to do
- Major assessment has no rubric, no due date, or no submission link
- Navigation labels are so ambiguous that first-time users cannot find content
- Required tools or accounts not announced before Week 1

### 🟠 High — Students will be confused and likely email the instructor
- Module overview missing — student doesn't know the purpose of activities
- Activity sequence not clear — student doesn't know what order to do things in
- Grading criteria not visible from the assessment page
- Late policy not visible near assessments
- No course questions discussion forum
- No process stated for missed timed assessments

### 🟡 Medium — Students will manage but experience is poor
- Mobile navigation is functional but clunky
- Discussion prompts are too vague
- No model answers for major assessments
- Instructor contact info buried (not on the landing page)
- Long pages with no section navigation

### 🟢 Minor — Polish items
- Section headers could be clearer
- Images could have better captions
- Some pages are text-heavy with no visual breaks

---

## Student Experience Report Format

```markdown
# Student Experience Preview Report
## [Course Name] — [Term]
Date: [date]
Student profile: [year level, device, prior experience]

## 🔴 Critical Issues ([count])
| # | Location | What a student encounters | Fix |
|---|---|---|---|

## 🟠 High Priority Issues ([count])
| # | Location | What a student encounters | Fix |
|---|---|---|---|

## 🟡 Medium Priority Issues ([count])
| # | Location | What a student encounters | Fix |
|---|---|---|---|

## 🟢 Minor Polish Items ([count])
| # | Location | Note | Fix |
|---|---|---|---|

## What Works Well
[3–5 things the course does well from a student perspective — always include this section.
If fewer than 3 things work well, note what's close to working and what small fix would get it there.]

## Overall Readiness
[Ready to launch / Ready with critical fixes / Needs significant work before launch]

## Top 3 Actions Before Launch
1. [most important fix]
2. [second most important]
3. [third most important]
```

---

## Quality Checks

| Check | Action |
|---|---|
| "Start here" or orientation exists | Flag if absent |
| Week 1 module has an overview | Flag if absent |
| Every major assessment has rubric or criteria | Flag if absent |
| Late policy visible near assessments | Flag if only in course outline |
| Timed assessment missed-activity process stated | Flag if absent |
| Mobile navigation tested | Flag if not checked |
| Course questions discussion forum exists | Flag if absent |
| "What works well" section always included | Ensure at least 3 positive observations; if fewer than 3 exist, note near-wins |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Instructor uploads very little content | Flag that preview is limited; identify the highest-risk gaps from what's available |
| Course uses no HTML Topics — pure Classic View | Calibrate walkthrough to text-based pages; note that Classic View navigation is less intuitive for new students |
| Course is in NCE (New Content Experience) | Note any NCE-specific navigation considerations |
| Course is fully in-person with minimal online presence | Calibrate preview to in-person navigation (course outline + Gradebook + Announcements) |
| Instructor is defensive about findings | Frame all findings as student perspective observations, not judgments of course quality |

---

## Handoff

> "Your student experience preview is complete. Suggested next steps:
> 1. **HTML Builder** — rebuild or fix the HTML Topics with critical or high issues
> 2. **Announcement Writer** — a strong Week 1 announcement can proactively answer the most common student questions
> 3. **Accessibility Auditor** — check any HTML Topics with accessibility flags
> 4. **Content Currency Auditor** — if outdated content was flagged, audit it in depth"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Student Experience Preview
Date: [date]
Course: [name and code]
Student profile: [year level, device, experience]
Critical issues: [count]
High priority issues: [count]
Medium issues: [count]
Minor items: [count]
Overall readiness: [Ready / Ready with fixes / Needs work]
Report saved: [student-experience-report.md yes/no]
Next recommended skill: [name]
---
```
