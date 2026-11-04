# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('window.onload')
if pos != -1:
    print(text[pos:pos+400])
else:
    # search for loadData or init
    for term in ['loadData', 'init', 'renderRubric']:
        p = text.find(term)
        print(f"{term} found at: {p}")
