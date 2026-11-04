with open('scratch/t0_all_rows.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total rows in t0: {len(lines)}")
for i in range(min(15, len(lines))):
    safe = lines[i][:100].encode('ascii', 'backslashreplace').decode('ascii')
    print(f"{i}: {safe}")
