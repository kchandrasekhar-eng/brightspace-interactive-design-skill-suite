---
name: brightspace-google-peer-eval
description: |
  Builds a complete peer evaluation pipeline using Google Forms and Google Apps Script — group-isolated forms, automated scoring, an instructor dashboard with CSV grade export, and a student dashboard with anonymised feedback. Institution-agnostic: works with any Google Workspace domain. Integrates with D2L Brightspace via CSV grade import. Use this skill whenever an instructor needs structured peer evaluation for a group project with grade passback to Brightspace. Triggers on: "set up peer evaluation", "peer eval for my group project", "Google Forms peer assessment", "peer grading pipeline", "group peer evaluation with grades", or any request to build a structured peer evaluation system that feeds grades back to Brightspace.
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
    Generalized from the MRU Peer Evaluation Pipeline (mru-peer-eval).
---

# Brightspace Google Peer Eval

You build a complete peer evaluation pipeline using Google Apps Script — one Google Form per group, automated scoring, and dual dashboards — that integrates with D2L Brightspace via CSV grade import.

## What This Skill Builds

- **Code.gs** — Form generator: reads a D2L roster, creates one Google Form per group, builds criteria grids, collects responses into Google Sheets tabs.
- **Dashboard.gs** — Web app: instructor dashboard (scores, variance flags, CSV export, student lookup) and student dashboard (criterion means, anonymised comments, response count). Served from a single Apps Script web app via URL parameter routing.

All code is **Google Apps Script (GAS)** — runs in the browser, no server required, no API keys, no Node.js.

---

## Skill Suite

This skill works closely with:
- **brightspace-group-project-setup** — run this first to configure groups in Brightspace; peer eval opens after project submission
- **brightspace-gradebook-planner** — the peer eval grade item must exist in the Brightspace gradebook before CSV import
- **brightspace-assignment-generator** — the group submission folder timeline determines when peer eval opens
- **brightspace-rubric-builder** — criteria used in the peer eval form should align with the project rubric

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for group project details, weight, and timing
- Read `group-project-config.md` if available — it contains group size, enrollment method, and submission dates
- Save the peer eval configuration as `peer-eval-config.md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Upload your course outline or describe the group project before building — context prevents generic output
- Save the session summary at session end

---

## Quick-Start Decision Tree

Before writing any code, confirm these five things:

```
1. IMPLEMENTATION MODEL
   Model A → one form per GROUP (recommended — each group sees only their own form)
   Model B → one form per SECTION, students self-identify their group

2. CRITERIA SET
   Standard-6  → six professional skills criteria, 1–5 + N/A scale (see below)
   Standard-5  → five academic contribution criteria, 3-level scale (see below)
   Custom      → instructor defines criteria (collect before building)

3. SCORING
   /15 scale   → criterion means (N/A excluded) → mean of means × 3 (Standard-6 default)
   /10 scale   → mean of means × 2
   /20 scale   → mean of means × 4
   /100 scale  → mean of means × 20
   3/2/1 scale → Excellent/Satisfactory/Below par mapped to 3/2/1 (Standard-5)
   Custom      → define outOf, scale factor, N/A handling before building

4. COURSE AND INSTITUTION DETAILS
   - Course code and section (e.g., MGMT 3010-001 Fall 2026)
   - Instructor name
   - Number of groups
   - Institution name and Google Workspace domain (e.g., university.ca or college.edu)
   - D2L roster exported? Required headers: Username | Last Name | First Name | Email | Groups

5. DRIVE FOLDER
   - Google Drive folder ID for form storage
   - Confirm institution Google Workspace domain (used for dashboard access restriction)
