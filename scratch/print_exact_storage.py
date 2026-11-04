# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('STORAGE_KEY_PREFIX')
if pos != -1:
    print(text[pos-40:pos+1200])
