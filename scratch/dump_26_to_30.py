# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

def print_table_text(idx):
    t = doc.tables[idx]
    full = "\n".join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
    print(f"=== TABLE {idx} ===")
    print(full)
    print("---------------------------------------")

for i in [26, 27, 28, 29, 30]:
    print_table_text(i)
