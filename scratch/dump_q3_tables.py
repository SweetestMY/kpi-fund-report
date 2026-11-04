# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

d3 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx')

print("==================== Q3 TABLES (19 to 30) ====================")
for t_idx in range(19, min(31, len(d3.tables))):
    t = d3.tables[t_idx]
    full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
    print(f"\n--- TABLE {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)}) ---")
    print(full_text[:400])
