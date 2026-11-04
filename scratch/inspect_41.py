# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find tabs / views / pages
views = re.findall(r'id=["\'](view-[^"\']+|tab-[^"\']+|page-[^"\']+|section-[^"\']+)["\']', text)
print("Views/Tabs found:", set(views))

# Search for the table in the overview
table_match = re.search(r'(<table[^>]*>.*?</table>)', text, re.DOTALL)
if table_match:
    print("First table preview (first 500 chars):")
    print(table_match.group(1)[:500])

# Search for the quote box
for line in text.splitlines():
    if any(k in line for k in ['กำหนดปัจจัยเสี่ยง 8 ปัจจัย', 'ระดับสูงสุด', 'คำแนะนำ:', 'สารสนเทศและการสื่อสาร']):
        print("MATCH:", line.strip()[:100])
