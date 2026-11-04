import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def find_42_in_master_table(doc_path, label):
    print(f"\n=== {label}: {doc_path} ===")
    doc = docx.Document(doc_path)
    for t_idx, table in enumerate(doc.tables):
        for r_idx, row in enumerate(table.rows):
            r_text = " | ".join(c.text.strip().replace('\n', ' ') for c in row.cells)
            if '4.2' in r_text and ('ตรวจสอบภายใน' in r_text or 'การตรวจสอบ' in r_text):
                print(f"Table {t_idx} R{r_idx}: {r_text}")

find_42_in_master_table('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
find_42_in_master_table('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
find_42_in_master_table('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
