# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

for q_label, path in [('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
                      ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')]:
    d = docx.Document(path)
    for t_idx, t in enumerate(d.tables):
        for r_idx, r in enumerate(t.rows):
            for c_idx, c in enumerate(r.cells):
                txt = c.text.strip().replace('\n', ' ')
                if '4.1' in txt and ('การบริหารความเสี่ยง' in txt or 'ตัวชี้วัด' in txt):
                    print(f"{q_label} Table {t_idx} (r{r_idx}, c{c_idx}): {txt[:120]}")
                    break
