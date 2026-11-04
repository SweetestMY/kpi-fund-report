import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 1.1.html', encoding='utf-8') as f:
    text = f.read()

import re
m_opt = re.search(r'<select[^>]*id=["\']select-kpi-page["\'][^>]*>(.*?)</select>', text, re.DOTALL)
if m_opt:
    print("=== 1.1 SELECT OPTIONS ===")
    print(m_opt.group(0))

m_routes = re.search(r'function navigateToKPI.*?\n    \}', text, re.DOTALL)
if m_routes:
    print("\n=== 1.1 ROUTES ===")
    print(m_routes.group(0))
