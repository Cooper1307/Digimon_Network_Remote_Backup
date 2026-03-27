---
description: Generate a consolidated export file for a completed translation phase
---

# Consolidation Export Skill

This skill defines the procedure for merging individual chapter exports into a single, cohesive phase-level consolidated file.

## When to Use

- When all chapters in a phase have passed LQA and are ready for final export.
- As the final step before sealing a phase.

## Procedure

### Step 1: Collect Chapter Exports

1. List all chapter files in `English_Versions/[Current_Phase]/`.
2. Verify each file has passed LQA (score ≥ 95).
3. Confirm the correct reading order (Preface → Chapters → Gaiden/Side Stories).

### Step 2: Generate Table of Contents

1. Extract all chapter/section headers from the individual files.
2. Build a markdown TOC with internal anchor links.
3. Ensure TOC header names exactly match content headers (avoid MD051 errors).

### Step 3: Consolidate

1. Create a new file: `Final_Consolidated_[Volume]_v1.0.md`.
2. Insert TOC at the top.
3. Append each chapter in reading order, separated by horizontal rules.
4. Remove any per-file headers that duplicate the TOC entry.

### Step 4: Lint & Polish

1. Run markdown linting (MD012, MD022, MD024, MD025, MD026, MD032, MD037, MD051).
2. Fix all errors:
   - MD024: Ensure unique heading names.
   - MD051: Ensure TOC links match content headings exactly.
   - MD012: Remove multiple blank lines.
3. Verify encoding: no replacement characters (�), no stray artifacts.

### Step 5: Final Verification

1. Spot-check 3 random chapters for content integrity.
2. Verify word count is within expected range.
3. Confirm all Glossary-locked terms are used consistently.

### Step 6: Export & Log

1. Save the consolidated file.
2. Record in `AIE_Project_Edit_Log_v4.0.md` with SEAL marker.
