import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 6.1.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function switchTopicView')
print(html[idx:idx+800])
