# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

for q_label, path in [('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')]:
    d = docx.Document(path)
    for t_idx, t in enumerate(d.tables):
        for r_idx, r in enumerate(t.rows):
            cells_text = [c.text.strip().replace('\n', ' ') for c in r.cells]
            if len(cells_text) > 2 and '4.1' in cells_text[0]:
                print(f"{q_label} Table {t_idx} Row {r_idx}: {' | '.join(cells_text[:8])}")
