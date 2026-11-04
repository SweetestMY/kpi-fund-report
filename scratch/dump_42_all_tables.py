import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def print_kpi_tables(doc_path, label, table_indices):
    print(f"\n=======================================================")
    print(f"=== {label}: {doc_path} ===")
    print(f"=======================================================")
    doc = docx.Document(doc_path)
    for t_idx in table_indices:
        if t_idx < len(doc.tables):
            table = doc.tables[t_idx]
            print(f"\n--- TABLE {t_idx} (rows: {len(table.rows)}, cols: {len(table.columns)}) ---")
            for r_idx, row in enumerate(table.rows):
                cells_clean = []
                last = None
                for c in row.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells_clean.append(ct)
                        last = ct
                print(f"  [R{r_idx}]: {' | '.join(cells_clean)}")

print_kpi_tables('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4 Tables', range(35, 43))
