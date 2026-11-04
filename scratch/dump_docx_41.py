# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

found = False
for i, p in enumerate(doc.paragraphs):
    if 'ตัวชี้วัดที่ 4.1' in p.text:
        found = True
        print(f"=== Paragraph {i} ===")
    if found:
        print(p.text)
        if 'ตัวชี้วัดที่ 4.2' in p.text:
            break

print("\n=== Tables in Docx around 4.1 ===")
for t_idx, t in enumerate(doc.tables):
    txt = " ".join([c.text for row in t.rows for c in row.cells])
    if '4.1' in txt or 'การกำหนดวัตถุประสงค์การบริหารความเสี่ยง' in txt:
        print(f"\n--- Table {t_idx} ---")
        for r_idx, row in enumerate(t.rows):
            row_vals = [c.text.strip().replace('\n', ' ') for c in row.cells]
            # eliminate duplicates in merged cells
            seen = []
            for rv in row_vals:
                if not seen or rv != seen[-1]:
                    seen.append(rv)
            print(f"R{r_idx}: " + " | ".join(seen))
