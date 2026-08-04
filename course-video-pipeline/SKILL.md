---
name: course-video-pipeline
description: >
  Produces complete AI-generated short video clips for online or blended
  courses. Use this skill whenever the user wants to create a course video,
  engagement break, visual analogy, scenario clip, or recap clip for any
  course or educational context. Triggers on: "create a video clip for my
  course", "write a video script", "make an engagement break", "produce a
  visual analogy", "generate a scenario clip", "make a recap video", "add a
  video to my session", or any request to produce short educational video
  content. Course-agnostic and platform-agnostic. Produces all seven pipeline
  stages in one pass: script with integrated fact-check gate, ElevenLabs
  voice selection and settings, Fal.ai image prompt, Fal.ai animation brief,
  merge instructions (terminal or cloud), end card, HTML embed with
  transcript, sensitivity check, content note, credits block, and CSS.
license: CC BY-NC 4.0
metadata:
  author: Kumar Chandrasekhar, PhD
  affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
  version: 1.2
  date: 2026
  contact: https://github.com/kchandrasekhar-eng/brightspace-interactive-design-skill-suite/issues
  changelog: |
    - v1.0 — Initial release
    - v1.1 — Added Speed column to Stage 2b settings table; added Speed field
    to Stage 2b spec block output; added Step 2c (Generate Audio) —
    pipeline previously jumped from settings spec to image generation
    without instructing the user to produce the audio file
    - v1.2 — Step 0: replaced "merge preference" question with tool availability
    diagnostic (Python / FFmpeg / Fal.ai API key); Stage 5: removed
    references to pre-existing scripts/, added Python + MoviePy 2.x as
    Option C, added MoviePy version compatibility note, Claude now
    generates the merge script based on available tools; Stage 6: added
    transcript filename convention ([slug]-transcript.txt); Stage 7:
    added LMS upload guidance for Brightspace and generic LMS; quality
    checklist: added audio gate, transcript filename, and LMS upload
    checks; cost summary: added Python/MoviePy option (free); credits
    block and HTML embed credits: updated Assembly line to include
    MoviePy + Pillow (Python) as third option
---
# Course Video Pipeline

Produces all production assets for one AI-generated short course video in a single pass.

**Core formula:** Text teaches. Video re-engages. Interaction confirms.

**Target:** ≤60 seconds per clip. One idea per clip. Always ends with a bridge to
the next activity.

---

## Step 0 — Gather course context

Before producing any output, collect:

1. **Course name and institution**
2. **Clip type** — see taxonomy below
3. **Topic** — what concept, scenario, or moment this clip covers
4. **Where it sits** in the session (after which section)
5. **Available tools** — ask: "Do you have any of the following?
   Python installed / FFmpeg installed / Fal.ai API key"
   Claude selects the merge option from the answer:
   - Python only → Option C (MoviePy + Pillow — generated script)
   - FFmpeg → Option A (Terminal)
   - Fal.ai API key → Option B (Cloud)
   - None → Option C (install Python + MoviePy — simplest path)
6. **Citation needed?** — specific source to credit in the end card

Then run the **sensitivity check** before anything else:

### Sensitivity check

Does the topic involve any of the following?
- Loss, grief, bereavement, death
- Trauma, abuse, violence
- Mental health, suicide, self-harm
- Serious patient harm, medical error with patient death
- Discrimination, racism, systemic injustice
- Any content that could distress vulnerable students

**If yes:**
- Flag the topic as sensitive in your output
- Apply "Gentle and unhurried" ElevenLabs settings (see Stage 2)
- Add a content note to the HTML embed (see Stage 7)
- In the visual brief: emphasise stillness, warmth, and abstraction —
  avoid clinical or harsh environments
- In the animation brief: no sudden motion, no flicker, no tension effects

**If no:** proceed normally.

Generate a filename slug: `[course-code]-[session-id]-[type]-[topic-slug]`

---

## Clip type taxonomy

| Type | Position in page | Max length | Tone |
|---|---|---|---|
| `engagement-break` | After pre-reading, before activities | 45s | Warm, orienting |
| `scenario` | Before the discussion/activity it supports | 60s | Narrative, specific |
| `analogy` | Inline with the concept it illustrates | 60s | Calm, explanatory |
| `recap` | End of session, before wrap-up | 60s | Consolidating, forward-looking |

---

## Pipeline stages

```
STAGE 1   — SCRIPT
STAGE 1b  — FACT CHECK GATE
STAGE 2   — AUDIO SPEC (ElevenLabs — voice + settings)
STAGE 3   — BASE IMAGE PROMPT (Fal.ai)
STAGE 4   — ANIMATION BRIEF (Fal.ai image-to-video)
STAGE 5   — MERGE (Terminal / Cloud / Python)
STAGE 6   — TRANSCRIPT
STAGE 7   — HTML EMBED + CSS
```

