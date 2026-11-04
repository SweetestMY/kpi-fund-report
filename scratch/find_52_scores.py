import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

# Search all paragraphs and tables for 5.2 scores
with open('scratch/kpi52_search_scores.txt', 'w', encoding='utf-8') as out:
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if any(w in t for w in ['5.2', 'ทรัพยากรบุคคล', 'Fundamental', 'คะแนนถ่วงน้ำหนัก']):
            out.write(f"P{i}: {t}\n")
            
    for i, tbl in enumerate(doc.tables):
        full = ""
        for row in tbl.rows:
            for cell in row.cells:
                full += cell.text + " "
        if '5.2' in full or 'ทรัพยากรบุคคล' in full:
            out.write(f"\n--- TABLE {i} ---\n")
            for r in tbl.rows:
                row_txt = [c.text.replace('\n', ' ').strip() for c in r.cells]
                out.write(" | ".join(row_txt) + "\n")

print("Done")
