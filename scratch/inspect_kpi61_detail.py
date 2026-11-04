import docx

def find_kpi61_tables(doc_path, label):
    doc = docx.Document(doc_path)
    output = [f"=== {label}: {doc_path} ==="]
    for i, p in enumerate(doc.paragraphs):
        if '6.1' in p.text:
            output.append(f"P{i}: {p.text.strip()}")
    for i, tbl in enumerate(doc.tables):
        txt = " ".join(c.text for r in tbl.rows for c in r.cells)
        if 'งบลงทุน' in txt and 'มติ ครม.' in txt:
            output.append(f"\n--- TABLE {i} ---")
            for r in tbl.rows:
                cells = [c.text.replace('\n', ' ').strip() for c in r.cells]
                seen = []
                for c in cells:
                    if not seen or c != seen[-1]:
                        seen.append(c)
                output.append(" | ".join(seen))
        elif 'การเบิกจ่ายงบประมาณ' in txt and '279,196,000' in txt:
            output.append(f"\n--- TABLE {i} (Details) ---")
            for r in tbl.rows:
                cells = [c.text.replace('\n', ' ').strip() for c in r.cells]
                output.append(" | ".join(cells[:2]))
    return "\n".join(output)

with open('scratch/kpi61_q3_q2.txt', 'w', encoding='utf-8') as out:
    for p, lbl in [
        ('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
    ]:
        out.write(find_kpi61_tables(p, lbl) + "\n\n")

print("Done")
