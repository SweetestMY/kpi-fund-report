import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function navigateToKPI.*?\n    \}', text, re.DOTALL)
if m:
    print(m.group(0))
