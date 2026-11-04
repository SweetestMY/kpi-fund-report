import docx

def search_kpi52(doc_path, label):
    doc = docx.Document(doc_path)
    output_lines = [f"==================== {label}: {doc_path} ===================="]
    
    # 1. Check paragraphs
    output_lines.append("--- PARAGRAPHS ---")
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if '5.2' in t or 'ทรัพยากรบุคคล' in t:
            output_lines.append(f"P{i}: {t}")
            
    # 2. Check tables
    output_lines.append("\n--- TABLES ---")
    for i, tbl in enumerate(doc.tables):
        full_tbl_text = ""
        for row in tbl.rows:
            for cell in row.cells:
                full_tbl_text += cell.text + " "
        if '5.2' in full_tbl_text or 'ทรัพยากรบุคคล' in full_tbl_text or 'Fundamental' in full_tbl_text:
            output_lines.append(f"\nTable {i} (rows={len(tbl.rows)}, cols={len(tbl.columns)}):")
            for r_idx, row in enumerate(tbl.rows):
                row_txt = [c.text.replace('\n', ' ').strip() for c in row.cells]
                seen = []
                for cell in row_txt:
                    if not seen or cell != seen[-1]:
                        seen.append(cell)
                output_lines.append(f"  R{r_idx}: {' | '.join(seen)}")
                
    return "\n".join(output_lines)

with open('scratch/kpi52_investigation.txt', 'w', encoding='utf-8') as out:
    for p, lbl in [
        ('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
    ]:
        res = search_kpi52(p, lbl)
        out.write(res + "\n\n")

print("Done writing to scratch/kpi52_investigation.txt")
