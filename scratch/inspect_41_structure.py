import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

# Let's inspect style block
style_start = text.find('<style>')
style_end = text.find('</style>')
print(f"Style length: {style_end - style_start}")

# Let's inspect from </style> to View 0
view0_start = text.find('id="view-topic-0"')
if view0_start == -1:
    view0_start = text.find('id="view0"')
if view0_start == -1:
    view0_start = text.find('view-topic-')

print("\n=== MARKUP BEFORE VIEW 0 ===")
print(text[style_end:style_end+4000])
