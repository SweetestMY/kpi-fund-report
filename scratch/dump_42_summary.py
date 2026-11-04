import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc4 = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

print("=================== 3 SUB-ISSUES OF KPI 4.2 IN Q4 ===================")
# Sub-issue 1 is in Table 35, Sub-issue 2 in Table 38, Sub-issue 3 in Table 40
for t_idx in [35, 38, 40]:
    table = doc4.tables[t_idx]
    header = [c.text.strip().replace('\n', ' ') for c in table.rows[0].cells]
    row2 = [c.text.strip().replace('\n', ' ') for c in table.rows[2].cells]
    print(f"\n--- Sub-issue from Table {t_idx} ---")
    print(f"Name: {row2[0]}")
    print(f"Weight: {row2[1]}%")
    print(f"Scale 1: {row2[2]}")
    print(f"Scale 2: {row2[3]}")
    print(f"Scale 3: {row2[4]}")
    print(f"Scale 4: {row2[5]}")
    print(f"Scale 5: {row2[6]}")
    print(f"Result Q4: {row2[7]}")

# Also let's inspect the narrative tables Table 36, 37, 39, 41
for t_idx in [36, 37, 39, 41]:
    if t_idx < len(doc4.tables):
        t = doc4.tables[t_idx]
        print(f"\n--- Narrative Table {t_idx} ---")
        for r in t.rows:
            print(" ".join(c.text.strip() for c in r.cells)[:500])
