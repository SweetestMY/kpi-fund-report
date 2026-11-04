import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<div class="toolbar-container">')
# find end of toolbar-container
end_idx = text.find('<!-- Dashboard Presentation Container (16:9 Landscape Frame) -->')
if end_idx == -1:
    end_idx = text.find('class="dashboard-container"')
if end_idx == -1:
    end_idx = start_idx + 6000

print(text[start_idx:end_idx])
