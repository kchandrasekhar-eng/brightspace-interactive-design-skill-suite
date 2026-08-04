---
name: brightspace-end-of-term-workflow
description: |
  Guides instructors through the complete end-of-term process in Brightspace — final grade submission, student communication, grade appeals preparation, course archiving, and preparation for the next offering. Produces checklists, email templates, and a course closeout report. Triggers on phrases like "end of term", "final grades", "grade submission", "close out my course", "archive my course", "course wrap-up", "end of semester checklist", or any request to manage the end-of-term process in Brightspace.
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

# Brightspace End of Term Workflow

You guide instructors through a complete, stress-free end-of-term process — from final grading to course archiving to handoff for the next offering.

## Skill Suite

This skill works closely with:
- **brightspace-gradebook-planner** — gradebook must be fully configured before final grades are released
- **brightspace-email-template-builder** — end-of-term student communication templates
- **brightspace-announcement-writer** — final course announcements
- **brightspace-intelligent-agent-builder** — at-risk or incomplete-grade student outreach
- **brightspace-course-analytics-guide** — export engagement data as part of the course archive
- **brightspace-course-copy-auditor** — run before copying the course to the next term
- **brightspace-content-currency-auditor** — run before the next offering to flag outdated content
- **brightspace-session-debrief** — close out the end-of-term session with a structured summary

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for assessment weights and grade structure
- Read `course-calendar.md` for final assessment dates
- Save the closeout report as `end-of-term-report.md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Describe your course and institution — grade submission processes vary by institution
- Save the session summary at session end

---

## Session Start — Establish Context

Ask:
1. Course name, code, and term
2. Institution name (grade submission processes are institution-specific)
3. Approximate number of students enrolled
4. Grade submission deadline (registrar's deadline)
5. Has the final assessment been graded and entered in Brightspace?
6. Are there any students with incomplete grades, academic accommodations, or pending grade appeals?
7. Will this course run again next term? (affects archiving decisions)

---

## End-of-Term Phases

### Phase 1 — Final grading (before submission deadline)

**Step 1: Complete all grade entries**
- [ ] All assignments graded and returned
- [ ] All quiz/exam grades entered and reviewed
- [ ] Participation grades entered (if applicable)
- [ ] Late submissions resolved — graded, zeroed, or extension noted
- [ ] Incomplete grade arrangements documented outside Brightspace (institutional process)

**Step 2: Audit the gradebook**
- [ ] All grade items have entries for every student (no blanks that should be zeros)
- [ ] Calculated final grade matches manual spot-checks
- [ ] Grade scheme is applied correctly (letter grades, pass/fail, percentage — confirm with institutional requirements)
- [ ] Bonus or extra credit items are correctly weighted
- [ ] Override grades documented with rationale (in notes field or separate record)

**Step 3: Check final grade calculation**
Brightspace calculates final grades from grade items — but this can go wrong. Common issues:
- Grade items not included in the final grade calculation (excluded items show a dash, not zero)
- Ungraded items treated as zero vs excluded
- Dropped lowest score not working as expected
- Category weights that don't sum to 100%

**Spot-check process:**
- For classes of 10 or more: pick 3 students with different grade profiles (high, middle, low), calculate each final grade manually, and compare to Brightspace
- For classes of fewer than 10: spot-check all students — it takes 5 minutes and eliminates risk entirely
- If there's a discrepancy → flag for investigation before submission; do not submit until resolved

**Step 4: Release final grades to students**
- [ ] Decide when to release: before or after submission to registrar (institution policy may dictate)
- [ ] Draft and send a "final grades available" announcement (use **brightspace-announcement-writer**)
- [ ] Include: where to find grades in Brightspace, grade appeal process and deadline, next steps

### Phase 2 — Grade submission (to registrar)

> **Institution-specific:** Grade submission processes vary widely. This skill provides a framework — always follow your institution's registrar procedures. If you are unsure of the submission path at your institution, contact your registrar or LMS administrator before the deadline — do not guess.

**Common submission methods:**
- Direct from Brightspace to SIS (Student Information System) via integration
- Export from Brightspace Grades → upload to registrar portal
- Manual entry into registrar portal

**Pre-submission checklist:**
- [ ] All students have a final grade (no blanks unless Incomplete/Deferred is intentional)
- [ ] Grade scale matches registrar's requirements (letter grade vs percentage vs GPA)
- [ ] Audit trail: screenshot or export of Brightspace final grades saved before submission
- [ ] Submission deadline confirmed: [date/time]

**If using Brightspace-SIS integration:**
- Confirm the integration is active for this course section
- Check that course section IDs match between Brightspace and SIS
- Submit via Course Admin → Grades → Release Final Calculated Grades (exact path varies by institution — confirm with your LMS team if unsure)

### Phase 3 — Student communication

**Communication sequence:**

| When | Message | Channel | Timing note |
|---|---|---|---|
| Final grades calculated | "Final grades are available in Brightspace" | Brightspace Announcement | As soon as grades are released |
| Grade appeal window opens | "Grade appeal process and deadline" | Brightspace Announcement or Email | Same day grades released |
| Grade appeal window closes | "Grade appeals closed — thank you for a great term" | Optional email | Day of close |
| Course access expiry approaching | "Course closes on [date] — save any work you need" | Brightspace Announcement | At least 2 weeks before expiry |

**Templates:** Use **brightspace-email-template-builder** to generate these. Key messages to have ready:
- Final grades announcement
- Grade appeal instructions
- Incomplete grade agreement (if applicable)
- Course access expiry notice

### Phase 4 — Grade appeals preparation

Document while memory is fresh:
- [ ] Save all graded work (Brightspace retains submissions, but confirm your institution's data retention policy)
- [ ] Note any unusual grading decisions made during the term (accommodations, extensions, late penalty waivers)
- [ ] Save a copy of the final rubrics used for major assessments
- [ ] Note any students who had documented accommodations that affected grading

**If a grade appeal is received:**
- Pull the student's submission from Brightspace Assignments
- Pull their complete grade history from the Gradebook
- Review the rubric and feedback provided
- Compare to the stated assessment criteria in the course outline

### Phase 5 — Course archiving

**What to preserve before the course closes:**
- [ ] Export final gradebook (Grades → Export → Full Grade Book as .csv)
- [ ] Export student submission files for major assessments (Assignments → Download All Submissions)

> **Large course caveat:** For courses with 100+ students, the Download All Submissions function may time out. If this happens, download submissions by individual assignment folder rather than all at once, or contact your LMS administrator for a bulk export option.

- [ ] Save a copy of the course outline / syllabus
- [ ] Export course analytics report (Class Progress → Export if available; otherwise screenshot key views) — see **brightspace-course-analytics-guide** for export steps
- [ ] Note any content that should be updated before next offering

**Brightspace data retention:**
- Student submissions are typically retained for [institution-specific period — confirm with registrar]
- Instructor grades are accessible until the course is deactivated
- After deactivation, data may only be available through institutional backup systems

**If the course will be offered again:**
- [ ] Run **brightspace-content-currency-auditor** to flag outdated content
- [ ] Run **brightspace-course-copy-auditor** before copying to the next shell
- [ ] Note improvements for next offering (add to `session-log.md` as "Next offering notes")

### Phase 6 — Reflective close

Before closing the session, capture while the term is fresh:

**Quick course reflection (5 minutes — saves hours next term):**
1. What worked well this term that should be preserved?
2. What didn't work and should be changed?
3. Any assessments that need redesigning?
4. Any content that felt outdated or didn't land well?
5. What student questions came up most frequently? (Answers to these should be added to the course for next term)

Save these notes in `session-log.md` under "Next offering notes."

---

## Output Formats

### Format 1 — End-of-term checklist (Markdown)
A complete, printable checklist covering all six phases with checkboxes.

### Format 2 — Communication templates
Ready-to-send announcement and email drafts for each Phase 3 communication. Pass to **brightspace-announcement-writer** or **brightspace-email-template-builder** for formatting.

### Format 3 — Course closeout report (Markdown)
```markdown
# Course Closeout Report
## [Course Name] — [Term]
Date: [date]

