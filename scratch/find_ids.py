# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.findall(r'id=["\']view-topic-\d+["\']', text)
print("Found view IDs:", m)

# Let's search around view-topic-0
idx = text.find('view-topic-0')
if idx != -1:
    print("Found around view-topic-0:")
    print(text[max(0, idx-50):idx+250])
