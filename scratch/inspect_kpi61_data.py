import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect quarterData in build_kpi61.py
m = re.search(r'const quarterData = \{.*?\n        \};', text, re.DOTALL)
if m:
    print("Found quarterData definition:")
    print(m.group(0)[:1000])
    print("...")
    print(m.group(0)[-1000:])
else:
    print("quarterData not found with regex, searching keys...")
    for line in text.splitlines():
        if 'quarterData' in line or 'switchQuarter' in line or 'switchView' in line:
            print(line)
