# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# ==============================================================
# 1. VIEW-TOPIC-3: 3 Real Milestones (ระบุ 8 ปัจจัยเสี่ยง -> Risk Profile -> Cost-Benefit & มติ กก.)
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

                    <!-- 3 Real Operational Milestones (Large, Concise Cards) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>สรุปผลการดำเนินงาน 3 ขั้นตอนหลัก (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px;">
                            <!-- Milestone 1 -->
                            <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 18px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
                                <div style="display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                    <span style="font-size: 20px;">🎯</span>
                                    <div>
                                        <div style="font-size: 12px; color: #0077b6; font-weight: 800;">ขั้นตอนที่ 1</div>
                                        <div contenteditable="true" id="t3-m1-t" style="font-size: 15px; font-weight: 800; color: #003666;">ระบุความเสี่ยง 4 ด้าน 8 ปัจจัย</div>
                                    </div>
                                </div>
                                <div contenteditable="true" id="t3-m1-d" style="font-size: 13.5px; color: #1e293b; line-height: 1.6;">
                                    ระบุความเสี่ยงระดับองค์กรครอบคลุม 4 ด้าน รวม 8 ปัจจัยเสี่ยง เชื่อมโยงกับเป้าหมายประจำปี 2569 และความเสี่ยงที่เหลืออยู่จากปีก่อนหน้า
                                </div>
                                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 8px 12px; font-size: 12.5px; color: #475569;">
                                    • กลยุทธ์ (3) • ปฏิบัติการ (3) • การเงิน (1) • กฎหมาย (1)
                                </div>
                            </div>

                            <!-- Milestone 2 -->
                            <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 18px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
                                <div style="display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                    <span style="font-size: 20px;">📊</span>
                                    <div>
                                        <div style="font-size: 12px; color: #0077b6; font-weight: 800;">ขั้นตอนที่ 2</div>
                                        <div contenteditable="true" id="t3-m2-t" style="font-size: 15px; font-weight: 800; color: #003666;">ประเมินความรุนแรง & Risk Profile</div>
                                    </div>
                                </div>
                                <div contenteditable="true" id="t3-m2-d" style="font-size: 13.5px; color: #1e293b; line-height: 1.6;">
                                    ประเมินระดับความรุนแรงทั้งโอกาสและผลกระทบ โดยใช้ฐานข้อมูลจริงของเงินทุนหมุนเวียน พร้อมจัดทำแผนภาพความเสี่ยง (Risk Profile) 4 แผนงาน
                                </div>
                                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 8px 12px; font-size: 12.5px; color: #475569;">
                                    • ใช้ฐานข้อมูลลูกหนี้และการเงินจริง • แผนบริหาร 4 แผนงาน
                                </div>
                            </div>

                            <!-- Milestone 3 -->
                            <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 18px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
                                <div style="display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #bbf7d0; padding-bottom: 8px;">
                                    <span style="font-size: 20px;">🏛️</span>
                                    <div>
                                        <div style="font-size: 12px; color: #047857; font-weight: 800;">ขั้นตอนที่ 3 (ระดับ 5)</div>
                                        <div contenteditable="true" id="t3-m3-t" style="font-size: 15px; font-weight: 800; color: #065f46;">วิเคราะห์ Cost-Benefit & กก.เห็นชอบ</div>
                                    </div>
                                </div>
                                <div contenteditable="true" id="t3-m3-d" style="font-size: 13.5px; color: #1e293b; line-height: 1.6;">
                                    วิเคราะห์ต้นทุนเทียบประโยชน์ (Cost-Benefit) ในทุกมาตรการ และผ่านความเห็นชอบจากคณะกรรมการบริหารฯ มติ 2/2569 (27 ก.พ. 69 ไตรมาส 2)
                                </div>
                                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 8px 12px; font-size: 12.5px; color: #166534; font-weight: 600;">
                                    ✅ มติเห็นชอบครั้งที่ 2/2569 • ภายในไตรมาสที่ 2 ครบถ้วน
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t3-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> ดำเนินการบริหารความเสี่ยงครบถ้วนทั้ง 3 ขั้นตอนหลัก ระบุความเสี่ยง 4 ด้าน 8 ปัจจัย ประเมินความรุนแรง จัดทำ Risk Profile วิเคราะห์ Cost-Benefit และผ่านความเห็นชอบคณะกรรมการบริหารฯ ภายในไตรมาส 2 ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
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
# 2. VIEW-TOPIC-4: 3 Real Pillars (3 กระบวนงานหลัก -> 12 Workflows -> ทบทวนตามแผนปี 69)
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

                    <!-- 3 Real Operational Pillars (Large, Concise Cards) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>สรุปผลการดำเนินงานการวางระบบและกิจกรรมควบคุม (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px;">
                            <!-- Pillar 1 -->
                            <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 18px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
                                <div style="display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                    <span style="font-size: 20px;">📑</span>
                                    <div>
                                        <div style="font-size: 12px; color: #0077b6; font-weight: 800;">สาระสำคัญที่ 1</div>
                                        <div contenteditable="true" id="t4-p1-t" style="font-size: 15px; font-weight: 800; color: #003666;">3 กระบวนงานหลักสำคัญ (แบบ ปค.5)</div>
                                    </div>
                                </div>
                                <div contenteditable="true" id="t4-p1-d" style="font-size: 13.5px; color: #1e293b; line-height: 1.6;">
                                    วางระบบการควบคุมภายในครอบคลุมภารกิจหลักของเงินทุนหมุนเวียนครบทั้ง 3 กระบวนงานหลัก (เอกสารหมายเลข 4):
                                </div>
                                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 8px 12px; font-size: 12.5px; color: #334155;">
                                    1) การจัดสรรเงินให้กู้ยืม<br>
                                    2) การกำกับ ติดตามหนี้ค้างชำระ<br>
                                    3) การบังคับคดีกับลูกหนี้ตามคำพิพากษา
                                </div>
                            </div>

                            <!-- Pillar 2 -->
                            <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 18px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
                                <div style="display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                    <span style="font-size: 20px;">🔄</span>
                                    <div>
                                        <div style="font-size: 12px; color: #0077b6; font-weight: 800;">สาระสำคัญที่ 2</div>
                                        <div contenteditable="true" id="t4-p2-t" style="font-size: 15px; font-weight: 800; color: #003666;">ผังกระบวนงานรวม 12 Workflows</div>
                                    </div>
                                </div>
                                <div contenteditable="true" id="t4-p2-d" style="font-size: 13.5px; color: #1e293b; line-height: 1.6;">
                                    กำหนดขั้นตอนการทำงานและการควบคุมครอบคลุมกระบวนงานย่อยทั้งหมด จัดทำผัง Work Flow ครบ 12 กระบวนงาน (เอกสารหมายเลข 6):
                                </div>
                                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 8px 12px; font-size: 12.5px; color: #334155;">
                                    • 3 กระบวนงานหลักสำคัญ<br>
                                    • 2 กระบวนงานสนับสนุน (บริหาร / การเงิน)<br>
                                    • 7 กระบวนงานย่อยภายในองค์กร
                                </div>
                            </div>

                            <!-- Pillar 3 -->
                            <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 18px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
                                <div style="display: flex; align-items: center; gap: 8px; border-bottom: 1.5px solid #bbf7d0; padding-bottom: 8px;">
                                    <span style="font-size: 20px;">🛡️</span>
                                    <div>
                                        <div style="font-size: 12px; color: #047857; font-weight: 800;">สาระสำคัญที่ 3 (ระดับ 5)</div>
                                        <div contenteditable="true" id="t4-p3-t" style="font-size: 15px; font-weight: 800; color: #065f46;">ทบทวนกิจกรรมควบคุมตามแผนปี 69</div>
                                    </div>
                                </div>
                                <div contenteditable="true" id="t4-p3-d" style="font-size: 13.5px; color: #1e293b; line-height: 1.6;">
                                    ปรับปรุงทบทวนกิจกรรมควบคุมให้สอดคล้องกับผัง Workflow ปัจจุบัน และแผนปฏิบัติการปี 2569 (วงเงินกู้ 250 ล้านบาท) เรียบร้อยแล้ว (เอกสารหมายเลข 8)
                                </div>
                                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 8px 12px; font-size: 12.5px; color: #166534; font-weight: 600;">
                                    ✅ ทบทวนกิจกรรมควบคุมครบทั้งหลักและย่อย 100%
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t4-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> กำหนดกิจกรรมการควบคุมภายใน (Control Activity) ครอบคลุม 3 กระบวนงานหลัก 2 งานสนับสนุน และ 7 งานย่อย รวม 12 Workflows พร้อมทบทวนตามแผนปฏิบัติการปี 2569 ครบถ้วน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
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
# 3. VIEW-TOPIC-5: 2 Real Criteria (การใช้สารสนเทศติดตาม 20% + การทบทวนแผนระหว่างปี 10%)
# ==============================================================
old_v5_match = re.search(r'(<div class="topic-view" id="view-topic-5">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 6:)', text, re.DOTALL)
assert old_v5_match, "view-topic-5 match not found"

