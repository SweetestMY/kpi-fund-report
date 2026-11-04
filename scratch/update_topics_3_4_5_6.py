# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# ==============================================================
# 1. VIEW-TOPIC-3 (กระบวนการบริหารความเสี่ยง 45%)
# ==============================================================
old_v3_match = re.search(r'(<div class="topic-view" id="view-topic-3">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 4:)', text, re.DOTALL)
assert old_v3_match, "view-topic-3 match not found"

new_v3 = """<div class="topic-view" id="view-topic-3">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t3-title" style="font-size: 16px; font-weight: 800; color: #003666;">⚙️ 3. กระบวนการบริหารความเสี่ยง (น้ำหนัก 45% - สำคัญที่สุด)</span>
                        <span contenteditable="true" id="t3-badge" class="panel-title-badge" style="background: #fef3c7; color: #92400e; border-color: #fde68a;">น้ำหนัก 45% | ผลงานระดับ 5</span>
                    </div>

                    <!-- Progressive Rubric 1-5 -->
                    <div class="rubric-5step-grid">
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div><div contenteditable="true" id="t3-r1" class="rstep-desc">ระบุปัจจัยเสี่ยงระดับองค์กร เชื่อมโยงเป้าหมายประจำปี</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div><div contenteditable="true" id="t3-r2" class="rstep-desc">ประเมินระดับความรุนแรงทั้งโอกาสและผลกระทบครบทุกความเสี่ยง</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div><div contenteditable="true" id="t3-r3" class="rstep-desc">ผ่านระดับ 2 และจัดทำแผนภาพความเสี่ยงองค์กร (Risk Profile)</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div><div contenteditable="true" id="t3-r4" class="rstep-desc">มีแผนบริหารความเสี่ยงสอดคล้องกับการควบคุมภายในอย่างชัดเจน</div></div>
                        <div class="rstep-card active-target"><div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div><div contenteditable="true" id="t3-r5" class="rstep-desc">ผ่านระดับ 4 + วิเคราะห์ Cost-Benefit + คณะกรรมการฯ เห็นชอบในไตรมาส 2</div></div>
                    </div>

                    <!-- Process Steps Flow (5 Operational Steps from Official Document) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>ผลการดำเนินงาน 5 ขั้นตอนสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div class="flow-steps-row" style="padding: 18px 14px; background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; gap: 8px;">
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 1</span>
                                <span contenteditable="true" id="t3-s1-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ระบุปัจจัยเสี่ยง 4 ด้าน</span>
                                <span contenteditable="true" id="t3-s1-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ระบุความเสี่ยง 4 ด้าน รวม 8 ปัจจัยเสี่ยง เชื่อมโยงเป้าหมายประจำปีและปีก่อนหน้า</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 2</span>
                                <span contenteditable="true" id="t3-s2-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ประเมินโอกาส & ผลกระทบ</span>
                                <span contenteditable="true" id="t3-s2-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ประเมินระดับความรุนแรงโดยใช้ฐานข้อมูลของเงินทุนหมุนเวียนครบทุกปัจจัย</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 3</span>
                                <span contenteditable="true" id="t3-s3-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">จัดทำ Risk Profile</span>
                                <span contenteditable="true" id="t3-s3-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">จัดทำแผนภาพความเสี่ยงระดับองค์กร และแผนบริหารความเสี่ยง 4 แผนงาน</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 4</span>
                                <span contenteditable="true" id="t3-s4-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">วิเคราะห์ Cost-Benefit</span>
                                <span contenteditable="true" id="t3-s4-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">วิเคราะห์ต้นทุนเทียบประโยชน์ (Cost-Benefit) ในทุกทางเลือกอย่างรอบคอบ</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 5</span>
                                <span contenteditable="true" id="t3-s5-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">คณะกรรมการฯ เห็นชอบ</span>
                                <span contenteditable="true" id="t3-s5-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ผ่านความเห็นชอบ กก.บริหารฯ มติ 2/2569 (27 ก.พ. 69 ภายในไตรมาส 2)</span>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t3-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> ดำเนินการบริหารความเสี่ยงครบถ้วนทั้ง 5 ขั้นตอน มีการระบุความเสี่ยง 4 ด้าน 8 ปัจจัย ประเมินความรุนแรง จัดทำ Risk Profile 4 แผนงาน วิเคราะห์ Cost-Benefit และผ่านความเห็นชอบคณะกรรมการบริหารฯ ภายในไตรมาส 2 ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="padding: 14px 22px;">
                            <div>
                                <div contenteditable="true" id="t3-sc-lbl" class="score-lbl" style="font-size: 13.5px;">ผลการดำเนินงานข้อที่ 3 (น้ำหนัก 45%)</div>
                                <div contenteditable="true" id="t3-sc-val" class="big-score-val" style="font-size: 26px;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="t3-sc-stars" class="score-pill-stars" style="font-size: 22px;">⭐⭐⭐⭐⭐</div>
                        </div>
                    </div>
                </div>
            </div>"""

