import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def dump_kpi_42_full(doc_path, label):
    print(f"\n=======================================================")
    print(f"=== FULL DUMP FOR 4.2: {label} ===")
    print(f"=======================================================")
    doc = docx.Document(doc_path)
    
    # We want tables that correspond to 4.2
    # In Q4: Table 35 to 41
    # Let's detect automatically
    for t_idx, table in enumerate(doc.tables):
        full = " ".join(c.text.strip() for r in table.rows for c in r.cells)
        if ('การปฏิบัติงาน ตรวจสอบภายใน' in full or 'การประชุม ปิดการตรวจสอบ' in full or 'การปฏิบัติงาน ตามข้อเสนอแนะ' in full or 
            'แต่งตั้งผู้ตรวจสอบภายในของสำนักงาน ก.ค.ศ.' in full or 'รายงานการเงินของเงินทุนหมุนเวียน' in full) and not ('4.1' in full or '4.3' in full or 'สารสนเทศและดิจิทัล' in full):
            print(f"\n--- [Table {t_idx}] (rows={len(table.rows)}, cols={len(table.columns)}) ---")
            for r_idx, r in enumerate(table.rows):
                unique_cells = []
                last = None
                for c in r.cells:
                    ct = c.text.strip()
                    if ct != last and ct:
                        unique_cells.append(ct)
                        last = ct
                if len(unique_cells) > 1:
                    print(f"  R{r_idx}: " + " | ".join(c.replace('\n', ' ') for c in unique_cells))
                elif len(unique_cells) == 1:
                    print(f"  R{r_idx} TEXT:\n{unique_cells[0]}")

dump_kpi_42_full('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
dump_kpi_42_full('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
dump_kpi_42_full('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
