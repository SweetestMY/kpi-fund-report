# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if any(k in line for k in ['5.000', 'ระดับ 5', '5.00', 'บรรลุครบ 5']):
        print(f"L{idx+1}: {line.strip()}")
