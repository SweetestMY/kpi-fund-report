# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

d = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx')

for j in range(130, 220):
    t = d.paragraphs[j].text.strip()
    if t:
        print(f"[{j}] {t}")
