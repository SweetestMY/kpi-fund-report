import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def find_kpi_summary_table(doc_path, label):
    print(f"\n=================== {label} ===================")
    doc = docx.Document(doc_path)
    for t_idx, t in enumerate(doc.tables):
        full = " ".join(c.text.strip() for r in t.rows for c in r.cells)
        if 'ผลการดำเนินงาน' in full and 'น้ำหนัก' in full and ('4.1' in full or '4.2' in full):
            # check if it has multiple KPIs (like 1.1, 1.2, etc.)
            if '1.1' in full and '2.1' in full:
                print(f"Master Summary Table found at Table {t_idx} (rows: {len(t.rows)})")
                for r_idx, r in enumerate(t.rows):
                    row_str = " | ".join(c.text.strip().replace('\n', ' ') for c in r.cells)
                    if '4.2' in row_str or '4.1' in row_str or '4.3' in row_str:
                        print(f"  R{r_idx}: {row_str}")

find_kpi_summary_table('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
find_kpi_summary_table('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
find_kpi_summary_table('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
