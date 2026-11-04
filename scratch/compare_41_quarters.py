# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

docs = {
    'Q2': 'ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx',
    'Q3': 'ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx',
    'Q4': 'ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx'
}

topics = [
    ("ข้อ 1: ข้อร้องเรียน", "ข้อร้องเรียน"),
    ("ข้อ 2: คู่มือความเสี่ยง", "คู่มือ"),
    ("ข้อ 3: ระบุความเสี่ยง", "การระบุความเสี่ยง"),
    ("ข้อ 4: กิจกรรมควบคุม", "กิจกรรมควบคุม"),
    ("ข้อ 5.1: สารสนเทศติดตาม", "การใช้สารสนเทศ"),
    ("ข้อ 5.2: ทบทวนแผน", "การทบทวน"),
    ("ข้อ 6.1: ประเมินการควบคุม", "การประเมินผล  การควบคุม"),
    ("ข้อ 6.2: ส่งรายงาน", "การส่งรายงาน"),
]

for q_name, path in docs.items():
    print(f"\n==================== {q_name} ====================")
    d = docx.Document(path)
    for t in d.tables:
        full_text = '\n'.join([c.text.strip() for row in t.rows for c in row.cells if c.text.strip()])
        if 'ประเด็นย่อย' in full_text and 'ระดับคะแนน' in full_text:
            for r_idx in range(2, len(t.rows)):
                r_text = ' '.join([c.text.strip() for c in t.rows[r_idx].cells])
                for t_label, t_kw in topics:
                    if t_kw in r_text:
                        weight = t.rows[r_idx].cells[1].text.strip()
                        score = t.rows[r_idx].cells[-1].text.strip()
                        print(f"  {t_label} (น้ำหนัก {weight}%): ผลการดำเนินงาน = '{score}'")
