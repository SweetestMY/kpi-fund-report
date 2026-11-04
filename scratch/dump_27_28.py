# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

for i in [27, 28]:
    t = doc.tables[i]
    full = "\n".join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
    print(f"=== TABLE {i} ===")
    print(full)
    print("---------------------------------------")