Do not skip any stage. Label each section clearly.

---

## STAGE 1 — SCRIPT

Write three components:

### Narration text
- ≤120 words — count explicitly and state the count
- Aim for ~110 words — TTS needs breathing room
- Warm, direct — "you" and "we" — not lecture voice
- One idea only. No sub-points, no lists.
- End with a sentence that bridges to the next activity
- No inline citations — these go in the end card only
- **Sensitive topics:** slower sentence rhythm, shorter sentences,
  more white space in pacing. Avoid clinical language.

### Visual brief
- Describe the single frame that becomes the base image
- Subject, setting, lighting, colour palette, mood
- Style: `photorealistic` for scenario clips,
  `stylised illustration` for analogy/recap/break clips
- 16:9 composition — describe what sits centre-frame
- **Always include:** "No faces, no identifiable people"
  (Fal.ai generates faces by default — must be explicitly suppressed)
- **Avoid:** text embedded in image, logos, brand colours,
  cluttered backgrounds
- **Sensitive topics:** abstract or nature-based imagery —
  avoid clinical, harsh, or institutional settings

### Animation brief
- Subtle motion only — 2 sentences maximum
- Background atmosphere, not foreground action
- Examples: slow camera drift, soft light shift, ambient particles,
  surface ripple, water reflection, breathing light
- Motion reinforces emotional tone — never distracts
- **Sensitive topics:** stillness preferred — minimal or no motion,
  no flicker, no tension effects

---

## STAGE 1b — FACT CHECK GATE

**This stage must complete before Stage 2.**
Read `references/fact-check-gate.md` for the full procedure.

Key rules:
- Extract every verifiable factual claim
- **Avoid superlatives** — "primary", "most", "always", "never",
  "the leading" — unless directly supported by a cited source.
  Flag these for revision even if the general claim is defensible.
- Classify each claim: ✓ Verified / ⚠ Needs revision / ✗ Incorrect
  / ○ Opinion or framing
- Rewrite and re-check if any ⚠ or ✗ found
- Only proceed when all verifiable claims are ✓

**Fact-check report format:**
```
FACT CHECK RESULTS
──────────────────────────────────────────────────────
Claim                         | Status | Source
──────────────────────────────────────────────────────
[claim 1]                     | ✓      | [source]
[claim 2]                     | ○      | Pedagogical framing
──────────────────────────────────────────────────────
[All claims verified / Revised narration below]
Proceeding to Stage 2.
```

---

## STAGE 2 — AUDIO SPEC (ElevenLabs)

### Step 2a — Voice selection

Before specifying settings, recommend a voice selection process:

```
VOICE SELECTION
Recommended step before finalising settings:
1. Go to elevenlabs.io → Voice Library
2. Filter by: [tone category from table below]
3. Test 2–3 voices with this sentence from the narration:
   "[paste the most emotionally weighted sentence]"
4. Choose the voice that feels right for this topic
5. Note the voice name — use it consistently across all clips
   in this course for continuity
```

**For sensitive topics:** recommend voices described as "soft",
"gentle", or "warm" in ElevenLabs. Avoid voices described as
"confident", "authoritative", or "crisp".

### Step 2b — Settings by tone category

Select the tone category that matches the clip:

| Tone category | When to use | Stability | Similarity | Style exag | Speaker boost | Speed |
|---|---|---|---|---|---|---|
| **Warm and inviting** | First-week welcome, orientation breaks | 0.65 | 0.75 | 0.20 | false | 0.90× |
| **Conversational** | Light engagement breaks, general analogy | 0.70 | 0.75 | 0.15 | false | 1.00× |
| **Calm and explanatory** | Scientific/conceptual analogy, recap | 0.75 | 0.80 | 0.10 | false | 0.90× |
| **Measured and serious** | Clinical scenario, patient safety, ethics | 0.80 | 0.80 | 0.08 | true | 0.88× |
| **Gentle and unhurried** | Loss, grief, trauma, mental health | 0.85 | 0.70 | 0.05 | false | 0.82× |
| **Authoritative** | Legal, regulatory, policy content | 0.82 | 0.85 | 0.06 | true | 0.95× |

Produce the full spec block:

