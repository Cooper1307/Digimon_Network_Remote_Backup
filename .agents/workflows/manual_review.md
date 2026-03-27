---
description: Automated review pipeline for manually translated chapters
---

# Manual Translation Review Workflow

Use this workflow to review a chapter that was translated manually by the user, skipping the MTPE generation step.

## Steps

// turbo-all

1. **Source Verification** (Skill: `source_verification`)
   - Compare the user's English translation against the Chinese source in `1_Source_Material/`.
   - Verify translation completeness (no omissions, no unsupported additions).
   - Flag any source text typos for the record.

2. **Terminology Audit** (Skill: `terminology_audit`)
   - Scan the user's translation for proper nouns, entity names, and specialized terms.
   - Cross-reference strictly with `4_System_Center/Glossary_v1.0.md`.
   - Ensure 100% compliance with locked glossary terms.
   - Flag any newly introduced terms for glossary addition.

3. **LQA Review** (Skill: `lqa_review`)
   - Perform full LQA scorecard evaluation on the user's translation.
   - Target: 95+/100.
   - Focus on maintaining the "Mature/Dark Fantasy" tone and natural fluency.
   - If score < 95, provide a consolidated list of fix recommendations.

4. **Database & Sync**
   - If new entities were introduced, index them using `database_indexing` into `Database_[Current_Phase]_v*.md`.
   - Confirm proper saving to `English_Versions/[Current_Phase]/` and `2_Draft_Components/MTPE/[Current_Phase]/`.

5. **Log Entry**
   - Record the review session in `AIE_Project_Edit_Log_v4.0.md`, including the final LQA score.
