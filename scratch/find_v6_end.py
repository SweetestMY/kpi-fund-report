# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'<div class="topic-view" id="view-topic-6">.*', text, re.DOTALL)
if m:
    print(m.group(0)[:800])
    print("\n--- End of file or canvas ---")
    print(m.group(0)[-500:])
