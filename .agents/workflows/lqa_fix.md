---
description: Apply fixes for LQA issues found after initial seal
---

# LQA Fix Workflow

Use this workflow when LQA issues are discovered after a chapter has been sealed (e.g., terminology inconsistencies, omissions, tone issues).

## Steps

1. **Load LQA Report**
   - Identify the specific issues from the LQA report or user feedback.
   - Classify each issue: Critical / Major / Minor.

2. **Load Affected Files**
   - Open the relevant file(s) from `English_Versions/[Current_Phase]/` and/or `2_Draft_Components/MTPE/[Current_Phase]/`.
   - Load `4_System_Center/Glossary_v1.0.md` for terminology reference.

// turbo
3. **Apply Fixes**

- Address issues in priority order: Critical → Major → Minor.
- For terminology fixes: update all instances across the file consistently.
- For omission fixes: restore content from `1_Source_Material/` source.
- For tone fixes: rewrite affected passages following "Mature/Dark Fantasy" tone.

1. **Re-Score**
   - Run the `lqa_review` skill on the modified file.
   - Confirm score ≥ 95/100.

2. **Sync Dual-Save**
   - Ensure both `English_Versions/[Current_Phase]/` and `2_Draft_Components/MTPE/[Current_Phase]/` are updated.

3. **Log Entry**
   - Record the fix session in `AIE_Project_Edit_Log_v4.0.md` with:
     - Issue description, fix applied, before/after score.
