import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def analyze_kpi42_quarters():
    docs = [
        ('Q2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
        ('Q3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
        ('Q4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx'),
    ]
    
    for label, path in docs:
        print(f"\n=================== {label} ===================")
        doc = docx.Document(path)
        for t_idx, t in enumerate(doc.tables):
            full = " ".join(c.text.strip() for r in t.rows for c in r.cells)
            for sub_name in ['1. การปฏิบัติงาน ตรวจสอบภายใน', '1. การปฏิบัติงาน\nตรวจสอบภายใน', '2. การประชุม ปิดการตรวจสอบ', '2. การประชุม\nปิดการตรวจสอบ', '3. การปฏิบัติงาน ตามข้อเสนอแนะ', '3. การปฏิบัติงาน\nตามข้อเสนอแนะ']:
                if sub_name in full and 'น้ำหนัก' in full:
                    last_row = t.rows[-1]
                    cells = [c.text.strip().replace('\n', ' ') for c in last_row.cells]
                    # unique cells
                    u = []
                    for c in cells:
                        if not u or u[-1] != c:
                            u.append(c)
                    print(f"Table {t_idx}: {u[0]} | Weight: {u[1]} | Result: {u[-1]}")

analyze_kpi42_quarters()
