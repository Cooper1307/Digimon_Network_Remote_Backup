# Workspace Rules — AIE Translation Project

## Context Loading (Mandatory per Session)

1. Read `4_System_Center/system_context.md` — the **sole authoritative source** for all AIE protocols.
2. Read `4_System_Center/Glossary_v1.0.md` — locked terminology glossary.
3. Check `AIE_Project_Edit_Log_v4.0.md` — latest progress and pending items.
4. Load relevant `4_System_Center/Database/` files for lore entities when translating.

## Behavioral Constraints

1. **Terminology Inheritance:** All terms must inherit from `Glossary_v1.0.md`. Never silently override a locked term. If an official source conflicts with the glossary, **flag it and escalate to the user**.
2. **Pre-Audit Mandatory:** Before translating any new chapter, execute the `terminology_audit` skill (Rule 0).
3. **Omission Audit:** After every major task, perform a mandatory check for missing or dropped information.
4. **Edit Log Discipline:** Record all changes in `AIE_Project_Edit_Log_v4.0.md` with accurate timestamps. Historical log: `AIE_Project_Edit_Log_v4.0.md` (Phase 1–5, SEALED — read-only).
5. **Path Authority:** All file paths follow the Asset Map defined in `system_context.md` §6. When in doubt, refer there — do not assume.

## Resource Index

| File | Purpose |
| --- | --- |
| `4_System_Center/system_context.md` | Master protocol document (v4.0) |
| `4_System_Center/system_context_CN.md` | Chinese translation of master protocol |
| `4_System_Center/Glossary_v1.0.md` | Locked terminology glossary (EN) |
| `4_System_Center/Glossary_v1.0_CN.md` | Locked terminology glossary (CN) |
| `4_System_Center/Database/` | Entity & lore repository |
| `AIE_Project_Edit_Log_v4.0.md` | Active change log (Maintenance phase) |
| `AIE_Project_Edit_Log_v4.0.md` | Archived change log (Phase 1–5, SEALED) |