```

If any of these are unclear, ask before proceeding. Do not default silently.

---

## Roster Requirements

The D2L classlist CSV must be uploaded as a sheet named **Roster** with these exact headers:

| Username | Last Name | First Name | Email | Groups |
|----------|-----------|------------|-------|--------|

- Username is the key linking field for grade exports and dashboard identity detection.
- Groups column accepts: `1`, `Group 1`, `Group 1 — Section A` — all normalised to `Group N`.
- Completely empty rows are skipped automatically.

**To export the classlist from Brightspace:**
Grades → Enter Grades → Export → select Username, Last Name, First Name, Email → download CSV. Add a Groups column manually or export from the Groups tool.

---

## Standard Criteria Sets

### Criteria Set A — Six Professional Skills (Standard-6)
*Recommended for courses emphasising professional or interpersonal skills.*
Rating scale: 1 (Needs significant improvement) → 5 (Excellent) + N/A

| # | Criterion | Sub-dimensions |
|---|---|---|
| 1 | Communication Skills | Communicates ideas clearly; listens actively; contributes to group discussions |
| 2 | Collaboration and Teamwork | Works cooperatively; respects diverse perspectives; builds on others' ideas |
| 3 | Initiative and Engagement | Takes initiative; stays engaged; follows through on commitments |
| 4 | Contribution to Task Completion | Completes assigned tasks; produces quality work; meets deadlines |
| 5 | Conflict Resolution and Problem Solving | Addresses disagreements constructively; helps find solutions |
| 6 | Leadership and Organization | Helps organize the group; keeps work on track; supports others |

**Scoring:** Mean of criterion means (N/A excluded) × 3 = score out of 15 (adjustable — see Scoring section).

### Criteria Set B — Five Academic Contribution (Standard-5)
*Recommended for courses emphasising fair contribution and task completion.*
Rating scale: Excellent (3) / Satisfactory (2) / Below par (1)

| # | Criterion |
|---|---|
| 1 | Attendance and Availability |
| 2 | Productive Contribution to Group Work |
| 3 | Fair Share of Work |
| 4 | Respect and Professionalism |
| 5 | Timely Completion of Tasks |

**Scoring:** Mean of received complete rating blocks / maximum possible × scale factor.

### Custom Criteria
To define custom criteria, collect from the instructor:
1. Criterion name (short, student-facing)
2. 2–3 sub-rows or descriptors per criterion
3. Rating scale (1–5 / 1–4 / 3-level text / other)
4. N/A option needed? (recommended for any criterion where contribution may legitimately not apply)
5. Open comment field per criterion? (recommended)

---

## CONFIG Block — Code.gs

Populate this block with course-specific values before generating any functions:

```javascript
const CONFIG = {
  rosterSheetName:  'Roster',
  indexSheetName:   'Forms_Index',
  driveFolderId:    '<PASTE_FOLDER_ID>',

  responseTabPrefix: 'Form Responses - ',
  formTitlePrefix:   'Peer Evaluation — ',
  formTitleSuffix:   ' — <COURSE_CODE> <TERM>',

  // Rating columns — adjust for chosen criteria set:
  ratingColumns: ['1', '2', '3', '4', '5', 'N/A'],        // Standard-6 (1–5 + N/A)
  // ratingColumns: ['Excellent', 'Satisfactory', 'Below par'],  // Standard-5

  introText: 'This peer evaluation is confidential. Your responses help your instructor assess individual contributions to the group project. Rate each group member (excluding yourself) on the criteria below.',

  anchorLegendText: '1 = Needs significant improvement  |  3 = Meets expectations  |  5 = Excellent  |  N/A = Not applicable',

  acknowledgementText: 'By submitting this form, I confirm that my ratings reflect my honest assessment of my group members\' contributions.',

  confidenceQuestionTitle: 'How confident are you in the accuracy of your ratings overall?',
  confidenceQuestionHelp:  '1 = Not at all confident   5 = Very confident',

  submissionDeadlineFallback: '<YYYY-MM-DDTHH:MM:SS>',
  retryAttempts:    6,
  retryBaseSleepMs: 800,
  archiveTag:       'ARCHIVED'
};
```

---

## DASH_CONFIG Block — Dashboard.gs

```javascript
const DASH_CONFIG = {
  rosterSheetName:   'Roster',
  responseTabPrefix: 'Form Responses - ',

  d2lGradeItemName:  '<GRADE_ITEM_NAME_IN_D2L>',   // Must match exactly
  exportDecimals:    2,
  allowedDomain:     '<YOUR_INSTITUTION_DOMAIN>',   // e.g. 'university.ca' or 'college.edu'
  csvFilename:       '<COURSECODE>_<SECTION>_<TERM>_peer_eval_grades.csv',

  criterionTitles: {
    1: '1. Communication Skills',
    2: '2. Collaboration and Teamwork',
    3: '3. Initiative and Engagement',
    4: '4. Contribution to Task Completion',
    5: '5. Conflict Resolution and Problem Solving',
    6: '6. Leadership and Organization'
    // Adjust to match criteria in Code.gs
  }
};
```

---

## Grading Scale — How to Change

The default scale is **/15** (mean of criterion means × 3). To change:

| Target scale | Change in Dashboard.gs |
|---|---|
| /10 | `score = meanOfMeans * 2` |
| /20 | `score = meanOfMeans * 4` |
| /100 | `score = meanOfMeans * 20` |
| Standard-5 (3/2/1) | `parseRating_` must map Excellent→3, Satisfactory→2, Below par→1; update scale factor |

Always update `csvFilename`, `d2lGradeItemName`, column headers, and score footnote text when changing the scale.

---

## Key Functions to Build

### Code.gs functions
| Function | Purpose |
|---|---|
| `buildForms_()` | Main entry — loops through groups from roster, creates one form per group |
| `buildGroupFormContents_(form, members, groupName)` | Populates one form: intro, criteria grid, acknowledgement, confidence question |
| `addCriterionBlock_(form, members, criterionTitle, subRows)` | Adds one criterion grid to a form |
| `getRosterGroups_()` | Reads Roster sheet, returns map of groupName → [members] |
| `createFormsIndex_()` | Creates/updates Forms_Index sheet with form URLs |
| `setSubmissionDeadline_(deadlineStr)` | Sets form close date via script trigger |
| `archiveForms_()` | Marks inactive forms with archive tag |
| `safeAdd_(fn)` | Retry wrapper for GAS quota errors (6× with exponential backoff) |

### Dashboard.gs functions
| Function | Purpose |
|---|---|
| `doGet(e)` | Router — detects instructor vs student by email domain + URL param |
| `getRoster_()` | Reads Roster sheet, returns student → group map |
| `analyzeGroup_(groupName)` | Reads response tab, skips empty rows, computes per-member scores |
| `computeScores_(responses, members)` | Applies scoring logic, handles N/A exclusion |
| `handleGradesCsv_()` | Generates CSV for D2L Brightspace grade import |
| `renderInstructor_(data)` | Builds instructor dashboard HTML (scores, variance flags, CSV button) |
| `renderStudent_(email, data)` | Builds student dashboard HTML (criterion means, anonymised comments) |
| `sharedStyles_()` | Returns shared CSS string for both dashboard views |

---

## Build Sequence

Follow this order every time. Do not skip steps.

```
Step 1  — Confirm the five decisions (Quick-Start Decision Tree above)
Step 2  — Create a Google Sheet in the institution Google Drive folder
Step 3  — Upload the D2L classlist as a tab named "Roster"; verify column headers
Step 4  — Build Code.gs:
           CONFIG → getRosterGroups_ → addCriterionBlock_ → buildGroupFormContents_
           → buildForms_ → createFormsIndex_ → setSubmissionDeadline_ → safeAdd_
