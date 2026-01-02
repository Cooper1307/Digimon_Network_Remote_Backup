
import re

def scan_chinese(filename):
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    pattern = re.compile(r'[\u4e00-\u9fff]+')
    
    found = False
    print(f"Scanning {filename} for Chinese characters...")
    for i, line in enumerate(lines, 1):
        matches = pattern.findall(line)
        if matches:
            print(f"Line {i}: {matches} -> {line.strip()}")
            found = True
            
    if not found:
        print("No Chinese characters found.")

if __name__ == "__main__":
    scan_chinese("Final_Consolidated_Up_Volume_v1.0.md")
