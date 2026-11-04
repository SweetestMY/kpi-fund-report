import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of build_kpi61.py:", len(text))
print("Does it contain select-kpi-page?", 'select-kpi-page' in text)
print("Does it contain quarter-focus?", 'quarter-focus' in text)

# find select-kpi-page
m = re.search(r'<select id="select-kpi-page".*?</select>', text, re.DOTALL)
if m:
    print("select-kpi-page in build_kpi61.py:")
    for line in m.group(0).splitlines():
        if '<option' in line:
            print("  ", line.strip())

# find quarter-focus
m2 = re.search(r'<select id="quarter-focus".*?</select>', text, re.DOTALL)
if m2:
    print("quarter-focus in build_kpi61.py:")
    for line in m2.group(0).splitlines():
        if '<option' in line:
            print("  ", line.strip())

# find routes
m3 = re.search(r'const routes = \{.*?\};', text, re.DOTALL)
if m3:
    print("routes in build_kpi61.py:")
    print(m3.group(0))
