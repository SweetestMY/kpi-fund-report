import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
for t_idx in range(5):
    t = doc.tables[t_idx]
    print(f"Table {t_idx}: rows={len(t.rows)}, cols={len(t.columns)}")
    for r_idx in range(min(5, len(t.rows))):
        print(f"   R{r_idx}: " + " | ".join(c.text.strip().replace('\n', ' ') for c in t.rows[r_idx].cells)[:150])
