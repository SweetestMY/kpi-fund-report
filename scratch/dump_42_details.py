import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def dump_section_42(doc_path, label):
    print(f"\n=======================================================")
    print(f"=== {label}: {doc_path} ===")
    print(f"=======================================================")
    doc = docx.Document(doc_path)
    
    start = False
    count = 0
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if 'ตัวชี้วัดที่ 4.2' in t or 'ตัวชี้วัดที่ 4.2 ' in t:
            start = True
            print(f"\n--- PARAGRAPH START at {i}: {t} ---")
        elif start and ('ตัวชี้วัดที่ 4.3' in t or 'ตัวชี้วัดที่ 5' in t):
            print(f"--- END PARAGRAPHS at {i}: {t} ---")
            break
        elif start:
            if t:
                print(f"P{i}: {t}")

    # Now let's find tables for 4.2
    for t_idx, table in enumerate(doc.tables):
        table_full_text = " ".join(c.text.strip() for row in table.rows for c in row.cells)
        if '4.2' in table_full_text and ('ตรวจสอบภายใน' in table_full_text or 'กฎบัตร' in table_full_text or 'แผนการตรวจสอบ' in table_full_text or 'รายงานผลการตรวจสอบ' in table_full_text):
            print(f"\n--- TABLE {t_idx} (rows: {len(table.rows)}, cols: {len(table.columns)}) ---")
            for r_idx, row in enumerate(table.rows):
                cells_clean = []
                last = None
                for c in row.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells_clean.append(ct)
                        last = ct
                print(f"  R{r_idx}: {' | '.join(cells_clean)}")

dump_section_42('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
dump_section_42('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
dump_section_42('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
