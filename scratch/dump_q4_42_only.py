import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for t_idx in [35, 36, 37, 38, 39, 40, 41]:
    t = doc.tables[t_idx]
    print(f"\n==================== TABLE {t_idx} ====================")
    for r_idx, r in enumerate(t.rows):
        cells = []
        last = None
        for c in r.cells:
            ct = c.text.strip()
            if ct != last and ct:
                cells.append(ct)
                last = ct
        print(f"--- Row {r_idx} ---")
        for idx, cell in enumerate(cells):
            print(f"[{idx}]: {cell}\n")
