import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def dump_range(doc_path, label, t_start, t_end):
    print(f"\n=================== {label}: {doc_path} ===================")
    doc = docx.Document(doc_path)
    for t_idx in range(t_start, t_end + 1):
        if t_idx < len(doc.tables):
            t = doc.tables[t_idx]
            print(f"\n--- TABLE {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)}) ---")
            for r_idx, r in enumerate(t.rows):
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells.append(ct)
                        last = ct
                print(f"  R{r_idx}: {' | '.join(cells)}")

dump_range('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2', 28, 35)
dump_range('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3', 30, 37)
