# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for v in [1, 2]:
    m = re.search(r'<div class="topic-view" id="view-topic-' + str(v) + r'"[\s\S]*?(?=<div class="topic-view" id="view-topic-' + str(v+1) + r'")', text)
    if m:
        print(f"==================== VIEW {v} ====================")
        # print first 1500 chars
        print(m.group(0)[:1500])
        print("...\n" + m.group(0)[-800:])
