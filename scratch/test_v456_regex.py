# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# View 4
v4_m = re.search(r'<div class="topic-view" id="view-topic-4">[\s\S]*?(?=<div class="topic-view" id="view-topic-5")', text)
if v4_m:
    print("Found View 4, length:", len(v4_m.group(0)))

# View 5
v5_m = re.search(r'<div class="topic-view" id="view-topic-5">[\s\S]*?(?=<div class="topic-view" id="view-topic-6")', text)
if v5_m:
    print("Found View 5, length:", len(v5_m.group(0)))

# View 6
v6_m = re.search(r'<div class="topic-view" id="view-topic-6">[\s\S]*?(?=</div>\s*<!-- FOOTER BAR -->)', text)
if v6_m:
    print("Found View 6, length:", len(v6_m.group(0)))