text = text[:old_v3_match.start()] + new_v3 + text[old_v3_match.end():]
print("Step 1 (view-topic-3) ready")

# ==============================================================
# 2. VIEW-TOPIC-4 (กิจกรรมการควบคุมภายใน 5%)
# ==============================================================
old_v4_match = re.search(r'(<div class="topic-view" id="view-topic-4">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 5:)', text, re.DOTALL)
assert old_v4_match, "view-topic-4 match not found"

new_v4 = """<div class="topic-view" id="view-topic-4">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t4-title" style="font-size: 16px; font-weight: 800; color: #003666;">⚙️ 4. กิจกรรมการควบคุมภายใน (น้ำหนัก 5%) - กำหนด Control Activity ครอบคลุมทุกกระบวนงาน</span>
                        <span contenteditable="true" id="t4-badge" class="panel-title-badge">น้ำหนัก 5% | ผลงานระดับ 5</span>
                    </div>

                    <!-- Progressive Rubric 1-5 -->
                    <div class="rubric-5step-grid">
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div><div contenteditable="true" id="t4-r1" class="rstep-desc">กำหนดกระบวนการทำงานที่สำคัญและกระบวนการย่อย</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div><div contenteditable="true" id="t4-r2" class="rstep-desc">กำหนด Control Activity แต่ยังไม่ครบทุกกระบวนการที่สำคัญ</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div><div contenteditable="true" id="t4-r3" class="rstep-desc">กำหนด Control Activity ครบทุกกระบวนการที่สำคัญ</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div><div contenteditable="true" id="t4-r4" class="rstep-desc">กำหนด Control Activity ครบทุกกระบวนการหลัก แต่ไม่ครบกระบวนงานย่อย</div></div>
                        <div class="rstep-card active-target"><div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div><div contenteditable="true" id="t4-r5" class="rstep-desc">กำหนด Control Activity ครบทุกกระบวนงานหลักและย่อย พร้อมทบทวนตาม Workflow</div></div>
                    </div>

                    <!-- Process Steps Flow (5 Operational Steps from Official Document) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>ผลการดำเนินงาน 5 ขั้นตอนสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div class="flow-steps-row" style="padding: 18px 14px; background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; gap: 8px;">
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 1</span>
                                <span contenteditable="true" id="t4-s1-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">วางระบบ 3 กระบวนงานหลัก</span>
                                <span contenteditable="true" id="t4-s1-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">กำหนด 3 กระบวนงานสำคัญ: การจัดสรรเงินกู้, กำกับติดตามหนี้, และบังคับคดี</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 2</span>
                                <span contenteditable="true" id="t4-s2-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ครอบคลุมกระบวนงานย่อย</span>
                                <span contenteditable="true" id="t4-s2-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">กำหนดกระบวนการทำงานย่อยครอบคลุมครบถ้วนทุกขั้นตอนปฏิบัติงาน</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 3</span>
                                <span contenteditable="true" id="t4-s3-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">กำหนด Control Activity</span>
                                <span contenteditable="true" id="t4-s3-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">วางจุดกิจกรรมควบคุม (Control Activity) ครอบคลุมทั้งกระบวนงานหลักและย่อย</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 4</span>
                                <span contenteditable="true" id="t4-s4-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">สอดคล้องแผนปี 2569</span>
                                <span contenteditable="true" id="t4-s4-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ปรับปรุงกิจกรรมควบคุมให้สอดคล้องกับแผนปฏิบัติการประจำปีบัญชี 2569</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 5</span>
                                <span contenteditable="true" id="t4-s5-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ทบทวนผัง Workflow</span>
                                <span contenteditable="true" id="t4-s5-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ปรับปรุงและทบทวนตามผังกระบวนการทำงานปัจจุบัน (เอกสารหมายเลข 8)</span>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t4-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ มีการกำหนดกิจกรรมการควบคุมการปฏิบัติงาน (Control Activity) ครอบคลุม 3 กระบวนงานหลักและกระบวนงานย่อยทั้งหมด พร้อมปรับปรุงทบทวนให้สอดคล้องกับแผนปฏิบัติการปี 2569 และผัง Workflow ครบถ้วน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="padding: 14px 22px;">
                            <div>
                                <div contenteditable="true" id="t4-sc-lbl" class="score-lbl" style="font-size: 13.5px;">ผลการดำเนินงานข้อที่ 4 (น้ำหนัก 5%)</div>
                                <div contenteditable="true" id="t4-sc-val" class="big-score-val" style="font-size: 26px;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="t4-sc-stars" class="score-pill-stars" style="font-size: 22px;">⭐⭐⭐⭐⭐</div>
                        </div>
                    </div>
                </div>
            </div>"""

