import glob, re

for f in sorted(glob.glob('ตัวชี้วัดที่ *.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    m = re.search(r'<select[^>]*id=["\'](?:quarter-focus|quarter-select|select-quarter)["\'][^>]*>(.*?)</select>', txt, re.DOTALL)
    if not m:
        # try find any select with onchange containing switchQuarter
        m = re.search(r'<select[^>]*onchange=["\']switchQuarter[^"\']*["\'][^>]*>(.*?)</select>', txt, re.DOTALL)
    safe_fn = f.encode('ascii', 'backslashreplace').decode('ascii')
    if m:
        opts = re.findall(r'<option[^>]*value=["\']?([^"\'>]+)["\']?[^>]*>(.*?)</option>', m.group(1))
        opt_vals = [v for v, label in opts]
        print(f"{safe_fn}: {opt_vals}")
    else:
        print(f"{safe_fn}: NO MATCH")
