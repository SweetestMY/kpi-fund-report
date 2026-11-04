import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

hdr_idx = text.find('<div class="header-banner">')
v0_idx = text.find('id="view-topic-0"')
print(text[hdr_idx:v0_idx+100])
