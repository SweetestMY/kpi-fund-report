import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 6.1.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Subtopic tags:")
for m in re.finditer(r'<button[^>]*class="[^"]*subtopic-tab[^"]*"[^>]*>', html):
    print("  ", m.group(0))

print("View containers:")
for m in re.finditer(r'<div[^>]*id="[^"]*view[^"]*"[^>]*>', html):
    print("  ", m.group(0))

idx = html.find('function switchView')
print(html[idx:idx+800])
