import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

import re
select_kpi = re.search(r'<select id="select-kpi-page".*?</select>', text, re.DOTALL)
if select_kpi:
    print(select_kpi.group(0))

nav_fn = re.search(r'function navigateToKPI.*?\n    }', text, re.DOTALL)
if nav_fn:
    print("\n" + nav_fn.group(0))
