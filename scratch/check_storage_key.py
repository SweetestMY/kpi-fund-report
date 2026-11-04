# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'STORAGE_KEY[A-Za-z0-9_]*\s*=\s*[\'"][^\'"]+[\'"]', text):
    print(m.group(0))
