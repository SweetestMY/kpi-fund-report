import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

v0_idx = text.find('id="view-topic-0"')
v1_idx = text.find('id="view-topic-1"')
print(text[v0_idx:v1_idx])
