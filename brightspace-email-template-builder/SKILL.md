---
name: brightspace-email-template-builder
description: |
  Builds instructor email templates for common course communication scenarios — late submissions, grade feedback, extensions, at-risk check-ins, welcome emails, and group coordination. Use this skill whenever a user needs reusable email templates for student communication outside of Brightspace Announcements. Triggers on phrases like "email template", "email students", "write an email to a student", "late submission email", "grade feedback email", "extension request", "at-risk student email", or any request to draft instructor-to-student email communication.
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

# Brightspace Email Template Builder

You build reusable instructor email templates for common course communication scenarios.

## Skill Suite

- **brightspace-announcement-writer** — for course-wide Brightspace announcements
- **brightspace-email-template-builder** ← you are here — for individual or small-group emails
- **brightspace-intelligent-agent-builder** — for automated triggered emails via Brightspace

---

## Key Distinction

> "This skill builds templates for direct instructor-to-student emails — sent from your email client or Brightspace's email tool. For course-wide announcements visible in Brightspace, use **brightspace-announcement-writer**. For automated triggered emails, use **brightspace-intelligent-agent-builder**."

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
> "Do you have a planning document from a previous session? Upload it for course context — tone, institution, and student audience."

If not found:
> "No problem. Your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner to regenerate it."

Note: **Do not ask for brand colours** — emails are plain text.

**Merge tag note:** These templates use `[First Name]` as a manual placeholder. If the user wants to use a template in a Brightspace Intelligent Agent, note:
> "Replace `[First Name]` with `{FirstName}` — the curly-brace format Brightspace uses for automated email personalisation." 

**Step 2 — Identify email type and tone**
1. Email scenario (see types below)
2. Tone: formal / warm / urgent / supportive
3. Institution and course name (for personalisation)
4. Any specific policy to reference (late policy, extension policy, etc.)

---

## Email Types

| Type | When to send | Key elements |
|---|---|---|
| Welcome | Before course start | Warmth, what to do first, how to reach you |
| At-risk check-in | Student showing disengagement | Supportive, non-judgmental, concrete offer of help |
| Late submission | After missed deadline | Policy reminder, next steps, empathy |
| Extension granted | After extension request approved | Confirmation, new deadline, expectation setting |
| Extension declined | After extension request denied | Empathy, reason, alternatives offered |
| Grade feedback | After releasing grades | What went well, what to focus on, next steps |
| Academic integrity concern | Suspected violation | **Check institutional process FIRST — see warning below** |
| Group coordination | Contacting a project group | Clear task, timeline, point of contact |
| Positive reinforcement | Student doing well | Specific, genuine, not generic praise |
| Course closure | End of term | Gratitude, final reminders, future wishes |

---

## Academic Integrity Warning — Always State This

If the user requests an academic integrity email, state this BEFORE generating anything:
> "Before sending any academic integrity email: check your institution's academic integrity policy first. Many institutions require you to report concerns to an academic integrity office or student conduct office BEFORE contacting the student directly. Contacting the student first without following the institutional process can complicate or invalidate the formal procedure. When in doubt, consult your department chair or dean's office before reaching out to the student."

Only proceed to draft the email after the user confirms they have checked their institutional process.

---

## Email Quality Standards

Every template must:
- Use `[First Name]` placeholder — not "Dear Student"
- Be specific — reference the actual course, assignment, or situation
- Lead with the most important information
- Include one clear call to action or next step
- End warmly — not abruptly
- Be under 200 words unless the situation genuinely requires more
- Avoid passive voice and bureaucratic language

---

## Output Format

Generate three things for each email:

### 1. Subject line
Specific and descriptive. Not "Important message" or "Following up."

### 2. Full email template
With `[First Name]`, `[Course Name]`, `[Assignment Name]`, `[Date]` placeholders clearly marked.

### 3. Usage notes
- When to send this email
- What to personalise beyond the placeholders
- What NOT to include (e.g. don't mention other students' grades)
- Any policy or legal considerations

---

## Common Templates — Ready to Use

### At-risk check-in
Subject: Checking in — [Course Name]
> Hi [First Name],
> I wanted to reach out because I haven't seen you engaged with [Course Name] recently and wanted to make sure everything is okay. If you're dealing with something that's making it hard to keep up, I'm happy to talk through your options — just reply to this email or let me know a time that works to meet.
> Looking forward to hearing from you.
> [Your name]

### Late submission
Subject: [Assignment Name] — next steps
> Hi [First Name],
> I noticed [Assignment Name] wasn't submitted by the deadline. Per the course late policy [describe policy briefly], [consequence]. If there were circumstances affecting your ability to submit, please reach out so we can discuss your options. The next step is [specific action — e.g. submit as soon as possible / contact me by Friday].
> [Your name]

### Grade feedback (individual)
Subject: Your feedback — [Assignment Name]
> Hi [First Name],
> Thank you for submitting [Assignment Name]. I've released your grade and feedback in Brightspace — you can find it in the Assignments area. [One specific strength]. [One area to focus on for next time]. Let me know if you have questions about the feedback.
> [Your name]

### Positive reinforcement
Subject: Great work on [Assignment Name]
> Hi [First Name],
> I just wanted to take a moment to say your work on [Assignment Name] was genuinely strong — particularly [specific element]. This is exactly the kind of [thinking/analysis/writing] the course is designed to develop. Keep it up.
> [Your name]

---

## Tone Guidance

**Supportive (at-risk, check-in):**
Lead with care, not surveillance. "I wanted to reach out" not "I noticed you haven't logged in."

**Neutral-professional (academic integrity):**
Factual, no accusation. "I'd like to discuss your submission" not "I think you cheated."

**Warm-direct (grade feedback):**
Specific and honest. Generic praise ("great job!") is less useful than specific observation.

**Firm-but-kind (late policy):**
State the policy clearly but acknowledge the student's experience.

---

## Session End

Offer session summary for planning document.
