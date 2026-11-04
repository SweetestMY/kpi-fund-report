import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for t_idx, table in enumerate(doc.tables):
    text = " ".join(c.text.strip() for row in table.rows for c in row.cells)
    if 'ตรวจสอบภายใน' in text or 'กฎบัตร' in text or '4.2' in text:
        print(f"Table {t_idx}: rows={len(table.rows)}, cols={len(table.columns)}")
        # print first 2 rows
        for r_idx in range(min(5, len(table.rows))):
            row = table.rows[r_idx]
            cells_clean = []
            last = None
            for c in row.cells:
                ct = c.text.strip().replace('\n', ' ')
                if ct != last:
                    cells_clean.append(ct)
                    last = ct
            print(f"   R{r_idx}: {' | '.join(cells_clean)[:180]}")
