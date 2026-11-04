# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.finditer(r'activeQuarter[\s\S]{0,80}', text)
for m in matches:
    print(m.group(0).replace('\n', ' '))
