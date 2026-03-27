---
description: Verify source text accuracy and translation completeness
---

# Source Verification Skill

This skill defines the procedure for verifying the accuracy of the Chinese source text and the completeness of the English translation.

## When to Use

- During MTPE review when the source text seems inconsistent.
- When the user reports a potential source text error.
- As a supplementary check after LQA identifies potential omissions.

## Procedure

### Step 1: Source Text Review

1. Read the Chinese source text from `1_Source_Material/`.
2. Flag potential source text issues:
   - Typos (e.g., "开上去" → "看上去", "亲不自禁" → "情不自禁").
   - Missing punctuation or broken sentences.
   - Inconsistent character names or pronouns.
3. Document each flagged issue with line number and proposed correction.

### Step 2: Translation Completeness Check

1. Compare source and translation line-by-line or paragraph-by-paragraph.
2. For each source paragraph, verify:
   - A corresponding English paragraph exists.
   - All sentences are accounted for (no omissions).
   - No unsupported additions exist in the translation.
3. Flag any gaps with source line references.

### Step 3: Cross-Reference Verification

1. Verify all proper nouns match the Glossary.
2. Verify all system notifications, UI elements, and game terms are consistently translated.
3. Check that dialogue attributions are correct (speaker identity).

### Step 4: Report Generation

Generate a verification report:

```markdown
## Source Verification Report — [Chapter/Section]

### Source Text Issues
| Line | Original | Issue | Suggested Fix |
| --- | --- | --- | --- |
| L15 | 开上去 | Typo | 看上去 |

### Translation Completeness
- Total source paragraphs: [N]
- Translated paragraphs: [N]
- Omissions found: [list or "None"]

### Terminology Consistency
- Glossary violations: [list or "None"]
- New terms identified: [list or "None"]
```

### Step 5: Resolution

1. For source typos: note them in the report but translate the intended meaning.
2. For omissions: restore missing content in the translation.
3. For terminology issues: escalate via `glossary_update` workflow if needed.
4. Record in `AIE_Project_Edit_Log_v4.0.md`.
