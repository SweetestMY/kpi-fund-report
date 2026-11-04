# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

docs = [
    ('Q2_DOC', 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx'),
    ('Q3_DOC', 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx'),
    ('Q4_DOC', 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx'),
]

for doc_label, doc_path in docs:
    print(f"\n=======================================================")
    print(f"SEARCHING IN {doc_label}: {doc_path}")
    print(f"=======================================================")
    d = docx.Document(doc_path)
    for p_idx, p in enumerate(d.paragraphs):
        t = p.text.strip()
        if ('4.1' in t or 'การบริหารความเสี่ยง' in t) and ('ไตรมาส' in t or 'Q1' in t):
            print(f"P {p_idx}: {t[:160]}")
    for t_idx, t in enumerate(d.tables):
        full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
        if ('4.1' in full_text or 'การบริหารความเสี่ยง' in full_text or 'ข้อร้องเรียน' in full_text) and 'ไตรมาสที่ 1' in full_text:
            print(f"\nTable {t_idx} mentions 'ไตรมาสที่ 1':")
            for r in t.rows[:6]:
                r_txt = ' | '.join([c.text.strip().replace('\n', ' ') for c in r.cells])
                print("  " + r_txt[:140])
