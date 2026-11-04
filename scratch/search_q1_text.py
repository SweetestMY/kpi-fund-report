# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

for q_label, path in [('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')]:
    d = docx.Document(path)
    for i, t in enumerate(d.tables):
        full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
        if 'ไตรมาส 1' in full_text or 'ไตรมาสที่ 1' in full_text:
            lines = [l for l in full_text.split('\n') if 'ไตรมาส' in l or '4.1' in l or 'ความเสี่ยง' in l]
            print(f"{q_label} Table {i}: {len(lines)} matching lines")
            for l in lines[:5]:
                print(f"   {l[:120]}")
