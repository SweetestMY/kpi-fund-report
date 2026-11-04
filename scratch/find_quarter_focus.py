# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = 0
while True:
    p = text.find('quarter-focus', pos)
    if p == -1: break
    print(f"quarter-focus found at {p}:")
    print(text[max(0, p-60):p+300])
    print("---------------------------------")
    pos = p + 1
