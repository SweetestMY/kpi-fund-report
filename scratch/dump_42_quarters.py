import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def check_q_details(doc_path, label):
    print(f"\n=================== {label}: {doc_path} ===================")
    doc = docx.Document(doc_path)
    # Check overview table for 4.2
    for t_idx, table in enumerate(doc.tables):
        for r in table.rows:
            r_str = " | ".join(c.text.strip().replace('\n', ' ') for c in r.cells)
            if '4.2' in r_str and 'ตรวจสอบภายใน' in r_str:
                print(f"Table {t_idx} row: {r_str}")
    
    # Check specific 4.2 tables
    for t_idx, table in enumerate(doc.tables):
        full = " ".join(c.text.strip() for r in table.rows for c in r.cells)
        if 'การปฏิบัติงาน ตรวจสอบภายใน' in full and 'น้ำหนัก' in full:
            print(f"--- 4.2 Criteria Table {t_idx} ---")
            for r in table.rows:
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells.append(ct)
                        last = ct
                print(" | ".join(cells))
        elif 'การประชุม ปิดการตรวจสอบ' in full and 'น้ำหนัก' in full:
            print(f"--- 4.2 Sub2 Table {t_idx} ---")
            for r in table.rows:
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells.append(ct)
                        last = ct
                print(" | ".join(cells))
        elif 'การปฏิบัติงาน ตามข้อเสนอแนะ' in full and 'น้ำหนัก' in full:
            print(f"--- 4.2 Sub3 Table {t_idx} ---")
            for r in table.rows:
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last:
                        cells.append(ct)
                        last = ct
                print(" | ".join(cells))

check_q_details('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
check_q_details('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
check_q_details('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
