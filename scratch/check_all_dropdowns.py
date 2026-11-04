import os, re, glob

html_files = sorted(glob.glob("ตัวชี้วัดที่ *.html"))
print(f"Found {len(html_files)} files:")
for fpath in html_files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    m_opt = re.findall(r'<option\s+value="([^"]+)"', content)
    safe_fname = fname.encode("ascii", "backslashreplace").decode("ascii")
    print(f"{safe_fname}: options count = {len(m_opt)}, values = {m_opt}")
