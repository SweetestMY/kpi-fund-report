import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'ตัวชี้วัดที่ 1.1.html',
    'ตัวชี้วัดที่ 1.2.1.html',
    'ตัวชี้วัดที่ 1.2.2.html',
    'ตัวชี้วัดที่ 2.1.html',
    'ตัวชี้วัดที่ 2.2.html',
    'ตัวชี้วัดที่ 3.1.html',
    'ตัวชี้วัดที่ 3.2.html',
    'ตัวชี้วัดที่ 3.3.html',
    'ตัวชี้วัดที่ 4.1.html'
]

for fname in files:
    if not os.path.exists(fname):
        print("Missing file:", fname)
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    has_switcher = 'id="select-kpi-page"' in content
    has_routes = 'routes' in content and 'ตัวชี้วัดที่ 3.3.html' in content
    print(fname, "has_switcher:", has_switcher, "has_routes:", has_routes)
