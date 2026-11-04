# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for v_num in [4, 5, 6]:
    v_m = re.search(r'<div class="topic-view" id="view-topic-' + str(v_num) + r'">[\s\S]*?(?=<div class="topic-view"|</div>\s*<!-- FOOTER BAR -->)', text)
    if v_m:
        ids = re.findall(r'id=["\']([^"\']+)["\']', v_m.group(0))
        print(f"IDs in View {v_num}:", ids)
