import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 6.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if '\\ge' in line or 'ge 75' in line or '\\%' in line or '$\\' in line:
        print(line)
