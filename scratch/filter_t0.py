with open('scratch/t0_all_rows.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('scratch/t0_filtered.txt', 'w', encoding='utf-8') as out:
    for l in lines:
        if any(w in l for w in ['ด้านที่ 5', '5.1', '5.2', 'ทรัพยากร', 'บุคคล', 'ผู้บริหาร', 'ลูกจ้าง']):
            out.write(l)

print("Done filtering.")
