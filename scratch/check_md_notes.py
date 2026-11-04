with open('รายละเอียดการพัฒนา_KPI_Template.md', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('คู่มือการปรับปรุง_KPI.md', 'r', encoding='utf-8') as f:
    text2 = f.read()

with open('scratch/md_notes_52.txt', 'w', encoding='utf-8') as out:
    out.write("=== รายละเอียดการพัฒนา_KPI_Template.md ===\n")
    for l in text1.split('\n'):
        if '5.2' in l or 'ทรัพยากรบุคคล' in l:
            out.write(l + "\n")
    out.write("\n=== คู่มือการปรับปรุง_KPI.md ===\n")
    for l in text2.split('\n'):
        if '5.2' in l or 'ทรัพยากรบุคคล' in l:
            out.write(l + "\n")

print("Done")
