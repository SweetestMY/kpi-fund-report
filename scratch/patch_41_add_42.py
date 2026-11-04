import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("ตัวชี้วัดที่ 4.1.html", "r", encoding="utf-8") as f:
    c = f.read()

# Update option list in 4.1
old_option = '<option value="4.1" selected>4.1 การบริหารความเสี่ยงฯ (ปัจจุบัน)</option>'
new_option = '<option value="4.1" selected>4.1 การบริหารความเสี่ยงฯ (ปัจจุบัน)</option>\n                            <option value="4.2">4.2 การตรวจสอบภายใน</option>'

if old_option in c:
    c = c.replace(old_option, new_option)
    print("Added 4.2 to options in 4.1")

# Update routes in 4.1
old_route = "'4.1': 'ตัวชี้วัดที่ 4.1.html'"
new_route = "'4.1': 'ตัวชี้วัดที่ 4.1.html',\n                '4.2': 'ตัวชี้วัดที่ 4.2.html'"

if old_route in c:
    c = c.replace(old_route, new_route)
    print("Added 4.2 to routes in 4.1")

with open("ตัวชี้วัดที่ 4.1.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Saved 4.1")
