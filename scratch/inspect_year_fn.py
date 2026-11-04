with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function changeFiscalYear\([^)]*\)\s*\{(.*?)\}', text, re.DOTALL)
if m:
    safe = m.group(0).encode('ascii', 'backslashreplace').decode('ascii')
    print(safe)
else:
    print("No changeFiscalYear found")
