import io, sys, docx
sys.stdout.reconfigure(encoding='utf-8')

# Q3
doc3 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx')
print("=== Q3 6.1 PARAGRAPHS & TABLES ===")
for idx, p in enumerate(doc3.paragraphs):
    if '6.1' in p.text:
        print(f"P {idx}: {p.text}")
        for j in range(idx, min(idx+35, len(doc3.paragraphs))):
            if doc3.paragraphs[j].text.strip():
                print(f"   p{j}: {doc3.paragraphs[j].text[:120]}")
        break

for idx, tbl in enumerate(doc3.tables):
    txt = "".join(cell.text for row in tbl.rows for cell in row.cells)
    if '6.1' in txt or 'การเบิกจ่ายเงินตามแผน' in txt:
        print(f"Q3 Table {idx}: {txt[:200]}")

# Q2
doc2 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx')
print("\n=== Q2 6.1 PARAGRAPHS & TABLES ===")
for idx, p in enumerate(doc2.paragraphs):
    if '6.1' in p.text:
        print(f"P {idx}: {p.text}")
        for j in range(idx, min(idx+35, len(doc2.paragraphs))):
            if doc2.paragraphs[j].text.strip():
                print(f"   p{j}: {doc2.paragraphs[j].text[:120]}")
        break

for idx, tbl in enumerate(doc2.tables):
    txt = "".join(cell.text for row in tbl.rows for cell in row.cells)
    if '6.1' in txt or 'การเบิกจ่ายเงินตามแผน' in txt:
        print(f"Q2 Table {idx}: {txt[:200]}")
