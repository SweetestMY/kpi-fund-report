import docx

with open('scratch/kpi52_t0_output.txt', 'w', encoding='utf-8') as out:
    for doc_path, label in [
        ('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3'),
        ('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
    ]:
        try:
            doc = docx.Document(doc_path)
            out.write(f"\n=== {label}: {doc_path} ===\n")
            t0 = doc.tables[0]
            for r_idx, row in enumerate(t0.rows):
                txt = [c.text.replace('\n', ' ').strip() for c in row.cells]
                joined = ' | '.join(txt)
                if '5.2' in joined or 'ทรัพยากรบุคคล' in joined:
                    out.write(f"  T0 R{r_idx}: {joined}\n")
        except Exception as e:
            out.write(f"Error {label}: {e}\n")

print("Done writing to scratch/kpi52_t0_output.txt")
