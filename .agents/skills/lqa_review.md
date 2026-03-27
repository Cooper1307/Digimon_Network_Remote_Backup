---
description: Perform Linguistic Quality Assurance review and scoring on translated content
---

# LQA Review Skill

This skill defines the procedure for performing a Linguistic Quality Assurance (LQA) review on translated content, following AIE Protocols v3.0.

## When to Use

- After MTPE is complete for a chapter section.
- As the final quality gate before generating the clean English export.
- When the user requests a quality review of existing translations.

## LQA Scorecard Dimensions

| Dimension | Weight | Description |
|---|---|---|
| **Accuracy** | 25% | Faithfulness to source meaning; no omissions or additions |
| **Fluency** | 25% | Natural, idiomatic English; reads like native prose |
| **Terminology** | 20% | Consistent use of locked Glossary terms; correct Bandai localization |
| **Style** | 15% | Maintains "Mature/Dark Fantasy" tone; dynamic verbs, verb-centricity |
| **Completeness** | 15% | No missing paragraphs, sentences, or critical details |

## Procedure

### Step 1: Preparation

1. Load the translated file from `2_Draft_Components/English_Versions/` or `2_Draft_Components/MTPE/`.
2. Load the corresponding source from `1_Source_Material/`.
3. Load `4_System_Center/Glossary_v1.0.md`.

### Step 2: Paragraph-by-Paragraph Audit

For each paragraph:

1. **Accuracy Check:** Compare against source. Flag omissions, mistranslations, or unsupported additions.
2. **Fluency Check:** Read the English in isolation. Flag awkward phrasing, unnatural word order, or calques.
3. **Terminology Check:** Verify all proper nouns and technical terms against the Glossary.
4. **Style Check:** Confirm "Mature/Dark Fantasy" tone. Flag any "Kodomo" or overly casual language.
5. **Completeness Check:** Ensure every sentence in the source has a corresponding translation.

### Step 3: Issue Classification

Classify each issue by severity:

- **Critical:** Meaning error, omission, or wrong Digimon name → must fix.
- **Major:** Noticeable fluency issue or terminology inconsistency → should fix.
- **Minor:** Stylistic preference or micro-optimization → optional fix.

### Step 4: Scoring

1. Score each dimension out of its weighted maximum.
2. Calculate the total score out of 100.
3. Target: **95+ /100** for final export approval.

### Step 5: Report & Export

1. Generate an LQA report summarizing findings and score.
2. If score ≥ 95: Approve for final export.
3. If score < 95: List required fixes and iterate.
4. Record the review in `AIE_Project_Edit_Log_v4.0.md`.

### Step 6: Delta Review Mode

Use this mode when reviewing a file that has been modified after a previous LQA pass:

1. Identify the previous version of the file (pre-fix).
2. Generate a diff between the previous and current versions.
3. Focus the LQA review **only on changed sections**:
   - Verify the fix addresses the original issue.
   - Check for regressions introduced by the fix.
   - Re-score only affected dimensions.
4. Update the overall LQA score.
5. Document: original issue → fix applied → score impact.

