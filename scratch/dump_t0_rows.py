import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
t0 = doc.tables[0]
with open('scratch/t0_all_rows.txt', 'w', encoding='utf-8') as out:
    for r_idx, row in enumerate(t0.rows):
        txt = [c.text.replace('\n', ' ').strip() for c in row.cells]
        # remove consecutive duplicate texts from merged cells
        compact = []
        for cell in txt:
            if not compact or cell != compact[-1]:
                compact.append(cell)
        out.write(f"R{r_idx}: {' | '.join(compact)}\n")

print("Done writing to scratch/t0_all_rows.txt")
