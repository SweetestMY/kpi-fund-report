# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'// Auto-purge[\s\S]*?(?=function|const)', text)
if m:
    print("Found purge code:", m.group(0))
else:
    print("No purge code found")
