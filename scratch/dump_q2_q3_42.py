import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def dump_q(doc_path, label):
    print(f"\n=================== {label} ===================")
    doc = docx.Document(doc_path)
    for t_idx, t in enumerate(doc.tables):
        full = " ".join(c.text.strip() for r in t.rows for c in r.cells)
        if 'ตรวจสอบภายใน' in full and ('ประเด็น' in full or 'กฎบัตร' in full or '4.2' in full or 'N/A' in full):
            print(f"Table {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)})")
            for r in t.rows:
                row_str = " | ".join(c.text.strip().replace('\n', ' ') for c in r.cells)
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells.append(ct)
                        last = ct
                print("   " + " | ".join(cells)[:200])

dump_q('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
dump_q('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
