import re

with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

m1 = re.search(r'<select[^>]*id=["\']select-kpi-page["\'][^>]*>(.*?)</select>', text, re.DOTALL)
if m1:
    print('SELECT OPTIONS in 5.1:')
    for opt in re.findall(r'<option[^>]*>.*?</option>', m1.group(1)):
        # print ascii-safe
        safe_opt = opt.encode('ascii', 'backslashreplace').decode('ascii')
        print('  ', safe_opt)

m2 = re.search(r'const\s+routes\s*=\s*\{([^}]+)\}', text)
if m2:
    print('ROUTES in 5.1:')
    safe_r = m2.group(0).encode('ascii', 'backslashreplace').decode('ascii')
    print(safe_r)
