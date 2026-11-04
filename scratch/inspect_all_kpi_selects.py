import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('ตัวชี้วัดที่*.html')):
    with open(f, encoding='utf-8') as file:
        content = file.read()
    m = re.search(r'<select[^>]*id=["\'](?:select-kpi-page|kpiSelect)["\'][^>]*>(.*?)</select>', content, re.DOTALL)
    if m:
        options = re.findall(r'<option[^>]*value=["\']([^"\']+)["\'][^>]*>(.*?)</option>', m.group(1))
        vals = [opt[0] for opt in options]
        print(f"{f}: options = {vals}")
    else:
        print(f"{f}: NO KPI SELECT FOUND!")
