# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for t_idx in range(20, min(45, len(doc.tables))):
    t = doc.tables[t_idx]
    first_cell = t.rows[0].cells[0].text.strip().replace('\n', ' ')[:100]
    second_cell = t.rows[0].cells[1].text.strip().replace('\n', ' ')[:100] if len(t.rows[0].cells) > 1 else ""
    print(f"Table {t_idx} (rows={len(t.rows)}, cols={len(t.columns)}): {first_cell} | {second_cell}")
