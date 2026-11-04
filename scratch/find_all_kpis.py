import io, sys, docx, re
sys.stdout.reconfigure(encoding='utf-8')

doc4 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
print("All KPI headers found in Q4 docx:")
for idx, p in enumerate(doc4.paragraphs):
    m = re.search(r'(ด้านที่\s*\d+|ตัวชี้วัดที่\s*[\d\.]+)', p.text)
    if m and len(p.text.strip()) < 100:
        print(f"P {idx}: {p.text.strip()}")
