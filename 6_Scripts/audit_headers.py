import re

output_file = 'header_report.txt'
input_file = r'Final_Consolidated_Up_Volume_v1.0.md'

with open(output_file, 'w', encoding='utf-8') as out:
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                if line.strip().startswith('#'):
                    out.write(f"Line {i}: {line.strip()}\n")
    except Exception as e:
        out.write(f"Error reading file: {e}")

print("Report generated.")
