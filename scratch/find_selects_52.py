import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 5.2.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<select[^>]*>(.*?)</select>', text, re.DOTALL):
    full = m.group(0)
    tag = full[:full.find('>')+1]
    print("TAG:", tag)
