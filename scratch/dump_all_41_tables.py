# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for t_idx, t in enumerate(doc.tables):
    txt = " ".join([c.text for row in t.rows for c in row.cells])
    if any(k in txt for k in ['กระบวนการบริหารความเสี่ยง', 'Control Activity', 'สารสนเทศและการสื่อสาร', 'การติดตามผลและการประเมินผล', '4.1']):
        print(f"\n================ Table {t_idx} ================")
        for r_idx, row in enumerate(t.rows):
            row_vals = [c.text.strip().replace('\r', '').replace('\n', ' ') for c in row.cells]
            seen = []
            for rv in row_vals:
                if not seen or rv != seen[-1]:
                    seen.append(rv)
            print(f"  R{r_idx}: " + " | ".join(seen)[:180])
