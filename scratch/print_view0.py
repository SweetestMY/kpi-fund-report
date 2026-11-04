# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'(<div[^>]*id=["\']view-topic-0["\'].*?)(?=<div[^>]*id=["\']view-topic-1|\s*</div>\s*<!-- CANVAS FOOTER|$)', text, re.DOTALL)
if m:
    print(m.group(1))
