import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

v1_idx = text.find('id="view-topic-1"')
v2_idx = text.find('id="view-topic-2"')
print(text[v1_idx:v2_idx])
