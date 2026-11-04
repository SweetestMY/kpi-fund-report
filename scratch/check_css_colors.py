# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find CSS for big-score-box and overview-kpi-table
for m in re.finditer(r'(\.big-score-box|\.overview-kpi-table)[^{]*\{([^}]*)\}', text):
    print(m.group(1))
    print(m.group(2))
    print('-'*40)
