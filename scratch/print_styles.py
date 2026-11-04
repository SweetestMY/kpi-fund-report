# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.score-box-na[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)

matches2 = re.findall(r'(\.rating-badge-card-na[^{]*\{[^}]*\})', text)
for m in matches2:
    print(m)