```
Platform: ElevenLabs (elevenlabs.io)
Tone category: [selected category]
Voice: [recommended voice or "test 2–3 from library — see Step 2a"]
Stability: [value]
Similarity boost: [value]
Style exaggeration: [value]
Speaker boost: [true/false]
Speed: [value]×
Export format: MP3, 128kbps
Filename: [slug].mp3
Estimated duration: [N] seconds
Character count: [N]
Free tier note: 10,000 chars/month free · Starter = $5/month for 30,000
```

### Step 2c — Generate audio

**This step must complete before Stage 3. Stage 5 (Merge) requires the
audio file to exist on disk.**

```
AUDIO GENERATION — ElevenLabs
──────────────────────────────────────────────────────────────────────
1. Go to elevenlabs.io → Text to Speech (or Speech Synthesis)
2. Select the voice chosen in Step 2a
3. Apply all settings from Step 2b exactly:
     Stability / Similarity boost / Style exaggeration /
     Speaker boost / Speed
4. Paste the narration text below verbatim — do not paraphrase,
   trim, or reformat. This text must match the transcript exactly.

   ┌─ PASTE THIS TEXT ────────────────────────────────────────────┐
   │ [Full narration from Stage 1 — reproduced here verbatim]     │
   └──────────────────────────────────────────────────────────────┘

5. Preview the audio. Check:
     - Pacing feels natural and unhurried
     - No mispronounced words or awkward pauses
     - Tone matches the selected category
   Adjust Speed ±0.02 if needed, then re-preview.
6. Generate and download.
   Save as: [slug].mp3
   Confirm file is in your working directory before proceeding.
──────────────────────────────────────────────────────────────────────
✓ Audio file ready → proceed to Stage 3
✗ Not yet generated → do not proceed
──────────────────────────────────────────────────────────────────────
```

---

## STAGE 3 — BASE IMAGE PROMPT (Fal.ai)

```
Platform: Fal.ai (fal.ai) — any image generation model
Full prompt:
[Detailed, optimised image generation prompt based on the visual brief.
 Always end with: "No faces, no identifiable people, no readable text."]

Aspect ratio: 16:9
Resolution: 1920×1080
Style: [photorealistic / stylised illustration]
Negative prompt: faces, people, text, watermarks, logos, distorted faces,
  blurry, low quality[, add topic-specific negatives if sensitive]
Filename: [slug]-base.png
Estimated cost: ~$0.03–0.05
```

---

## STAGE 4 — ANIMATION BRIEF (Fal.ai image-to-video)

```
Model: Fal.ai Kling v2 (image-to-video)
Input image: [slug]-base.png
Duration: 8 seconds
Motion prompt: [Expanded animation brief]
Negative motion prompt: fast cuts, shaking, text appearing, faces morphing,
  dramatic zoom, strobing, rapid movement
  [For sensitive topics, add: flickering, sudden motion, tension effects]
Export format: MP4 H.264
Filename: [slug]-raw.mp4
Estimated cost: ~$0.08–0.12
```

---

## STAGE 5 — MERGE

**No pre-existing scripts are assumed.** Claude generates the appropriate
merge script based on the tools the user has available (confirmed in Step 0).
Always present ALL applicable options — the user may want to switch later.

### Option selection guide

| User has | Use option |
|---|---|
| FFmpeg installed | A — Terminal |
| Fal.ai API key | B — Cloud |
| Python installed (no FFmpeg, no API key) | C — Python/MoviePy |
| Nothing installed | C — install Python + MoviePy (simplest path) |

---

```
MERGE OPTIONS — present all that apply:

┌─────────────────────────────────────────────────────────────┐
│ OPTION A: Terminal (local FFmpeg)                           │
│ Cost: free · Works offline · Full control                   │
│ Requires: FFmpeg installed (ffmpeg.org)                     │
└─────────────────────────────────────────────────────────────┘

Claude generates a merge.py script for this clip.
Fill in END_CARD_LINES with the values below, then run:

END_CARD_LINES = [
    "[Citation — APA format, or empty string if none]",
    "AI narration: ElevenLabs",
    "AI visuals: Fal.ai (image-to-video)",
    "© [year] [instructor], [institution]",
]

Run:
  python merge_[slug].py


┌─────────────────────────────────────────────────────────────┐
│ OPTION B: Cloud (Fal.ai API)                                │
│ Cost: ~$0.03 extra · No local setup · Requires internet     │
│ Requires: Fal.ai API key (fal.ai)                           │
└─────────────────────────────────────────────────────────────┘

Claude generates a cloud_merge_[slug].py script for this clip.
Fill in END_CARD_LINES with the values below, then run:

END_CARD_LINES = [
    "[Citation — APA format, or empty string if none]",
    "AI narration: ElevenLabs",
    "AI visuals: Fal.ai (image-to-video)",
    "© [year] [instructor], [institution]",
]

Run:
  pip install fal-client requests
  export FAL_KEY="your-fal-api-key"
  python cloud_merge_[slug].py


┌─────────────────────────────────────────────────────────────┐
│ OPTION C: Python + MoviePy (recommended for most users)     │
│ Cost: free · No API key needed · Works offline after setup  │
│ Requires: Python installed · pip install moviepy            │
└─────────────────────────────────────────────────────────────┘

Claude generates a merge_[slug].py script for this clip.
MoviePy version compatibility note:
  - Install MoviePy 2.x: pip install moviepy
  - Do NOT use moviepy.editor imports — removed in v2.x
  - Claude-generated scripts always use MoviePy 2.x API:
    subclipped() / with_audio() / with_duration() / with_position()
  - End card is built with Pillow (installed automatically with MoviePy)
  - No ImageMagick required

Run:
  pip install moviepy
  python merge_[slug].py

Place the script in the same folder as your source files:
  [slug].mp3
  [slug]-raw.mp4
  merge_[slug].py
```

