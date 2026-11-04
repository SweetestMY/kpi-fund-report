# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

# Search in 1.txt
if os.path.exists('1.txt'):
    with open('1.txt', 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    print("In 1.txt:")
    for line in txt.splitlines():
        if any(k in line for k in ['คู่มือ', 'องค์ประกอบ', 'ความเสี่ยง', '4.1']):
            print("  ", line[:100])

# Search in docx
try:
    import docx
    for doc_name in ['ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx']:
        if os.path.exists(doc_name):
            print(f"\nSearching in {doc_name}...")
            doc = docx.Document(doc_name)
            for p in doc.paragraphs:
                if any(k in p.text for k in ['คู่มือการบริหารความเสี่ยง', 'องค์ประกอบของคู่มือ', '4.1', 'การกำหนดวัตถุประสงค์']):
                    print("  P:", p.text[:120])
            for t in doc.tables:
                for row in t.rows:
                    for cell in row.cells:
                        if any(k in cell.text for k in ['คู่มือการบริหารความเสี่ยง', 'องค์ประกอบของคู่มือ', 'การกำหนดวัตถุประสงค์']):
                            print("  Table Cell:", cell.text.strip().replace('\n', ' ')[:120])
except Exception as e:
    print("Docx error:", e)
