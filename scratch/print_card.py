# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1250, min(1390, len(lines))):
    print(f"L{i+1}: {lines[i]}", end='')
