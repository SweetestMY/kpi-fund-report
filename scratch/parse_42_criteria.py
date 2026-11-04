import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_42_from_doc(doc_path, label):
    print(f"\n=======================================================")
    print(f"=== {label}: {doc_path} ===")
    print(f"=======================================================")
    doc = docx.Document(doc_path)
    for t_idx, table in enumerate(doc.tables):
        full = " ".join(c.text.strip() for r in table.rows for c in r.cells)
        if 'การปฏิบัติงาน' in full and 'ตรวจสอบภายใน' in full and 'น้ำหนัก' in full:
            print(f"--- Sub-issue Table {t_idx} ---")
            for r_idx, r in enumerate(table.rows):
                row_str = " | ".join(c.text.strip().replace('\n', ' ') for c in r.cells)
                # deduplicate
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells.append(ct)
                        last = ct
                print(f"  R{r_idx}: {' | '.join(cells)}")
        elif 'การติดตามการปฏิบัติตาม' in full or 'รายงานผลการตรวจสอบ' in full and 'น้ำหนัก' in full and len(table.rows) <= 5:
            print(f"--- Table {t_idx} ---")
            for r_idx, r in enumerate(table.rows):
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells.append(ct)
                        last = ct
                print(f"  R{r_idx}: {' | '.join(cells)}")

parse_42_from_doc('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
parse_42_from_doc('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
parse_42_from_doc('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
