# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

for fn in ['ตัวชี้วัดที่ 1.1.html', 'ตัวชี้วัดที่ 3.1.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    p = c.find('function switchQuarter')
    if p != -1:
        print(f"=== {fn} ===")
        print(c[p:p+1200])
