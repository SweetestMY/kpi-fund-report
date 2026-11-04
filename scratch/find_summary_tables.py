# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

for q_label, path in [('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')]:
    print(f"\n==================== {q_label} Summary Tables ====================")
    d = docx.Document(path)
    for t_idx, t in enumerate(d.tables):
        full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
        if '4.1' in full_text and ('รวมผลการประเมิน' in full_text or 'สรุปผลการประเมิน' in full_text or 'ถ่วงน้ำหนัก' in full_text):
            print(f"Table {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)})")
            for r in t.rows[:10]:
                print("  " + " | ".join([c.text.strip().replace('\n', ' ') for c in r.cells[:6]]))
