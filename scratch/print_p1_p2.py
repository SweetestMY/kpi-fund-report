# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

p1 = text.find("const STORAGE_KEY_PREFIX = 'kpi_official_41_v3_Q';")
p2 = text.find("function resetCurrentQuarter")
print(f"p1: {p1}, p2: {p2}")
if p1 != -1 and p2 != -1:
    print(text[p1:p2])
