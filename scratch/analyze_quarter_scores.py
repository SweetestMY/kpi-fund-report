# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

def analyze_quarters():
    docs = [
        ('ไตรมาส 2', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
        ('ไตรมาส 3', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
        ('ไตรมาส 4', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
    ]
    
    for q_label, path in docs:
        print(f"\n=======================================================")
        print(f"            {q_label} ({path})")
        print(f"=======================================================")
        d = docx.Document(path)
        for t_idx, t in enumerate(d.tables):
            full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
            if 'ประเด็นย่อย' in full_text and ('น้ำหนัก' in full_text or 'ระดับคะแนน' in full_text):
                # This is an evaluation table!
                header_row = [c.text.strip().replace('\n', ' ') for c in t.rows[0].cells]
                last_col_header = header_row[-1] if header_row else ''
                print(f"\nTable {t_idx} (Cols: {len(t.columns)}) - Header: {last_col_header}")
                for r_idx in range(2, len(t.rows)):
                    row_cells = [c.text.strip().replace('\n', ' ') for c in t.rows[r_idx].cells]
                    topic_name = row_cells[0] if len(row_cells) > 0 else ''
                    weight = row_cells[1] if len(row_cells) > 1 else ''
                    score = row_cells[-1] if len(row_cells) > 0 else ''
                    print(f"  Row {r_idx}: Topic='{topic_name[:40]}' | Weight={weight} | Score={score}")

analyze_quarters()
