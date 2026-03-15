---
description: Index new entities (characters, items, locations) into the project database
---

# Database Indexing Skill

This skill defines the procedure for adding newly discovered entities to the project's structured lore database.

## When to Use

- After translating a chapter that introduces new characters, items, or locations.
- During a terminology audit when new entities are identified.
- As part of the Database Update step in the translation pipeline.

## Procedure

### Step 1: Entity Extraction

1. Read the translated chapter or section.
2. Identify all entities not yet in `4_System_Center/Database/Database_[Current_Phase]_v*.md`:
   - **Characters:** Human players, Digimon partners, NPCs.
   - **Items:** Equipment, consumables, key items, materials.
   - **Locations:** Zones, dungeons, landmarks, buildings.

### Step 2: Classification & Template

For each new entity, fill in the template:

```markdown
### [Entity Name]

- **Type:** Character / Item / Location
- **Chinese Name:** [原文名]
- **English Name:** [Translation]
- **First Appearance:** Chapter [N]
- **Description:** [Brief description from context]
- **Relations:** [Connected entities, if any]
- **Notes:** [Translation decisions, lore significance]
```

### Step 3: Write to Database

1. Open the active Database file (e.g., `Database_[Current_Phase]_v*.md`).
2. Append the new entity entries in the appropriate section.
3. Maintain alphabetical or chronological order within sections.

### Step 4: Cross-Reference

1. Verify each entity's name against `4_System_Center/Glossary_v1.0.md`.
2. If the entity name is a locked term, use the Glossary version.
3. If the entity is new to the Glossary, flag for addition via the `glossary_update` workflow.

### Step 5: Log

1. Record the addition in `AIE_Project_Edit_Log_v2.0.md`.
