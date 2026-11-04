import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

style_end = text.find('</style>')
print(text[style_end+3000:style_end+7000])