## Grade summary
Enrollment: [count]
Final grade distribution: [A/B/C/D/F counts or percentage bands]
Incomplete grades: [count and reason]
Grade appeals: [none / pending / resolved]

## Grading audit
Spot-check result: [pass / discrepancy found — describe]
Gradebook export saved: [yes/no]
Submissions exported: [yes/no]

## Student communication
Final grades announcement sent: [date]
Grade appeal window: [open date → close date]
Course access expiry: [date]
Expiry notice sent: [date]

## Archive status
Gradebook exported: [yes/no]
Submissions saved: [yes/no]
Analytics exported: [yes/no]
Course copy scheduled: [yes/no — target term]

## Next offering notes
[What worked / What to change / Content to update]
```

Ask which formats are needed before generating.

---

## Quality Checks

| Check | Action if failed |
|---|---|
| All students have a final grade before submission | Flag blanks; confirm Incomplete/Deferred is intentional |
| Spot-check passes (manual vs Brightspace calculation) | Investigate discrepancy before submission — do not submit if grades don't match |
| Grade submission deadline confirmed | Flag if unknown; registrar deadline is non-negotiable |
| Course access expiry notice sent at least 2 weeks before close | Flag if not scheduled |
| Grade appeal process communicated | Flag if not sent |
| Gradebook exported before course deactivation | Flag if not done |
| Analytics exported | Flag if not done |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Grade discrepancy found in spot-check | Do not submit grades; investigate and resolve before deadline |
| Student has no final grade and no Incomplete arrangement | Flag immediately — this student needs a grade before submission |
| Grade submission deadline has passed | Advise instructor to contact registrar immediately — late submissions have institutional consequences |
| Instructor wants to change a submitted grade | Explain institutional process (typically a Grade Change form through the registrar) |
| Course data retention policy unknown | Advise instructor to confirm with registrar before deactivating the course |
| Download All Submissions times out | Download by individual assignment folder; or contact LMS admin for bulk export |

---

## Handoff

> "Your end-of-term workflow is complete. Suggested next steps:
> 1. **Course Analytics Guide** — export and save engagement data as part of your course archive
> 2. **Course Copy Auditor** — run before copying the course to the next term
> 3. **Content Currency Auditor** — flag outdated content before the next offering
> 4. **Announcement Writer** — draft any remaining student communications
> 5. **Course Outline Builder** — if the outline needs updating for the next term"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: End of Term Workflow
Date: [date]
Course: [name and code]
Term: [term]
Enrollment: [count]
Grade submission deadline: [date]
Grades submitted: [yes / no / pending]
Grade appeals: [none / count]
Incomplete grades: [none / count]
Gradebook exported: [yes / no]
Submissions exported: [yes / no]
Analytics exported: [yes / no]
Course copy planned: [yes — target term / no]
Next offering notes: [brief summary]
Next recommended skill: [name]
---
```
