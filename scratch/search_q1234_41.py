# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

docs = [
    ('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
    ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
    ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
]

for q_label, path in docs:
    print(f"==================== {q_label}: {path} ====================")
    try:
        d = docx.Document(path)
        found = []
        for i, t in enumerate(d.tables):
            text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
            if 'ตัวชี้วัดที่ 4.1' in text or 'การบริหารความเสี่ยง' in text:
                found.append((i, text))
        print(f"Found {len(found)} matching tables for 4.1 in {q_label}")
        for i, text in found:
            first_line = text.split('\n')[0] if text else ''
            print(f"  Table {i}: {first_line[:100]} (len: {len(text)})")
    except Exception as e:
        print(f"Error reading {path}: {e}")
