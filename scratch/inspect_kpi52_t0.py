import docx

def check_kpi52_in_doc(doc_path, label):
    try:
        doc = docx.Document(doc_path)
        print(f"\n=== {label}: {doc_path} ===")
        t0 = doc.tables[0]
        for r_idx, row in enumerate(t0.rows):
            txt = [c.text.replace('\n', ' ').strip() for c in row.cells]
            joined = ' | '.join(txt)
            if '5.2' in joined or 'ทรัพยากรบุคคล' in joined:
                print(f"  T0 R{r_idx}: {joined}")
    except Exception as e:
        print(f"Error {label}: {e}")

check_kpi52_in_doc('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
check_kpi52_in_doc('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
check_kpi52_in_doc('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
