# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for t_idx in [29, 30]:
    t = doc.tables[t_idx]
    print(f"\n================ TABLE {t_idx} ================")
    for r_idx, row in enumerate(t.rows):
        vals = [c.text.strip().replace('\r', '') for c in row.cells]
        seen = []
        for v in vals:
            if not seen or v != seen[-1]:
                seen.append(v)
        print(f"--- Row {r_idx} ---")
        for item in seen:
            print(item)
