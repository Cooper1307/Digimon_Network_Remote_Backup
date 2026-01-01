import re

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text

print("--- Header Debug Report ---")
with open(r'd:\MyData\projects\翻译\重启项目2025年12月18日\Final_Consolidated_Up_Volume_v1.0.md', 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        if line.strip().startswith('#'):
            header_text = line.strip().lstrip('#').strip()
            anchor = slugify(header_text)
            print(f"Line {line_num}: {line.strip()} -> #{anchor}")
