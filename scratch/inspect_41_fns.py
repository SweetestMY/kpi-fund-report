import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find functions after quarterDefaults41
idx = text.find('function switchTopicView')
print(text[idx:idx+3500])
