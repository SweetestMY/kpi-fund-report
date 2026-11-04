import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
t = doc.tables[77]
print(f"Table 77 rows: {len(t.rows)}, cols: {len(t.columns)}")
for r_idx, r in enumerate(t.rows):
    for c_idx, c in enumerate(r.cells):
        safe = c.text.replace('\n', ' ').strip()
        safe = safe.encode('ascii', 'backslashreplace').decode('ascii')
        print(f"R{r_idx} C{c_idx}: {safe}")
