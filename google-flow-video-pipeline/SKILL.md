---
name: google-flow-video-pipeline
description: >
  Produces a Google Flow (Veo) production package for a short course video.
  Use this skill whenever the user wants to create a course video with Google
  Flow, Veo, native synchronised audio, cinematic clips, spoken dialogue, or a
  storyboard-driven sequence. Triggers on: "make a Flow video", "Veo course
  video", "Google Flow storyboard", "generate clips in Flow", "cinematic
  explainer", "video with native audio", "AI video with dialogue", or any
  request to produce short course video content using Google Flow. Distinct
  from course-video-pipeline (ElevenLabs + Fal.ai, cheap, no native audio):
  reach for this skill when the instructor has a paid Google AI plan and wants
  Veo's native synced audio or cinematic quality. Produces: a
  storyboard-initiating Flow prompt, sensitivity check, fact-check gate,
  clip-by-clip generation guidance, SceneBuilder/Premiere combine
  instructions, a Brightspace HTML embed with transcript, and a credits block.
license: CC BY-NC 4.0
metadata:
  author: Kumar Chandrasekhar, PhD
  affiliation: Academic Development Centre | Department of General Education, Mount Royal University, Calgary, Alberta, Canada
  version: 0.1.0
  date: 2026
  contact: https://github.com/kchandrasekhar-eng/brightspace-interactive-design-skill-suite/issues
  changelog: |
    - v0.1.0 — Initial release. Storyboard-initiating prompt model: Claude writes
    the prompt; Flow develops the storyboard and grid. Clip-by-clip
    generation, dual combine path (Flow tools / Premiere Pro),
    Brightspace embed for 16:9 native-audio video.
---
# Google Flow Video Pipeline

Produces the Claude-side assets for one short course video generated in Google
Flow (powered by Veo). Flow does the storyboarding, the grid, and the clip
generation. This skill produces the prompt that starts it and the material that
surrounds it.

**Core formula:** Text teaches. Video re-engages. Interaction confirms.

**Target:** ≤60 seconds total, assembled from Flow's ~8-second clips. One idea
per video. Always ends with a bridge to the next activity.

**How Flow fits:** Claude writes a prompt engineered to initiate storyboard
development in Flow. Flow generates the storyboard and the scene grid. The
instructor generates each clip one by one, then combines them in Flow's own
tools or in Adobe Premiere Pro. Claude never writes the storyboard or the grid —
Flow does that.

**Requirements:** A paid Google AI plan. Google AI Pro includes Flow with a
monthly generation limit; Google AI Ultra raises the limits and unlocks the
highest Veo tier. Flow is web-based (flow.google). Veo 3.1 produces ~8-second
clips with native synchronised audio at 720p–4K.

---

## Step 0 — Gather course context

Before producing any output, collect:

1. **Course name and institution**
2. **Clip type** — see taxonomy below
3. **Topic** — the single concept, scenario, or moment this video covers
4. **Where it sits** in the session (after which section)
5. **Google AI plan** — ask: "Are you on Google AI Pro or Ultra?" (needed for
   Flow access; Ultra unlocks the highest Veo tier and higher limits)
6. **Spoken content?** — will the video have spoken narration or dialogue?
   (Veo generates native audio, so this is built into the clip, not a separate
   track)
7. **Reference assets** — does the instructor have images, characters, or a
   colour palette to feed Flow as ingredients for visual consistency?
8. **Citation needed?** — a specific source to credit in the video and embed

Then run the **sensitivity check** before anything else.

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
- In the storyboard-initiating prompt: request a calm, unhurried pace, warm and
  abstract imagery, no sudden motion, no harsh or clinical environments, gentle
  audio
