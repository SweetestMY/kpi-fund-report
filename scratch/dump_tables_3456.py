# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

tables_to_dump = [
    (24, "ข้อ 3: เกณฑ์ประเมิน"),
    (25, "ข้อ 3: ผลการดำเนินงาน ตอนที่ 1"),
    (26, "ข้อ 3: ผลการดำเนินงาน ตอนที่ 2"),
    (27, "ข้อ 4: เกณฑ์ประเมิน"),
    (28, "ข้อ 4: ผลการดำเนินงาน"),
    (29, "ข้อ 5: เกณฑ์ประเมิน"),
    (30, "ข้อ 5: ผลการดำเนินงาน"),
    (31, "ข้อ 6.1: เกณฑ์ประเมิน"),
    (32, "ข้อ 6.1: ผลการดำเนินงาน"),
    (33, "ข้อ 6.2: เกณฑ์ประเมิน"),
    (34, "ข้อ 6.2: ผลการดำเนินงาน"),
]

for idx, label in tables_to_dump:
    print(f"==================== TABLE {idx}: {label} ====================")
    t = doc.tables[idx]
    for r_i, row in enumerate(t.rows):
        cells = [c.text.strip() for c in row.cells]
        print(f"Row {r_i}: {' | '.join(cells)}")
