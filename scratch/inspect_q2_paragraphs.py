# -*- coding: utf-8 -*-
import sys, docx
sys.stdout.reconfigure(encoding='utf-8')

d = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx')

for i, p in enumerate(d.paragraphs):
    if '4.1' in p.text:
        print(f"P {i}: {p.text}")
        for j in range(max(0, i-2), min(len(d.paragraphs), i+15)):
            print(f"   [{j}] {d.paragraphs[j].text[:120]}")
        print("---------------------------------------")
