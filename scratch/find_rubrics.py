import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 6.1.html', 'r', encoding='utf-8') as f:
    html = f.read()

for p in ['v1', 'v2']:
    for i in range(1, 6):
        rub_id = f'{p}-rubric-{i}'
        found = f'id="{rub_id}"' in html or f"id='{rub_id}'" in html
        print(f"{rub_id}: {found}")
