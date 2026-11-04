import io, sys, docx
sys.stdout.reconfigure(encoding='utf-8')

doc4 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
print("Total paragraphs:", len(doc4.paragraphs))
print("Paragraphs after 581:")
for idx in range(582, len(doc4.paragraphs)):
    p = doc4.paragraphs[idx].text.strip()
    if 'ด้านที่' in p or 'ตัวชี้วัด' in p:
        print(f"P {idx}: {p}")
