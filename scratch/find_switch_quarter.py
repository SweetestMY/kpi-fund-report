with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'switchQuarter' in l:
        print(f"Line {i+1}: {l.strip()[:80]}")
