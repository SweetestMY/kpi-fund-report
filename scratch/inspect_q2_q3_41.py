# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

for q_label, path in [('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx')]:
    print(f"\n============================== {q_label} ==============================")
    d = docx.Document(path)
    # Search in paragraphs
    for p_idx, p in enumerate(d.paragraphs):
        if '4.1' in p.text or 'การบริหารความเสี่ยง' in p.text:
            print(f"P {p_idx}: {p.text.strip()[:150]}")
    # Search in tables
    for t_idx, t in enumerate(d.tables):
        full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
        if 'ตัวชี้วัดที่ 4.1' in full_text or 'การบริหารความเสี่ยง' in full_text or 'ข้อร้องเรียน' in full_text or 'ควบคุมภายใน' in full_text:
            first_line = full_text.split('\n')[0]
            print(f"--- Table {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)}) : {first_line[:80]} ---")
            # print rows that contain headers or scores
            for r in t.rows:
                r_text = ' | '.join([c.text.strip().replace('\n', ' ') for c in r.cells])
                if any(k in r_text for k in ['ประเด็น', 'น้ำหนัก', 'ผลการดำเนินงาน', 'ระดับ', 'ไตรมาส', 'คะแนน']):
                    print("  Row:", r_text[:160])
