import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def print_clean(doc_path, label, indices):
    print(f"\n=================== {label} ===================")
    doc = docx.Document(doc_path)
    for idx in indices:
        if idx < len(doc.tables):
            t = doc.tables[idx]
            print(f"\n--- TABLE {idx} ---")
            for r in t.rows:
                # get unique cells
                cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip().replace('\n', ' ')
                    if ct != last and ct:
                        cells.append(ct)
                        last = ct
                if cells:
                    print(" | ".join(cells))

print_clean('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2', [30, 32, 33, 34])
print_clean('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3', [32, 34, 35, 36])
