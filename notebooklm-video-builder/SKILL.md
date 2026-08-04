---
name: notebooklm-video-builder
description: >
  Produces the source document and custom prompt to generate a NotebookLM Short
  Video Overview (9:16 vertical, ~60 seconds, one concept) for a course, then
  embeds it in Brightspace. Use whenever the user wants a NotebookLM video, a
  short vertical explainer from a reading or notes, a notes-to-video clip, a
  module recap short, or any source-grounded short video. Triggers on:
  "NotebookLM video", "short video overview", "vertical video from my notes",
  "turn this reading into a video", "notebook video for my module", or
  "60-second explainer from my sources". Because NotebookLM builds video from
  uploaded sources rather than a free prompt, the skill's real work is preparing
  a clean source document per module or concept and a custom steering prompt per
  video. Produces notebook-per-course setup, a Claude-written source document, a
  per-video prompt, a mandatory accuracy review gate, a vertical Brightspace
  embed with transcript, a copyright caution, and a credits block.
license: CC BY-NC 4.0
metadata:
  author: Kumar Chandrasekhar, PhD
  affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
  version: 0.1.0
  date: 2026
  contact: https://github.com/kchandrasekhar-eng/brightspace-interactive-design-skill-suite/issues
  changelog: |
    - v0.1.0 — Initial release. One notebook per course; Claude generates a source
    document per module/concept plus a custom per-video prompt; Short
    Video Overview (9:16, ~60s) default; mandatory accuracy review gate;
    vertical-aware Brightspace embed.
---
# NotebookLM Video Builder

Produces the Claude-side assets for a NotebookLM Short Video Overview: a clean
source document and a custom prompt. NotebookLM generates the video from those
sources; this skill prepares them and embeds the result in Brightspace.

**What a Short Video Overview is:** a 9:16 vertical clip, roughly 60 seconds,
built from your uploaded sources, distilled to one idea. It is mobile-first and
source-grounded. NotebookLM also offers a horizontal standard Video Overview
(Explainer / Brief) and a Cinematic option (Google AI Ultra). This skill
defaults to the Short format; note the alternatives when the instructor wants a
longer or horizontal piece.

**Key difference from other video skills:** NotebookLM does not take a free
creative prompt the way Flow does. It reads sources and summarises them. So the
quality of the video depends almost entirely on the quality of the source
document you give it. That document is the main thing this skill produces.

**Requirements:** A NotebookLM account. The Short format is available on the free
tier with daily caps; Cinematic requires Google AI Ultra. Web and mobile.

---

## Step 0 — Gather course context

Before producing any output, collect:

1. **Course name and institution**
2. **Module or topic/concept** — the single concept this clip covers
3. **Learning goal** — the one takeaway a student should leave with
4. **Audience** — level and background
5. **Source materials** — what the instructor has, and whether they hold the
   rights to it (see copyright check below)
6. **Where it sits** in the module
7. **Citation needed?** — a source to credit

Then run the **sensitivity check** and the **copyright check**.

### Sensitivity check

Does the topic involve loss, grief, trauma, abuse, violence, mental health,
self-harm, serious patient harm, or discrimination and systemic injustice — or
anything that could distress vulnerable students?

**If yes:** flag it, keep the source document calm and factual, and add a
content note to the embed (Stage 6).

### Copyright check

NotebookLM ingests whatever you upload. Only upload sources you have the rights
to: your own materials, openly licensed content, or works your institution
licenses for this use. Do not upload full copyrighted readings or textbook
chapters you do not have rights to. The source document this skill produces is
written by Claude with the instructor's direction, which keeps the input clean.
If the instructor wants to base a video on a copyrighted reading, work from the
instructor's own summary and the bibliographic details, not the pasted text.

Generate a filename slug: `[course-code]-[module]-[concept-slug]`

---

## Pipeline stages

```
STAGE 1   — NOTEBOOK SETUP (one per course)
STAGE 2   — SOURCE DOCUMENT (Claude generates)   ← the core deliverable
STAGE 2b  — FACT CHECK GATE
STAGE 3   — CUSTOM PER-VIDEO PROMPT
STAGE 4   — GENERATE IN NOTEBOOKLM
STAGE 5   — ACCURACY REVIEW GATE (mandatory)
STAGE 6   — DOWNLOAD + BRIGHTSPACE EMBED
```

Do not skip Stage 2b or Stage 5. Label each section clearly.

---

## STAGE 1 — NOTEBOOK SETUP

One notebook per course, the same way one Claude Project holds one course.

Guidance for the instructor:
1. In NotebookLM, create a notebook named after the course
   (e.g. "BIOL 1101 — Cell and Molecular Biology").
