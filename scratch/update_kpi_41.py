# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Update Storage Key Prefix and add purgeLegacyKeys
# -------------------------------------------------------------
old_prefix = "const STORAGE_KEY_PREFIX = 'kpi_official_41_Q';"
new_prefix = "const STORAGE_KEY_PREFIX = 'kpi_official_41_v2_Q';"
assert old_prefix in text, "old_prefix not found"
text = text.replace(old_prefix, new_prefix, 1)

# Purge snippet right after <script>
old_script = "<script>\n        let lastFocusedElement = null;"
new_script = """<script>
        // Auto purge old v1 cached state
        try {
            ['kpi_official_41_Q1', 'kpi_official_41_Q2', 'kpi_official_41_Q3', 'kpi_official_41_Q4'].forEach(k => {
                localStorage.removeItem(k);
            });
        } catch(e) {}

        let lastFocusedElement = null;"""
assert old_script in text, "old_script not found"
text = text.replace(old_script, new_script, 1)

# Backup export check
old_backup = "if (k.startsWith('kpi_official_41_Q')) {"
new_backup = "if (k.startsWith('kpi_official_41_v2_Q')) {"
if old_backup in text:
    text = text.replace(old_backup, new_backup, 1)

# Reset function reload
old_reset = """        function resetQuarterDefaults() {
            if (confirm(`ต้องการคืนค่าเริ่มต้นสำหรับ "ไตรมาส ${activeQuarter}" ใช่หรือไม่? ข้อมูลที่แก้ไขจะถูกรีเซ็ต`)) {
                localStorage.removeItem(getStorageKey(activeQuarter));
                applyQuarterDefault(activeQuarter);
                showToast(`🔄 คืนค่าเริ่มต้นไตรมาส ${activeQuarter} แล้ว`);
            }
        }"""
new_reset = """        function resetQuarterDefaults() {
            if (confirm(`ต้องการคืนค่าเริ่มต้นสำหรับ "ไตรมาส ${activeQuarter}" ใช่หรือไม่? ข้อมูลที่แก้ไขจะถูกรีเซ็ต`)) {
                localStorage.removeItem(getStorageKey(activeQuarter));
                location.reload();
            }
        }"""
if old_reset in text:
    text = text.replace(old_reset, new_reset, 1)

print("Step 1 (Storage & Cache) ready")

# -------------------------------------------------------------
# 2. Replace view-topic-0 with new, larger, cleaner overview
# -------------------------------------------------------------
import re

old_v0_match = re.search(r'(<div class="topic-view active-view" id="view-topic-0">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 1:)', text, re.DOTALL)
assert old_v0_match, "view-topic-0 match not found"

