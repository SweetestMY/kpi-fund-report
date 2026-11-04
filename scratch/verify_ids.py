with open('ตัวชี้วัดที่ 4.1.html', encoding='utf-8') as f:
    text = f.read()

print('ov-sc-val:', 'id="ov-sc-val"' in text)
print('ov-r4-score:', 'id="ov-r4-score"' in text)
print('ov-r5-score:', 'id="ov-r5-score"' in text)
