import re

file_path = "Final_Consolidated_Up_Volume_v1.0.md"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    print("--- GENERATED TOC ---")
    for line in lines:
        if line.startswith("### "):
            title = line.strip().replace("### ", "").strip()
            # Skip Phase headers if they are just in TOC (or check if they are in file)
            # Actually, I want to see ALL h3 headers in file
            print(f"- [{title}](#{slugify(title)})")
            
except Exception as e:
    print(f"Error: {e}")
