---
description: Audit and verify Digimon terminology against official sources and glossary
---

# Terminology Audit Skill

This skill defines how to perform a comprehensive terminology audit for any chapter or section, ensuring alignment with official Bandai/Digimon localization and the project glossary.

## When to Use

- Before starting translation of a new chapter (Rule 0 — mandatory).
- When encountering unfamiliar Digimon terms mid-translation.
- During periodic glossary maintenance.

## Procedure

### Step 1: Term Extraction

1. Read the source text from `1_Source_Material/`.
2. Extract all proper nouns and specialized terms:
   - Digimon names (e.g., 亚古兽 → Agumon)
   - Evolution stages (e.g., 成熟期 → Champion)
   - Skills / attacks (e.g., 勇气之盾 → Brave Shield)
   - Items and materials
   - Location names
   - Character names (human and Digimon)

### Step 2: Glossary Cross-Reference

1. Load `4_System_Center/Glossary_v1.0.md`.
2. For each extracted term:
   - If found in glossary → use the locked translation.
   - If NOT found → flag for web verification.

### Step 3: Web Verification

1. For flagged terms, search official sources:
   - Digimon Wiki / Wikimon
   - Official Bandai localization databases
   - Previous official English releases
2. Prefer official Bandai localization over fan translations.
3. Document the source of each verified term.

### Step 4: Conflict Resolution

- If an official term conflicts with the glossary, **flag it** and note both versions.
- Do NOT silently override a locked glossary term.
- Escalate conflicts to the user for a decision.

### Step 5: Update & Document

1. Add verified new terms to the Glossary with:
   - Chinese source | English translation | Source/authority | Date added
2. Record any glossary changes in `AIE_Project_Edit_Log_v1.0.md`.
3. Update `4_System_Center/Database/` if new entities are discovered.
