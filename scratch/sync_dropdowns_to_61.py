# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

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
    ('5.2', '5.2 การบริหารทรัพยากรบุคคล', 'ตัวชี้วัดที่ 5.2.html'),
    ('6.1', '6.1 การเบิกจ่ายเงินตามแผนฯ', 'ตัวชี้วัดที่ 6.1.html'),
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
                '5.1': 'ตัวชี้วัดที่ 5.1.html',
                '5.2': 'ตัวชี้วัดที่ 5.2.html',
                '6.1': 'ตัวชี้วัดที่ 6.1.html'
            }"""

base_dir = 'd:/ตัวชี้วัด/form'

for key, label, fname in kpi_list:
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Skipping {fname} (not found)")
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update <select id="select-kpi-page">
    options = []
    for k, lbl, _ in kpi_list:
        if k == key:
            options.append(f'                <option value="{k}" selected>{lbl} (ปัจจุบัน)</option>')
        else:
            options.append(f'                <option value="{k}">{lbl}</option>')
    new_options_block = "\n" + "\n".join(options) + "\n            "

    def select_replacer(m):
        tag_open = m.group(1)
        tag_close = m.group(3)
        return f'{tag_open}{new_options_block}{tag_close}'

    content = re.sub(r'(<select[^>]*id=["\']select-kpi-page["\'][^>]*>)(.*?)(</select>)', select_replacer, content, flags=re.DOTALL)

    # 2. Update routes
    content = re.sub(r'const\s+routes\s*=\s*\{[^}]+\}', routes_str, content)

    # 3. Ensure quarter dropdown order 1 -> 2 -> 3 -> 4
    # Pattern for quarter dropdowns (id="quarter-focus" or "report-quarter")
    quarter_block_asc = '''
                <option value="1">ไตรมาส 1 (ต.ค. - ธ.ค.)</option>
                <option value="2">ไตรมาส 2 (ต.ค. - มี.ค.)</option>
                <option value="3">ไตรมาส 3 (ต.ค. - มิ.ย.)</option>
                <option value="4" selected>ไตรมาส 4 (ครบปี ต.ค. - ก.ย.)</option>
            '''
    
    def quarter_replacer(m):
        tag_open = m.group(1)
        tag_close = m.group(3)
        return f'{tag_open}{quarter_block_asc}{tag_close}'

    content = re.sub(r'(<select[^>]*id=["\'](?:quarter-focus|report-quarter)["\'][^>]*>)(.*?)(</select>)', quarter_replacer, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {fname} successfully.")

print("All 14 files synced to KPI 6.1!")
