import codecs
import os

path = r'd:\MyData\projects\翻译\重启项目2025年12月18日\2_Draft_Components\English_Versions\Phase5\Ch15_v1.0.md'
with codecs.open(path, 'r', 'utf-8') as f:
    lines = f.readlines()

new_lines = [lines[0], lines[1]] + lines[60:]
text = ''.join(new_lines)

# Apply Terminology and Formatting Fixes
text = text.replace('[Five Nordic Countries Raiders]', '**Nordic 5**')
text = text.replace('"Final Strike Slash"', '**Final Strike Roll**')
text = text.replace('"Promotion Seed"', '**Seed of Promotion**')
text = text.replace('[Windrunner Brigade]', '**Wind-Chasing Brigade**')
text = text.replace('Master Nagasumi', 'Master Changsun')
text = text.replace('"Rainbow Starlight"', '**Rainbow Starlight**')
text = text.replace('[Fang of the Beast King]', "**Beast King's Fangs**")
text = text.replace('"Charm"', '**Charm**')
text = text.replace('**Rosemon** (蔷薇兽) — **Burst Evolution** — **Rosemon: Burst Mode** (蔷薇兽：爆裂形态)', '**Rosemon** — **Burst Evolution** — **Rosemon: Burst Mode**')

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(text)

print("Done")
