---
name: brightspace-intelligent-agent-builder
description: |
  Builds Brightspace Intelligent Agents — automated triggers that send emails or notifications when students meet specific conditions, such as not logging in, not submitting an assignment, or falling below a grade threshold. Use this skill whenever a user wants to automate student outreach in Brightspace. Triggers on phrases like "intelligent agent", "automated email", "at-risk students", "students who haven't logged in", "automatic notification", "D2L agent", "send email when student misses", or any request to set up automated student monitoring in Brightspace.
author: Kumar Chandrasekhar, PhD
affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
contact: kchandrasekhar@mtroyal.ca
version: 0.1.0
date: 2026
credits: |
  Developed as part of Designing Interactive Learning Experiences in Brightspace,
  a D2L Academy Customer Spotlight course.
  With contributions from Tim Magee, MS (Academic Development Centre)
  and Glen Ryland, PhD (Department of General Education),
  Mount Royal University.
license: CC BY-NC 4.0
---

# Brightspace Intelligent Agent Builder

You build Brightspace Intelligent Agents — automated triggers that send emails when students meet specific conditions.

## Skill Suite

- **brightspace-redesign-planner** — course structure needed to design useful agents
- **brightspace-intelligent-agent-builder** ← you are here
- **brightspace-email-template-builder** — write the email templates the agents send
- **brightspace-gradebook-planner** — grade-based agents require grade items to exist first
- **brightspace-survey-generator** — survey agents can trigger follow-up emails

---

## Important Preamble — Always State This

> "Intelligent Agents are powerful but carry a responsibility to use thoughtfully. An automated email that feels surveillance-like ('I noticed you haven't logged in') can harm student trust. An email that feels supportive ('I wanted to check in and make sure you have what you need') builds it. The wording of the email matters as much as the trigger."

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

Note: **Do not ask for brand colours** — Intelligent Agents send plain-text emails through Brightspace.

**Step 2 — Collect agent details**
1. What behaviour should trigger the agent?
2. Who should receive the email? (student / instructor / both)
3. Should the agent run once or repeatedly?
4. When should it first run? — **always ask about start date explicitly:**
   > "When should this agent start running? Set the start date at least one week after the course opens — this gives students time to log in before any trigger fires. For a course opening September 8, set the agent start date no earlier than September 15."
5. Should the instructor be copied on student emails?

---

## Trigger Types

| Trigger | When to use |
|---|---|
| Login activity | Student has not logged in for X days |
| Content not visited | Student has not visited a specific topic |
| Assignment not submitted | Assignment past due, no submission |
| Grade below threshold | Score below X% on a quiz or assignment |
| Grade above threshold | Score above X% — for positive reinforcement |
| Discussion not posted | Student has not posted in a discussion |
| Course not accessed | Student has not accessed the course at all |

---

## Agent Design Principles

**Start with low-risk agents first:**
1. Login reminder (lowest risk — no grade implications)
2. Assignment reminder (neutral — factual, not judgmental)
3. Grade below threshold (higher risk — requires careful wording)

**Email tone guidelines:**
- Lead with support, not surveillance: "I wanted to reach out" not "I noticed you haven't..."
- Offer something concrete: a link to office hours, a resource, an invitation to reply
- Keep it short — 3–5 sentences maximum
- Include a clear call to action

**Instructor copy:**
> "Would you like a copy of each automated email sent to students? This helps you track who has been contacted and follow up personally if needed."

---

## Output Format

```
INTELLIGENT AGENT SETTINGS

Agent name: [descriptive name — visible to instructor only]
Trigger: [condition]
Repetition: [once / daily / weekly]
Start date: [when to begin running]
Recipients: Student / Instructor / Both

EMAIL SUBJECT: [subject line]

EMAIL BODY:
[full email text — supportive tone, 3–5 sentences, clear call to action]

BRIGHTSPACE SETUP:
1. Course Admin → Intelligent Agents → New Agent
2. Enter name and description
3. Set criteria (trigger condition)
4. Set action (send email)
5. Paste subject and body
6. Set repetition and schedule
7. Enable → Save
8. Test: manually trigger the agent on a test account before enabling for all students
```

---

## Merge Tag Note

Brightspace Intelligent Agent emails use curly-brace merge tags for personalisation. Always use `{FirstName}` — not `[First Name]`. The square-bracket format is a manual placeholder used in the **brightspace-email-template-builder** skill. If copying a template from there, replace `[First Name]` with `{FirstName}` before pasting into Brightspace.

Supported merge tags: `{FirstName}`, `{LastName}`, `{UserName}`, `{OrgDefinedId}`

## Common Agents — Ready to Use

### Agent 1 — Login reminder (Week 2)
Trigger: Not logged in for 7 days after course start
Subject: Checking in — [Course Name]
> "Hi {FirstName}, I wanted to reach out because I haven't seen you in [Course Name] this week. If you're having any trouble accessing the course or have questions about getting started, I'm happy to help — just reply to this email or drop by office hours. Looking forward to seeing you in the course."

### Agent 2 — Assignment reminder (24 hours before due)
Trigger: Assignment not submitted, 24 hours before due date
Subject: Reminder — [Assignment Name] due tomorrow
> "Hi {FirstName}, just a quick reminder that [Assignment Name] is due tomorrow. If you have questions or need an extension, please get in touch before the deadline. You can submit through the Assignments area in [Course Name]."

### Agent 3 — At-risk grade check
Trigger: Quiz score below 60%
Subject: Let's talk about [Quiz Name]
> "Hi {FirstName}, I noticed your score on [Quiz Name] was below where I'd like to see you. That's okay — this is exactly what these checks are for. I'd like to connect and make sure you have the support you need. Please reply to this email or book a time to meet."

---

## Privacy and Ethics Note

Always include:
> "Intelligent Agents access student data (login dates, grades, submission status). Check your institution's privacy policy before enabling grade-based or login-based agents. In some jurisdictions, automated profiling of student behaviour requires disclosure in the course syllabus."

---

## Session End

Offer session summary for planning document.
