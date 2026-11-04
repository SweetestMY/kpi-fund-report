import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

for path, label in [('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2'), ('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')]:
    doc = docx.Document(path)
    for p in doc.paragraphs:
        t = p.text.strip()
        if 'ไตรมาสที่ 1' in t and ('ตรวจสอบภายใน' in t or '4.2' in t):
            print(f"[{label}] {t}")
