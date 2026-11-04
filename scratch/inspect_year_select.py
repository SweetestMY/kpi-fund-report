import re

for fn in ['ตัวชี้วัดที่ 5.1.html', 'ตัวชี้วัดที่ 5.2.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        txt = f.read()
    m = re.search(r'(<select[^>]*id=["\']select-fiscal-year["\'][^>]*>.*?</select>)', txt, re.DOTALL)
    safe_fn = fn.encode('ascii', 'backslashreplace').decode('ascii')
    if m:
        safe_m = m.group(1).encode('ascii', 'backslashreplace').decode('ascii')
        print(f"{safe_fn}:")
        print(safe_m)