text = text[:old_v4_match.start()] + new_v4 + text[old_v4_match.end():]
print("Step 2 (view-topic-4) ready")

# ==============================================================
# 3. VIEW-TOPIC-5 (สารสนเทศและการสื่อสาร 30%)
# ==============================================================
old_v5_match = re.search(r'(<div class="topic-view" id="view-topic-5">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 6:)', text, re.DOTALL)
assert old_v5_match, "view-topic-5 match not found"

new_v5 = """<div class="topic-view" id="view-topic-5">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t5-title" style="font-size: 16px; font-weight: 800; color: #003666;">📡 5. สารสนเทศและการสื่อสาร (น้ำหนัก 30%) - ติดตาม 13 กิจกรรม & ทบทวนแผน 2 ครั้ง</span>
                        <span contenteditable="true" id="t5-badge" class="panel-title-badge">น้ำหนัก 30% | ผลงานระดับ 5</span>
                    </div>

                    <!-- Progressive Rubric 1-5 -->
                    <div class="rubric-5step-grid">
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div><div contenteditable="true" id="t5-r1" class="rstep-desc">ใช้สารสนเทศติดตามไม่ครบทุกด้านตามแผนบริหารความเสี่ยง</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div><div contenteditable="true" id="t5-r2" class="rstep-desc">ใช้สารสนเทศติดตามครบ 4 ด้าน แต่ไม่ครบ 13 กิจกรรม</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div><div contenteditable="true" id="t5-r3" class="rstep-desc">ใช้สารสนเทศติดตามครบทั้ง 4 ด้าน รวม 13 กิจกรรมตามแผน</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div><div contenteditable="true" id="t5-r4" class="rstep-desc">ใช้สารสนเทศติดตามครบ 13 กิจกรรม และทบทวนแผนระหว่างปี 1 ครั้ง</div></div>
                        <div class="rstep-card active-target"><div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div><div contenteditable="true" id="t5-r5" class="rstep-desc">ใช้สารสนเทศติดตามครบ 13 กิจกรรม + ทบทวนแผนระหว่างปีครบ 2 ครั้ง</div></div>
                    </div>

                    <!-- Process Steps Flow (5 Operational Steps from Official Document) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>ผลการดำเนินงาน 5 ขั้นตอนสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div class="flow-steps-row" style="padding: 18px 14px; background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; gap: 8px;">
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 1</span>
                                <span contenteditable="true" id="t5-s1-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ใช้สารสนเทศติดตาม 4 ด้าน</span>
                                <span contenteditable="true" id="t5-s1-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ใช้ระบบสารสนเทศสนับสนุนการกำกับติดตามแผนบริหารความเสี่ยงครบทั้ง 4 ด้าน</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 2</span>
                                <span contenteditable="true" id="t5-s2-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ดำเนินงานครบ 13 กิจกรรม</span>
                                <span contenteditable="true" id="t5-s2-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ขับเคลื่อนและติดตามการดำเนินกิจกรรมตามแผนบริหารความเสี่ยงครบถ้วน 13 กิจกรรม</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 3</span>
                                <span contenteditable="true" id="t5-s3-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ลดความรุนแรงตามเป้าหมาย</span>
                                <span contenteditable="true" id="t5-s3-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ระดับความรุนแรงของปัจจัยเสี่ยงลดลงได้ตามเป้าหมายที่กำหนดครบทุกปัจจัย</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 4</span>
                                <span contenteditable="true" id="t5-s4-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ทบทวนระหว่างปี ครั้งที่ 1</span>
                                <span contenteditable="true" id="t5-s4-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ไตรมาส 2: คณะอนุกรรมการฯ มติรับทราบผลการทบทวน (27 มี.ค. 69)</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 5</span>
                                <span contenteditable="true" id="t5-s5-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ทบทวนระหว่างปี ครั้งที่ 2</span>
                                <span contenteditable="true" id="t5-s5-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ไตรมาส 3: คณะกรรมการบริหารฯ มติเห็นชอบผลการทบทวน (26 มิ.ย. 69)</span>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t5-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ ใช้ระบบสารสนเทศติดตามการดำเนินกิจกรรมครบ 4 ด้าน 13 กิจกรรม ระดับความรุนแรงลดลงตามเป้าหมาย และผ่านการทบทวนความเหมาะสมของแผนระหว่างปีครบถ้วน 2 ครั้ง ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="padding: 14px 22px;">
                            <div>
                                <div contenteditable="true" id="t5-sc-lbl" class="score-lbl" style="font-size: 13.5px;">ผลการดำเนินงานข้อที่ 5 (น้ำหนัก 30%)</div>
                                <div contenteditable="true" id="t5-sc-val" class="big-score-val" style="font-size: 26px;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="t5-sc-stars" class="score-pill-stars" style="font-size: 22px;">⭐⭐⭐⭐⭐</div>
                        </div>
                    </div>
                </div>
            </div>"""

