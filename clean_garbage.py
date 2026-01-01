
def clean_file(filename):
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Replace the replacement character with nothing (or specific fixes if context allows)
    # Based on the output, it seems they are often trailing characters or weird separators.
    # Safe bet is to remove them or replace with - if they look like dashes.
    
    # Given "Dorugoramon?" -> likely just removal or a dash.
    # "Holy Knights?Rasielmon?Raguelmon" -> likely separators.
    
    new_content = content.replace('\ufffd', '')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    clean_file("Final_Consolidated_Up_Volume_v1.0.md")
