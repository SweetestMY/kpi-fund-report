import io, sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc3 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx')
print("Q3 tables after 60:")
for idx in range(60, len(doc3.tables)):
    txt = "".join(c.text for r in doc3.tables[idx].rows for c in r.cells)
    print(f"Table {idx}: length {len(txt)} | preview: {txt[:120]}")

doc2 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx')
print("\nQ2 tables after 60:")
for idx in range(60, len(doc2.tables)):
    txt = "".join(c.text for r in doc2.tables[idx].rows for c in r.cells)
    print(f"Table {idx}: length {len(txt)} | preview: {txt[:120]}")
