with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<select[^>]*id=["\']quarter-focus["\'][^>]*>.*?</select>)', text, re.DOTALL)
if m:
    safe = m.group(1).encode('ascii', 'backslashreplace').decode('ascii')
    print("In 5.1:")
    print(safe)
