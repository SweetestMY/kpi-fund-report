# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'function\s+changeQuarter[\s\S]*?(?=function\s+[a-zA-Z0-9_]+|\</script\>)', text)
for m in matches:
    print("=== changeQuarter ===")
    print(m[:1200])

# Also check for any QUARTER data objects
q_obj = re.search(r'const\s+(?:quarterData|QUARTER_DATA|QUARTERS)[\s\S]*?;', text)
if q_obj:
    print("=== QUARTER DATA OBJECT ===")
    print(q_obj.group(0)[:1200])
else:
    print("No QUARTER_DATA object found, looking for quarterly logic...")
