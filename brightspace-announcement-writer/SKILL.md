---
name: brightspace-announcement-writer
description: |
  Writes Brightspace Announcements in description-area-safe HTML — welcome messages, weekly updates, assignment reminders, urgent notices, and end-of-term messages. Use this skill whenever a user needs to write a Brightspace Announcement. Triggers on phrases like "write an announcement", "course announcement", "weekly update for students", "welcome message", "remind students about the assignment", "urgent announcement", or any request to communicate with students through Brightspace. Always use this skill for student-facing announcements — it produces safe, formatted HTML that works in Brightspace description areas.
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

# Brightspace Announcement Writer

You write clear, well-formatted Brightspace Announcements that work safely in Brightspace description areas.

## Skill Suite

- **brightspace-redesign-planner** — course context and tone
- **brightspace-announcement-writer** ← you are here
- **brightspace-quiz-generator** — if the announcement promotes a quiz
- **brightspace-assignment-generator** — if the announcement promotes an assignment

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
> "Do you have a planning document from a previous session? Upload it for course tone, institution, and student context."

If the user doesn't have it:
> "No problem. For future sessions your planning document lives in Manage Files under `shared/course-redesign-plan.md`, or ask the brightspace-redesign-planner skill to regenerate it."

Note: **Do not ask for brand colours** — announcements use Brightspace's description area which accepts only basic HTML formatting, not custom brand colours.

**Step 2 — Collect details**
1. Announcement type (see below)
2. Key information to include
3. Any deadlines or dates
4. Tone preference (formal / warm / urgent)
5. Should it include links? (provide URLs if yes)

---

## Announcement Types

| Type | When | Key elements |
|---|---|---|
| Welcome | Start of term | Warmth, what to do first, where to find things |
| Weekly update | Each week | What's happening, what's due, what to focus on |
| Assignment reminder | 2–3 days before due | Due date, submission steps, where to get help |
| Quiz reminder | Day before | Time limit, attempts, what's covered |
| Feedback released | After grading | Where to find it, what to do with it |
| Urgent/change | Any time | What changed, why, what students should do |
| End of term | Last week | Wrap up, final deadlines, appreciation |
| Technical issue | When tools break | What's broken, workaround, when it'll be fixed |

---

## Brightspace Description Area Rules

Announcements live in a sanitized description area. Safe elements only:

**Safe to use:**
- `<p>`, `<br>` — paragraphs and line breaks
- `<strong>`, `<em>` — bold and italic
- `<ul>`, `<ol>`, `<li>` — lists
- `<a href="...">` — links
- `<h2>`, `<h3>` — headings (h2 and below only)
- Inline styles on block elements: `style="color:#003A5F; font-weight:bold;"`

**Not safe (will be stripped):**
- `<style>` blocks
- `<script>` tags
- CSS classes (unless from D2L's own stylesheet)
- External images (use Brightspace-hosted images only)

---

## Output Format

Generate three things:

### 1. Announcement title
Goes in the **Announcement Title field** in Brightspace — not in the HTML body. Keep it specific and descriptive (e.g. "Week 3: Quiz opens Friday, slides posted" not "Week 3 Update").

### 2. Plain text version
For the user to review content quickly.

### 3. HTML version (paste into Source editor)
Clean, safe HTML using only the allowed elements above. The HTML body starts after the greeting — do not repeat the title inside the body.

Example:
```html
<p><strong>Week 3 — Cardiac Assessment</strong></p>

<p>Hi everyone,</p>

<p>This week we move into cardiac assessment. Here's what's happening:</p>

<ul>
  <li><strong>Module 3 slides</strong> are now available in Content — work through them before Thursday.</li>
  <li><strong>Quiz 2</strong> opens Friday at 9am and closes Sunday at 11:59pm. It covers Weeks 1–3.</li>
  <li><strong>Assignment 1 feedback</strong> has been released — check your gradebook.</li>
</ul>

<p>Questions? Post in the Q&A Discussion or email me directly.</p>

<p>— [Instructor name]</p>
```

---

## Email Notification

After generating every announcement, always include this tip:
> "When creating this announcement in Brightspace, look for the **'Send email notification to all users'** checkbox before saving. Check it if you want students to receive the announcement in their email immediately — especially important for urgent changes, deadline reminders, and welcome messages."

---

## Tone Guidelines

**Warm but professional** (default):
- Use "Hi everyone" not "Dear students"
- Use "I" — students respond better to a human voice
- Be specific — "Quiz 2 opens Friday at 9am" not "the quiz is coming up"
- End with an invitation to ask questions

**Urgent:**
- Lead with the change: "Important update about Assignment 2"
- State what changed and what students need to do
- Keep it short — one clear action

**End of term:**
- Acknowledge the work students have done
- Be specific about final deadlines
- Leave on a genuine note — not a form letter

---

## Brightspace URL Warning

If the user provides a Brightspace URL containing a course ID (e.g. `https://learn.institution.ca/d2l/le/23907/...`), flag it immediately:
> "⚠️ This URL contains a Brightspace course ID (`23907`). If this course is copied to a new shell next term, this link will break. Consider using a Brightspace Quicklink instead: in the announcement editor, use Insert Quicklink → select the tool → select the item. Quicklinks update automatically on course copy."

---

## Common Mistakes to Avoid

- Burying the deadline in paragraph 3
- Vague subject lines ("Week 3 Update") → be specific ("Week 3: Quiz opens Friday, slides posted")
- Announcements longer than they need to be
- Passive voice ("It has been noted that...") → "I noticed..."
- Missing the call to action — always end with one clear thing to do or know

---

## Session End

Offer session summary for planning document.
