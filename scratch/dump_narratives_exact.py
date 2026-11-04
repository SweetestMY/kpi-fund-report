import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def print_tables_text(doc_path, label, indices):
    print(f"\n=================== {label} ===================")
    doc = docx.Document(doc_path)
    for idx in indices:
        if idx < len(doc.tables):
            t = doc.tables[idx]
            print(f"\n--- TABLE {idx} ---")
            for r in t.rows:
                for c in r.cells:
                    ct = c.text.strip()
                    if ct:
                        print(ct)

print_tables_text('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2', [29, 30, 31, 32, 33, 34])
print_tables_text('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3', [31, 32, 33, 34, 35, 36])
print_tables_text('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4', [35, 36, 37, 38, 39, 40, 41])
