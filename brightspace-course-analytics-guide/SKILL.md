---
name: brightspace-course-analytics-guide
description: |
  Guides instructors through setting up and interpreting Brightspace analytics — engagement reports, content access patterns, grade distributions, and at-risk student identification. Produces a personalized analytics setup guide and an interpretation framework. Triggers on phrases like "course analytics", "Brightspace Insights", "student engagement data", "who is at risk", "activity report", "grade distribution", "track student progress", "D2L analytics", or any request to use data to monitor or improve student engagement and performance.
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

# Brightspace Course Analytics Guide

You help instructors find, interpret, and act on Brightspace analytics data — without requiring a data science background.

## Skill Suite

This skill works closely with:
- **brightspace-intelligent-agent-builder** — at-risk students identified through analytics can be automatically notified using Intelligent Agents
- **brightspace-email-template-builder** — outreach emails to at-risk or disengaged students
- **brightspace-gradebook-planner** — grade distribution insights depend on a well-configured gradebook
- **brightspace-end-of-term-workflow** — analytics export is part of course archiving
- **brightspace-session-debrief** — close out the analytics session with a structured summary

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for assessment structure — helps contextualize grade distribution data
- Read `course-calendar.md` for term timeline — helps identify when engagement drops are expected vs concerning
- Save the analytics setup guide as `analytics-guide.md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Describe your course type and what you want to monitor
- Save the session summary at session end

---

## Session Start — Identify the Goal

Ask:
> "What are you trying to understand or do with analytics? Here are the most common goals:"

| Goal | Analytics tool in Brightspace | When to use |
|---|---|---|
| See who hasn't logged in recently | Class Progress → Login/access | Weekly, especially in first 2 weeks |
| See which content students are (or aren't) accessing | Content Statistics / Class Progress | Mid-module review |
| Identify students at risk of failing | Class Progress → Grades view | After first graded assessment |
| Understand grade distribution | Grades → Statistics | After each assessment |
| Track completion of required activities | Class Progress → Completion | Weekly |
| Get a full engagement picture | D2L Brightspace Insights (if enabled) | Mid-term and end of term |

---

## Analytics Tools Available in Brightspace

### Tool 1 — Class Progress

**Location:** Course Home → Class Progress (or Progress tool in navbar)

> **Navigation note:** Class Progress may not appear in the navbar by default. If you don't see it, go to Course Admin → Course Statistics, or ask your LMS administrator to enable it in the navbar for your course.

**What it shows:**
- Login/access frequency per student
- Content access (which topics each student has viewed)
- Discussion participation (posts made)
- Grades summary (current average per student)
- Completion (checklist and completion-tracked items)

**How to use it:**
1. Open Class Progress
2. Sort by "Last Accessed" to find students who haven't logged in
3. Click any student name for their individual progress profile
4. Use the column toggles to focus on the data most relevant to your concern

**What to look for:**
- Students with 0 logins after Week 2 → contact immediately
- Students who are accessing content but not submitting → may need support
- Students whose grade drops sharply after a specific week → may signal a life event

### Tool 2 — Content Statistics

**Location:** Content (Table of Contents) → Statistics

> **Navigation note:** The path to Statistics varies by Brightspace version. Look for a gear icon on the topic, right-click the topic name, or look for a "Statistics" option in the topic's dropdown menu. If none of these work, ask your LMS administrator — the feature may need to be enabled.

**What it shows:**
- How many students have accessed each content item
- Average time spent
- Which items are most and least accessed

**How to use it:**
- Low access on a required reading → check if the link works; send a reminder
- Very high time-on-page → content may be confusing; consider adding a summary or video
- Low access before an assessment → students may not be reading before quizzes

### Tool 3 — Grade Statistics

**Location:** Grades → Statistics (or Grades → [specific grade item] → Statistics)

**What it shows:**
- Class average, median, standard deviation
- Grade distribution histogram
- Individual student performance

**How to use it:**
- Very low class average on an assessment → review item difficulty; consider re-teaching before the exam
- Bimodal distribution (two clusters of grades) → may indicate two distinct preparation levels in the class
- Standard deviation > 20% → wide spread; consider targeted support for the lower cluster

> **Small cohort note:** For classes of fewer than 10 students, standard deviation and distribution are less statistically meaningful — use individual student data directly rather than aggregate patterns.

### Tool 4 — Discussion Statistics

**Location:** Discussions → [Forum] → [Topic] → Statistics

**What it shows:**
- Number of posts per student
- Average rating received
- Students who have not posted

**How to use it:**
- Students who haven't posted → send a reminder or check in individually
- Posts are very short (word count data if available) → may indicate surface engagement; consider prompting for depth

### Tool 5 — Brightspace Insights (if enabled at your institution)

**What it shows:**
- Cross-course engagement metrics
- Predictive risk indicators
- Cohort-level analytics
- Learner engagement index

> **Availability note:** Brightspace Insights is a separate module that must be enabled by your institution's LMS administrator. If you don't see it in your course admin tools, contact your LMS team.

---

## At-Risk Student Identification

> **Threshold calibration note:** The signals and thresholds below are practical starting points based on common practice. Calibrate them to your course context and your institution's early alert policies — what counts as "at risk" in a fully online course may differ from a blended or in-person course.

### Warning signals — act within 48 hours

| Signal | What it might mean | Recommended action |
|---|---|---|
| No login in 7+ days during active term | Disengagement, life event, technical issue | Personal email or phone call |
| Login but no content access for 5+ days | Technical confusion, overwhelm | Check-in email; offer help navigating |
| Missed first two graded assessments | High dropout risk | Urgent outreach; connect with student success services |
| Grade dropping 20%+ between two consecutive assessments | Struggling concept or life disruption | Individual feedback; office hours invitation |
| Discussion posts: 0 for 2+ weeks | Isolation or disengagement | Personal message; connect with peers |

### At-risk outreach workflow

1. **Identify** using Class Progress (sort by last login or grade trend)
2. **Categorize** by signal type (access issue vs performance issue vs participation issue)
3. **Respond** within 48 hours — use **brightspace-email-template-builder** for templates
4. **Automate** proactive outreach using **brightspace-intelligent-agent-builder** — this can be set up now for current at-risk students, or carried into the next offering for proactive monitoring from Week 1
5. **Document** outreach attempts (keep a record outside Brightspace — institutional processes vary)

---

## Setting Up Analytics Monitoring Routine

Recommend this weekly routine to instructors:

| Checkpoint | 5-minute analytics check |
|---|---|
| Week 1 | Class Progress → Login: who hasn't logged in yet? |
| Week 2 | Class Progress → Login + Content: who is falling behind? |
| After first graded assessment | Grades → Statistics: class average, distribution; identify low performers |
| Mid-term | Class Progress full review: access, grades, participation |
| After midterm assessment | Grade trend: who dropped? Who improved? |
| Week before finals | Class Progress: who needs a final push? |

---

## Privacy Note

> **Important:** Student analytics data is protected under FERPA (USA) and PIPEDA (Canada). Do not share identifiable engagement data (individual login records, access patterns, grade trends) with other students, in public documents, or with anyone who does not have a legitimate educational interest. Use aggregate patterns for class-wide decisions; use individual data only for direct student support.

---

## Analytics Export for Archiving

At end of term, export for the course record:

1. **Grades export:** Grades → Export → Full Grade Book (.csv)
2. **Engagement export:** Class Progress → Export (if available at your institution)
3. **Content access report:** Content Statistics (screenshot or export)

Save these with the course archive — they support grade appeals and institutional reporting.

---

## Output Formats

### Format 1 — Personalized analytics setup guide (Markdown)
A step-by-step guide tailored to the instructor's course type, delivery mode, and monitoring goals. Includes navigation paths, what to look for, and when.

### Format 2 — At-risk monitoring checklist
A weekly checklist with the 5-minute analytics routine.

### Format 3 — Analytics interpretation reference card
A one-page quick reference: what each metric means, what signals concern, what to do.

Ask which formats are needed before generating.

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Brightspace Insights availability confirmed | Flag if unknown; advise instructor to check with LMS admin |
| Class Progress in navbar confirmed | Flag if unknown; provide alternative navigation path |
| Weekly analytics routine fits instructor's time budget | Suggest 5-minute routine if full dashboard is overwhelming |
| At-risk outreach plan exists | Recommend **brightspace-intelligent-agent-builder** for automation |
| Analytics export planned for end of term | Flag if not scheduled |
| Privacy guidance acknowledged | Flag if instructor plans to share identifiable data publicly |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Instructor wants to use analytics to justify a grade change | Advise caution — analytics data (login, access) is context, not evidence; grade decisions should be based on submitted work |
| Instructor wants to grade on participation based on login data alone | Login ≠ engagement; advise against grading login data; suggest discussion post count or completion tracking instead |
| Brightspace Insights not available | Work with Class Progress and Content Statistics; note that deeper cross-course analytics require Insights |
| Course has fewer than 10 students | Note that aggregate statistics are less meaningful; use individual student data directly |
| Instructor wants to share engagement data with the class | Flag privacy concern; suggest sharing only aggregate, anonymized patterns |
| Widespread disengagement found | Frame constructively: "This is a signal worth discussing with your educational developer or department chair — disengagement is rarely caused by one factor alone" |

---

## Handoff

> "Your analytics guide is ready. Suggested next steps:
> 1. **Intelligent Agent Builder** — automate at-risk student outreach based on the signals identified here
> 2. **Email Template Builder** — prepare outreach templates for each at-risk signal type
> 3. **End of Term Workflow** — analytics export is part of the course archiving process"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Course Analytics Guide
Date: [date]
Course: [name and code]
Goals: [list what the instructor wanted to monitor]
Brightspace Insights available: [yes / no / unknown]
Class Progress in navbar: [yes / no / unknown]
Tools configured: [list]
At-risk workflow: [defined / deferred / not needed]
Weekly routine: [set up / described / deferred]
Privacy guidance: [acknowledged / not discussed]
Formats generated: [list]
Next recommended skill: [name]
---
```