### End card content (filled in for every clip)

```
Line 1: [Citation — APA format. Omit entirely if no citation.]
Line 2: AI narration: ElevenLabs
Line 3: AI visuals: Fal.ai (image-to-video)
Line 4: © [year] [instructor name], [institution]
```

---

## STAGE 6 — TRANSCRIPT

**Filename:** `[slug]-transcript.txt`
Save alongside all other clip assets. The transcript is also embedded
inline in the HTML embed (Stage 7) — the .txt file is for archiving
and accessibility records.

```
[TRANSCRIPT — [Course] · [Clip name]]

[Full narration text verbatim — must match audio exactly]

---
Sources: [APA citation, or "No external sources cited."]
Production: AI narration (ElevenLabs), AI visuals (Fal.ai image-to-video),
directed by [instructor], [institution] ([year]).
```

---

## STAGE 7 — HTML EMBED + CSS

### Content note (sensitive topics only)

If the sensitivity check flagged this topic, add a content note
**above** the video component:

```html
<div class="u-content-note" role="note">
  <strong>Content note:</strong> This clip discusses [topic — e.g. grief
  and loss]. Take a moment before watching if you need one.
</div>
```

Add this CSS once to your stylesheet:
```css
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

### LMS upload — before embedding the HTML

The video file must be uploaded to the LMS before the HTML embed will work.
The `src` path in the HTML component points to where the file lives in the LMS.

**Brightspace (D2L):**
1. Course Admin → Manage Files
2. At the course root, create a folder named `videos` (if it doesn't exist)
3. Upload `[slug].mp4` into the `videos` folder
4. The correct `src` path will be:
   `/content/enforced/[course-id]-[course-name]/videos/[slug].mp4`
   Brightspace auto-resolves this when the file is in the right location.

**Generic LMS / web server:**
Upload to any accessible path and update the `src` attribute accordingly.
Brightspace file paths are case-sensitive — match the filename exactly.

**Transcript file:** does not need to be uploaded — it is embedded inline
in the HTML `<details>` block and requires no separate file reference.

### HTML component

```html
<!-- ═══ VIDEO: [Clip name] ═══ -->
[content note here if sensitive — see above]
<div class="u-video-break" role="region"
     aria-label="[Descriptive label for screen readers]">
  <div class="u-video-break__player-wrap">
    <video
      class="u-video-break__player"
      src="[path-to-videos/slug.mp4]"
      controls
      preload="metadata"
      playsinline
      aria-label="[Label] — [N] seconds">
      Your browser does not support HTML5 video.
      <a href="[path-to-videos/slug.mp4]">Download the video</a>
    </video>
  </div>
  <p class="u-video-credit">
    <span class="u-video-credit__label">[Clip type]:</span>
    [Citation sentence if applicable.]
    AI narration: ElevenLabs &middot; AI visuals: Fal.ai &middot;
    &copy; [year] [instructor], [institution].
  </p>
  <details class="u-video-break__transcript">
    <summary class="u-video-break__transcript-toggle">
      Read transcript
    </summary>
    <div class="u-video-break__transcript-body">
      <p>[Full narration — paragraph breaks preserved]</p>
      <p class="u-video-credit" style="margin-top:12px;">
        Production: AI narration (ElevenLabs), AI visuals (Fal.ai),
        directed by [instructor], [institution] ([year]).
      </p>
    </div>
  </details>