- Add a content note to the HTML embed (see Stage 5)

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
STAGE 1   — SPOKEN CONTENT (if any)
STAGE 1b  — FACT CHECK GATE
STAGE 2   — STORYBOARD-INITIATING FLOW PROMPT   ← the core deliverable
STAGE 3   — GENERATE CLIPS ONE BY ONE (in Flow)
STAGE 4   — COMBINE (Flow tools / Premiere Pro)
STAGE 5   — TRANSCRIPT + BRIGHTSPACE EMBED
```

Do not skip Stage 1b. Label each section clearly.

---

## STAGE 1 — SPOKEN CONTENT

Only if the video has narration or dialogue. Veo speaks this natively, so write
it as the words the video will say.

- Budget ~110 words per minute of finished video. A 45–60s clip is ~85–110
  words. Count explicitly and state the count.
- Warm, direct — "you" and "we", not lecture voice.
- One idea only. No sub-points, no lists.
- End with a sentence that bridges to the next activity.
- No inline citations — these go in the end of the video and the embed credit.
- **Sensitive topics:** slower rhythm, shorter sentences, plain language.

If the video is purely visual (no speech), skip to Stage 1b with the concept
description only.

---

## STAGE 1b — FACT CHECK GATE

**This stage must complete before Stage 2.**

- Extract every verifiable factual claim from the spoken content and concept.
- **Avoid unsupported superlatives** — "primary", "most", "always", "never",
  "the leading" — unless a cited source supports them.
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
[claim 2]                     | ○      | Pedagogical framing
──────────────────────────────────────────────────────
[All claims verified / Revised content below]
Proceeding to Stage 2.
```

---

## STAGE 2 — STORYBOARD-INITIATING FLOW PROMPT

This is the core deliverable. Write a single prompt the instructor pastes into
Flow. Its job is to make Flow develop the storyboard and the scene grid — not to
describe every shot yourself. Give Flow the concept, the constraints, and the
creative direction, then ask it to build the storyboard and generate the
sequence.

Use Veo-friendly language: shot and camera vocabulary (wide, close, slow push
in, drift), lighting and palette, mood, and audio direction. Keep it a
description of intent, not a rigid shot-by-shot script — Flow's storyboard step
works best with room to compose.

### Prompt template

```
Develop a storyboard and scene grid for a short educational video, then
generate the clips.

Concept / logline: [one sentence — what the video shows and teaches]
Audience: [e.g. first-year students, non-specialist]
Total length: [~45–60s, assembled from ~8s clips → roughly N scenes]
Tone: [warm / calm / narrative — from the clip type]
Visual style: [photorealistic for scenarios; stylised illustration for
              analogy/recap/break]
Sequence intent: [the beats you want, in order, as intent not exact shots —
                  e.g. "open on the problem, show the mechanism, land on the
                  takeaway"]
Camera and motion: [subtle, purposeful moves; slow push-in, gentle drift;
                    no fast cuts]
Audio: [native synced audio — describe the voice tone and any ambient sound;
        if there is spoken content, paste the Stage 1 lines here for Flow to
        voice]
On-screen text: [none, unless a single key term is intended]
Consistency: [reference ingredients/characters/palette to keep across clips —
             list any uploaded assets, or the brand colours]
Aspect ratio: 16:9
Resolution: [1080p or 4K if the plan allows]

Please build the storyboard first, show the scene grid, then generate each clip.
```

Fill every bracket from Step 0 and Stage 1. Produce one complete, ready-to-paste
prompt, then a short note on what the instructor should expect Flow to return
(a storyboard, a scene grid, and per-scene clips).

**Reference assets:** if the instructor has images or characters, tell them to
add these as ingredients in Flow before generating, so faces, style, and colour
stay consistent across the ~8-second clips.

---

## STAGE 3 — GENERATE CLIPS ONE BY ONE

Guidance for the instructor once Flow has produced the storyboard and grid:

1. Work through the scene grid in order, generating one clip per scene.
2. Each clip is ~8 seconds with native audio. Review each before moving on.
3. Regenerate any weak clip with a small prompt tweak rather than rebuilding the
   whole sequence. Keep the same ingredients/style for continuity.
4. Watch continuity across clips — subject, palette, lighting, and any character
   should hold from clip to clip. Flow's ingredients and the Extend feature help
   here.
5. Mind the generation budget: Google AI Pro includes a monthly cap; regenerate
   deliberately.
6. Download each approved clip (or keep them in the Flow project for Stage 4).

---

## STAGE 4 — COMBINE

Two supported paths. Recommend based on what the instructor has.

**Path A — Flow's own tools.** Use SceneBuilder and Extend to sequence and
lengthen clips inside Flow, then export the finished video. Simplest when the
whole video lives in one Flow project and needs no outside editing.

