import re

file_path = "Final_Consolidated_Up_Volume_v1.0.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
blue_login_count = 0

for line in lines:
    # 1. Fix Second Confirm Login (Blue)
    if line.strip() == "#### Confirm Login (Blue)":
        blue_login_count += 1
        if blue_login_count == 2:
            line = "#### Confirm Login (Blue - Ch 12)\n"
            print("Fixed Second Confirm Login (Blue)")

    # 2. Fix Side Story IV Header (Remove Chinese)
    # Match: ### Side Story IV: Operation: Pluto Extermination...
    if line.startswith("### Side Story IV: Operation: Pluto Extermination"):
        # Just force it to be clean
        line = "### Side Story IV: Operation: Pluto Extermination\n"
        print("Cleaned Side Story IV Header")
    
    # 3. Ensure Gaiden I -> Gaiden 1 (Safety check)
    if "### Gaiden I:" in line:
        line = line.replace("Gaiden I:", "Gaiden 1:")
        print("Fixed Gaiden I -> 1")
    if "### Gaiden II:" in line:
        line = line.replace("Gaiden II:", "Gaiden 2:")
        print("Fixed Gaiden II -> 2")

    out.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(out)
