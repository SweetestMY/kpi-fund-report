import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.2.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('1.2.1 หหนี้ไม่เกิน 1 ปี', '1.2.1 หนี้ไม่เกิน 1 ปี')

with open('ตัวชี้วัดที่ 4.2.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed typo: หหนี้ -> หนี้")
