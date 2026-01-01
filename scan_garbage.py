
def scan_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        for i, line in enumerate(f, 1):
            if '\ufffd' in line:
                print(f"Line {i}: {line.strip()}")

if __name__ == "__main__":
    scan_file("Final_Consolidated_Up_Volume_v1.0.md")
