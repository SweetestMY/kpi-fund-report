with open('ตัวชี้วัดที่ 5.1.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'changeFiscalYear' in l:
        for j in range(i, min(i+10, len(lines))):
            safe = lines[j].strip().encode('ascii', 'backslashreplace').decode('ascii')
            print(f"{j+1}: {safe}")
        break
