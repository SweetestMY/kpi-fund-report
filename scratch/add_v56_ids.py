# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Ensure sub-criteria badges in View 5 have IDs
text = text.replace(
    '<span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (1.0000)</span>',
    '<span id="t5-p1-badge" style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (1.0000)</span>'
)
text = text.replace(
    '<span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.5000)</span>',
    '<span id="t5-p2-badge" style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.5000)</span>'
)

# 2. Ensure sub-criteria badges in View 6 have IDs
text = text.replace(
    '<span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.1000)</span>',
    '<span id="t6-p1-badge" style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.1000)</span>'
)
text = text.replace(
    '<span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.1500)</span>',
    '<span id="t6-p2-badge" style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.1500)</span>'
)

# 3. Add achievement pill IDs in View 5
text = text.replace(
    '✅ ผลสัมฤทธิ์: ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมายครบถ้วนทุกด้าน (เอกสารหมายเลข 3)',
    '<span id="t5-p1-achieve">✅ ผลสัมฤทธิ์: ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมายครบถ้วนทุกด้าน (เอกสารหมายเลข 3)</span>'
)
text = text.replace(
    '✅ ผลสัมฤทธิ์: ดำเนินการทบทวนแผนระหว่างปีครบถ้วน 2 ครั้งตามเกณฑ์มาตรฐาน',
    '<span id="t5-p2-achieve">✅ ผลสัมฤทธิ์: ดำเนินการทบทวนแผนระหว่างปีครบถ้วน 2 ครั้งตามเกณฑ์มาตรฐาน</span>'
)

# 4. Add achievement pill IDs in View 6
text = text.replace(
    '✅ ผลสัมฤทธิ์: จัดส่งรายงานวันที่ 9 ต.ค. 2569 ทันตามกรอบ 90 วันอย่างสมบูรณ์',
    '<span id="t6-p2-achieve">✅ ผลสัมฤทธิ์: จัดส่งรายงานวันที่ 9 ต.ค. 2569 ทันตามกรอบ 90 วันอย่างสมบูรณ์</span>'
)

with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Added IDs to dynamic elements in View 5 and View 6")
