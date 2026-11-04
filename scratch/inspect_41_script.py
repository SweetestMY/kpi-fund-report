import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

script_start = text.find('<script>')
script_end = text.rfind('</script>')
print(f"Script length: {script_end - script_start}")
print(text[script_start:script_start+1500])
