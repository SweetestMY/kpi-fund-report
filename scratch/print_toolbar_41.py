import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<div class="toolbar')
# print 3000 chars from start_idx
print(text[start_idx:start_idx+3500])
