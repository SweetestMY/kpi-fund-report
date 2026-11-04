import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_42_full(doc_path, label):
    print(f"\n=======================================================")
    print(f"=== {label}: {doc_path} ===")
    print(f"=======================================================")
    doc = docx.Document(doc_path)
    
    # In doc, find paragraphs and tables between "ตัวชี้วัดที่ 4.2" and "ตัวชี้วัดที่ 4.3"
    capture = False
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if 'ตัวชี้วัดที่ 4.2' in t or '4.2 การตรวจสอบภายใน' in t or '4.2  การตรวจสอบภายใน' in t:
            capture = True
            print(f"\n[P{i}] {t}")
        elif capture and ('ตัวชี้วัดที่ 4.3' in t or '4.3  การบริหารจัดการสารสนเทศ' in t):
            capture = False
            print(f"[P{i} END OF 4.2] {t}")
            break
        elif capture and t:
            print(f"[P{i}] {t}")

extract_42_full('ข้อมูลไตรมาส/รวมไตรมาส 2 ปี 69 ผอ. แก้ ok.docx', 'Q2')
extract_42_full('ข้อมูลไตรมาส/รวมไตรมาส 3 ปี 69 ผอ. แก้ ok.docx', 'Q3')
extract_42_full('ข้อมูลไตรมาส/รวมไตรมาส 4 ปี 69 ล่าสุด.docx', 'Q4')
