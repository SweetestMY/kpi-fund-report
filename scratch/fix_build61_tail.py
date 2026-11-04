import io, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'r', encoding='utf-8') as f:
    text = f.read()

# find the last occurrences of </html>
end_idx = text.find('</html>\n\'\'\'')
if end_idx != -1:
    fixed_code = text[:end_idx + len('</html>\n\'\'\'')] + '''
    with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 6.1.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("SUCCESS_BUILD_61")

if __name__ == '__main__':
    generate_kpi61()
'''
    with open('d:/ตัวชี้วัด/form/build_kpi61.py', 'w', encoding='utf-8') as f:
        f.write(fixed_code)
    print("Fixed build_kpi61.py cleanly.")
