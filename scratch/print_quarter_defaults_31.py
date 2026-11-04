# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 3.1.html', 'r', encoding='utf-8') as f:
    c = f.read()

p = c.find('quarterDefaults31')
if p != -1:
    print(c[p-30:p+1200])
