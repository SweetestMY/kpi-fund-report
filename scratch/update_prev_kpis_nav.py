import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [
    'ตัวชี้วัดที่ 1.1.html',
    'ตัวชี้วัดที่ 1.2.1.html',
    'ตัวชี้วัดที่ 1.2.2.html',
    'ตัวชี้วัดที่ 2.1.html',
    'ตัวชี้วัดที่ 2.2.html',
    'ตัวชี้วัดที่ 3.1.html',
    'ตัวชี้วัดที่ 3.2.html',
    'ตัวชี้วัดที่ 3.3.html'
]

opt_to_find = '<option value="4.1">4.1 การบริหารความเสี่ยงฯ</option>'
opt_replace = '<option value="4.1">4.1 การบริหารความเสี่ยงฯ</option>\n                            <option value="4.2">4.2 การตรวจสอบภายใน</option>'

route_to_find = "'4.1': 'ตัวชี้วัดที่ 4.1.html'"
route_replace = "'4.1': 'ตัวชี้วัดที่ 4.1.html',\n                '4.2': 'ตัวชี้วัดที่ 4.2.html'"

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if '4.2' not in content:
        if opt_to_find in content:
            content = content.replace(opt_to_find, opt_replace)
            modified = True
        elif '<option value="4.1" selected>4.1 การบริหารความเสี่ยงฯ (ปัจจุบัน)</option>' in content:
            content = content.replace(
                '<option value="4.1" selected>4.1 การบริหารความเสี่ยงฯ (ปัจจุบัน)</option>',
                '<option value="4.1" selected>4.1 การบริหารความเสี่ยงฯ (ปัจจุบัน)</option>\n                            <option value="4.2">4.2 การตรวจสอบภายใน</option>'
            )
            modified = True
            
        if route_to_find in content:
            content = content.replace(route_to_find, route_replace)
            modified = True
            
        if modified:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {fname} with 4.2 navigation")
        else:
            print(f"Failed to find patterns in {fname}")
    else:
        print(f"{fname} already has 4.2")