2. This single notebook holds every source and every video for the course.
3. Each module or concept gets its own source document (Stage 2), added to the
   same notebook. Videos are generated per concept from within it.

State this once at the start; the instructor sets it up on the first video and
reuses it for the rest of the course.

---

## STAGE 2 — SOURCE DOCUMENT

The main deliverable. Write one clean, self-contained document for the single
concept, built so NotebookLM produces a faithful one-idea short.

What makes a good source document for a Short Video Overview:
- **One concept only.** The Short format lands one idea. Do not cover a whole
  module in one document — split it.
- **Lead with the takeaway.** State the single thing the student should remember
  in the first line.
- **Accurate and specific.** Include the key facts, terms, and one concrete
  example. NotebookLM foregrounds what is in the source, so put the right things
  in and leave filler out.
- **Plain, clear language.** Short sentences. Define the term once.
- **Self-contained.** No "see the slides"; everything the video needs is in the
  document.
- **Length:** roughly 300–600 words. Enough substance for a 60-second distillation,
  not so much that the model has to guess what matters.

Produce the document as a downloadable file (`.md` or `.docx`) named
`[slug]-source.md`, ready to upload to the course notebook.

---

## STAGE 2b — FACT CHECK GATE

**This stage must complete before Stage 3.**

The video will only be as accurate as this document.
- Extract every verifiable factual claim.
- Avoid unsupported superlatives unless a cited source supports them.
- Classify each claim: ✓ Verified / ⚠ Needs revision / ✗ Incorrect /
  ○ Opinion or framing.
- Rewrite and re-check if any ⚠ or ✗ appears.
- Proceed only when every verifiable claim is ✓.

```
FACT CHECK RESULTS
──────────────────────────────────────────────────────
Claim                         | Status | Source
──────────────────────────────────────────────────────
[claim 1]                     | ✓      | [source]
──────────────────────────────────────────────────────
[All claims verified / Revised document above]
Proceeding to Stage 3.
```

---

## STAGE 3 — CUSTOM PER-VIDEO PROMPT

The steering prompt the instructor pastes when generating the Short Video
Overview. It tells NotebookLM what to foreground.

### Prompt template

```
Create a 60-second vertical Short Video Overview on one concept: [concept].
Audience: [level and background].
The single takeaway: [the one thing a student should remember].
Tone: [clear and encouraging / calm].
Focus only on the concept above — do not summarise the whole notebook.
Ground everything in the source document [slug]-source.md.
```

Fill every bracket from Step 0 and Stage 2. Produce one ready-to-paste prompt,
then a short note that NotebookLM may still make its own choices — the accuracy
review in Stage 5 is where the instructor confirms it got it right.

---

## STAGE 4 — GENERATE IN NOTEBOOKLM

Guidance for the instructor:
1. Open the course notebook and confirm `[slug]-source.md` is added as a source.
   For a tightly focused short, deselect the other sources so the model draws
   only from this document.
2. In the Studio panel, choose Video Overview, then the Short (vertical) format.
3. Paste the custom prompt from Stage 3. Set the language and, if offered, a
   visual style.
4. Generate. It runs in the background; the notebook can be closed and checked
   later.
5. Note the daily generation cap on the free tier; generate deliberately.

---

## STAGE 5 — ACCURACY REVIEW GATE (mandatory)

**Do not publish until this passes.** NotebookLM is source-grounded but can
flatten nuance, overstate, or add framing that is not in your source.

1. Watch the full clip.
2. Check every claim against `[slug]-source.md`. Confirm the takeaway is the one
   you intended and nothing was invented or distorted.
3. Confirm nothing sensitive or off-topic slipped in.
4. If anything is wrong: fix the source document or tighten the prompt, then
   regenerate. Do not hand-edit the video around an error in the source.
5. Only when the clip is faithful, download it.

Report the review outcome in your output as a short checklist the instructor
fills in, so accuracy is confirmed on the record before the video goes live.

---

## STAGE 6 — DOWNLOAD + BRIGHTSPACE EMBED

### Download

Download the finished video from NotebookLM as `[slug].mp4`. Write the
transcript from the source document's narration (or NotebookLM's captions) and
save as `[slug]-transcript.txt`.

### LMS upload

**Brightspace (D2L):**
1. Course Admin → Manage Files
2. Create a `videos` folder at the course root if it does not exist
3. Upload `[slug].mp4`
4. `src` path: `/content/enforced/[course-id]-[course-name]/videos/[slug].mp4`

Paths are case-sensitive — match the filename exactly.

