---
description: Standardized procedure for archiving a completed phase and initializing the next
---

# Phase Migration Workflow

Use this workflow when a translation phase is complete and needs to be archived, and a new phase needs to be initialized.

## Steps

1. **Final Verification**
   - Confirm all chapters in the current phase have passed LQA (score ≥ 95).
   - Confirm all entities are indexed in `4_System_Center/Database/`.
   - Confirm the Milestone Export (consolidated file) has been generated.

2. **Archive Current Phase**
   - Mark the phase as SEALED in `AIE_Project_Edit_Log_v2.0.md`.
   - Archive the phase's Database file to `4_System_Center/Database/Archive/`.

// turbo
3. **Generate Migration Package**
   - Create a `Preparation_for_PhaseN_Migration.md` file containing:
     - Summary of completed phase (chapters covered, key decisions).
     - List of new terms added to the Glossary during this phase.
     - Unresolved issues or notes for the next phase.
     - Context loading instructions for a new conversation.

4. **Initialize New Phase**
   - Create new Database file: `Database_PhaseN_v1.0.md`.
   - Create new directories in `2_Draft_Components/MTPE/PhaseN/` and `English_Versions/PhaseN/` if needed.

5. **Update System Context**
   - Update `system_context.md` §6 (Project Status & Asset Map) to reflect the new phase.
   - Sync changes to `system_context_CN.md`.

6. **Log Entry**
   - Record the migration in `AIE_Project_Edit_Log_v2.0.md` with SEAL and INIT markers.
