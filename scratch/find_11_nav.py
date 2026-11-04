import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 1.1.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('navigateToKPI')
print(text[idx:idx+400])
idx2 = text.find('navigateToKPI', idx+50)
print("Second:", text[idx2:idx2+400])
