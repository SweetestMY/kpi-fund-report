with open('build_kpi52.py', 'r', encoding='utf-8') as f:
    text = f.read()

target1 = '''                    <select id="quarter-focus" class="select-input" onchange="switchQuarter(this.value)">
                        <option value="4" selected>ไตรมาส 4 (ครบปี ต.ค. - ก.ย.)</option>
                        <option value="3">ไตรมาส 3 (ต.ค. - มิ.ย.)</option>
                        <option value="2">ไตรมาส 2 (ต.ค. - มี.ค.)</option>
                        <option value="1">ไตรมาส 1 (ต.ค. - ธ.ค.)</option>
                    </select>'''

replace1 = '''                    <select id="quarter-focus" class="select-input" onchange="switchQuarter(this.value)">
                        <option value="1">ไตรมาส 1 (ต.ค. - ธ.ค.)</option>
                        <option value="2">ไตรมาส 2 (ต.ค. - มี.ค.)</option>
                        <option value="3">ไตรมาส 3 (ต.ค. - มิ.ย.)</option>
                        <option value="4" selected>ไตรมาส 4 (ครบปี ต.ค. - ก.ย.)</option>
                    </select>'''

target2 = '''                    <select id="select-fiscal-year" class="select-input">
                        <option value="2569" selected>ปี 2569</option>
                        <option value="2568">ปี 2568</option>
                        <option value="2570">ปี 2570</option>
                    </select>'''

replace2 = '''                    <select id="select-year" class="select-input" onchange="changeFiscalYear(this.value)">
                        <option value="2568">ปี 2568</option>
                        <option value="2569" selected>ปี 2569</option>
                        <option value="2570">ปี 2570</option>
                    </select>'''

if target1 in text:
    text = text.replace(target1, replace1)
    print("Replaced target1 in build_kpi52.py")
else:
    print("target1 NOT found")

if target2 in text:
    text = text.replace(target2, replace2)
    print("Replaced target2 in build_kpi52.py")
else:
    print("target2 NOT found")

# Add changeFiscalYear if not present
if 'function changeFiscalYear' not in text:
    text = text.replace('function switchQuarter(qNum) {', 'function changeFiscalYear(yr) {\n            showToast(`เลือกดูข้อมูลปีงบประมาณ ${yr}`);\n        }\n\n        function switchQuarter(qNum) {')
    print("Added changeFiscalYear to build_kpi52.py")

with open('build_kpi52.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done updating build_kpi52.py")
