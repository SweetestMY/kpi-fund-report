# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
v5_m = re.search(r'<div class="topic-view" id="view-topic-5">[\s\S]*?(?=<div class="topic-view" id="view-topic-6")', text)
if v5_m:
    print(v5_m.group(0))
