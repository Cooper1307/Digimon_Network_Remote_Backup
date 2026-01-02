
import re

def report_hallucinations(filename, report_file):
    with open(report_file, 'w', encoding='utf-8') as out:
        with open(filename, 'r', encoding='utf-8', errors='replace') as f:
            for i, line in enumerate(f, 1):
                # Search for Chinese characters
                if re.search(r'[\u4e00-\u9fff]', line):
                    out.write(f"Line {i}: {line.strip()}\n")

if __name__ == "__main__":
    report_hallucinations("Final_Consolidated_Up_Volume_v1.0.md", "hallucination_report.txt")
