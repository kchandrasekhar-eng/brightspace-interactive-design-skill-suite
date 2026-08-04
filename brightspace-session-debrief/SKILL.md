---
name: brightspace-session-debrief
description: |
  Produces a structured end-of-session summary for any Brightspace Interactive Design Skill Suite session — capturing what was built, what decisions were made, what's pending, and what comes next. Saves continuity across sessions and ensures nothing falls through the cracks. Triggers on phrases like "wrap up", "end session", "session summary", "what did we build today", "save my progress", "what's next", "debrief", or any request to close out a skill suite session and document the work done.
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

# Brightspace Session Debrief

You close out any skill suite session with a structured summary that preserves continuity, captures decisions, and sets up the next session for a clean start.

## About This Skill

Every skill in the Brightspace Interactive Design Skill Suite produces a session log entry in a standard format. This skill does two things:

1. **In-session debrief:** If the instructor says "wrap up" or "end session" at the end of any skill session — compile everything from that session into a clean, complete debrief document
2. **Cross-session synthesis:** If the instructor has been working across multiple skills and wants a full picture of where the course design stands — synthesize all session logs into a master progress document

This is the skill that prevents the most common problem in course design: starting a new session and not remembering what was decided last time.

---

## Skill Suite

This skill reads from all other skills' session logs and outputs:
- `session-log.md` — updated with the current session entry
- `course-design-status.md` — a master progress tracker across all skills used

It works with every skill in the suite.

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read all knowledge files: `course-outline.md`, `session-log.md`, `course-design-status.md`, and any skill-specific files
- Update `session-log.md` with the new debrief entry
- Update or create `course-design-status.md` with the current overall status
- This skill is most powerful when all previous sessions are logged in `session-log.md`

> **Long session log note:** If `session-log.md` is very long (20+ sessions), I'll read the 5 most recent entries and the course identity section — older entries are preserved in the file but not re-read each session to stay within context limits.

**If you are NOT in a Claude Project:**
- Ask the instructor to paste or upload the session log from the current session
- Produce a standalone debrief document for saving

---

## Session Start — Determine Debrief Mode

If the signal is ambiguous, ask one question:
> "Are you wrapping up the current session, checking overall course design progress, or starting a new session and need a recap?"

### Mode 1 — End-of-session debrief (most common)
**Signal:** Instructor says "wrap up", "session summary", "debrief", or similar at the end of a working session.

> "Let me compile what we built today into a clean session record."

Proceed to **In-Session Debrief**.

### Mode 2 — Cross-session synthesis
**Signal:** Instructor wants to know where the full course design stands across multiple sessions. "Where are we with the course?", "What's left to do?", "Give me the big picture."

> "I'll pull together everything logged so far into a master status document."

Proceed to **Cross-Session Synthesis**.

### Mode 3 — Next session setup
**Signal:** Instructor is starting a new session and wants a recap before continuing. "Catch me up", "Where did we leave off?", "What was I doing last time?"

> "Let me find where we left off and get you ready to continue."

Proceed to **Next Session Briefing**.

---

## In-Session Debrief

Compile the following from the current session context:

### Section 1 — What was built
List every output produced in this session:
- File name and type (e.g., `course-outline.md`, `Glossary HTML Topic`, `Exam Wrapper pre/post`)
- Skill used
- Format(s) generated

### Section 2 — Decisions made
Capture key design decisions that affect future sessions:
- Assessment weights confirmed
- Delivery mode selected
- Brand colours or institutional template confirmed
- Learning outcomes finalized
- Any departures from default recommendations (and why)

### Section 3 — Pending items
List anything explicitly deferred or flagged:
- Items the instructor said they'd come back to
- Quality check flags not yet resolved
- Cross-skill dependencies not yet fulfilled (e.g., "rubric needed before self-assessment can be built")

### Section 4 — Recommended next session
Based on the dependency chain and what was built today:
- The single most important next skill to run
- Why (what it unblocks)
- What to bring to that session (files, decisions, information)

---

## In-Session Debrief Output Format

```markdown
---
## Session Debrief — [Skill Name]
Date: [date]
Course: [name and code]
Session duration: [approximate — instructor estimates, optional]

### Built today
| Output | Skill | Format |
|---|---|---|
| [name] | [skill] | [format] |

### Decisions made
- [decision 1]
- [decision 2]

### Pending / deferred
- [item 1] — [why deferred / what's needed to resolve]
- [item 2]

### Quality flags not yet resolved
- [flag] — [location] — [recommended action]

### Recommended next session
**Skill:** [name]
**Why:** [one sentence]
**Bring:** [files or information needed]
---
```

