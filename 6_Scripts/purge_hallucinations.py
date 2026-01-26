
import re

def purge_artifacts(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove standard parenthesized Chinese: (神圣骑士团)
    # Match '(' followed by content with at least one Chinese char, ending with ')'
    # We use [^)\n]* to avoid spanning lines widely, though some might.
    # We allow '?' at the end for the corrupted cases seen (e.g. (攻略?)
    content = re.sub(r'\s*\([^)\n]*[\u4e00-\u9fff]+[^)\n]*[)?]', '', content)

    # 2. Fix specific broken punctuation seen in report
    # "?Seiken" -> "Seiken", "?All" -> "All"
    # Logic: ? followed by Capital letter, preceeded by space or start.
    content = re.sub(r'(?<=\s)\?([A-Z])', r'"\1', content)
    
    # 3. Fix "using the name '疤爷'" -> "using the name 'Ba-ye'" (or just remove the Chinese chars if covered above? No, '疤爷' is not in parens)
    # Remove '疤爷' 
    content = re.sub(r"'[\u4e00-\u9fff]+'", "'Ba-ye'", content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    purge_artifacts("Final_Consolidated_Up_Volume_v1.0.md")
