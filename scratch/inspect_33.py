# -*- coding: utf-8 -*-
with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Find script sections and Q4 data
in_script = False
for idx, line in enumerate(lines):
    if '<script>' in line or '<script ' in line:
        in_script = True
        print(f"--- Script starts around line {idx+1} ---")
    if in_script and idx < 1200:
        if any(w in line for w in ['STORAGE_KEY_PREFIX', 'defaultQuarterData', 'quarterDefaults', 'renderQuarter', 'applyCapturedState', 'kpi_official_33']):
            print(f"L{idx+1}: {line.strip()[:100]}")
    if '</script>' in line:
        in_script = False
