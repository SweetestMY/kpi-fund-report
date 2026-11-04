import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

with open('scratch/search_52_all.txt', 'w', encoding='utf-8') as out:
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if '5.2' in t:
            out.write(f"P{i}: {t}\n")
    for i, tbl in enumerate(doc.tables):
        for r_idx, r in enumerate(tbl.rows):
            for c_idx, c in enumerate(r.cells):
                txt = c.text.strip()
                if '5.2' in txt:
                    out.write(f"T{i} R{r_idx} C{c_idx}: {txt[:100]}\n")

print("Done")
