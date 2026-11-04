import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
with open('scratch/t80_t81_full.txt', 'w', encoding='utf-8') as out:
    for t_idx in [79, 80, 81]:
        t = doc.tables[t_idx]
        out.write(f"\n=== TABLE {t_idx} ===\n")
        for r in t.rows:
            row_txt = [c.text.strip() for c in r.cells]
            out.write(" | ".join(row_txt) + "\n")

print("Done")
