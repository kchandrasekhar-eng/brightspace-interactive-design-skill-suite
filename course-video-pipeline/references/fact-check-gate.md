<!--
  © 2026 Kumar Chandrasekhar, PhD
  Department of General Education & Academic Development Centre
  Mount Royal University, Calgary, Alberta, Canada

  Licensed under CC BY-NC-SA 4.0
  https://creativecommons.org/licenses/by-nc-sa/4.0/
  See LICENSE.md for full terms.
-->
# Fact Check Gate

This gate runs after Stage 1 (Script) and before Stage 2 (Audio Spec).
No clip proceeds to production until all factual claims are verified.

## What counts as a verifiable claim

Verify:
- Named researchers, theorists, or practitioners
- Specific dates or years ("discovered in 1885")
- Statistics or percentages ("we forget 50% within an hour")
- Named studies, books, or publications
- Causal claims ("retrieval slows forgetting")
- Institutional or legal facts

Do NOT fact-check:
- Pedagogical framing ("this is useful to know")
- Bridging sentences ("as you work through this session...")
- Rhetorical questions
- Pure opinion or interpretation clearly marked as such

## Procedure

1. Read the narration text from Stage 1
2. Extract every verifiable claim as a bullet list
3. For each claim, run a web search
4. Classify:
   - ✓ Verified — source found, claim accurate
   - ⚠ Needs revision — partially accurate or ambiguous — rewrite to be more precise
   - ✗ Incorrect — factually wrong — rewrite or remove
   - ○ Opinion/framing — not fact-checkable, flag as such

5. If any ✗ or ⚠: rewrite narration, repeat fact check
6. Only proceed when all verifiable claims are ✓

## Common errors to watch for

- Misattributed discoveries (who actually first proposed a concept)
- Rounded statistics stated as precise facts
- Historical dates off by a decade
- Overgeneralised research findings ("studies show" without specificity)
- Confusing a popular account of research with the research itself
  (e.g., Dweck's popularised growth mindset vs. her actual 2015 revision)
- **Superlatives without direct support** — flag and revise any use of:
  "primary", "leading", "main", "most common", "always", "never",
  "the biggest", "the only". These require a specific cited source
  that explicitly makes the ranking claim. If no such source exists,
  rewrite to: "consistently associated with", "a significant factor in",
  "one of the most frequently cited", etc.

## Output format

Present as a compact table:

```
FACT CHECK RESULTS
──────────────────────────────────────────────────────────────
Claim                               | Status | Source
──────────────────────────────────────────────────────────────
[claim 1 — quoted from narration]   | ✓      | [author, year]
[claim 2]                           | ✓      | [source]
──────────────────────────────────────────────────────────────
All claims verified. Proceeding to Stage 2.
```

If any revision was made, show the original and revised narration side by side
before presenting the table.
