import re

def generate_toc(filename):
    toc_lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('### '):
                header = line.strip().replace('### ', '')
                # Create anchor
                anchor = header.lower()
                anchor = re.sub(r'[^\w\s-]', '', anchor) # Remove punctuation
                anchor = anchor.replace(' ', '-')
                toc_lines.append(f"- [{header}](#{anchor})")
    return toc_lines

toc = generate_toc('Final_Consolidated_Up_Volume_v1.0.md')
print("## Table of Contents")
print("")
for line in toc:
    print(line)