</div>
<!-- ═══ END VIDEO ═══ -->
```

### Video component CSS (add once to course stylesheet)

```css
.u-video-break {
  margin: 24px 0;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #DDD9D1;
  background: #000;
}
.u-video-break__player-wrap { position: relative; }
.u-video-break__player {
  width: 100%;
  display: block;
  max-height: 420px;
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
.u-video-break__transcript { border-top: 1px solid #DDD9D1; }
.u-video-break__transcript-toggle {
  display: block;
  padding: 10px 14px;
  font-size: 13px;
  font-weight: 600;
  color: #0077AE;
  cursor: pointer;
  background: #FAFAF7;
}
.u-video-break__transcript-toggle:hover { background: #EAF4FB; }
.u-video-break__transcript-body {
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

- [ ] Narration ≤120 words — count stated explicitly
- [ ] Sensitivity check completed — flag applied if needed
- [ ] All facts verified in Stage 1b — no unchecked superlatives
- [ ] Visual brief includes "No faces, no identifiable people"
- [ ] Animation brief: subtle only — no fast motion
- [ ] Sensitive topic: no flicker, no tension effects in animation brief
- [ ] Tone category selected and ElevenLabs settings applied from table
- [ ] Voice selection step included
- [ ] Step 2c: audio generated, downloaded, and saved as [slug].mp3 ← gate before Stage 3
- [ ] All merge options shown with filled-in END_CARD_LINES
- [ ] End card Line 1 filled in or intentionally omitted
- [ ] Merge script generated by Claude (not referencing pre-existing scripts/)
- [ ] HTML path correct or clearly marked as placeholder
- [ ] LMS upload path noted (Brightspace: Manage Files → videos/ folder)
- [ ] Transcript matches narration verbatim
- [ ] Transcript saved as [slug]-transcript.txt
- [ ] Content note added above video if sensitive topic
- [ ] Credits block printed at end of output (mandatory)

---

## Cost summary

```
Base image (Fal.ai): ~$0.04  ·  Image-to-video: ~$0.10
Cloud merge:         ~$0.03  ·  ElevenLabs: [N] chars (10,000/month free)
──────────────────────────────────────────────────────
Option A — Terminal total:       ~$0.14
Option B — Cloud total:          ~$0.17
Option C — Python/MoviePy total: ~$0.14  (merge is free; same as terminal)
```

---

## CREDITS — print at the end of every output, no exceptions

After Stage 7, always print this block.
Populate the Content section from information provided during the session (Project
context, intake questions, or user-supplied details). If the user has not provided
their name, institution, or AI tools used, insert the placeholder text shown and
note that they should fill it in before publishing.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRODUCTION CREDITS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pipeline design:  Kumar Chandrasekhar, PhD (2026)
                  CC BY-NC 4.0

Content author:   [Your name]
                  [Your institution]
AI narration:     [Tool used — e.g. ElevenLabs (elevenlabs.io)]
AI visuals:       [Tool used — e.g. Fal.ai image-to-video (fal.ai)]
Assembly:         [Method used — e.g. FFmpeg (terminal) / Fal.ai API / MoviePy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CITATION
Cite the pipeline:
  Chandrasekhar, K. (2026). Course video pipeline [Claude skill]. CC BY-NC 4.0.

Cite the content:
  [Your name] ([year]). [Video title] [Course video]. [Your institution].
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Also add the credits as an expandable block inside the HTML embed,
after the transcript `<details>` block. Populate fields from session context;
use placeholder text for anything the user has not supplied:

```html
<details class="u-video-break__credits">
  <summary class="u-video-break__transcript-toggle">
    Production credits &amp; citation
  </summary>
  <div class="u-video-break__transcript-body">
    <p style="font-size:12.5px; line-height:1.8; color:#555550;">
      <strong>Pipeline design:</strong> Kumar Chandrasekhar, PhD (2026) — CC BY-NC 4.0<br>
      <strong>Content author:</strong> [Your name], [Your institution]<br>
      <strong>AI narration:</strong> [Tool used]<br>
      <strong>AI visuals:</strong> [Tool used]<br>
      <strong>Assembly:</strong> [Method used]
    </p>
    <p style="font-size:12px; line-height:1.7; color:#6B6B65;
              margin-top:10px; padding-top:10px;
              border-top:1px solid #DDD9D1;">
      <strong>Cite pipeline:</strong> Chandrasekhar, K. (2026).
      Course video pipeline [Claude skill]. CC BY-NC 4.0.<br>
      <strong>Cite content:</strong> [Your name] ([year]).
      [Video title] [Course video]. [Your institution].
    </p>
  </div>
</details>
```

And in the transcript footer, after the Sources line:

```
Pipeline: Chandrasekhar, K. (2026). Course video pipeline [Claude skill]. CC BY-NC 4.0.
Content: [Your name] ([year]). [Video title]. [Your institution].
```
