import re

file_path = r'd:\MyData\projects\翻译\重启项目2025年12月18日\2_Draft_Components\English_Versions\Phase5\Gaiden3_v1.0.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements Dictionary
replacements = {
    r'\[Raiders\] \(攻略组\)': r'**Raiders**',
    r'\[Raiders\]': r'**Raiders**',
    r'\[Raiding\]': r'**Raiding**',
    r'\[Raid\]': r'**Raid**',
    
    r'"Zero Domain" \(零域\)': r'**Zero Domain**',
    r"'Zero Domain'": r'**Zero Domain**',
    
    r'"Demon Lord of Lust," Lilithmon': r'**Demon Lord of Lust**, Lilithmon',
    r'"Leviamon Subjugation War" \[Raid\]': r'**Leviamon Subjugation War** Raid',
    r'"Demon Lord of Envy,"': r'**Demon Lord of Envy**,',
    
    r'\[Vanguard Position\]': r'**Vanguard** position',
    r'\[Support Position\]': r'**Support** position',
    r'\[Defense Position\]': r'**Defense** position',
    r'\[Main Attacker Position\]': r'**Main Attacker** position',
    r'\[Substitute Position\]': r'**Substitute** position',
    r'\[Vanguard\], \[Support\], and \[Defense\]': r'**Vanguard**, **Support**, and **Defense**',
    r'\[Substitute\]': r'**Substitute**',
    r'\[Main Attacker\]': r'**Main Attacker**',
    r'\[Defense\]': r'**Defense**',
    
    r'"Sword Spirits" \(剑灵\)': r'**Sword Spirits**',
    r'"Aus Generieren" \(辙剑审判\)': r'**Aus Generieren**',
    
    r'"stop-at-contact"': r'pull my punches',  # Handled lower case
    r'"Iron Fist Punishment" \(铁拳制裁\)': r'**Iron Fist Punishment**',
    r'"Iron Fist Punishment"': r'**Iron Fist Punishment**',
    r'"Defense Training"': r'**Defense Training**',
    
    r'DoruGoramon, HerculesKabuterimon, and LordKnightmon\. I could have guessed the first and third—they were Dragon, the Chinese \*\*Raiders\*\* representative, and Owl \(He\), the leader of the \[Holy Knight Regiment\] \(神圣骑士团\)\.': 
    r'DoruGoramon, HerculesKabuterimon, and Dynasmon. I could have guessed the first and third—they were Dragon, the Chinese **Raiders** representative, and the Guild Master of the **Order of Holy Knights**.',
    # Original text form:
    r'DoruGoramon, HerculesKabuterimon, and LordKnightmon\. I could have guessed the first and third—they were Dragon, the Chinese \[Raiders\] representative, and Owl \(He\), the leader of the \[Holy Knight Regiment\] \(神圣骑士团\)\.': 
    r'DoruGoramon, HerculesKabuterimon, and Dynasmon. I could have guessed the first and third—they were Dragon, the Chinese **Raiders** representative, and the Guild Master of the **Order of Holy Knights**.',

    r"'Giga Blaster'": r'**Giga Blaster**',
    
    r'Ebemon \(机械脑魔\)': r'Ebemon',
    r'"Brain Rupture" \(脑裂\)': r'**Brain Rupture**',
    r'"Planet Destroyer" \(行星毁灭者\)': r'**Planet Destroyer**',
    r'"Sword Spirits"': r'**Sword Spirits**',
    r'"All For One" \(我为人人\)': r'**All For One**',
    r'"All For One"': r'**All For One**',
    r'"God Breath" \(神之庇佑\)': r'**God Breath**',
    r'"Avalon"': r'**Avalon**',
    r'"Aussterben" \(毁天灭地\)': r'**Aussterben**',
    r'"Urgent Fear" \(急迫恐惧\)': r'**Urgent Fear**',
    r'"Seiken Metsuha" \(圣拳灭破\)': r'**Seiken Metsuha**',
    r'"End Waltz" \(终结华尔兹\)': r'**End Waltz**',
    r'"Spiral Masquerade" \(回旋华舞\)': r'**Spiral Masquerade**',
    r'"Pile Bunker" \(冲击锥\)': r'**Pile Bunker**',
    
    r'Daemon \(究极魔兽\)': r'Daemon',
    r"'Mousse Mine'": r'**Mousse Mine**',
    r'\[Steel Legions\] \(钢铁雄兵\)': r'**Steel Legions**',
    
    r'"Quaking Table" \(掀饭桌\)': r'**Quaking Table**',
    r'"Gijin! Shinkou! Shinkaku! Oyaji!" \(地神！神鸣！神驰！亲父！\)': r'**Gijin! Shinkou! Shinkaku! Oyaji!**',
    r'"Hinokamuy" \(火神威\)': r'**Hinokamuy**',
    r'"Hinokamuy"': r'**Hinokamuy**',
    
    r"'User Identification Medal'": r'**User Identification Medal**',
    r"\[Imperial Dragon's Nest\] \(御龙巢穴\)": r"**Imperial Dragon's Nest**",
    
    r'"Endless Gauntlet" \(无尽手套\)': r'**Endless Gauntlet**'
}

for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
