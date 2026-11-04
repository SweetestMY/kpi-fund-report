with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
selects = re.findall(r'<select[^>]*>.*?</select>', text, re.DOTALL)
for s in selects:
    safe = s.encode('ascii', 'backslashreplace').decode('ascii')
    print("--- SELECT ---")
    print(safe)