new_v0 = """<div class="topic-view active-view" id="view-topic-0">
                <div class="grid-split" style="grid-template-columns: 1.38fr 1fr; gap: 16px; flex: 1;">
                    
                    <!-- Left: Summary Table of 6 Components -->
                    <div class="panel-box" style="padding: 20px 22px; justify-content: flex-start; gap: 16px;">
                        <div class="panel-title-line" style="margin-bottom: 2px;">
                            <span contenteditable="true" id="ov-t1" style="font-size: 16.5px; font-weight: 800; color: #003666;">📊 ผลการดำเนินงานรวม 6 องค์ประกอบ (ตัวชี้วัดที่ 4.1)</span>
                            <span contenteditable="true" id="ov-t1-sub" class="panel-title-badge" style="font-size: 13px; padding: 4px 10px;">น้ำหนักรวม 100%</span>
                        </div>

                        <div style="overflow-x: auto; flex: 1; display: flex; flex-direction: column; justify-content: center;">
                            <table class="overview-kpi-table" style="font-size: 15px;">
                                <thead>
                                    <tr>
                                        <th contenteditable="true" id="ov-th-1" style="width: 55px; font-size: 15px; padding: 13px 8px;">ข้อ</th>
                                        <th contenteditable="true" id="ov-th-2" style="font-size: 15px; padding: 13px 14px; text-align: left;">องค์ประกอบการประเมิน</th>
                                        <th contenteditable="true" id="ov-th-3" style="width: 95px; font-size: 15px; padding: 13px 8px;">น้ำหนัก (%)</th>
                                        <th contenteditable="true" id="ov-th-4" style="width: 105px; font-size: 15px; padding: 13px 8px;">ระดับคะแนน</th>
                                        <th contenteditable="true" id="ov-th-5" style="width: 125px; font-size: 15px; padding: 13px 10px;">คะแนนถ่วงน้ำหนัก</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr onclick="switchTopicView(1)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r1-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 13px 8px;">1</td>
                                        <td contenteditable="true" id="ov-r1-name" style="font-size: 15px; font-weight: 600; padding: 13px 14px;">สภาพแวดล้อมการควบคุมภายใน</td>
                                        <td contenteditable="true" id="ov-r1-w" style="text-align: center; font-weight: 700; font-size: 15px; padding: 13px 8px;">7%</td>
                                        <td contenteditable="true" id="ov-r1-score" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #005691; padding: 13px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r1-weighted" style="text-align: right; font-weight: 700; font-size: 15.5px; padding: 13px 16px;">0.3500</td>
                                    </tr>
                                    <tr onclick="switchTopicView(2)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r2-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 13px 8px;">2</td>
                                        <td contenteditable="true" id="ov-r2-name" style="font-size: 15px; font-weight: 600; padding: 13px 14px;">การกำหนดวัตถุประสงค์การบริหารความเสี่ยง</td>
                                        <td contenteditable="true" id="ov-r2-w" style="text-align: center; font-weight: 700; font-size: 15px; padding: 13px 8px;">8%</td>
                                        <td contenteditable="true" id="ov-r2-score" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #005691; padding: 13px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r2-weighted" style="text-align: right; font-weight: 700; font-size: 15.5px; padding: 13px 16px;">0.4000</td>
                                    </tr>
                                    <tr onclick="switchTopicView(3)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r3-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 13px 8px;">3</td>
                                        <td contenteditable="true" id="ov-r3-name" style="font-size: 15px; font-weight: 700; color: #004b87; padding: 13px 14px;">กระบวนการบริหารความเสี่ยง (สำคัญที่สุด)</td>
                                        <td contenteditable="true" id="ov-r3-w" style="text-align: center; font-weight: 800; font-size: 15px; color: #b45309; padding: 13px 8px;">45%</td>
                                        <td contenteditable="true" id="ov-r3-score" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #005691; padding: 13px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r3-weighted" style="text-align: right; font-weight: 800; font-size: 15.5px; color: #b45309; padding: 13px 16px;">2.2500</td>
                                    </tr>
                                    <tr onclick="switchTopicView(4)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r4-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 13px 8px;">4</td>
                                        <td contenteditable="true" id="ov-r4-name" style="font-size: 15px; font-weight: 600; padding: 13px 14px;">กิจกรรมการควบคุมภายใน</td>
                                        <td contenteditable="true" id="ov-r4-w" style="text-align: center; font-weight: 700; font-size: 15px; padding: 13px 8px;">5%</td>
                                        <td contenteditable="true" id="ov-r4-score" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #005691; padding: 13px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r4-weighted" style="text-align: right; font-weight: 700; font-size: 15.5px; padding: 13px 16px;">0.2500</td>
                                    </tr>
                                    <tr onclick="switchTopicView(5)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r5-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 13px 8px;">5</td>
                                        <td contenteditable="true" id="ov-r5-name" style="font-size: 15px; font-weight: 700; color: #004b87; padding: 13px 14px;">สารสนเทศและการสื่อสาร</td>
                                        <td contenteditable="true" id="ov-r5-w" style="text-align: center; font-weight: 800; font-size: 15px; color: #0369a1; padding: 13px 8px;">30%</td>
                                        <td contenteditable="true" id="ov-r5-score" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #005691; padding: 13px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r5-weighted" style="text-align: right; font-weight: 800; font-size: 15.5px; color: #0369a1; padding: 13px 16px;">1.5000</td>
                                    </tr>
                                    <tr onclick="switchTopicView(6)" style="cursor: pointer;">
                                        <td contenteditable="true" id="ov-r6-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 13px 8px;">6</td>
                                        <td contenteditable="true" id="ov-r6-name" style="font-size: 15px; font-weight: 600; padding: 13px 14px;">การติดตามผลและการประเมินผล</td>
                                        <td contenteditable="true" id="ov-r6-w" style="text-align: center; font-weight: 700; font-size: 15px; padding: 13px 8px;">5%</td>
                                        <td contenteditable="true" id="ov-r6-score" style="text-align: center; font-weight: 800; font-size: 15.5px; color: #005691; padding: 13px 8px;">5.0000</td>
                                        <td contenteditable="true" id="ov-r6-weighted" style="text-align: right; font-weight: 700; font-size: 15.5px; padding: 13px 16px;">0.2500</td>
                                    </tr>
                                    <tr class="total-kpi-row">
                                        <td colspan="2" contenteditable="true" id="ov-tot-lbl" style="text-align: center; font-weight: 800; font-size: 16px; color: #002d54; padding: 15px 14px;">รวมผลการประเมินถ่วงน้ำหนักทั้งหมด</td>
                                        <td contenteditable="true" id="ov-tot-w" style="text-align: center; font-weight: 800; font-size: 16px; color: #002d54; padding: 15px 8px;">100%</td>
                                        <td contenteditable="true" id="ov-tot-sc" style="text-align: center; font-weight: 800; font-size: 16.5px; color: #047857; padding: 15px 8px;">ระดับ 5</td>
                                        <td contenteditable="true" id="ov-tot-weighted" style="text-align: right; font-weight: 800; font-size: 18px; color: #047857; padding: 15px 16px;">5.0000 คะแนน</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Right: Executive Scorecard & Highlights -->
                    <div class="panel-box" style="padding: 22px 24px; justify-content: space-between; gap: 16px;">
                        <div class="panel-title-line">
                            <span contenteditable="true" id="ov-t2" style="font-size: 16.5px; font-weight: 800; color: #003666;">🏆 สรุปคะแนนผลการประเมินภาพรวม</span>
                        </div>

                        <!-- High-Contrast Executive Navy Scorecard -->
                        <div class="big-score-box" style="padding: 22px 24px;">
                            <div>
                                <div contenteditable="true" id="ov-sc-lbl" class="score-lbl" style="font-size: 15px; margin-bottom: 4px;">ผลการดำเนินงานเทียบเท่า</div>
                                <div contenteditable="true" id="ov-sc-val" class="big-score-val" style="font-size: 32px; font-weight: 900; color: #ffdd00;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="ov-sc-stars" class="score-pill-stars" style="font-size: 24px;">⭐⭐⭐⭐⭐</div>
                        </div>

                        <div style="background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; padding: 18px 20px; flex: 1; display: flex; flex-direction: column; justify-content: center;">
                            <strong contenteditable="true" id="ov-sum-h" style="color: #004b87; font-size: 16px; margin-bottom: 8px; display: block;">🎯 สรุปผลการดำเนินงานสำคัญ:</strong>
                            <div contenteditable="true" id="ov-sum-p" style="color: #0f172a; font-size: 14.5px; line-height: 1.65;">
                                เงินทุนหมุนเวียนฯ ดำเนินงานครบถ้วนตามมาตรฐานการควบคุมภายในและการบริหารความเสี่ยงทั้ง 6 องค์ประกอบ มีคู่มือที่มีองค์ประกอบครบถ้วน, จัดทำ Risk Profile 4 ด้าน 8 ปัจจัยเสี่ยง, ติดตามสารสนเทศ 13 กิจกรรม และรายงานผลทันภายในกรอบเวลา
                            </div>
                        </div>

                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                            <div style="background: #ecfdf5; border: 1.5px solid #86efac; border-radius: 10px; padding: 12px 14px; text-align: center;">
                                <div contenteditable="true" id="ov-st1-lbl" style="font-size: 13px; color: #065f46; font-weight: 700;">ความสำเร็จ</div>
                                <div contenteditable="true" id="ov-st1-val" style="font-size: 22px; font-weight: 800; color: #047857; margin-top: 3px;">ครบ 6 ข้อ</div>
                            </div>
                            <div style="background: #eff6ff; border: 1.5px solid #93c5fd; border-radius: 10px; padding: 12px 14px; text-align: center;">
                                <div contenteditable="true" id="ov-st2-lbl" style="font-size: 13px; color: #1e40af; font-weight: 700;">สถานะประเมิน</div>
                                <div contenteditable="true" id="ov-st2-val" style="font-size: 22px; font-weight: 800; color: #1d4ed8; margin-top: 3px;">ระดับ 5 (เต็ม)</div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>"""

