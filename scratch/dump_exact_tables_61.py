import io, sys, docx
sys.stdout.reconfigure(encoding='utf-8')

def print_table_data(doc, tbl_idx, title):
    print(f"\n================ {title} (Table {tbl_idx}) ================")
    tbl = doc.tables[tbl_idx]
    for r_idx, row in enumerate(tbl.rows):
        cells = [c.text.strip().replace('\n', ' ') for c in row.cells]
        print(f"Row {r_idx}: " + " | ".join(cells))

# Q2
doc2 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx')
print_table_data(doc2, 65, "Q2 Score Table")
print_table_data(doc2, 66, "Q2 Framework")
print_table_data(doc2, 67, "Q2 Detail")

# Q3
doc3 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx')
print_table_data(doc3, 68, "Q3 Score Table")
print_table_data(doc3, 69, "Q3 Framework")
print_table_data(doc3, 70, "Q3 Detail")

# Q4
doc4 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
print_table_data(doc4, 79, "Q4 Score Table")
print_table_data(doc4, 80, "Q4 Framework")
print_table_data(doc4, 81, "Q4 Detail")
