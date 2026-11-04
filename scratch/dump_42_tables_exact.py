import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for t_idx in [35, 36, 37, 38, 39, 40, 41]:
    table = doc.tables[t_idx]
    print(f"\n==================== TABLE {t_idx} (rows: {len(table.rows)}, cols: {len(table.columns)}) ====================")
    for r_idx, row in enumerate(table.rows):
        cells_clean = []
        last = None
        for c in row.cells:
            ct = c.text.strip().replace('\n', ' ')
            if ct != last:
                cells_clean.append(ct)
                last = ct
        print(f"[R{r_idx}]: {' | '.join(cells_clean)}")
