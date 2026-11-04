# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

kpi_files = [
    'ตัวชี้วัดที่ 1.1.html',
    'ตัวชี้วัดที่ 1.2.1.html',
    'ตัวชี้วัดที่ 1.2.2.html',
    'ตัวชี้วัดที่ 2.1.html',
    'ตัวชี้วัดที่ 2.2.html',
    'ตัวชี้วัดที่ 3.1.html',
    'ตัวชี้วัดที่ 3.2.html',
    'ตัวชี้วัดที่ 3.3.html',
    'ตัวชี้วัดที่ 4.1.html',
    'ตัวชี้วัดที่ 4.2.html',
    'ตัวชี้วัดที่ 4.3.html',
    'ตัวชี้วัดที่ 5.1.html',
    'ตัวชี้วัดที่ 5.2.html',
    'ตัวชี้วัดที่ 6.1.html',
]

base_dir = 'd:/ตัวชี้วัด/form'
all_good = True

for fname in kpi_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check select-kpi-page
    m_kpi = re.search(r'<select[^>]*id=["\']select-kpi-page["\'][^>]*>(.*?)</select>', content, re.DOTALL)
    if not m_kpi:
        print(f"ERROR: {fname} missing select-kpi-page")
        all_good = False
        continue

    opts = re.findall(r'<option[^>]*value=["\']([^"\']+)["\'][^>]*>(.*?)</option>', m_kpi.group(1))
    if len(opts) != 14:
        print(f"ERROR: {fname} has {len(opts)} options in select-kpi-page, expected 14")
        all_good = False
    
    # Check for any future KPI
    for val, lbl in opts:
        if val not in ['1.1', '1.2.1', '1.2.2', '2.1', '2.2', '3.1', '3.2', '3.3', '4.1', '4.2', '4.3', '5.1', '5.2', '6.1']:
            print(f"ERROR: {fname} contains unexpected future KPI {val}: {lbl}")
            all_good = False

    # Check quarter ordering
    m_q = re.search(r'<select[^>]*id=["\'](?:quarter-focus|report-quarter)["\'][^>]*>(.*?)</select>', content, re.DOTALL)
    if m_q:
        q_vals = re.findall(r'value=["\']([^"\']+)["\']', m_q.group(1))
        if q_vals != ['1', '2', '3', '4']:
            print(f"ERROR: {fname} quarter options are {q_vals}, expected ['1', '2', '3', '4']")
            all_good = False

if all_good:
    print("SUCCESS: All 14 files have 100% verified navigation and quarter order!")
else:
    print("Verification failed on some checks.")
