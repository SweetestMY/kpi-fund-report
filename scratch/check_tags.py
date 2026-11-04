# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check if there is an unclosed tag or syntax error
import re
print("Count of <div>:", text.count('<div'))
print("Count of </div>:", text.count('</div>'))
print("Count of <table>:", text.count('<table'))
print("Count of </table>:", text.count('</table>'))
