import docx

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

print(f"Total paragraphs: {len(doc.paragraphs)}")
print(f"Total tables: {len(doc.tables)}")

found_p = []
for i, p in enumerate(doc.paragraphs):
    if '5.2' in p.text or 'การบริหารทรัพยากรบุคคล' in p.text:
        found_p.append((i, p.text.strip()))

with open('scratch/scratch_kpi52_p.txt', 'w', encoding='utf-8') as f:
    for idx, txt in found_p[:50]:
        f.write(f"P{idx}: {txt}\n")

print(f"Found {len(found_p)} matching paragraphs. Saved to scratch/scratch_kpi52_p.txt")
