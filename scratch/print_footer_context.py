# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'สำนักงานคณะกรรมการข้าราชการครู' in line:
        for j in range(max(0, idx - 15), min(len(lines), idx + 10)):
            print(f"L{j+1}: {lines[j]}", end='')
        break
