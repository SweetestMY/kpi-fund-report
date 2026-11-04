import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'function switchQuarter\(qNum\)\s*\{.*?\n        \}', text, re.DOTALL)
if m:
    print(m.group(0))
else:
    idx = text.find('function switchQuarter')
    print(text[idx:idx+3000])
