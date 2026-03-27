import codecs

with codecs.open(r'd:\MyData\projects\翻译\重启项目2025年12月18日\ch15_missing.md', 'r', 'utf-8') as f:
    missing = f.read()

with codecs.open(r'd:\MyData\projects\翻译\重启项目2025年12月18日\2_Draft_Components\English_Versions\Phase5\Ch15_v1.0.md', 'a', 'utf-8') as f:
    f.write('\n' + missing + '\n')