### HTML component — vertical

A 9:16 clip needs a constrained, centred frame or it dominates the page. This
component caps the width and centres the video.

```html
<!-- ═══ SHORT VIDEO: [Concept] ═══ -->
[content note here if sensitive]
<div class="u-video-short" role="region"
     aria-label="[Descriptive label for screen readers]">
  <div class="u-video-short__player-wrap">
    <video
      class="u-video-short__player"
      src="[path-to-videos/slug.mp4]"
      controls
      preload="metadata"
      playsinline
      aria-label="[Label] — about 60 seconds">
      Your browser does not support HTML5 video.
      <a href="[path-to-videos/slug.mp4]">Download the video</a>
    </video>
  </div>
  <p class="u-video-credit">
    <span class="u-video-credit__label">Short video:</span>
    [Citation sentence if applicable.]
    AI-generated from course sources with NotebookLM &middot;
    &copy; [year] [instructor], [institution].
  </p>
  <details class="u-video-short__transcript">
    <summary class="u-video-short__transcript-toggle">Read transcript</summary>
    <div class="u-video-short__transcript-body">
      <p>[Full narration — paragraph breaks preserved]</p>
    </div>
  </details>
</div>
<!-- ═══ END SHORT VIDEO ═══ -->
```

### CSS (add once to the course stylesheet)

```css
.u-video-short {
  margin: 24px auto;
  max-width: 360px;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #DDD9D1;
  background: #000;
}
.u-video-short__player-wrap { position: relative; }
.u-video-short__player {
  width: 100%;
  display: block;
  aspect-ratio: 9 / 16;
  background: #000;
}
.u-video-credit {
  padding: 8px 14px;
  font-size: 11.5px;
  color: #555550;
  background: #FAFAF7;
  border-top: 1px solid #DDD9D1;
  line-height: 1.5;
}
.u-video-credit__label { font-weight: 600; color: #003A5F; }
.u-video-short__transcript { border-top: 1px solid #DDD9D1; }
.u-video-short__transcript-toggle {
  display: block;
  padding: 10px 14px;
  font-size: 13px;
  font-weight: 600;
  color: #0077AE;
  cursor: pointer;
  background: #FAFAF7;
}
.u-video-short__transcript-toggle:hover { background: #EAF4FB; }
.u-video-short__transcript-body {
  padding: 14px 16px;
  font-size: 13.5px;
  line-height: 1.75;
  color: #1A1A1A;
  background: #FFFFFF;
}
.u-content-note {
  background: #FDF6EE;
  border-left: 4px solid #A84A0A;
  border-radius: 4px;
  padding: 10px 16px;
  margin-bottom: 12px;
  font-size: 13.5px;
  line-height: 1.65;
  color: #3A2A1A;
}
```

---

## Quality checks before presenting output

- [ ] One concept only — source document does not cover a whole module
- [ ] Sensitivity check completed — flag and content note applied if needed
- [ ] Copyright check completed — only rights-cleared sources used
- [ ] Source document leads with the takeaway, self-contained, ~300–600 words
- [ ] All facts verified in Stage 2b — no unchecked superlatives
- [ ] Custom per-video prompt is complete and ready to paste
- [ ] Short (9:16) format specified; alternatives noted if relevant
- [ ] Accuracy review gate (Stage 5) included as a checklist to complete
- [ ] Vertical embed used (capped width, centred, 9:16 aspect)
- [ ] Brightspace upload path noted (Manage Files → videos/)
- [ ] Credit names NotebookLM and states AI-generated-from-sources
- [ ] Transcript saved as [slug]-transcript.txt
- [ ] Credits block printed at end of output (mandatory)

---

## Cost / access summary

```
NotebookLM free tier: Short Video Overviews with a daily cap
Google AI Ultra:      Cinematic Video Overviews (18+)
```

Short vertical videos are available at no cost within the daily limit, which
makes this the low-cost source-grounded video path.

---

## CREDITS — print at the end of every output, no exceptions

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRODUCTION CREDITS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Skill design:     Kumar Chandrasekhar, PhD (2026)
                  CC BY-NC 4.0

Content author:   [Your name]
                  [Your institution]
Source document:  Written with Claude from the author's direction
AI video:         NotebookLM (Google) — from the author's sources
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CITATION
Cite the skill:
  Chandrasekhar, K. (2026). NotebookLM video builder [Claude skill].
  CC BY-NC 4.0.

Cite the content:
  [Your name] ([year]). [Video title] [Course video]. [Your institution].
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Populate the content fields from session context; use placeholder text for
anything the user has not supplied and note that they should fill it in before
publishing.
