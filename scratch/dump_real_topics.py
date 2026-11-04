# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

print("=== TABLE 28 (TOPIC 4) ===")
for row in doc.tables[28].rows:
    for cell in row.cells:
        print(cell.text.strip())

print("\n=== TABLE 30 (TOPIC 5) ===")
for r_idx, row in enumerate(doc.tables[30].rows):
    print(f"--- Row {r_idx} ---")
    for cell in row.cells:
        print(cell.text.strip()[:400])

print("\n=== TABLE 32 & 34 (TOPIC 6) ===")
for r_idx, row in enumerate(doc.tables[32].rows):
    print(f"Table 32 Row {r_idx}:", [c.text.strip() for c in row.cells])
for r_idx, row in enumerate(doc.tables[34].rows):
    print(f"Table 34 Row {r_idx}:", [c.text.strip() for c in row.cells])
