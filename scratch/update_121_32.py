import sys

sys.stdout.reconfigure(encoding='utf-8')

files = ['ตัวชี้วัดที่ 1.2.1.html', 'ตัวชี้วัดที่ 3.2.html']

opt_to_find = '<option value="4.1">4.1 การบริหารความเสี่ยงฯ</option>'
opt_replace = '<option value="4.1">4.1 การบริหารความเสี่ยงฯ</option>\n                            <option value="4.2">4.2 การตรวจสอบภายใน</option>'

route_to_find = "'4.1': 'ตัวชี้วัดที่ 4.1.html'"
route_replace = "'4.1': 'ตัวชี้วัดที่ 4.1.html',\n                '4.2': 'ตัวชี้วัดที่ 4.2.html'"

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if opt_to_find in content:
        content = content.replace(opt_to_find, opt_replace)
    if route_to_find in content:
        content = content.replace(route_to_find, route_replace)
        
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fname}")
