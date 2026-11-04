import os

pdf_path = r'd:\ตัวชี้วัด\form\test_print_default.pdf'
print("PDF exists:", os.path.exists(pdf_path))
if os.path.exists(pdf_path):
    print("PDF size:", os.path.getsize(pdf_path))
