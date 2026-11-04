# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

for q_label, path in [('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')]:
    d = docx.Document(path)
    print(f"\n==================== {q_label} TOTAL TABLE ====================")
    # Search for summary table
    for i, t in enumerate(d.tables):
        full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
        if 'สภาพแวดล้อมการควบคุมภายใน' in full_text and 'กระบวนการบริหารความเสี่ยง' in full_text:
            print(f"Found table {i} in {q_label}:")
            for r in t.rows:
                row_str = ' | '.join([c.text.strip().replace('\n', ' ') for c in r.cells])
                print("  " + row_str)
