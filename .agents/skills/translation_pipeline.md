---
description: Execute the full AIE translation pipeline for a chapter or section
---

# Translation Pipeline Skill

This skill defines the step-by-step procedure for translating a chapter/section following AIE Protocols v3.0.

## Prerequisites

- Load `4_System_Center/system_context.md` for protocol context.
- Load `4_System_Center/Glossary_v1.0.md` for locked terminology.
- Load relevant `4_System_Center/Database/` files for lore entities.

## Pipeline Steps

### Step 0: Pre-Flight Checklist

Before proceeding, verify all prerequisites:

- [ ] Source file exists and is complete in `1_Source_Material/`.
- [ ] `4_System_Center/Glossary_v1.0.md` is loaded.
- [ ] Previous chapter/section is SEALED (no open dependencies).
- [ ] Relevant `4_System_Center/Database/` files are loaded.
- [ ] `AIE_Project_Edit_Log_v4.0.md` has been reviewed for latest status.

If any item fails, resolve it before continuing.

### Step 1: Pre-Audit (Lore & Terminology Scan)

1. Read the source chapter from `1_Source_Material/`.
2. Extract all Digimon names, skills, items, locations, and character references.
3. Web-verify each term against official Bandai/Digimon localization.
4. Cross-reference with the locked Glossary. Flag any conflicts or new terms.
5. Document findings in a pre-audit note.

### Step 2: Initial Translation

1. Translate paragraph-by-paragraph, maintaining "Mature/Dark Fantasy" tone.
2. Prioritize **dynamic verbs** and **verb-centricity**.
3. Apply "dramatic impact over literal accuracy" where appropriate.
4. Preserve all meta-references with context notes.

### Step 3: MTPE (Machine Translation Post-Editing)

1. Review sentence-by-sentence for fluency and naturalness.
2. Verify terminology consistency against the Glossary.
3. Check for omissions — every sentence in the source must be accounted for.
4. Save analysis file to `2_Draft_Components/MTPE/`.

### Step 4: LQA (Linguistic Quality Assurance)

1. Perform a final quality pass using the LQA scorecard criteria.
2. Check: accuracy, fluency, terminology, style, completeness.
3. Generate an LQA score (target: 95+/100).
4. Save LQA report.

### Step 5: Database & Glossary Update

1. Index any new characters, items, or locations in `4_System_Center/Database/`.
2. If new locked terms are introduced, update `4_System_Center/Glossary_v1.0.md` (with version bump if needed).

### Step 6: Final Export

1. Generate the clean English export to `2_Draft_Components/English_Versions/`.
2. Update `AIE_Project_Edit_Log_v4.0.md` with second-accurate timestamps.
3. If this is the last part of a chapter, perform a **Milestone Export** (consolidated file).