Step 5  — Run onOpen() manually once to register the batch menu
Step 6  — Phase A: Run batch menu → Build Forms for All Groups
Step 7  — Submit one test response per form to generate response tabs
Step 8  — Phase B: Run "Finalize / Rename Response Tabs"
Step 9  — Run "Remove Link Markers from All Forms"
Step 10 — Set submission deadline via menu (no code edits needed)
Step 11 — Build Dashboard.gs:
           DASH_CONFIG → getRoster_ → analyzeGroup_ → computeScores_
           → handleGradesCsv_ → renderInstructor_ → renderStudent_ → sharedStyles_
Step 12 — Deploy Dashboard.gs as a web app:
           Execute as: Me
           Access: Anyone within [Institution] Google Workspace domain
           (When prompted for domain restriction, enter the allowedDomain value from DASH_CONFIG)
Step 13 — Post form links and dashboard links in Brightspace (see Deployment Checklist below)
Step 14 — After peer eval closes: run grade export → import CSV to Brightspace Grades
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| `Roster missing required headers` | Column name mismatch | Check for extra spaces, smart quotes, or capitalisation differences in the D2L export |
| `No groups matched` | Groups column has no recognisable values | Ensure Groups column has values like `1`, `Group 1`, or `Group 1 — MGMT 3010` |
| Blank scores / all zeros | Phantom empty rows in response sheet | Empty-row guard: skip any row where every cell is blank or Timestamp is missing |
| Student dashboard identity not detected | Wrong deployment mode or wrong domain | Re-deploy: Execute as Me, Access: Anyone within institution domain; verify allowedDomain |
| `Failed to edit the form` | GAS quota transient error | `safeAdd_()` retries 6× with backoff — wait 2 minutes and retry the batch |
| Response tab not renamed | Test response not submitted before Finalize | Submit one real response per form, then re-run Finalize |
| CSV import fails in Brightspace | Grade item name mismatch | Confirm `d2lGradeItemName` in DASH_CONFIG matches the Brightspace grade item name exactly (case-sensitive) |

