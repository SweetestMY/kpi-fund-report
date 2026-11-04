import docx

def dump_kpi61(doc_path, label):
    doc = docx.Document(doc_path)
    output = [f"==================== {label}: {doc_path} ===================="]
    
    # 1. Paragraphs
    output.append("--- PARAGRAPHS ---")
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if any(w in t for w in ['ด้านที่ 6', '6.1', 'เบิกจ่ายเงินตามแผน']):
            output.append(f"P{i}: {t}")
            
    # 2. Tables
    output.append("\n--- TABLES ---")
    for i, tbl in enumerate(doc.tables):
        full_text = " ".join(c.text for r in tbl.rows for c in r.cells)
        if any(w in full_text for w in ['6.1', 'งบลงทุน', 'เบิกจ่ายภาพรวม', '279,196,000']):
            output.append(f"\nTable {i} (rows={len(tbl.rows)}, cols={len(tbl.columns)}):")
            for r_idx, row in enumerate(tbl.rows):
                cells = [c.text.replace('\n', ' ').strip() for c in row.cells]
                seen = []
                for cell in cells:
                    if not seen or cell != seen[-1]:
                        seen.append(cell)
                output.append(f"  R{r_idx}: {' | '.join(seen)}")
                
    return "\n".join(output)

with open('scratch/kpi61_investigation.txt', 'w', encoding='utf-8') as out:
    for p, lbl in [
        ('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
    ]:
        res = dump_kpi61(p, lbl)
        out.write(res + "\n\n")

print("Done writing to scratch/kpi61_investigation.txt")
