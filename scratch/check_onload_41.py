# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'window\.onload\s*=\s*function\(\)\s*\{.*?\n        \};', text, re.DOTALL)
if m:
    print(m.group(0))
