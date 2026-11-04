with open('ตัวชี้วัดที่ 4.3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m1 = re.search(r'<select[^>]*id=["\']select-kpi-page["\'][^>]*>(.*?)</select>', text, re.DOTALL)
if m1:
    safe = m1.group(0).encode('ascii', 'backslashreplace').decode('ascii')
    print("Dropdown in 4.3:")
    print(safe)

m2 = re.search(r'const\s+routes\s*=\s*\{([^}]+)\}', text)
if m2:
    safe2 = m2.group(0).encode('ascii', 'backslashreplace').decode('ascii')
    print("Routes in 4.3:")
    print(safe2)
