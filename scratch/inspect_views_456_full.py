# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for v in [4, 5, 6]:
    needle = f'id="view-topic-{v}"'
    p = text.find(needle)
    p_end = text.find('id="view-topic-' + str(v+1) + '"') if v < 6 else text.find('<!-- FOOTER BAR -->')
    print(f"\n==================== VIEW {v} MARKUP ====================")
    print(text[p:p_end])
