import codecs

terms = ["Muca", "Muba", "幕疤", "Trial Badge", "Trial Badge", "Seed of Ascension", "Promotion Seed", "Hephaestus", "Core Forge", "Giga Blaster"]
filepath = r"d:\MyData\projects\翻译\重启项目2025年12月18日\Final_Consolidated_Up_Volume_v1.0.md"

try:
    with codecs.open(filepath, 'r', 'utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            for term in terms:
                if term.lower() in line.lower():
                    print(f"Line {i+1}: Found '{term}' -> {line.strip()}")
except Exception as e:
    # Try utf-8-sig if utf-8 fails or mixed content
    try:
        with codecs.open(filepath, 'r', 'utf-8-sig') as f:
             lines = f.readlines()
             for i, line in enumerate(lines):
                for term in terms:
                    if term.lower() in line.lower():
                        print(f"Line {i+1}: Found '{term}' -> {line.strip()}")
    except Exception as e2:
        print(f"Error: {e2}")
