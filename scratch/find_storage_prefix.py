# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = 0
while True:
    pos = text.find('STORAGE_KEY_PREFIX', idx)
    if pos == -1: break
    print("=== Found at pos:", pos)
    print(text[max(0, pos-100):pos+400])
    print("-----------------------------------------")
    idx = pos + 1
