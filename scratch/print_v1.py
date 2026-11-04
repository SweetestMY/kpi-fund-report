import io, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_v1 = text.find('id="view-topic-1"')
idx_v2 = text.find('id="view-topic-2"')
print(text[idx_v1:idx_v2])
