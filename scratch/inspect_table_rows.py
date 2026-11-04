with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
table_match = re.search(r'<tbody>(.*?)</tbody>', text, re.DOTALL)
if table_match:
    rows = re.findall(r'<tr.*?>(.*?)</tr>', table_match.group(1), re.DOTALL)
    print(f"Total rows in tbody: {len(rows)}")
    for i, r in enumerate(rows):
        safe_r = re.sub(r'\s+', ' ', r).strip().encode('ascii', 'backslashreplace').decode('ascii')
        print(f"Row {i+1}: {safe_r[:120]}")
