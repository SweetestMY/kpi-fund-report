import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function navigateToKPI')
if idx != -1:
    print(text[idx:idx+600])
else:
    print("Not found as 'function navigateToKPI'")