text = text[:old_v5_match.start()] + new_v5 + text[old_v5_match.end():]
print("Step 3 (view-topic-5) ready")

# ==============================================================
# 4. VIEW-TOPIC-6 (การติดตามผลและการประเมินผล 5%)
# ==============================================================
old_v6_match = re.search(r'(<div class="topic-view" id="view-topic-6">.*?)(?=\s*</div>\s*<!-- FOOTER BAR -->)', text, re.DOTALL)
assert old_v6_match, "view-topic-6 match not found"

new_v6 = """<div class="topic-view" id="view-topic-6">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t6-title" style="font-size: 16px; font-weight: 800; color: #003666;">📊 6. การติดตามผลและการประเมินผล (น้ำหนัก 5%) - ประเมินหน่วยงาน & รายงานใน 90 วัน</span>
                        <span contenteditable="true" id="t6-badge" class="panel-title-badge">น้ำหนัก 5% | ผลงานระดับ 5</span>
                    </div>

                    <!-- Progressive Rubric 1-5 -->
                    <div class="rubric-5step-grid">
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div><div contenteditable="true" id="t6-r1" class="rstep-desc">กำหนดผู้รับผิดชอบ/คณะทำงานในการประเมินผลตามหลักเกณฑ์ กค.</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div><div contenteditable="true" id="t6-r2" class="rstep-desc">ประเมินผลการควบคุมภายใน แต่ไม่ครบถ้วนตามภารกิจของทุนฯ</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div><div contenteditable="true" id="t6-r3" class="rstep-desc">ประเมินผลการควบคุมภายในครบถ้วนตามภารกิจของทุนหมุนเวียน</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div><div contenteditable="true" id="t6-r4" class="rstep-desc">ประเมินครบถ้วนและรายงานผลการประเมินตามกำหนดเวลา</div></div>
                        <div class="rstep-card active-target"><div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div><div contenteditable="true" id="t6-r5" class="rstep-desc">ส่งรายงานการประเมินให้หน่วยงานต้นสังกัดได้ทัน (ภายใน 90 วัน สิ้นปีบัญชี)</div></div>
                    </div>

                    <!-- Process Steps Flow (5 Operational Steps from Official Document) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>ผลการดำเนินงาน 5 ขั้นตอนสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div class="flow-steps-row" style="padding: 18px 14px; background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; gap: 8px;">
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 1</span>
                                <span contenteditable="true" id="t6-s1-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">แต่งตั้งคณะทำงาน</span>
                                <span contenteditable="true" id="t6-s1-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">แต่งตั้งคณะทำงานจัดทำรายงานผลการควบคุมภายใน (เอกสารหมายเลข 9)</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 2</span>
                                <span contenteditable="true" id="t6-s2-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ประเมินครบภารกิจหลัก</span>
                                <span contenteditable="true" id="t6-s2-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ประเมินครอบคลุมภารกิจหลักและกระบวนงานสำคัญครบถ้วน (เอกสารหมายเลข 10)</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 3</span>
                                <span contenteditable="true" id="t6-s3-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ประชุมติดตามผล 3 ครั้ง</span>
                                <span contenteditable="true" id="t6-s3-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ประชุมติดตามผลการดำเนินงาน 3 ครั้ง (21 ม.ค., 25 พ.ค., 21 ส.ค. 69 เอกสารหมายเลข 11)</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 4</span>
                                <span contenteditable="true" id="t6-s4-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">จัดทำรายงานตามเกณฑ์</span>
                                <span contenteditable="true" id="t6-s4-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">จัดทำรายงานประเมินผลการควบคุมภายในตามมาตรฐานกระทรวงการคลัง พ.ศ. 2561</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 5</span>
                                <span contenteditable="true" id="t6-s5-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ส่งรายงานทันใน 90 วัน</span>
                                <span contenteditable="true" id="t6-s5-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">จัดส่งรายงานให้ต้นสังกัดในวันที่ 9 ต.ค. 2569 ทันตามกำหนดเวลา (เอกสารหมายเลข 12)</span>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t6-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ มีการประเมินผลการควบคุมภายในครอบคลุมภารกิจหลัก ประชุมติดตามผล 3 ครั้ง และจัดส่งรายงานผลการควบคุมภายในให้หน่วยงานต้นสังกัดได้ทันภายในกรอบ 90 วัน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="padding: 14px 22px;">
                            <div>
                                <div contenteditable="true" id="t6-sc-lbl" class="score-lbl" style="font-size: 13.5px;">ผลการดำเนินงานข้อที่ 6 (น้ำหนัก 5%)</div>
                                <div contenteditable="true" id="t6-sc-val" class="big-score-val" style="font-size: 26px;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="t6-sc-stars" class="score-pill-stars" style="font-size: 22px;">⭐⭐⭐⭐⭐</div>
                        </div>
                    </div>
                </div>
            </div>"""

text = text[:old_v6_match.start()] + new_v6 + text[old_v6_match.end():]
print("Step 4 (view-topic-6) ready")

with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("ALL TOPICS 3, 4, 5, 6 SUCCESSFULLY UPDATED TO 5-STEP FORMAT!")
