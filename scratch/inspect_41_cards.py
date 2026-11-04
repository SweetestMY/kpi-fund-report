import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

# Let's see the classes of header and cards in 4.1
header_idx = text.find('class="header-')
if header_idx != -1:
    print(text[header_idx-20:header_idx+300])

meta_idx = text.find('class="kpi-meta-')
if meta_idx != -1:
    print(text[meta_idx-20:meta_idx+300])
