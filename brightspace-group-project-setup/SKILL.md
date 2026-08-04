---
name: brightspace-group-project-setup
description: |
  Sets up group projects in Brightspace — group categories, group enrollment methods, group-restricted discussions, group assignment submission folders, grade configuration, and peer evaluation integration. Produces a complete setup guide, student-facing instructions as an HTML Topic, and configuration checklists. Triggers on phrases like "set up a group project", "group assignment", "create groups in Brightspace", "group categories", "group enrollment", "group submission", "team project setup", or any request to configure group-based work in Brightspace.
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

# Brightspace Group Project Setup

You configure complete group project infrastructure in Brightspace — from group creation to grading — and produce student-facing instructions students can actually follow.

## Skill Suite

This skill works closely with:
- **brightspace-course-outline-builder** — group project details (weight, timing) come from the course outline; also feeds into the "build last" outline workflow
- **brightspace-gradebook-planner** — group grade items must exist before the assignment folder is created; run this first
- **brightspace-assignment-generator** — group submission folder is created after groups are set up
- **brightspace-discussion-generator** — group-restricted discussion forums are part of the group workspace
- **brightspace-rubric-builder** — group project evaluation criteria
- **brightspace-self-assessment-generator** — group contribution self-report pairs with this skill at project submission
- **brightspace-google-peer-eval** — peer evaluation within groups after project submission (institution-agnostic Google Forms pipeline); MRU instructors may use **mru-peer-eval** for the MRU-specific implementation

---

## Working in a Claude Project (Recommended)

**If you are in a Claude Project:**
- Read `course-outline.md` for group project details, weight, and timing
- Read `course-calendar.md` for the week the project is due
- Save the group setup configuration as `group-project-config.md` in knowledge files
- Append session summary to `session-log.md`

**If you are NOT in a Claude Project:**
- Upload your course outline or describe the group project — context prevents generic output
- Save the session summary at session end

---

## Session Start — Quick Mode Check

Before collecting detailed context, ask two questions:

> "Are you setting up groups from scratch, or are groups already created and you need to configure the workspace or assignment folder?"

- **From scratch** → collect all four context groups below
- **Groups exist** → skip to the relevant step (Step 3 workspace, Step 4 assignment, or Step 5 grading)

> "How many group projects do you need to set up in this course? I can build them in sequence."

---

## Context Collection

Read from `course-outline.md` if available. Ask only for what's missing.

### Group 1 — Project basics
1. Course name, code, and level
2. Project name and brief description
3. What is the final deliverable? (report, presentation, prototype, creative work, portfolio)
4. Is this individual grading within a group, or one shared grade for the group?
5. Project weight (% of final grade)
6. Due date or week

### Group 2 — Group structure
1. How many students are enrolled (approximate)?
2. What is the ideal group size?
3. How should groups be formed?
   - **Instructor-assigned** — you assign students to groups manually
   - **Random** — Brightspace randomly assigns students
   - **Self-enrollment** — students choose their own groups (with a signup deadline)
4. Should groups have names? (instructor-assigned names vs student-chosen)
5. Will the same groups be used for multiple activities (discussions + assignment + peer eval)?

### Group 3 — Group workspace
1. Does each group need a private discussion forum? (recommended for collaboration)
2. Does each group need a shared file locker? (for sharing drafts)
3. Should groups be visible to each other, or kept private?

### Group 4 — Grading
1. Will the group receive one shared grade, or will individual contributions be graded separately?
2. If separate: will a peer evaluation be used to adjust individual grades?
3. Is a group contribution self-report needed? (students document their own contribution — pairs with **brightspace-self-assessment-generator**)
4. Is a rubric needed? (refer to **brightspace-rubric-builder** for detailed rubric work)
5. Are there milestone check-ins before the final submission? (e.g., proposal, draft, final)

---

## Brightspace Group Configuration

> **Prerequisite check:** Before proceeding, confirm the grade item for this project exists in the Brightspace Gradebook. If it does not — stop here and run **brightspace-gradebook-planner** first. The assignment folder cannot be linked to a grade item that doesn't exist, and fixing this after the fact requires deleting and recreating the folder.

### Step 1 — Create a Group Category

A Group Category is the container for all groups in this project. Brightspace requires a category before individual groups can be created.

**Settings to configure:**

| Setting | Recommended value | Notes |
|---|---|---|
| Category name | [Project name] Groups | e.g., "Research Project Groups" |
| Enrollment type | Instructor-defined / Random / Self-enrollment | Depends on Group 2 answer |
| Number of groups | [total students ÷ group size, round up] | |
| Max members per group | [group size] | Set if self-enrollment |
| Auto-enroll new users | No | Prevents late additions causing imbalance |
| Group prefix | Group | Groups named "Group 1", "Group 2", etc. unless instructor prefers custom names |

