with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Length of HTML:", len(text))
# Check quarter switching function
m = re.search(r'function switchQuarter\(q\)\s*\{(.*?)\n\s*\}', text, re.DOTALL)
if m:
    safe = m.group(0)[:1500].encode('ascii', 'backslashreplace').decode('ascii')
    print("switchQuarter snippet:")
    print(safe)
