import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

with open('scratch/scratch_kpi52_full_text.txt', 'w', encoding='utf-8') as f:
    f.write("=== PARAGRAPHS 550 to END ===\n")
    for i in range(550, len(doc.paragraphs)):
        f.write(f"\n--- P{i} ---\n{doc.paragraphs[i].text}\n")
    
    f.write("\n\n=== TABLES 70 to END ===\n")
    for t_idx in range(70, len(doc.tables)):
        t = doc.tables[t_idx]
        f.write(f"\n=== TABLE {t_idx} (rows={len(t.rows)}, cols={len(t.columns)}) ===\n")
        for r_idx, row in enumerate(t.rows):
            row_txt = [c.text.replace('\n', ' ').strip() for c in row.cells]
            # eliminate duplicates if merged cells
            seen = []
            for cell in row_txt:
                if not seen or cell != seen[-1]:
                    seen.append(cell)
            f.write(f"R{r_idx}: {' | '.join(seen)}\n")

print("Dumped to scratch/scratch_kpi52_full_text.txt")
