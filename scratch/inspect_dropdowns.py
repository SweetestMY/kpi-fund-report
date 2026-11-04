import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

def inspect_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f"=== {filename} ===")
    rep = re.search(r'<select[^>]*id=["\']report-quarter["\'].*?</select>', text, re.DOTALL)
    if rep:
        print("REPORT-QUARTER:")
        for line in rep.group(0).splitlines():
            if '<option' in line:
                print("  ", line.strip())

    qf = re.search(r'<select[^>]*id=["\']quarter-focus["\'].*?</select>', text, re.DOTALL)
    if qf:
        print("QUARTER-FOCUS:")
        for line in qf.group(0).splitlines():
            if '<option' in line:
                print("  ", line.strip())

    kpi = re.search(r'<select[^>]*id=["\']select-kpi-page["\'].*?</select>', text, re.DOTALL)
    if kpi:
        options = re.findall(r'<option[^>]*>(.*?)</option>', kpi.group(0))
        print("SELECT-KPI-PAGE count options:", len(options))
        for opt in options:
            print("   ->", opt.strip())

inspect_file('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 5.2.html')
