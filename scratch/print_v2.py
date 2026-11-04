import io, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_v2 = text.find('id="view-topic-2"')
idx_js = text.find('<script>')
print(text[idx_v2:idx_js])
