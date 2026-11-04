# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for line in text.splitlines():
    if any(k in line for k in ['canvas-footer', 'view-topic-6', 'สำนักงานคณะกรรมการข้าราชการครู']):
        print(line[:100])
