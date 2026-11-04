import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read 4.1 HTML
with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text41 = f.read()

# Extract the style block from 4.1
style_start = text41.find('<style>')
style_end = text41.find('</style>') + len('</style>')
style_block = text41[style_start:style_end]

print(f"Extracted style block: {len(style_block)} chars")