text = text[:old_v0_match.start()] + new_v0 + text[old_v0_match.end():]
print("Step 2 (view-topic-0) updated successfully")

# -------------------------------------------------------------
# 3. Replace view-topic-5 with rich, elegant layout with Rubric & 13 Activities
# -------------------------------------------------------------
old_v5_match = re.search(r'(<div class="topic-view" id="view-topic-5">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 6:)', text, re.DOTALL)
assert old_v5_match, "view-topic-5 match not found"

new_v5 = """<div class="topic-view" id="view-topic-5">
                <div class="panel-box" style="padding: 18px 22px; justify-content: flex-start; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t5-title" style="font-size: 16px; font-weight: 800; color: #003666;">📡 5. สารสนเทศและการสื่อสาร (น้ำหนัก 30% - 2 ประเด็นพิจารณา)</span>
                        <span contenteditable="true" id="t5-badge" class="panel-title-badge">น้ำหนัก 30% | ผลงานระดับ 5</span>
                    </div>

                    <!-- Progressive Rubric 1-5 for Topic 5 -->
                    <div class="rubric-5step-grid">
                        <div class="rstep-card">
                            <div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div>
                            <div contenteditable="true" id="t5-r1" class="rstep-desc">ใช้สารสนเทศติดตามไม่ครบทุกด้านตามแผนบริหารความเสี่ยง</div>
                        </div>
                        <div class="rstep-card">
                            <div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div>
                            <div contenteditable="true" id="t5-r2" class="rstep-desc">ใช้สารสนเทศติดตามครบ 4 ด้าน แต่ไม่ครบ 13 กิจกรรม</div>
                        </div>
                        <div class="rstep-card">
                            <div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div>
                            <div contenteditable="true" id="t5-r3" class="rstep-desc">ใช้สารสนเทศติดตามครบทั้ง 4 ด้าน รวม 13 กิจกรรมตามแผน</div>
                        </div>
                        <div class="rstep-card">
                            <div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div>
                            <div contenteditable="true" id="t5-r4" class="rstep-desc">ใช้สารสนเทศติดตามครบ 13 กิจกรรม และทบทวนแผนระหว่างปี 1 ครั้ง</div>
                        </div>
                        <div class="rstep-card active-target">
                            <div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div>
                            <div contenteditable="true" id="t5-r5" class="rstep-desc">ใช้สารสนเทศติดตามครบ 13 กิจกรรม + ทบทวนแผนระหว่างปีครบ 2 ครั้ง</div>
                        </div>
                    </div>

                    <!-- Split 2 Sub-Criteria (Generous, well-padded cards that fill the space) -->
                    <div class="grid-split" style="gap: 16px; flex: 1;">
                        <!-- Sub-criterion 1: Information for monitoring (20%) -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 16px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                <span contenteditable="true" id="t5-sub1-t" style="font-size: 14.5px; font-weight: 800; color: #004b87;">ประเด็นที่ 1: การใช้สารสนเทศติดตาม (น้ำหนัก 20%)</span>
                                <span contenteditable="true" id="t5-sub1-sc" style="font-size: 13.5px; font-weight: 800; color: #047857; background: #ecfdf5; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">ระดับ 5 (เต็ม)</span>
                            </div>
                            <div contenteditable="true" id="t5-sub1-d" style="font-size: 13.5px; color: #0f172a; line-height: 1.5;">
                                ใช้ระบบสารสนเทศสนับสนุนการติดตามการดำเนินกิจกรรมตามแผนบริหารความเสี่ยงครบถ้วนทั้ง 4 ด้าน รวม 13 กิจกรรม ระดับความรุนแรงของปัจจัยเสี่ยงลดลงได้ตามเป้าหมาย
                            </div>
                            <!-- 4 Dimension Badges (2x2 Grid) -->
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12.5px;">
                                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 8px 10px;">
                                    <strong style="color: #0369a1; display: block; margin-bottom: 2px;">📌 ด้านกลยุทธ์ (3 กิจกรรม)</strong>
                                    <span contenteditable="true" id="t5-act-strat" style="color: #334155;">แจ้งจัดสรร, กำกับปฏิทินงาน, No Gift Policy</span>
                                </div>
                                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 8px 10px;">
                                    <strong style="color: #047857; display: block; margin-bottom: 2px;">⚙️ ด้านปฏิบัติการ (4 กิจกรรม)</strong>
                                    <span contenteditable="true" id="t5-act-ops" style="color: #334155;">ตรวจฐานข้อมูล, หนี้คงเหลือ, ติดตามหนี้โอนย้าย</span>
                                </div>
                                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 8px 10px;">
                                    <strong style="color: #b45309; display: block; margin-bottom: 2px;">💰 ด้านการเงิน (3 กิจกรรม)</strong>
                                    <span contenteditable="true" id="t5-act-fin" style="color: #334155;">เร่งรัดรายงานการเงิน, ตรวจสอบบัญชีประจำงวด</span>
                                </div>
                                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 8px 10px;">
                                    <strong style="color: #7c3aed; display: block; margin-bottom: 2px;">⚖️ ด้านกฎหมาย (3 กิจกรรม)</strong>
                                    <span contenteditable="true" id="t5-act-law" style="color: #334155;">กำกับหักหนี้ส่ง, บังคับคดีเร่งรัดหนี้, ประสานเบิกจ่าย</span>
                                </div>
                            </div>
                        </div>

                        <!-- Sub-criterion 2: Review & Update plan (10%) -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 16px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                <span contenteditable="true" id="t5-sub2-t" style="font-size: 14.5px; font-weight: 800; color: #004b87;">ประเด็นที่ 2: การทบทวนแผนระหว่างปี (น้ำหนัก 10%)</span>
                                <span contenteditable="true" id="t5-sub2-sc" style="font-size: 13.5px; font-weight: 800; color: #047857; background: #ecfdf5; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">ระดับ 5 (ทบทวน 2 ครั้ง)</span>
                            </div>
                            <div contenteditable="true" id="t5-sub2-d" style="font-size: 13.5px; color: #0f172a; line-height: 1.5;">
                                ทบทวนความเหมาะสมของแผนบริหารความเสี่ยงและการควบคุมภายในระหว่างปีครบถ้วน 2 ครั้ง ตามกำหนดเวลา:
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
                                <div style="background: #ecfdf5; border: 1.5px solid #86efac; border-radius: 8px; padding: 10px 12px; display: flex; align-items: center; gap: 8px;">
                                    <span style="font-size: 18px;">🗓️</span>
                                    <div>
                                        <strong contenteditable="true" id="t5-r2-1" style="color: #065f46; font-size: 13.5px;">ไตรมาส 2:</strong>
                                        <span style="color: #0f172a;"> มติคณะอนุกรรมการฯ ครั้งที่ 3/2569 (27 มี.ค. 69)</span>
                                    </div>
                                </div>
                                <div style="background: #eff6ff; border: 1.5px solid #93c5fd; border-radius: 8px; padding: 10px 12px; display: flex; align-items: center; gap: 8px;">
                                    <span style="font-size: 18px;">🏛️</span>
                                    <div>
                                        <strong contenteditable="true" id="t5-r2-2" style="color: #1e40af; font-size: 13.5px;">ไตรมาส 3:</strong>
                                        <span style="color: #0f172a;"> มติคณะกรรมการบริหารฯ ครั้งที่ 3/2569 (26 มิ.ย. 69)</span>
                                    </div>
                                </div>
                            </div>
                            <div style="background: #f0fdf4; border: 1px dashed #86efac; border-radius: 6px; padding: 6px 10px; font-size: 12.5px; color: #166534;">
                                ✅ มีการปรับปรุงมาตรการตอบสนองความเสี่ยงสอดคล้องตามสถานการณ์จริงรอบ 6 เดือน และ 9 เดือน
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 12px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t5-callout" style="font-size: 13.5px; line-height: 1.55;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> ดำเนินงานตามแผนบริหารความเสี่ยงได้ครบถ้วนทุกปัจจัยเสี่ยง และระดับความรุนแรงลดลงครบทั้ง 4 ด้าน พร้อมทบทวนระหว่างปีครบ 2 ครั้ง ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="padding: 12px 20px;">
                            <div>
                                <div contenteditable="true" id="t5-sc-lbl" class="score-lbl" style="font-size: 13.5px;">ผลการดำเนินงานข้อที่ 5 (30%)</div>
                                <div contenteditable="true" id="t5-sc-val" class="big-score-val" style="font-size: 24px;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="t5-sc-stars" class="score-pill-stars" style="font-size: 20px;">⭐⭐⭐⭐⭐</div>
                        </div>
                    </div>
                </div>
            </div>"""

text = text[:old_v5_match.start()] + new_v5 + text[old_v5_match.end():]
print("Step 3 (view-topic-5) updated successfully")

# Save file
with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated file successfully!")
