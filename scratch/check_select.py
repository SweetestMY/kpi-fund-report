import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

import re
select_match = re.search(r'<select[^>]*id=["\']kpiSelect["\'][^>]*>(.*?)</select>', text, re.DOTALL)
if select_match:
    print(select_match.group(1))
