import io, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/README.md', 'r', encoding='utf-8') as f:
    print(f.read()[:2000])
