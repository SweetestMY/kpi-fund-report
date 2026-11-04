# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'// LocalStorage Key[\s\S]*?(?=function renderRubric|function changeQuarter)', text)
if m:
    print(m.group(0))
