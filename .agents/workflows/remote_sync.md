---
description: Synchronize local project files with the GitHub remote repository
---

# Remote Sync Workflow

Use this workflow to push local changes to the GitHub remote repository.

- **Remote:** `https://github.com/Cooper1307/Digimon_Network_Remote_Backup`
- **Branch:** `main`

## Steps

1. **Pre-Sync Check**
   - Verify working directory is clean: `git status`.
   - Review pending changes and confirm they are intentional.

// turbo
2. **Stage Changes**
   - Stage all modified/new files: `git add -A`.
   - Review staged files: `git diff --cached --stat`.

3. **Commit**
   - Create a descriptive commit message in Chinese following project convention.
   - Example: `同步：[简要描述变更内容]`.
   - Command: `git commit -m "同步：[描述]"`.

4. **Push**
   - Attempt HTTPS push: `git push -u origin main`.
   - If HTTPS fails (port 443 blocked), note the error.
   - **Do NOT modify system SSH configuration** without user permission.

5. **Log Entry**
   - Record in `AIE_Project_Edit_Log_v2.0.md`:
     - Remote URL, branch, commit hash, push status (success/failure).
     - If failed: error details and recommended next steps.
