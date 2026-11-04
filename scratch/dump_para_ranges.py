import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def print_paras(doc_path, label, p_start, p_end):
    print(f"\n=== {label}: {doc_path} ===")
    doc = docx.Document(doc_path)
    for i in range(p_start, min(p_end, len(doc.paragraphs))):
        t = doc.paragraphs[i].text.strip()
        if t:
            print(f"P{i}: {t}")

print_paras('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4', 265, 275)
print_paras('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3', 225, 235)
print_paras('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2', 210, 220)