**Path B — Adobe Premiere Pro.** Import the downloaded clips, sequence them on
the timeline, add transitions and any titles, and export. Best when the
instructor wants fine control, external footage, or precise trimming.

**Export target (either path):** MP4, H.264, 16:9, 1080p, with audio. Name it
`[slug].mp4`.

---

## STAGE 5 — TRANSCRIPT + BRIGHTSPACE EMBED

### Transcript

Reproduce the spoken content verbatim (Stage 1). Save as
`[slug]-transcript.txt`. If the video is purely visual, write a one-line
descriptive caption instead.

### LMS upload — before embedding the HTML

Upload the video file to Brightspace first; the embed points to where it lives.

**Brightspace (D2L):**
1. Course Admin → Manage Files
2. At the course root, create a folder named `videos` if it does not exist
3. Upload `[slug].mp4` into `videos`
4. The `src` path resolves as:
   `/content/enforced/[course-id]-[course-name]/videos/[slug].mp4`

Brightspace file paths are case-sensitive — match the filename exactly.

### HTML component

Flow video carries its own native audio, so the credit names Flow/Veo and omits
any separate narration tool.

```html
<!-- ═══ VIDEO: [Clip name] ═══ -->
[content note here if sensitive — see below]
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
    AI video and audio: Google Flow (Veo) &middot;
    &copy; [year] [instructor], [institution].
  </p>
  <details class="u-video-break__transcript">
    <summary class="u-video-break__transcript-toggle">Read transcript</summary>
    <div class="u-video-break__transcript-body">
      <p>[Full spoken content — paragraph breaks preserved]</p>
    </div>
  </details>
</div>
<!-- ═══ END VIDEO ═══ -->
```

### Content note (sensitive topics only)

```html
<p class="u-content-note">Heads up: this short video touches on [topic].
If you would rather not watch, the key points are also in the text above.</p>
```

### CSS (add once to the course stylesheet)

Reuse the `.u-video-break`, `.u-video-credit`, `.u-video-break__transcript*`,
and `.u-content-note` rules from the course stylesheet. This skill uses the same
16:9 component as course-video-pipeline, so no new CSS is needed if that
stylesheet is already in the course.

---

## Quality checks before presenting output

- [ ] Spoken content ≤ target word count — count stated explicitly (or marked
      visual-only)
- [ ] Sensitivity check completed — flag and prompt adjustments applied if needed
- [ ] All facts verified in Stage 1b — no unchecked superlatives
- [ ] Storyboard-initiating prompt is complete and ready to paste
- [ ] Prompt asks Flow to build the storyboard and grid, then generate clips
- [ ] Reference/ingredient guidance included for visual consistency
- [ ] Clip-by-clip generation guidance included (~8s, continuity, budget)
- [ ] Both combine paths shown (Flow tools / Premiere Pro) with export settings
- [ ] Brightspace upload path noted (Manage Files → videos/)
- [ ] Credit names Google Flow (Veo); no separate narration tool listed
- [ ] Transcript matches spoken content verbatim (or visual-only caption)
- [ ] Credits block printed at end of output (mandatory)

---

## Cost / access summary

```
Google AI Pro:   Flow access + monthly generation cap
Google AI Ultra: higher limits + highest Veo tier
Assembly:        Flow tools (included) or Adobe Premiere Pro (separate licence)
```

State clearly that Flow requires a paid Google plan, so this path is not free —
course-video-pipeline is the low-cost alternative when native audio is not
needed.

---

## CREDITS — print at the end of every output, no exceptions

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRODUCTION CREDITS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pipeline design:  Kumar Chandrasekhar, PhD (2026)
                  CC BY-NC 4.0

Content author:   [Your name]
                  [Your institution]
AI video + audio: Google Flow (Veo) — flow.google
Assembly:         [Flow tools / Adobe Premiere Pro]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CITATION
Cite the pipeline:
  Chandrasekhar, K. (2026). Google Flow video pipeline [Claude skill].
  CC BY-NC 4.0.

Cite the content:
  [Your name] ([year]). [Video title] [Course video]. [Your institution].
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Populate the content fields from session context; use placeholder text for
anything the user has not supplied and note that they should fill it in before
publishing.
