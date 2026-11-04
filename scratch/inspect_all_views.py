# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for i in range(1, 7):
    m = re.search(rf'(<div[^>]*id=["\']view-topic-{i}["\'].*?)(?=<div[^>]*id=["\']view-topic-|\s*</div>\s*<!-- CANVAS FOOTER|$)', text, re.DOTALL)
    if m:
        content = m.group(1)
        print(f"\n================ VIEW TOPIC {i} ================")
        # list children inside panel-box
        panel = re.search(r'<div class="panel-box">(.*)</div>\s*</div>', content, re.DOTALL)
        if panel:
            lines = [l.strip() for l in panel.group(1).splitlines() if l.strip()]
            for l in lines[:15]:
                print("  ", l[:100])
