# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

for q_label, path in [('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')]:
    print(f"\n==================== {q_label} Overview Tables ====================")
    d = docx.Document(path)
    for t_idx in range(min(5, len(d.tables))):
        t = d.tables[t_idx]
        full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
        first_line = full_text.split('\n')[0] if full_text else ''
        print(f"Table {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)}): {first_line[:80]}")
        for r_idx, r in enumerate(t.rows[:6]):
            r_str = ' | '.join([c.text.strip().replace('\n', ' ') for c in r.cells])
            if '4.1' in r_str or 'การบริหารความเสี่ยง' in r_str or 'น้ำหนัก' in r_str:
                print(f"  Row {r_idx}: {r_str[:160]}")
