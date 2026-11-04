import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
for t_idx, t in enumerate(doc.tables):
    for r_idx, r in enumerate(t.rows):
        for c in r.cells:
            if '4.2' in c.text:
                print(f"Table {t_idx} Row {r_idx}: {c.text[:120].strip()}")
                break
