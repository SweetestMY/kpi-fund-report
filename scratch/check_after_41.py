import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for i in range(295, 312):
    if i < len(doc.paragraphs):
        print(f"P{i}: {doc.paragraphs[i].text.strip()}")
