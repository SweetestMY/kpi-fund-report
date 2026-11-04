import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("3: {")
print(text[idx:idx+3500])