### Step 2 — Enrollment method details

**If instructor-assigned:**
> Brightspace does not have a bulk import for group assignments — you must assign students to groups manually via the Groups tool. For large classes (30+ students), export the classlist, assign groups in a spreadsheet, and enroll student by student. Consider using a randomization tool (e.g., Excel RAND) to assign groups, then enroll manually.
>
> **Late enrolment:** When a new student joins after groups are formed, assign them manually to a group with available space. If all groups are full, either expand one group by one member or create a new group — communicate the change to the affected group.

**If random:**
> Brightspace will distribute students as evenly as possible. Review the result before the project begins — random enrollment can create groups with only one member if enrollment numbers don't divide evenly.
>
> **Late enrolment:** Brightspace will not auto-assign late-enrolling students to existing random groups. You must manually assign them. Check for stragglers one week after the enrollment deadline.

**If self-enrollment:**
> Set a signup deadline at least one week before project work begins. After the deadline, manually assign any students who did not self-enroll. Set a message in the signup sheet: "Groups with fewer than [minimum] members will be merged or dissolved."
>
> **Late enrolment:** Students who join after the signup deadline cannot self-enroll. Assign them manually to a group that will accept them, and notify both the student and the group.

### Step 3 — Group workspace setup

**Private discussion forum per group:**

In Brightspace, group-restricted discussions work at the **Topic** level, not the Forum level. The correct setup is:
1. Create one Discussion **Forum** (e.g., "Group Project Discussions")
2. Within that Forum, create one Discussion **Topic** (e.g., "[Project name] — Group Workspace")
3. On the Topic, set **Restrict to Group Category**: select the Group Category from Step 1
4. Brightspace automatically creates one thread per group — each group sees only their own thread

> Do not set the restriction at the Forum level — this does not create the group-restricted view. The restriction must be on the Topic.

**Group locker (shared files):**
- Brightspace Locker is provisioned per group when the Group Category is created
- Students access via: Course Tools → Groups → [their group name] → Locker
- No additional instructor setup is required
- **Caveat:** Locker availability depends on your institution's Brightspace configuration. If students cannot find the Locker tab, contact your LMS administrator to confirm it is enabled for your instance.

### Step 4 — Group assignment submission folder

**Create the assignment folder AFTER groups are confirmed and the grade item exists in the Gradebook.**

Key settings:

| Setting | Value |
|---|---|
| Submission type | Group submission |
| Group category | [category created in Step 1] |
| Grade item | [must exist in Gradebook first] |
| Submission format | File / Text / Video — per project deliverable |
| One submission per group | Yes — one member submits for the group |
| Allowed file types | Specify (PDF, .pptx, .docx, video formats, etc.) |

### Step 5 — Grading configuration

**One shared grade:**
- Grade is entered once per group; Brightspace automatically applies it to all group members
- Recommended when collaboration process cannot be distinguished from output

**Individual grades within group submission:**
- Brightspace does not natively support different grades for the same group submission
- Options: (a) use peer evaluation scores to adjust a shared grade manually; (b) create separate individual reflection assignments worth a portion of the project grade; (c) use the **mru-peer-eval** system for structured peer-based grade adjustment; (d) add a group contribution self-report via **brightspace-self-assessment-generator**

**Milestone check-ins:**
- Create a separate assignment folder for each milestone (proposal, draft, final)
- Each folder: same group category, lighter weight, descriptive name
- Consider making check-ins ungraded or low-stakes (5–10%) to reduce anxiety

---

## Output Formats

### Format 1 — Brightspace configuration checklist (Markdown — for instructor)
```markdown
# Group Project Configuration Checklist
## [Course Name] — [Project Name]

### Prerequisite
- [ ] Grade item exists in Gradebook: [item name, weight%]

### Step 1: Create Group Category
- [ ] Category name: [name]
- [ ] Enrollment type: [type]
- [ ] Number of groups: [n]
- [ ] Max members: [n]
- [ ] Auto-enroll new users: No

### Step 2: Enroll students
- [ ] [Method-specific steps]
- [ ] Review enrollment — no empty or single-member groups
- [ ] Late enrolment plan confirmed: [plan]

### Step 3: Group workspace
- [ ] Discussion Forum created: [name]
- [ ] Discussion Topic created with Group Category restriction: [topic name]
- [ ] Students notified about Group Locker (if enabled)

### Step 4: Create assignment folder
- [ ] Submission type: Group submission
- [ ] Group category linked: [name]
- [ ] Grade item linked: [name]

### Step 5: Grading
- [ ] Grade item weight confirmed: [weight]%
- [ ] Peer evaluation configured: [yes — mru-peer-eval pending / no]
- [ ] Group contribution self-report configured: [yes / no]
- [ ] Milestones set up: [list or none]
```

