# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Refine view-topic-0 right panel and table padding
old_v0_match = re.search(r'(<div class="topic-view active-view" id="view-topic-0">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 1:)', text, re.DOTALL)
assert old_v0_match, "view-topic-0 not found"

refined_v0 = """<div class="topic-view active-view" id="view-topic-0">
                <div class="grid-split" style="grid-template-columns: 1.35fr 1fr; gap: 18px; flex: 1;">
                    
                    <!-- Left: Summary Table of 6 Components -->
                    <div class="panel-box" style="padding: 22px 24px; justify-content: space-between; gap: 16px;">
                        <div class="panel-title-line" style="margin-bottom: 2px;">
                            <span contenteditable="true" id="ov-t1" style="font-size: 17px; font-weight: 800; color: #003666;">📊 ผลการดำเนินงานรวม 6 องค์ประกอบ (ตัวชี้วัดที่ 4.1)</span>
                            <span contenteditable="true" id="ov-t1-sub" class="panel-title-badge" style="font-size: 13.5px; padding: 5px 12px;">น้ำหนักรวม 100%</span>
                        </div>

                        <div style="overflow-x: auto; flex: 1; display: flex; flex-direction: column; justify-content: center;">
                            <table class="overview-kpi-table" style="font-size: 15.5px; height: 100%;">
                                <thead>
                                    <tr>
                                        <th contenteditable="true" id="ov-th-1" style="width: 55px; font-size: 15.5px; padding: 14px 8px;">ข้อ</th>
                                        <th contenteditable="true" id="ov-th-2" style="font-size: 15.5px; padding: 14px 14px; text-align: left;">องค์ประกอบการประเมิน</th>
                                        <th contenteditable="true" id="ov-th-3" style="width: 95px; font-size: 15.5px; padding: 14px 8px;">น้ำหนัก (%)</th>
                                        <th contenteditable="true" id="ov-th-4" style="width: 105px; font-size: 15.5px; padding: 14px 8px;">ระดับคะแนน</th>
                                        <th contenteditable="true" id="ov-th-5" style="width: 125px; font-size: 15.5px; padding: 14px 12px;">คะแนนถ่วงน้ำหนัก</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr onclick="switchTopicView(1)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r1-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">1</td>
                                        <td contenteditable="true" id="ov-r1-name" style="font-size: 15.5px; font-weight: 600; padding: 14px 14px;">สภาพแวดล้อมการควบคุมภายใน</td>
                                        <td contenteditable="true" id="ov-r1-w" style="text-align: center; font-weight: 700; font-size: 15.5px; padding: 14px 8px;">7%</td>
                                        <td contenteditable="true" id="ov-r1-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r1-weighted" style="text-align: right; font-weight: 700; font-size: 16px; padding: 14px 16px;">0.3500</td>
                                    </tr>
                                    <tr onclick="switchTopicView(2)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r2-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">2</td>
                                        <td contenteditable="true" id="ov-r2-name" style="font-size: 15.5px; font-weight: 600; padding: 14px 14px;">การกำหนดวัตถุประสงค์การบริหารความเสี่ยง</td>
                                        <td contenteditable="true" id="ov-r2-w" style="text-align: center; font-weight: 700; font-size: 15.5px; padding: 14px 8px;">8%</td>
                                        <td contenteditable="true" id="ov-r2-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r2-weighted" style="text-align: right; font-weight: 700; font-size: 16px; padding: 14px 16px;">0.4000</td>
                                    </tr>
                                    <tr onclick="switchTopicView(3)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r3-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">3</td>
                                        <td contenteditable="true" id="ov-r3-name" style="font-size: 15.5px; font-weight: 700; color: #004b87; padding: 14px 14px;">กระบวนการบริหารความเสี่ยง (สำคัญที่สุด)</td>
                                        <td contenteditable="true" id="ov-r3-w" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #b45309; padding: 14px 8px;">45%</td>
                                        <td contenteditable="true" id="ov-r3-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r3-weighted" style="text-align: right; font-weight: 800; font-size: 16px; color: #b45309; padding: 14px 16px;">2.2500</td>
                                    </tr>
                                    <tr onclick="switchTopicView(4)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r4-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">4</td>
                                        <td contenteditable="true" id="ov-r4-name" style="font-size: 15.5px; font-weight: 600; padding: 14px 14px;">กิจกรรมการควบคุมภายใน</td>
                                        <td contenteditable="true" id="ov-r4-w" style="text-align: center; font-weight: 700; font-size: 15.5px; padding: 14px 8px;">5%</td>
                                        <td contenteditable="true" id="ov-r4-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r4-weighted" style="text-align: right; font-weight: 700; font-size: 16px; padding: 14px 16px;">0.2500</td>
                                    </tr>
                                    <tr onclick="switchTopicView(5)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r5-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">5</td>
                                        <td contenteditable="true" id="ov-r5-name" style="font-size: 15.5px; font-weight: 700; color: #004b87; padding: 14px 14px;">สารสนเทศและการสื่อสาร</td>
                                        <td contenteditable="true" id="ov-r5-w" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #0369a1; padding: 14px 8px;">30%</td>
                                        <td contenteditable="true" id="ov-r5-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r5-weighted" style="text-align: right; font-weight: 800; font-size: 16px; color: #0369a1; padding: 14px 16px;">1.5000</td>
                                    </tr>
                                    <tr onclick="switchTopicView(6)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r6-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">6</td>
                                        <td contenteditable="true" id="ov-r6-name" style="font-size: 15.5px; font-weight: 600; padding: 14px 14px;">การติดตามผลและการประเมินผล</td>
                                        <td contenteditable="true" id="ov-r6-w" style="text-align: center; font-weight: 700; font-size: 15.5px; padding: 14px 8px;">5%</td>
                                        <td contenteditable="true" id="ov-r6-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 14px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r6-weighted" style="text-align: right; font-weight: 700; font-size: 16px; padding: 14px 16px;">0.2500</td>
                                    </tr>
                                    <tr class="total-kpi-row">
                                        <td colspan="2" contenteditable="true" id="ov-tot-lbl" style="text-align: center; font-weight: 800; font-size: 16.5px; color: #002d54; padding: 16px 14px;">รวมผลการประเมินถ่วงน้ำหนักทั้งหมด</td>
                                        <td contenteditable="true" id="ov-tot-w" style="text-align: center; font-weight: 800; font-size: 16.5px; color: #002d54; padding: 16px 8px;">100%</td>
                                        <td contenteditable="true" id="ov-tot-sc" style="text-align: center; font-weight: 800; font-size: 17px; color: #047857; padding: 16px 8px;">ระดับ 5</td>
                                        <td contenteditable="true" id="ov-tot-weighted" style="text-align: right; font-weight: 800; font-size: 18.5px; color: #047857; padding: 16px 16px;">5.0000 คะแนน</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Right: Executive Scorecard & Highlights -->
                    <div class="panel-box" style="padding: 22px 24px; justify-content: space-between; gap: 16px;">
                        <div class="panel-title-line">
                            <span contenteditable="true" id="ov-t2" style="font-size: 17px; font-weight: 800; color: #003666;">🏆 สรุปคะแนนผลการประเมินภาพรวม</span>
                        </div>

                        <!-- High-Contrast Executive Navy Scorecard -->
                        <div class="big-score-box" style="padding: 24px 26px;">
                            <div>
                                <div contenteditable="true" id="ov-sc-lbl" class="score-lbl" style="font-size: 15.5px; margin-bottom: 4px;">ผลการดำเนินงานเทียบเท่า</div>
                                <div contenteditable="true" id="ov-sc-val" class="big-score-val" style="font-size: 34px; font-weight: 900; color: #ffdd00;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="ov-sc-stars" class="score-pill-stars" style="font-size: 26px;">⭐⭐⭐⭐⭐</div>
                        </div>

                        <!-- Spacious Key Summary Card -->
                        <div style="background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; padding: 22px 22px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
                            <strong contenteditable="true" id="ov-sum-h" style="color: #004b87; font-size: 16.5px; margin-bottom: 10px; display: block;">🎯 สรุปผลการดำเนินงานสำคัญ:</strong>
                            <div contenteditable="true" id="ov-sum-p" style="color: #0f172a; font-size: 15px; line-height: 1.7;">
                                เงินทุนหมุนเวียนฯ ดำเนินงานครบถ้วนตามมาตรฐานการควบคุมภายในและการบริหารความเสี่ยงทั้ง 6 องค์ประกอบ มีคู่มือที่มีองค์ประกอบครบถ้วน, จัดทำ Risk Profile 4 ด้าน 8 ปัจจัยเสี่ยง, ติดตามสารสนเทศ 13 กิจกรรม และรายงานผลทันภายในกรอบเวลา
                            </div>
                        </div>

                        <!-- Two Bottom Achievement Status Badges -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                            <div style="background: #ecfdf5; border: 1.5px solid #86efac; border-radius: 10px; padding: 14px 16px; text-align: center;">
                                <div contenteditable="true" id="ov-st1-lbl" style="font-size: 13.5px; color: #065f46; font-weight: 700;">ความสำเร็จ</div>
                                <div contenteditable="true" id="ov-st1-val" style="font-size: 24px; font-weight: 800; color: #047857; margin-top: 4px;">ครบ 6 ข้อ</div>
                            </div>
                            <div style="background: #eff6ff; border: 1.5px solid #93c5fd; border-radius: 10px; padding: 14px 16px; text-align: center;">
                                <div contenteditable="true" id="ov-st2-lbl" style="font-size: 13.5px; color: #1e40af; font-weight: 700;">สถานะประเมิน</div>
                                <div contenteditable="true" id="ov-st2-val" style="font-size: 24px; font-weight: 800; color: #1d4ed8; margin-top: 4px;">ระดับ 5 (เต็ม)</div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>"""

