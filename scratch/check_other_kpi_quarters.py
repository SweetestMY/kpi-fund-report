# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

for kpi in ['1.1', '1.2.1', '2.1', '2.2', '3.1', '3.2', '3.3']:
    fn = f'ตัวชี้วัดที่ {kpi}.html'
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        has_quarter_data = 'QUARTER_DATA' in c or 'quarterData' in c or 'QUARTERS' in c
        has_switch = 'switchQuarter' in c
        print(f"{fn}: has_switch={has_switch}, has_quarter_data={has_quarter_data}")
        # print quarter switch implementation snippet
        pos = c.find('function switchQuarter')
        if pos != -1:
            print(f"  {fn} switchQuarter: {c[pos:pos+350].replace('\n', ' ')}")
    except Exception as e:
        print(f"Error {fn}: {e}")
