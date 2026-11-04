# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for i in range(7):
    m = re.search(r'<div class="topic-view" id="view-topic-' + str(i) + r'"[\s\S]*?(?=<div class="topic-view" id="view-topic-' + str(i+1) + r'"|<!-- FOOTER BAR -->)', text)
    if m:
        snippet = m.group(0)
        print(f"=== VIEW {i} (len {len(snippet)}) ===")
        # Print first 200 chars and search for headers
        lines = [line.strip() for line in snippet.split('\n') if 'class="panel-title-line"' in line or 'rstep-desc' in line or '5 ขั้นตอน' in line or 'ขั้นตอนที่' in line or 'Milestone' in line or 'ประเด็นที่' in line]
        for l in lines[:10]:
            print("  ", l[:120])
    else:
        print(f"=== VIEW {i} NOT FOUND ===")
