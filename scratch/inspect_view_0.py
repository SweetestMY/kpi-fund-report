# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<div class="topic-view active" id="view-topic-0">[\s\S]*?(?=<div class="topic-view" id="view-topic-1")', text)
if m:
    print("Found view-topic-0!")
    print(m.group(0)[:1200])
    print("...\n" + m.group(0)[-800:])
else:
    print("view-topic-0 NOT FOUND")
