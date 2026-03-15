---
description: Full translation lifecycle for a new chapter
---

# New Chapter Translation Workflow

Use this workflow when starting translation of a new chapter or section.

## Steps

1. **Identify Source File**
   - Locate the source chapter in `1_Source_Material/`.
   - Confirm file is complete and readable.

2. **Run Terminology Audit** (Skill: `terminology_audit`)
   - Extract all proper nouns and specialized terms from the source.
   - Cross-reference with `4_System_Center/Glossary_v1.0.md`.
   - Web-verify any unflagged terms against official Bandai/Digimon localization.
   - Document findings and flag conflicts.

// turbo
3. **Translate**
   - Translate paragraph-by-paragraph following "Mature/Dark Fantasy" tone.
   - Prioritize dynamic verbs and verb-centricity.
   - Preserve all meta-references with context notes.
   - Save draft to `2_Draft_Components/MTPE/[Current_Phase]/`.

4. **MTPE Review**
   - Review sentence-by-sentence for fluency and naturalness.
   - Verify terminology consistency against the Glossary.
   - Check for omissions — every sentence in the source must be accounted for.

5. **LQA Review** (Skill: `lqa_review`)
   - Perform full LQA scorecard evaluation.
   - Target: 95+/100.
   - If score < 95, iterate fixes and re-score.

6. **Database Update** (Skill: `database_indexing`)
   - Index any new characters, items, or locations in `4_System_Center/Database/Database_[Current_Phase]_v*.md`.

7. **Final Export**
   - Generate clean English export to `English_Versions/[Current_Phase]/`.
   - If this is the last section of a chapter, generate a Milestone Export (consolidated file).

8. **Log Entry**
   - Record all actions in `AIE_Project_Edit_Log_v2.0.md` with accurate timestamps.
