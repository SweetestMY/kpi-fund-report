with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('STORAGE_KEY_PREFIX:', re.findall(r'STORAGE_KEY_PREFIX\s*=\s*[\'\"].*?[\'\"]', text))
print('Count of ระดับ 5 in file:', text.count('ระดับ 5'))
print('Count of N/A in file:', text.count('N/A'))

# Find the summary card and score sections
for line in text.splitlines():
    if any(k in line for k in ['ผลการประเมินเทียบเกณฑ์', 'score-badge', 'สรุปผลการประเมินตัวชี้วัด', 'N/A', 'STORAGE_KEY']):
        print(line[:120])
