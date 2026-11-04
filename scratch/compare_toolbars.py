import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

# Find the toolbar area in 4.1
start_idx = text.find('<div class="toolbar')
end_idx = text.find('<div class="slide-canvas"')
if start_idx != -1 and end_idx != -1:
    print("=== TOOLBAR & CONTROLS IN 4.1 ===")
    print(text[start_idx:end_idx])
else:
    print("Start or end not found")
    print("start_idx:", start_idx, "end_idx:", end_idx)