text = text[:old_v0_match.start()] + refined_v0 + text[old_v0_match.end():]

# 2. Refine view-topic-4 (give middle flow-steps comfortable flex)
old_v4_match = re.search(r'(<div class="topic-view" id="view-topic-4">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 5:)', text, re.DOTALL)
if old_v4_match:
    old_v4 = old_v4_match.group(1)
    new_v4 = old_v4.replace('<div class="panel-box">', '<div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">')
    new_v4 = new_v4.replace('<div class="flow-steps-row">', '<div class="flow-steps-row" style="padding: 22px 18px; margin: 10px 0;">')
    text = text[:old_v4_match.start()] + new_v4 + text[old_v4_match.end():]

# 3. Refine view-topic-6 (give 2 main pillars comfortable flex)
old_v6_match = re.search(r'(<div class="topic-view" id="view-topic-6">.*?)(?=\s*<!-- CANVAS FOOTER\s*-->)', text, re.DOTALL)
if old_v6_match:
    old_v6 = old_v6_match.group(1)
    new_v6 = old_v6.replace('<div class="panel-box">', '<div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">')
    new_v6 = new_v6.replace('<div class="grid-split" style="gap: 14px;">\n                        <div style="background: #f8fbfe;', '<div class="grid-split" style="gap: 16px; flex: 1; margin: 8px 0;">\n                        <div style="background: #f8fbfe; display: flex; flex-direction: column; justify-content: space-between; padding: 18px 20px;')
    text = text[:old_v6_match.start()] + new_v6 + text[old_v6_match.end():]

with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Refinement completed successfully!")