### Format 2 — Student-facing HTML Topic

A structured student-facing page with these sections:
1. **Your group** — how to find which group you're in (Groups tool path)
2. **Your workspace** — how to access the group discussion forum and file locker (with navigation path)
3. **The project** — what you need to produce, how it will be graded, what good looks like
4. **Submission instructions** — who submits, what format, file naming convention, where to submit
5. **Milestone dates** — table of milestones with due dates (if applicable)
6. **Peer evaluation** — when it opens, how it works, how it affects your grade (if applicable)
7. **Group contribution report** — link and due date (if applicable)

Institutional branding if brand colours available; otherwise clean neutral styling. WCAG 2.1 AA accessible. Mobile responsive.

### Format 3 — Word document
- Full configuration guide for the instructor
- Student instructions formatted for distribution or printing
- Milestone schedule

Ask which formats are needed before generating.

---

## Peer Evaluation Integration

If peer evaluation is part of the project:

> "For structured peer evaluation that feeds grades back to Brightspace, use the **brightspace-google-peer-eval** skill. It builds the Google Form, scoring logic, and D2L grade passback via CSV. I'll note the peer evaluation in the student instructions and configuration checklist — run **brightspace-google-peer-eval** as the next session. MRU instructors may alternatively use **mru-peer-eval** for the MRU-specific pipeline."

Include in student instructions:
- When the peer evaluation opens (typically within 48–72 hours of final submission)
- How long it takes (5–10 minutes)
- Whether scores are visible to peers or instructor-only
- How peer evaluation scores affect the final grade

---

## Multi-Project Session

If the instructor needs more than one group project:
> "Ready for the next project. Should it use the same groups or new groups? I'll carry your course context forward — just tell me the new project name, deliverable, and weight."

---

## Quality Checks

| Check | Action if failed |
|---|---|
| Grade item exists in Gradebook before assignment folder creation | Block — do not proceed until confirmed |
| Group size produces a whole number of groups (or near-whole) | Flag remainder students; provide guidance |
| Self-enrollment has a signup deadline set | Flag if missing |
| Late enrolment plan defined for chosen enrollment method | Flag if not addressed |
| Discussion Topic (not Forum) has group category restriction | Flag if restriction set at wrong level |
| Group locker availability confirmed with LMS admin if needed | Flag caveat |
| Milestone check-ins are in the Gradebook if graded | Flag if missed |
| Peer evaluation timeline confirmed before submission deadline | Flag if too tight |

---

## Conflict Detection

| Situation | Response |
|---|---|
| Gradebook not yet set up | Run **brightspace-gradebook-planner** before proceeding |
| Class size doesn't divide evenly into groups | Flag; recommend plan for remainder students |
| Instructor wants different grades per group member in same submission | Explain Brightspace limitation; recommend peer eval or contribution self-report |
| Self-enrollment chosen but no deadline set | Ask for deadline before proceeding |
| Instructor wants groups carried across multiple courses or sections | Note this is not natively supported — each section requires its own Group Category |
| Instructor sets group restriction on Forum instead of Topic | Correct immediately — this is a common setup error |

---

## Handoff

> "Your group project is configured. Suggested next steps:
> 1. **Google Peer Eval** — set up structured peer evaluation with grade passback (institution-agnostic)
> 2. **Self-Assessment Generator** — build a group contribution self-report for individual accountability
> 3. **Assignment Generator** — create individual milestone submission folders
> 4. **Rubric Builder** — build the evaluation criteria for the project
> 5. **Discussion Generator** — full configuration of the group-restricted discussion forum
> 6. **Course Outline Builder** — if building the outline at the end, group project details feed in automatically"

---

## Standard Session Log Format

Append this entry to `session-log.md` at session end.

```markdown
---
## Session: Group Project Setup
Date: [date]
Course: [name and code]
Projects configured: [count]
Project names: [list]
Group size: [n]
Number of groups: [n]
Enrollment method: [instructor-assigned / random / self-enrollment]
Late enrolment plan: [brief description]
Group workspace: [discussion forum yes/no, locker yes/no]
Grading model: [shared grade / individual adjustment]
Peer evaluation: [yes — brightspace-google-peer-eval pending / yes — mru-peer-eval pending / no]
Contribution self-report: [yes / no]
Milestones: [list or none]
Formats generated: [list]
Next recommended skill: [name]
---
```
