import re
import sys

file_path = "Final_Consolidated_Up_Volume_v1.0.md"

try:
    with open(file_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

out = []
current_participant = "User"

for i, line in enumerate(lines):
    original_line = line
    modified = False

    # Capture Participant
    m_part = re.search(r"\*\*Participant Identity:\*\*\s*(.+)", line)
    if m_part:
        current_participant = m_part.group(1).strip()
        # print(f"Found participant: {current_participant}")

    # 1. Clean Chinese from Headers
    if line.startswith("### "):
        # Regex to find (Chinese) at end: space + ( + chars + Chinese + chars + ) + space + end
        # Using a simpler check for Chinese characters in parens
        if re.search(r"[\u4e00-\u9fa5]", line):
            new_line = re.sub(r"\s*[\(（][^\)）]*[\u4e00-\u9fa5]+[^\)）]*[\)）]\s*$", "", line.strip()) + "\n"
            if new_line != line:
                line = new_line
                modified = True
                print(f"Fixed Chinese Header: {line.strip()}")

    # 2. Fix Broken Emphasis Headers: #### Affiliated Guild:** **Order...
    if "#### Affiliated Guild:** **" in line:
        line = line.replace("#### Affiliated Guild:** **", "#### Affiliated Guild: ")
        modified = True
        print(f"Fixed Emphasis: {line.strip()}")

    # 3. Unique Login Headers
    if line.strip() == "#### Confirm Login":
        line = f"#### Confirm Login ({current_participant})\n"
        modified = True
        print(f"Fixed Duplicate: {line.strip()}")

    # 4. Trailing punctuation in headers (MD026) - Apply to ANY header #
    if line.strip().startswith("#"):
        sline = line.strip()
        if sline[-1] in [".", "!", "。", "！"]:
            # Check if it's text masking as header? No, it's header.
            # But MD026 ignores ? usually.
            line = sline[:-1] + "\n"
            modified = True
            print(f"Fixed Punctuation: {line.strip()}")

    out.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(out)

print("Script completed.")