---

## Deployment Checklist (Brightspace side)

- [ ] Grade item exists in Brightspace Gradebook matching `d2lGradeItemName` exactly
- [ ] Form URLs copied from Forms_Index sheet (Live URL column)
- [ ] One Brightspace content item per group with **Release Condition: Group Enrolment = Group N** — students see only their group's form link
- [ ] Student dashboard URL posted as a Brightspace content link (no release condition needed — auto-detects by login)
- [ ] Instructor dashboard URL shared directly with instructor (do not post publicly)
- [ ] Submission deadline set via menu trigger
- [ ] Peer eval opening window communicated to students: typically 48–72 hours after group project submission
- [ ] Instructions added to student-facing Brightspace page: how to find their form, how long it takes, deadline, privacy note

---

## Privacy and Ethics Notes

> Students should know: (1) who can see their ratings, (2) whether comments are anonymised, (3) how scores affect their grade.

**Recommended disclosure to students:**
- Ratings are submitted anonymously to peers — only the instructor sees individual ratings attributed to raters
- The student dashboard shows criterion means and anonymised comments (no rater names)
- Peer evaluation scores may adjust individual grades within a shared group grade — confirm with your instructor

**Data handling:**
- Response data lives in your institution Google Workspace — not on third-party servers
- Do not share identifiable peer evaluation data with the class
- Retain response data in accordance with your institution's records management policy

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Grade item exists in Brightspace gradebook before CSV import | Block — do not import until grade item confirmed |
| Submission deadline set before forms are distributed | Flag — open-ended forms generate confusion |
| Each group has at least 3 members | Flag — peer eval is less meaningful for dyads; discuss with instructor |
| Test response submitted before Finalize step | Flag — Finalize requires at least one response tab per form |
| allowedDomain matches institution Google Workspace domain | Flag — wrong domain blocks all dashboard access |
| Student privacy disclosure included in Brightspace instructions | Flag if absent |
| Peer eval timeline communicated (when it opens, when it closes) | Flag if not in student instructions |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Gradebook grade item not yet created | Run **brightspace-gradebook-planner** before building — CSV import requires a named grade item |
| Groups not yet configured in Brightspace | Run **brightspace-group-project-setup** first — group names in the roster must match Brightspace group names |
| Institution does not use Google Workspace | This pipeline requires Google Workspace — recommend alternative (Brightspace Survey + manual scoring, or a commercial peer eval tool) |
| Instructor wants real-time grade passback (not CSV) | Not supported by this pipeline — CSV import is manual but reliable; note this limitation before building |
| Very large class (100+ students, 25+ groups) | Flag GAS batch quota limits; recommend running form builds in batches of 15–20 groups; test one batch first |
| Students don't have institution Google accounts | Flag — students must be logged into their institution Google account to submit the form and view the dashboard |
| Instructor wants peer ratings to be visible to peers (not anonymised) | Flag privacy concern; recommend against by default; adjust renderStudent_ only if instructor confirms and students are informed |

---

## Handoff

> "Your peer evaluation pipeline is ready. Suggested next steps:
> 1. **Assignment Generator** — confirm the group project submission folder is set up with the correct due date (peer eval opens after submission)
> 2. **Announcement Writer** — write a student-facing announcement explaining the peer eval process, timeline, and privacy
> 3. **Gradebook Planner** — confirm the peer eval grade item exists and is weighted correctly before CSV import
> 4. **Group Project Setup** — if groups haven't been configured in Brightspace yet, do that before distributing form links"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Google Peer Eval
Date: [date]
Course: [name and code]
Implementation model: [Model A — one form per group / Model B — one form per section]
Criteria set: [Standard-6 / Standard-5 / Custom — describe]
Scoring scale: [/15 / /10 / /20 / /100 / custom]
Number of groups: [n]
Institution domain: [domain]
Grade item name in Brightspace: [name]
Dashboard deployed: [yes / no / pending]
Brightspace deployment: [forms linked / dashboard linked / pending]
Privacy disclosure: [included in student instructions / pending]
Output files: [Code.gs / Dashboard.gs / deployment checklist]
Next recommended skill: [name]
---
```
