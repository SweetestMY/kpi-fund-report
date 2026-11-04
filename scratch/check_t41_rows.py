import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
t = doc.tables[41]
print(f"Table 41 rows: {len(t.rows)}")
for i, r in enumerate(t.rows):
    print(f"--- Row {i} ---")
    for c in r.cells:
        print(c.text.strip())
