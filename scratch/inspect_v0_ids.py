# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
v0_m = re.search(r'<div class="topic-view active-view" id="view-topic-0">[\s\S]*?(?=<div class="topic-view" id="view-topic-1")', text)
if v0_m:
    v0_html = v0_m.group(0)
    ids = re.findall(r'id=["\']([^"\']+)["\']', v0_html)
    print("Found IDs in View 0:", ids)
    # print all rows of the table in View 0
    t_m = re.search(r'<table class="summary-table">[\s\S]*?</table>', v0_html)
    if t_m:
        print("\nTable in View 0:\n", t_m.group(0))
