# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find each view-topic block start and end
views = re.findall(r'(<div[^>]*id=["\']view-topic-\d+["\'][^>]*>.*?)(?=<div[^>]*id=["\']view-topic-|\s*</div>\s*<!-- CANVAS FOOTER|$)', text, re.DOTALL)
print(f"Total views found: {len(views)}")

for i, v in enumerate(views):
    v_id = re.search(r'id=["\']([^"\']+)["\']', v).group(1)
    print(f"\n--- {v_id} (Length: {len(v)} chars) ---")
    lines = v.strip().splitlines()
    print("Start:", lines[0][:100])
    for l in lines[1:25]:
        print("  ", l[:100])
    print("  ...")
    for l in lines[-10:]:
        print("  ", l[:100])
