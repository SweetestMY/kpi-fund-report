import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = docx.Document('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx')

def save_text(t_idx, fname):
    t = doc.tables[t_idx]
    with open(fname, 'w', encoding='utf-8') as f:
        for r_idx, r in enumerate(t.rows):
            f.write(f"=== Row {r_idx} ===\n")
            for c in r.cells:
                f.write(c.text.strip() + "\n\n")

save_text(36, 'scratch/table_36.txt')
save_text(37, 'scratch/table_37.txt')
save_text(39, 'scratch/table_39.txt')
save_text(41, 'scratch/table_41.txt')
print("Saved tables 36, 37, 39, 41")
