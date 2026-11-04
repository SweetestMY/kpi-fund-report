# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'(<div class="topic-view" id="view-topic-6">.*?</div>\s*</div>\s*</div>)', text, re.DOTALL)
if m:
    print("Found v6, length:", len(m.group(0)))
    idx = m.end()
    print("Next 200 chars after v6:")
    print(repr(text[idx:idx+200]))
