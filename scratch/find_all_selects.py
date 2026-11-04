import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

import re
selects = re.findall(r'<select[^>]*>.*?</select>', text, re.DOTALL)
for s in selects:
    print(s[:300])
    print("---")
