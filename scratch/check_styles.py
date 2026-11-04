# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
styles = re.findall(r'\.([a-zA-Z0-9_-]+)\s*\{([^}]+)\}', text)
for name, body in styles:
    if any(k in name for k in ['rubric', 'rstep', 'flow', 'sub', 'score', 'badge', 'panel', 'step']):
        print(f".{name}: {body[:100]}...")
