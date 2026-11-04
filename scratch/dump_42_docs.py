import docx
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_doc(doc_path, label):
    if not os.path.exists(doc_path):
        print(f"File not found: {doc_path}")
        return
    print(f"\n=================== {label} : {doc_path} ===================")
    doc = docx.Document(doc_path)
    
    # Check tables
    for t_idx, table in enumerate(doc.tables):
        has_kpi = False
        for row in table.rows:
            row_str = " | ".join(c.text.strip().replace('\n', ' ') for c in row.cells)
            if '4.2' in row_str or 'การตรวจสอบภายใน' in row_str:
                has_kpi = True
                break
        if has_kpi:
            print(f"\n--- TABLE {t_idx} (rows: {len(table.rows)}, cols: {len(table.columns)}) ---")
            for r_idx, row in enumerate(table.rows):
                # deduplicate adjacent identical cell strings (from merged cells)
                cells_clean = []
                last = None
                for c in row.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells_clean.append(ct)
                        last = ct
                print(f"  R{r_idx}: {' | '.join(cells_clean)[:250]}")

    # Check paragraphs
    print(f"\n--- PARAGRAPHS MENTIONING 4.2 ---")
    for p_idx, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if '4.2' in t or ('ตรวจสอบภายใน' in t and len(t) > 10):
            print(f"  P{p_idx}: {t[:200]}")

inspect_doc('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
inspect_doc('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
inspect_doc('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
