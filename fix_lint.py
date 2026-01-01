import re

file_path = "Final_Consolidated_Up_Volume_v1.0.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
current_participant = "User"

for i, line in enumerate(lines):
    # Capture Participant for unique headers
    m_part = re.search(r"\*\*Participant Identity:\*\* (.+)", line)
    if m_part:
        current_participant = m_part.group(1).strip()

    # 1. Clean Chinese from Headers (H3 only)
    # Match ### Chapter ... (Chinese)
    # Be careful not to match English parens
    if line.startswith("### "):
        # Remove (Chinese...) at end
        line = re.sub(r"\s*\([^\)]*[\u4e00-\u9fa5]+[^\)]*\)\s*$", "", line)
        # Remove fullwidth parens
        line = re.sub(r"\s*（[^）]*[\u4e00-\u9fa5]+[^）]*）\s*$", "", line)

    # 2. Fix Broken Emphasis Headers (MD037): #### Affiliated Guild:** **Order... -> #### Affiliated Guild: Order...
    if line.startswith("#### Affiliated Guild:** **"):
        line = line.replace("#### Affiliated Guild:** **", "#### Affiliated Guild: ")

    # 3. Unique Login Headers (MD024)
    if line.strip() == "#### Confirm Login":
        line = f"#### Confirm Login ({current_participant})\n"

    # 4. Trailing punctuation in headers (MD026)
    if line.startswith("#"):
        # Remove . ! 。 ！ at end, but keep newline
        content = line.strip()
        if content.endswith(".") or content.endswith("!") or content.endswith("。") or content.endswith("！"):
            content = content[:-1]
            line = content + "\n"

    out.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(out)
