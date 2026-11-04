# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

d2 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx')

print("==================== Q2 TABLES (15 to 28) ====================")
for t_idx in range(15, min(29, len(d2.tables))):
    t = d2.tables[t_idx]
    full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
    print(f"\n--- TABLE {t_idx} (rows: {len(t.rows)}, cols: {len(t.columns)}) ---")
    print(full_text[:400])
