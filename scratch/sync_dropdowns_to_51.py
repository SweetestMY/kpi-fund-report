# -*- coding: utf-8 -*-
import os, re, glob

kpi_list = [
    ('1.1', '1.1 ร้อยละการรับชำระหนี้', 'ตัวชี้วัดที่ 1.1.html'),
    ('1.2.1', '1.2.1 หนี้ไม่เกิน 1 ปี', 'ตัวชี้วัดที่ 1.2.1.html'),
    ('1.2.2', '1.2.2 หนี้เกิน 1 ปี', 'ตัวชี้วัดที่ 1.2.2.html'),
    ('2.1', '2.1 ร้อยละความพึงพอใจฯ', 'ตัวชี้วัดที่ 2.1.html'),
    ('2.2', '2.2 ความสำเร็จโครงการเสริมสร้างวินัยฯ', 'ตัวชี้วัดที่ 2.2.html'),
    ('3.1', '3.1 ร้อยละเงินอนุมัติให้กู้ยืม', 'ตัวชี้วัดที่ 3.1.html'),
    ('3.2', '3.2 ความสำเร็จการแก้ไขปัญหาหนี้สินฯ', 'ตัวชี้วัดที่ 3.2.html'),
    ('3.3', '3.3 การจัดเก็บข้อมูลประเมินผลลัพธ์ปี 2570', 'ตัวชี้วัดที่ 3.3.html'),
    ('4.1', '4.1 การบริหารความเสี่ยงฯ', 'ตัวชี้วัดที่ 4.1.html'),
    ('4.2', '4.2 การตรวจสอบภายใน', 'ตัวชี้วัดที่ 4.2.html'),
    ('4.3', '4.3 การบริหารจัดการสารสนเทศและดิจิทัล', 'ตัวชี้วัดที่ 4.3.html'),
    ('5.1', '5.1 บทบาทคณะกรรมการบริหารทุนหมุนเวียน', 'ตัวชี้วัดที่ 5.1.html'),
]

routes_str = """const routes = {
                '1.1': 'ตัวชี้วัดที่ 1.1.html',
                '1.2.1': 'ตัวชี้วัดที่ 1.2.1.html',
                '1.2.2': 'ตัวชี้วัดที่ 1.2.2.html',
                '2.1': 'ตัวชี้วัดที่ 2.1.html',
                '2.2': 'ตัวชี้วัดที่ 2.2.html',
                '3.1': 'ตัวชี้วัดที่ 3.1.html',
                '3.2': 'ตัวชี้วัดที่ 3.2.html',
                '3.3': 'ตัวชี้วัดที่ 3.3.html',
                '4.1': 'ตัวชี้วัดที่ 4.1.html',
                '4.2': 'ตัวชี้วัดที่ 4.2.html',
                '4.3': 'ตัวชี้วัดที่ 4.3.html',
                '5.1': 'ตัวชี้วัดที่ 5.1.html'
            }"""

for key, label, filename in kpi_list:
    if not os.path.exists(filename):
        print(f"Skipping {filename} (not found)")
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate options for this file
    options = []
    for k, lbl, fn in kpi_list:
        if k == key:
            options.append(f'                            <option value="{k}" selected>{lbl} (ปัจจุบัน)</option>')
        else:
            options.append(f'                            <option value="{k}">{lbl}</option>')
    new_options_block = "\n" + "\n".join(options) + "\n                        "

    # Replace <select id="select-kpi-page" ...> ... </select>
    def select_replacer(m):
        tag_open = m.group(1)
        tag_close = m.group(3)
        return f'{tag_open}{new_options_block}{tag_close}'

    content = re.sub(r'(<select[^>]*id=["\']select-kpi-page["\'][^>]*>)(.*?)(</select>)', select_replacer, content, flags=re.DOTALL)

    # Replace routes object
    content = re.sub(r'const\s+routes\s*=\s*\{[^}]+\}', routes_str, content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    safe_fn = filename.encode('ascii', 'backslashreplace').decode('ascii')
    print(f"Updated {safe_fn} successfully.")

print("All 12 files synced to KPI 5.1!")
