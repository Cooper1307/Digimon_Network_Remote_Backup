---
description: Add new terms to the glossary after web verification
---

# Glossary Update Workflow

Use this workflow when new Digimon terms, character names, or specialized vocabulary are discovered that need to be added to the locked glossary.

## Steps

1. **Term Identification**
   - Document the new term(s): Chinese source, proposed English translation, context of discovery.

2. **Web Verification**
   - Search official sources for each term:
     - Digimon Wiki / Wikimon
     - Official Bandai localization databases
     - Previous official English releases
   - Prefer official Bandai localization over fan translations.
   - Document the verification source.

3. **Conflict Check**
   - Cross-reference against `4_System_Center/Glossary_v1.0.md`.
   - If the new term conflicts with an existing locked entry, **stop and escalate to the user**.
   - Do NOT silently override a locked glossary term.

// turbo
4. **Add to Glossary**
   - Add the verified term to `4_System_Center/Glossary_v1.0.md` in the appropriate section.
   - Also add to the relevant sub-file in `4_System_Center/Glossary/`:
     - Characters → `characters.md`
     - Digimon/Levels → `digimon.md`
     - Skills/Gear → `skills_gear.md`
     - Lore items → `lore.md`
     - Idioms → `idioms.md`
   - Include: Chinese source | English translation | Source/authority | Date added.

5. **File Size Check**
   - Before appending, check the target file's line count.
   - If any file in `4_System_Center/` (including `Glossary_v1.0.md` and sub-files in `Glossary/`) exceeds **300 lines**, **do not continue appending**.
   - Instead, create a new versioned file (e.g., `Glossary_v2.0.md`, `skills_gear_v2.md`) and begin writing new entries there.
   - Update the header of the new file to reference the previous version.
   - This rule applies to ALL files under `4_System_Center/`, including the master glossary, category sub-files, and database files.

6. **Update CN Glossary**
   - Sync changes to `4_System_Center/Glossary_v1.0_CN.md` if applicable.

7. **Log Entry**
   - Record in `AIE_Project_Edit_Log_v2.0.md`: term added, source, date.
