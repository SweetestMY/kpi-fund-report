# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

topics = [
    '3. กระบวนการบริหารความเสี่ยง',
    '4. กิจกรรมการควบคุมภายใน',
    '5. สารสนเทศและการสื่อสาร',
    '6. การติดตามผลและการประเมินผล'
]

# Find tables for each topic
for t_idx, t in enumerate(doc.tables):
    txt = " ".join([c.text for row in t.rows for c in row.cells])
    for top in topics:
        if top in txt or any(k in txt for k in ['ระบุความเสี่ยง 4 ด้าน 8 ปัจจัย', 'Control Activity', 'สารสนเทศสนับสนุนการติดตาม', 'ส่งรายงานการประเมินให้หน่วยงานต้นสังกัด']):
            print(f"\n================ Table {t_idx} (Matches: {top[:25]}) ================")
            for r_idx, row in enumerate(t.rows):
                row_vals = [c.text.strip().replace('\r', '').replace('\n', ' ') for c in row.cells]
                seen = []
                for rv in row_vals:
                    if not seen or rv != seen[-1]:
                        seen.append(rv)
                print(f"R{r_idx}: " + " | ".join(seen)[:200])
            break