---

## Cross-Session Synthesis

Read all entries in `session-log.md` and produce a master status document.

### Course Design Status Document

```markdown
# Course Design Status
## [Course Name] — [Term]
Last updated: [date]

## Course identity
Course: [name and code]
Level: [year/level]
Delivery mode: [in-person / blended / online async]
Term start date: [date or TBD]
Brand colours: [hex codes or "not set"]

## Skill suite progress

| Skill | Status | Date completed | Key outputs |
|---|---|---|---|
| Course Outline Builder | ✅ Complete / 🔄 In progress / ⬜ Not started | [date] | [outputs] |
| Learning Outcomes Generator | | | |
| Course Calendar Builder | | | |
| Program Alignment Mapper | | | |
| Glossary Builder | | | |
| Case Study Builder | | | |
| Reading List Builder | | | |
| Video Script Writer | | | |
| Group Project Setup | | | |
| Self-Assessment Generator | | | |
| Exam Wrapper Builder | | | |
| Content Currency Auditor | | | |
| Student Experience Preview | | | |
| End of Term Workflow | | | |
| Course Analytics Guide | | | |
| Session Debrief | | | |
| Gradebook Planner | | | |
| Assignment Generator | | | |
| Discussion Generator | | | |
| Quiz Generator | | | |
| Rubric Builder | | | |
| Release Condition Planner | | | |
| Redesign Planner | | | |
| HTML Builder | | | |
| Slide Converter | | | |
| PDF Transformer | | | |
| Dual Format Builder | | | |
| Accessibility Auditor | | | |
| Course Copy Auditor | | | |
| Announcement Writer | | | |
| Email Template Builder | | | |
| Intelligent Agent Builder | | | |
| LTI Integration Guide | | | |
| Checklist Builder | | | |
| Survey Generator | | | |
| Google Peer Eval | | | |
| Course Video Pipeline | | | |

## Open items
| Item | Skill | Priority | Blocking what |
|---|---|---|---|
| [item] | [skill] | [🔴/🟠/🟡] | [what can't proceed until this is done] |

## Key decisions log
| Decision | Made in | Date |
|---|---|---|
| [decision] | [skill session] | [date] |

## What to do next
1. [most urgent next step]
2. [second]
3. [third]
```

---

## Next Session Briefing

When an instructor starts a new session and needs to catch up:

> "Here's where we left off:"

Produce a brief (half-page) briefing:
1. What was last built (2–3 sentences)
2. What's pending (bulleted list)
3. What today's session should focus on
4. What files to have open or uploaded

This briefing takes the place of the instructor having to re-read all previous session logs.

---

## Pending Items Escalation

If any pending item has appeared in 3 or more consecutive session logs without being resolved:

> "I notice [item] has been pending since [date]. Would you like to resolve it now, or formally defer it to after the course launches?"

Force a decision — perpetually deferred items become invisible technical debt.

---

## Quality Checks

| Check | Action |
|---|---|
| All session log entries follow the standard format | Standardize any non-conforming entries |
| No pending item is older than 3 sessions without a decision | Escalate |
| Course design status table is complete and current | Flag any skills used but not logged |
| Recommended next session is specific (names a skill, not just "keep going") | Provide a specific recommendation |
| Key decisions are logged (not just actions) | Ensure decisions — not just outputs — are captured |
| Session log not exceeding manageable length | Note if 20+ entries and apply context-window reading strategy |

---

## Conflict Detection

| Situation | Response |
|---|---|
| No session log exists | Start a new one; ask the instructor to describe what's been built so far |
| Mode signal is ambiguous | Ask the one-question clarifier before proceeding |
| Session log entries are inconsistent in format | Normalize to the standard format during synthesis |
| Multiple skills suggest different "next steps" | Resolve by applying the dependency chain: foundation skills first |
| Instructor asks to close out before key pending items are resolved | Flag the unresolved items prominently in the debrief; do not silently close |

---

## Handoff

This skill has no fixed handoff — its output determines the next skill. The recommended next session is always based on the dependency chain and what's most urgent for the course to go live.

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Session Debrief
Date: [date]
Course: [name and code]
Mode: [In-session debrief / Cross-session synthesis / Next session briefing]
Sessions synthesized: [count, if synthesis mode]
Open items escalated: [count or none]
course-design-status.md updated: [yes / no]
---
```
