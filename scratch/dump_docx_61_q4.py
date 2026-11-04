import io, sys, docx
sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect Q4 docx
doc4 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')
print("Q4 Tables around 6.1:")
for idx, tbl in enumerate(doc4.tables):
    txt = "".join(cell.text for row in tbl.rows for cell in row.cells)
    if '6.1' in txt or 'การเบิกจ่ายเงิน' in txt or 'งบลงทุน' in txt:
        print(f"Table {idx}: length {len(txt)} | preview: {txt[:200]}")

# Let's also check paragraphs
for idx, p in enumerate(doc4.paragraphs):
    if 'ตัวชี้วัดที่ 6.1' in p.text:
        print(f"P {idx}: {p.text}")
        for j in range(idx, min(idx+25, len(doc4.paragraphs))):
            if doc4.paragraphs[j].text.strip():
                print(f"   p{j}: {doc4.paragraphs[j].text[:150]}")
        break
