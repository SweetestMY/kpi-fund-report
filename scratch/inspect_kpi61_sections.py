import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the HTML template part in build_kpi61.py around the views
idx_v0 = text.find('id="view-topic-0"')
idx_v1 = text.find('id="view-topic-1"')
idx_v2 = text.find('id="view-topic-2"')
idx_js = text.find('<script>')

print("View 0 start:", idx_v0)
print("View 1 start:", idx_v1)
print("View 2 start:", idx_v2)
print("Script start:", idx_js)
