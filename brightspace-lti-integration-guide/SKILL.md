---
name: brightspace-lti-integration-guide
description: |
  Guides LTI tool integration in Brightspace — configuration, placement, grade passback, and troubleshooting. Use this skill whenever a user needs to connect an external tool to Brightspace via LTI. Triggers on phrases like "LTI tool", "external tool", "add a publisher tool", "connect to Brightspace", "grade passback", "LTI configuration", "add H5P", "connect publisher content", "LTI link", or any request to integrate a third-party tool into Brightspace.
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

# Brightspace LTI Integration Guide

You guide the integration of external tools into Brightspace via LTI (Learning Tools Interoperability).

## Skill Suite

- **brightspace-redesign-planner** — LTI tools are documented in the module plan
- **brightspace-lti-integration-guide** ← you are here
- **brightspace-gradebook-planner** — grade passback requires grade items to exist
- **brightspace-release-condition-planner** — LTI topics can have release conditions
- **brightspace-course-copy-auditor** — LTI links must be verified after course copy

---

## Important Preamble — Always State This

> "LTI configuration in Brightspace requires administrator access for the initial setup. If you are an instructor, you can add LTI links to Content once your institution's EdTech team has registered the tool — but you cannot register a new LTI tool yourself. Check with your EdTech team or IT before proceeding."

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

Note: **Do not ask for brand colours** — LTI tools have their own interface.

**Step 2 — Identify the situation**
> "Which of these best describes where you are?
> A — The tool is already registered at my institution and I need to add it to my course Content
> B — I need to request a new LTI tool to be registered (involves EdTech/IT)
> C — I have a tool registered and need to configure grade passback
> D — My LTI tool is broken and I need to troubleshoot it"

---

## LTI Versions

| Version | Notes |
|---|---|
| LTI 1.1 | Older, widely supported, simpler setup |
| LTI 1.3 | Current standard, more secure, required for newer tools |
| DEEP Linking | LTI 1.3 feature — lets tool push content directly into Content |

> "If you don't know which version your tool uses, check with your vendor or EdTech team. LTI 1.3 tools have a different registration process than LTI 1.1."

---

## Option A — Adding an existing LTI tool to Content

**Step-by-step:**
1. Go to Content → the module where the tool should appear
2. Upload/Create → Create a Link → External Tool Activity
3. Select the registered tool from the list
4. Configure the launch URL if required (vendor provides this)
5. Name the activity
6. Save
7. Test: click the link as an instructor to confirm it launches

---

## Option B — Requesting a new LTI tool (instructor guide)

Provide this information to your EdTech/IT team:
```
Tool name: [vendor name]
Tool URL: [launch URL from vendor]
LTI version: [1.1 / 1.3]
Key/Secret or Client ID: [from vendor — treat as confidential]
Grade passback needed: Yes / No
Deep Linking needed: Yes / No
Privacy requirements: [what data the tool accesses]
```

> "Ask your EdTech team for the expected turnaround time — LTI registration can take days to weeks depending on your institution's process."

---

## Option C — Grade Passback Configuration

Grade passback sends scores from the external tool back to the Brightspace gradebook.

**Requirements:**
- A grade item must exist in the Brightspace gradebook first — use **brightspace-gradebook-planner**
- The LTI tool must support grade passback (LTI Outcomes Service for 1.1, AGS for 1.3)
- The tool must be configured to send grades back (vendor setting)

**Setup in Brightspace:**
1. Edit the LTI activity → Assessment tab
2. Grade Item → select or create the grade item
3. Score out of → match the tool's maximum score
4. Save
5. Test: complete the activity as a student → check that the score appears in the gradebook

---

## Option D — Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Blank screen when launching | CORS or iframe issue | Ask EdTech team to check iframe embedding settings |
| "Consumer key not found" | Tool not registered at institution | Contact EdTech team |
| Grade not recording | Grade passback not configured | Check Assessment tab → Grade Item connection |
| H5P grades missing for some students | Student did not click Submit | H5P only sends grades when student clicks the Submit/Check button at the end — interaction alone is not enough. Check whether affected students completed and submitted the activity. |
| Works in one course, not another | Tool not enabled for that org unit | Contact EdTech team |
| Breaks after course copy | Launch URL contained old course ID | Re-link the tool activity in the new shell |
| LTI 1.3 login loop | Client ID mismatch | Verify registration details with EdTech team |

---

## Course Copy Warning

> "LTI tool activities do NOT always copy cleanly. After copying a course, always open each LTI activity and confirm it launches correctly. Grade passback connections may also need to be re-established. Add LTI verification to your post-copy checklist — use **brightspace-course-copy-auditor**."

---

## Session End

Offer session summary for planning document.
