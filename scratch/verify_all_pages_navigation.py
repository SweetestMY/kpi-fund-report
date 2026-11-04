import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

all_files = sorted(glob.glob('ตัวชี้วัดที่*.html'))

print(f"Total KPI HTML files found: {len(all_files)}")
expected_keys = ['1.1', '1.2.1', '1.2.2', '2.1', '2.2', '3.1', '3.2', '3.3', '4.1', '4.2']

for f in all_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # check options
    m = re.search(r'<select[^>]*id=["\']select-kpi-page["\'][^>]*>(.*?)</select>', content, re.DOTALL)
    if not m:
        print(f"❌ {f}: Missing select-kpi-page")
        continue
    
    opts = re.findall(r'<option[^>]*value=["\']([^"\']+)["\'][^>]*>(.*?)</option>', m.group(1))
    keys = [o[0] for o in opts]
    has_all = keys == expected_keys
    
    # check routes
    m_route = re.search(r'const routes = \{(.*?)\};', content, re.DOTALL)
    routes_ok = False
    if m_route:
        route_text = m_route.group(1)
        routes_ok = all(k in route_text for k in expected_keys)
    
    print(f"File: {f:<26} | Options match: {str(has_all):<5} | Routes match: {str(routes_ok):<5}")
