import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('ตัวชี้วัดที่*.html')):
    with open(f, encoding='utf-8') as file:
        content = file.read()
        has_42 = 'ตัวชี้วัดที่ 4.2.html' in content
        print(f'{f}: contains 4.2 option? {has_42}')
