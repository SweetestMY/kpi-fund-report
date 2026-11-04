# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find any fixed or absolute overlays, modals, backdrops
for m in re.finditer(r'(\.[^{]*?(?:modal|backdrop|overlay|mask)[^{]*\{[^}]*\})', text):
    print(m.group(0))
    print('-'*30)
