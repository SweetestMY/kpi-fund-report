# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1120, 1200):
    print(f"L{i+1}: {lines[i]}", end='')
