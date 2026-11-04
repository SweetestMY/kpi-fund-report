import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

# Check the exact structure around 5.2
with open('scratch/kpi52_structure.txt', 'w', encoding='utf-8') as out:
    for i in range(558, 581):
        out.write(f"P{i}: {doc.paragraphs[i].text}\n")
        
    out.write("\n=== TABLES 71 to 78 ===\n")
    for t_idx in range(71, 79):
        tbl = doc.tables[t_idx]
        out.write(f"\n--- TABLE {t_idx} (rows={len(tbl.rows)}, cols={len(tbl.columns)}) ---\n")
        for r_idx, row in enumerate(tbl.rows):
            cells = [c.text.replace('\n', ' ').strip() for c in row.cells]
            out.write(f"R{r_idx}: {' | '.join(cells)}\n")

print("Done")
