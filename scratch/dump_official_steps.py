# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

def dump_tables(indices):
    for i in indices:
        t = doc.tables[i]
        print(f"\n================ TABLE {i} ================")
        for r_idx, row in enumerate(t.rows):
            vals = [c.text.strip().replace('\r', '') for c in row.cells]
            seen = []
            for v in vals:
                if not seen or v != seen[-1]:
                    seen.append(v)
            print(f"--- Row {r_idx} ---")
            for item in seen:
                print(item)

print(">>> TOPIC 3 (TABLES 24, 25, 26) <<<")
dump_tables([24, 25, 26])

print("\n>>> TOPIC 4 (TABLES 27, 28) <<<")
dump_tables([27, 28])

print("\n>>> TOPIC 5 (TABLES 29, 30) <<<")
dump_tables([29, 30])

print("\n>>> TOPIC 6 (TABLES 31, 32, 33, 34) <<<")
dump_tables([31, 32, 33, 34])
