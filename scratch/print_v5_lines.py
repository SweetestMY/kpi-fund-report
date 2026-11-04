# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'id="view-topic-5"' in line:
        start = idx
        for j in range(start, min(start + 85, len(lines))):
            print(f"L{j+1}: {lines[j]}", end='')
        break