new_v5 = """<div class="topic-view" id="view-topic-5">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t5-title" style="font-size: 16px; font-weight: 800; color: #003666;">📡 5. สารสนเทศและการสื่อสาร (น้ำหนัก 30% - 2 ประเด็นพิจารณา)</span>
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

                    <!-- 2 Real Sub-Criteria Cards (Spacious, Large Font, No Clutter) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>ผลการดำเนินงาน 2 ประเด็นพิจารณาสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 16px;">
                            <!-- Criterion 1 -->
                            <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 20px 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                    <div style="font-size: 15.5px; font-weight: 800; color: #004b87;">ประเด็นที่ 1: การใช้สารสนเทศติดตาม (น้ำหนัก 20%)</div>
                                    <span style="font-size: 13px; font-weight: 800; color: #047857; background: #ecfdf5; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">ระดับ 5 (เต็ม)</span>
                                </div>
                                <div contenteditable="true" id="t5-c1-d" style="font-size: 14px; color: #1e293b; line-height: 1.65;">
                                    ใช้ระบบสารสนเทศสนับสนุนการกำกับติดตามกิจกรรมตามแผนบริหารความเสี่ยงครบถ้วนทั้ง <strong>4 ด้าน รวม 13 กิจกรรม</strong> ส่งผลให้ระดับความรุนแรงของทุกปัจจัยเสี่ยงลดลงได้ตามเป้าหมายที่กำหนดครบถ้วน 100%
                                </div>
                                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #334155; line-height: 1.6;">
                                    • ด้านกลยุทธ์ (3 กิจกรรม) • ด้านการปฏิบัติงาน (4 กิจกรรม)<br>
                                    • ด้านการเงิน (3 กิจกรรม) • ด้านกฎหมาย/ระเบียบ (3 กิจกรรม)
                                </div>
                            </div>

                            <!-- Criterion 2 -->
                            <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 20px 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #bbf7d0; padding-bottom: 8px;">
                                    <div style="font-size: 15.5px; font-weight: 800; color: #065f46;">ประเด็นที่ 2: การทบทวนแผนระหว่างปี (น้ำหนัก 10%)</div>
                                    <span style="font-size: 13px; font-weight: 800; color: #047857; background: #ffffff; padding: 4px 10px; border-radius: 6px; border: 1px solid #86efac;">ระดับ 5 (ครบ 2 ครั้ง)</span>
                                </div>
                                <div contenteditable="true" id="t5-c2-d" style="font-size: 14px; color: #1e293b; line-height: 1.65;">
                                    ทบทวนความเหมาะสมของแผนบริหารความเสี่ยงระหว่างปีครบถ้วน 2 ครั้งตามเกณฑ์ โดยระดับความรุนแรงลดลงอย่างต่อเนื่อง:
                                </div>
                                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px;">
                                    <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 8px 12px; display: flex; align-items: center; gap: 8px;">
                                        <span>🗓️</span>
                                        <span><strong>ไตรมาส 2:</strong> คณะอนุกรรมการฯ มติรับทราบ (27 มี.ค. 2569)</span>
                                    </div>
                                    <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 8px 12px; display: flex; align-items: center; gap: 8px;">
                                        <span>🏛️</span>
                                        <span><strong>ไตรมาส 3:</strong> คณะกรรมการบริหารฯ มติเห็นชอบ (26 มิ.ย. 2569)</span>
                                    </div>
                                </div>
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
# 4. VIEW-TOPIC-6: 2 Real Criteria (ประเมินการควบคุมภายใน 2% + ส่งรายงานใน 90 วัน 3%)
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

                    <!-- 2 Real Sub-Criteria Cards (Spacious, Large Font, No Clutter) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 4px 0;">
                        <div style="font-size: 14.5px; font-weight: 800; color: #004b87; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>ผลการดำเนินงาน 2 ประเด็นพิจารณาสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 16px;">
                            <!-- Sub-criterion 1 -->
                            <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 20px 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                    <div style="font-size: 15.5px; font-weight: 800; color: #004b87;">ประเด็นที่ 1: การประเมินผลควบคุมภายใน (น้ำหนัก 2%)</div>
                                    <span style="font-size: 13px; font-weight: 800; color: #047857; background: #ecfdf5; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">ระดับ 5 (เต็ม)</span>
                                </div>
                                <div contenteditable="true" id="t6-c1-d" style="font-size: 14px; color: #1e293b; line-height: 1.65;">
                                    แต่งตั้งคณะทำงานฯ (เอกสารหมายเลข 9) และจัดทำรายงานประเมินผลการควบคุมภายในครอบคลุมภารกิจหลักและกระบวนงานสำคัญครบถ้วนทั้ง 3 ด้าน (เอกสารหมายเลข 10)
                                </div>
                                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #334155; line-height: 1.6;">
                                    • ประชุมติดตามผลการควบคุมภายใน 3 ครั้ง (21 ม.ค., 25 พ.ค., 21 ส.ค. 69)<br>
                                    • ครอบคลุมการจัดสรรเงินกู้, กำกับหนี้ค้างชำระ, และบังคับคดี
                                </div>
                            </div>

                            <!-- Sub-criterion 2 -->
                            <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 20px 20px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #bbf7d0; padding-bottom: 8px;">
                                    <div style="font-size: 15.5px; font-weight: 800; color: #065f46;">ประเด็นที่ 2: การจัดส่งรายงานตามเกณฑ์ กค. (น้ำหนัก 3%)</div>
                                    <span style="font-size: 13px; font-weight: 800; color: #047857; background: #ffffff; padding: 4px 10px; border-radius: 6px; border: 1px solid #86efac;">ระดับ 5 (ทัน 90 วัน)</span>
                                </div>
                                <div contenteditable="true" id="t6-c2-d" style="font-size: 14px; color: #1e293b; line-height: 1.65;">
                                    จัดส่งรายงานการประเมินผลการควบคุมภายในให้สำนักงาน ก.ค.ศ. (ส่งเมื่อวันที่ 9 ตุลาคม 2569) เพื่อรวบรวมส่งให้สำนักงานปลัดกระทรวงศึกษาธิการ และกระทรวงการคลังตามลำดับ
                                </div>
                                <div style="background: #ffffff; border: 1px solid #86efac; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #166534; font-weight: 600;">
                                    ✅ จัดส่งรายงานในวันที่ 9 ต.ค. 2569 ทันตามกำหนดเวลาภายใน 90 วัน
                                </div>
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

print("SUCCESS: Updated topics 3, 4, 5, 6 based on real structure!")
