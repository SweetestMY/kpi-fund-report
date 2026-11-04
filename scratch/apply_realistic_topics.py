# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# ==============================================================
# 1. VIEW-TOPIC-3: 3 Real Milestones (น้ำหนัก 45%)
# ==============================================================
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
                        <div class="rstep-card active-target"><div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div><div contenteditable="true" id="t3-r5" class="rstep-desc">ผ่านระดับ 4 + วิเคราะห์ Cost-Benefit + กก.บริหารฯ เห็นชอบในไตรมาส 2</div></div>
                    </div>

                    <!-- 3 Real Operational Milestones (Large, Concise Cards) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 6px 0;">
                        <div style="font-size: 15px; font-weight: 800; color: #004b87; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>ผลการดำเนินงาน 3 ขั้นตอนสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div class="flow-steps-row" style="padding: 20px 16px; background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; gap: 14px;">
                            <!-- Milestone 1 -->
                            <div class="flow-step-item step-complete" style="padding: 16px 14px; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                    <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 1</span>
                                    <span style="font-size: 18px;">🔍</span>
                                </div>
                                <span contenteditable="true" id="t3-s1-t" class="flow-step-title" style="font-size: 15px; font-weight: 800; color: #003666; margin: 6px 0;">1. ระบุความเสี่ยง 4 ด้าน 8 ปัจจัย</span>
                                <span contenteditable="true" id="t3-s1-d" class="flow-step-desc" style="font-size: 13px; color: #334155; line-height: 1.55;">ระบุปัจจัยเสี่ยงระดับองค์กร 4 ด้าน (กลยุทธ์ 3, ปฏิบัติงาน 3, การเงิน 1, กฎ/ระเบียบ 1) รวม 8 ปัจจัยเสี่ยง เชื่อมโยงกับเป้าหมายประจำปี 2569 และปัจจัยเสี่ยงตกค้างปี 2568</span>
                            </div>

                            <span class="flow-arrow" style="font-size: 22px;">➔</span>

                            <!-- Milestone 2 -->
                            <div class="flow-step-item step-complete" style="padding: 16px 14px; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                    <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 2</span>
                                    <span style="font-size: 18px;">📊</span>
                                </div>
                                <span contenteditable="true" id="t3-s2-t" class="flow-step-title" style="font-size: 15px; font-weight: 800; color: #003666; margin: 6px 0;">2. ประเมินความรุนแรง & Risk Profile</span>
                                <span contenteditable="true" id="t3-s2-d" class="flow-step-desc" style="font-size: 13px; color: #334155; line-height: 1.55;">ประเมินระดับความรุนแรงทั้งโอกาส (Likelihood) และผลกระทบ (Impact) ครบทุก 8 ปัจจัยเสี่ยงจากฐานข้อมูลจริง จัดทำ Risk Profile และกำหนด 4 แผนบริหารความเสี่ยง</span>
                            </div>

                            <span class="flow-arrow" style="font-size: 22px;">➔</span>

                            <!-- Milestone 3 -->
                            <div class="flow-step-item step-complete" style="padding: 16px 14px; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                    <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 3</span>
                                    <span style="font-size: 18px;">⚖️</span>
                                </div>
                                <span contenteditable="true" id="t3-s3-t" class="flow-step-title" style="font-size: 15px; font-weight: 800; color: #003666; margin: 6px 0;">3. Cost-Benefit & กก. เห็นชอบ</span>
                                <span contenteditable="true" id="t3-s3-d" class="flow-step-desc" style="font-size: 13px; color: #334155; line-height: 1.55;">วิเคราะห์ความคุ้มค่า Cost-Benefit ในทุกทางเลือก คัดเลือกทางเลือกที่ดีที่สุด และผ่านความเห็นชอบจากคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ในไตรมาสที่ 2 (16 ธ.ค. 68)</span>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t3-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> ดำเนินการบริหารความเสี่ยงครบถ้วนทุกขั้นตอน มีการระบุความเสี่ยง 4 ด้าน 8 ปัจจัย ประเมินความรุนแรง จัดทำ Risk Profile 4 แผนงาน วิเคราะห์ Cost-Benefit และผ่านความเห็นชอบคณะกรรมการบริหารฯ ภายในไตรมาส 2 ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
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

# ==============================================================
# 2. VIEW-TOPIC-4: 3 Real Pillars (น้ำหนัก 5%)
# ==============================================================
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
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div><div contenteditable="true" id="t4-r4" class="rstep-desc">กำหนด Control Activity ครบทุกกระบวนการหลัก แต่ไม่ครบทุกกระบวนการย่อย</div></div>
                        <div class="rstep-card active-target"><div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div><div contenteditable="true" id="t4-r5" class="rstep-desc">กำหนด Control Activity ครบทุกกระบวนการหลักและย่อย พร้อมทบทวนตาม Workflow</div></div>
                    </div>

                    <!-- 3 Real Control Activity Pillars (Large, Concise Cards) -->
                    <div style="flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 6px 0;">
                        <div style="font-size: 15px; font-weight: 800; color: #004b87; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                            <span>📋</span>
                            <span>กิจกรรมการควบคุมภายใน 3 เสาหลักสำคัญ (ตามเอกสารทางการ ก.ค.ศ.):</span>
                        </div>
                        
                        <div class="flow-steps-row" style="padding: 20px 16px; background: #f8fbfe; border: 1.5px solid #b8d4ed; border-radius: 12px; gap: 14px;">
                            <!-- Pillar 1 -->
                            <div class="flow-step-item step-complete" style="padding: 16px 14px; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                    <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">เสาหลักที่ 1 (ปค.5)</span>
                                    <span style="font-size: 18px;">🛡️</span>
                                </div>
                                <span contenteditable="true" id="t4-s1-t" class="flow-step-title" style="font-size: 15px; font-weight: 800; color: #003666; margin: 6px 0;">1. กิจกรรมควบคุม 3 กระบวนงานหลัก</span>
                                <span contenteditable="true" id="t4-s1-d" class="flow-step-desc" style="font-size: 13px; color: #334155; line-height: 1.55;">กำหนดกิจกรรมควบคุม (Control Activity) ของกระบวนงานสำคัญครบถ้วน 3 กระบวนงานตามแบบ ปค.5 ได้แก่ 1) การจัดสรรเงินให้กู้ยืม 2) การกำกับติดตามหนี้ค้างชำระ และ 3) การบังคับคดีกับลูกหนี้ตามคำพิพากษา (เอกสารหมายเลข 4)</span>
                            </div>

                            <span class="flow-arrow" style="font-size: 22px;">➔</span>

                            <!-- Pillar 2 -->
                            <div class="flow-step-item step-complete" style="padding: 16px 14px; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                    <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">เสาหลักที่ 2 (ผังระบบ)</span>
                                    <span style="font-size: 18px;">🔄</span>
                                </div>
                                <span contenteditable="true" id="t4-s2-t" class="flow-step-title" style="font-size: 15px; font-weight: 800; color: #003666; margin: 6px 0;">2. จัดทำผัง 12 Workflows</span>
                                <span contenteditable="true" id="t4-s2-d" class="flow-step-desc" style="font-size: 13px; color: #334155; line-height: 1.55;">กำหนดขั้นตอนการทำงานอย่างเป็นระบบผ่าน Work Flow รวม 12 กระบวนงาน ครอบคลุม 3 กระบวนงานหลักสำคัญ, 2 กระบวนงานสนับสนุน (ด้านการบริหาร และด้านการเงินและบัญชี), และ 7 กระบวนงานย่อย (เอกสารหมายเลข 6)</span>
                            </div>

                            <span class="flow-arrow" style="font-size: 22px;">➔</span>

                            <!-- Pillar 3 -->
                            <div class="flow-step-item step-complete" style="padding: 16px 14px; flex: 1;">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                    <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">เสาหลักที่ 3 (แผนปี 69)</span>
                                    <span style="font-size: 18px;">📈</span>
                                </div>
                                <span contenteditable="true" id="t4-s3-t" class="flow-step-title" style="font-size: 15px; font-weight: 800; color: #003666; margin: 6px 0;">3. ทบทวนสอดคล้องตามแผนปี 2569</span>
                                <span contenteditable="true" id="t4-s3-d" class="flow-step-desc" style="font-size: 13px; color: #334155; line-height: 1.55;">ทบทวนกิจกรรมควบคุมให้สอดคล้องตาม Workflow และแผนปฏิบัติการเงินทุนหมุนเวียน ประจำปีบัญชี 2569 ที่กำหนดวงเงินจัดสรรให้กู้ยืม 250 ล้านบาท และการติดตามหนี้ค้างชำระอย่างเคร่งครัด (เอกสารหมายเลข 8)</span>
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

# ==============================================================
# 3. VIEW-TOPIC-5: 2 Real Sub-criteria (น้ำหนัก 30%) - FILLS CANVAS NICELY
# ==============================================================
new_v5 = """<div class="topic-view" id="view-topic-5">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t5-title" style="font-size: 16px; font-weight: 800; color: #003666;">📡 5. สารสนเทศและการสื่อสาร (น้ำหนัก 30% - รวม 2 ประเด็นพิจารณา)</span>
                        <span contenteditable="true" id="t5-badge" class="panel-title-badge" style="background: #e0f2fe; color: #0284c7; border-color: #bae6fd;">น้ำหนัก 30% | ผลงานระดับ 5.0000 เต็ม</span>
                    </div>

                    <!-- 2 Sub-criteria Scorecard Banner -->
                    <div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 14px;">
                        <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 10px 16px; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="font-size: 13.5px; font-weight: 800; color: #166534;">ประเด็นที่ 1: การใช้สารสนเทศติดตาม 4 ด้าน 13 กิจกรรม (น้ำหนัก 20%)</span>
                                <div style="font-size: 12px; color: #15803d; margin-top: 2px;">ติดตามผ่านระบบสารสนเทศ ความรุนแรงลดลงตามเป้าหมาย</div>
                            </div>
                            <span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (1.0000)</span>
                        </div>
                        <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 10px 16px; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="font-size: 13.5px; font-weight: 800; color: #166534;">ประเด็นที่ 2: การทบทวนแผนระหว่างปี 2 ครั้ง (น้ำหนัก 10%)</span>
                                <div style="font-size: 12px; color: #15803d; margin-top: 2px;">ทบทวนไตรมาส 2 (อนุกรรมการฯ) และไตรมาส 3 (กก.บริหารฯ)</div>
                            </div>
                            <span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.5000)</span>
                        </div>
                    </div>

                    <!-- 2 Executive Showcase Cards Filling the Canvas -->
                    <div style="flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; gap: 14px; margin: 4px 0;">
                        <!-- Left Card: Sub-criterion 1 (20%) -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 16px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                <div style="font-size: 14.5px; font-weight: 800; color: #003666; display: flex; align-items: center; gap: 6px;">
                                    <span>💻</span>
                                    <span>ประเด็นที่ 1: การใช้สารสนเทศติดตามความเสี่ยง (4 ด้าน 13 กิจกรรม)</span>
                                </div>
                                <span style="font-size: 12px; font-weight: 800; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 4px;">น้ำหนัก 20%</span>
                            </div>

                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; flex: 1;">
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-radius: 8px; padding: 8px 12px;">
                                    <div style="font-size: 13px; font-weight: 800; color: #004b87; margin-bottom: 4px;">🎯 1. ด้านกลยุทธ์ (3 กิจกรรม)</div>
                                    <div style="font-size: 12px; color: #334155; line-height: 1.45;">หนังสือจัดสรรวงเงินกู้ยืม, กำกับปฏิทินปฏิบัติงาน, และขับเคลื่อน No Gift Policy</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-radius: 8px; padding: 8px 12px;">
                                    <div style="font-size: 13px; font-weight: 800; color: #004b87; margin-bottom: 4px;">⚙️ 2. ด้านการปฏิบัติงาน (4 กิจกรรม)</div>
                                    <div style="font-size: 12px; color: #334155; line-height: 1.45;">ตรวจฐานข้อมูลหนี้, ติดตามยอดหนี้คงเหลือ, กำกับหนี้โอนย้าย, และประชุมติดตาม</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-radius: 8px; padding: 8px 12px;">
                                    <div style="font-size: 13px; font-weight: 800; color: #004b87; margin-bottom: 4px;">💰 3. ด้านการเงิน (4 กิจกรรม)</div>
                                    <div style="font-size: 12px; color: #334155; line-height: 1.45;">เร่งรัดรายงานการเงิน, ปรับปรุงระบบบัญชี, ควบคุมงบการเงิน, และพัฒนาบุคลากร</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-radius: 8px; padding: 8px 12px;">
                                    <div style="font-size: 13px; font-weight: 800; color: #004b87; margin-bottom: 4px;">⚖️ 4. ด้านกฎ/ระเบียบ (2 กิจกรรม)</div>
                                    <div style="font-size: 12px; color: #334155; line-height: 1.45;">แจ้งหลักเกณฑ์การหักเงินส่งชำระหนี้ และกำกับติดตาม สพท./ธ.ก.ส.</div>
                                </div>
                            </div>

                            <div style="background: #eefbf3; border: 1px solid #86efac; border-radius: 6px; padding: 7px 12px; font-size: 12.5px; color: #166534; font-weight: 700;">
                                ✅ ผลสัมฤทธิ์: ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมายครบถ้วนทุกด้าน (เอกสารหมายเลข 3)
                            </div>
                        </div>

                        <!-- Right Card: Sub-criterion 2 (10%) -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 16px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                <div style="font-size: 14.5px; font-weight: 800; color: #003666; display: flex; align-items: center; gap: 6px;">
                                    <span>🔄</span>
                                    <span>ประเด็นที่ 2: การทบทวนแผนระหว่างปี (2 ครั้ง)</span>
                                </div>
                                <span style="font-size: 12px; font-weight: 800; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 4px;">น้ำหนัก 10%</span>
                            </div>

                            <div style="display: flex; flex-direction: column; gap: 10px; flex: 1; justify-content: center;">
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0284c7; border-radius: 8px; padding: 10px 14px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                                        <span style="font-size: 13.5px; font-weight: 800; color: #003666;">🏛️ ครั้งที่ 1 (ไตรมาสที่ 2)</span>
                                        <span style="font-size: 11.5px; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 1px 6px; border-radius: 4px;">27 มี.ค. 2569</span>
                                    </div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">คณะอนุกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติรับทราบผลการทบทวนแผนบริหารความเสี่ยง ในคราวประชุมครั้งที่ 3/2569 ความรุนแรงลดลง จึงคงมาตรการเดิม</div>
                                </div>

                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #16a34a; border-radius: 8px; padding: 10px 14px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                                        <span style="font-size: 13.5px; font-weight: 800; color: #003666;">🏛️ ครั้งที่ 2 (ไตรมาสที่ 3)</span>
                                        <span style="font-size: 11.5px; font-weight: 700; color: #16a34a; background: #dcfce7; padding: 1px 6px; border-radius: 4px;">26 มิ.ย. 2569</span>
                                    </div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">คณะกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติรับทราบผลการทบทวนแผนบริหารความเสี่ยง ในคราวประชุมครั้งที่ 3/2569 ความรุนแรงลดลงต่อเนื่อง (เอกสารหมายเลข 3.5)</div>
                                </div>
                            </div>

                            <div style="background: #eefbf3; border: 1px solid #86efac; border-radius: 6px; padding: 7px 12px; font-size: 12.5px; color: #166534; font-weight: 700;">
                                ✅ ผลสัมฤทธิ์: ดำเนินการทบทวนแผนระหว่างปีครบถ้วน 2 ครั้งตามเกณฑ์มาตรฐาน
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t5-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ ใช้ระบบสารสนเทศสนับสนุนการติดตามการดำเนินกิจกรรมครบ 4 ด้าน 13 กิจกรรม ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมาย และผ่านการทบทวนความเหมาะสมของแผนระหว่างปีครบ 2 ครั้ง ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
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

# ==============================================================
# 4. VIEW-TOPIC-6: 2 Real Sub-criteria (น้ำหนัก 5%)
# ==============================================================
new_v6 = """<div class="topic-view" id="view-topic-6">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t6-title" style="font-size: 16px; font-weight: 800; color: #003666;">📊 6. การติดตามผลและการประเมินผล (น้ำหนัก 5% - รวม 2 ประเด็นพิจารณา)</span>
                        <span contenteditable="true" id="t6-badge" class="panel-title-badge">น้ำหนัก 5% | ผลงานระดับ 5.0000 เต็ม</span>
                    </div>

                    <!-- 2 Sub-criteria Scorecard Banner -->
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                        <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 10px 16px; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="font-size: 13.5px; font-weight: 800; color: #166534;">ประเด็นที่ 1: การประเมินผลการควบคุมภายใน (น้ำหนัก 2%)</span>
                                <div style="font-size: 12px; color: #15803d; margin-top: 2px;">ครอบคลุม 3 ภารกิจหลัก และประชุมติดตามผลครบ 3 ครั้ง</div>
                            </div>
                            <span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.1000)</span>
                        </div>
                        <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 10px 16px; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="font-size: 13.5px; font-weight: 800; color: #166534;">ประเด็นที่ 2: การส่งรายงานให้ต้นสังกัดใน 90 วัน (น้ำหนัก 3%)</span>
                                <div style="font-size: 12px; color: #15803d; margin-top: 2px;">จัดส่งให้สำนักงาน ก.ค.ศ. วันที่ 9 ต.ค. 2569 ทันตามกำหนด</div>
                            </div>
                            <span style="background: #16a34a; color: #ffffff; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px;">ระดับ 5 (0.1500)</span>
                        </div>
                    </div>

                    <!-- 2 Executive Showcase Cards Filling the Canvas -->
                    <div style="flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 4px 0;">
                        <!-- Left Card: Sub-criterion 1 (2%) -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 16px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                <div style="font-size: 14.5px; font-weight: 800; color: #003666; display: flex; align-items: center; gap: 6px;">
                                    <span>📝</span>
                                    <span>ประเด็นที่ 1: การประเมินผลการควบคุมภายใน (2%)</span>
                                </div>
                                <span style="font-size: 12px; font-weight: 800; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 4px;">น้ำหนัก 2%</span>
                            </div>

                            <div style="display: flex; flex-direction: column; gap: 10px; flex: 1; justify-content: center;">
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #005691; border-radius: 8px; padding: 9px 12px;">
                                    <div style="font-size: 13px; font-weight: 800; color: #003666; margin-bottom: 2px;">1. แต่งตั้งคณะทำงานจัดทำรายงาน</div>
                                    <div style="font-size: 12px; color: #334155; line-height: 1.45;">แต่งตั้งคณะทำงานจัดทำรายงานผลการควบคุมภายในของสำนักงาน ก.ค.ศ. ประจำปีงบประมาณ พ.ศ. 2569 (เอกสารหมายเลข 9)</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0077b6; border-radius: 8px; padding: 9px 12px;">
                                    <div style="font-size: 13px; font-weight: 800; color: #003666; margin-bottom: 2px;">2. ประเมินครอบคลุม 3 ภารกิจหลัก</div>
                                    <div style="font-size: 12px; color: #334155; line-height: 1.45;">ครอบคลุมภารกิจหลักและกระบวนงานสำคัญ: 1) การจัดสรรเงินให้กู้ยืม 2) การกำกับติดตามหนี้ค้างชำระ และ 3) การบังคับคดีลูกหนี้ (เอกสารหมายเลข 10)</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0096c7; border-radius: 8px; padding: 9px 12px;">
                                    <div style="font-size: 13px; font-weight: 800; color: #003666; margin-bottom: 2px;">3. ประชุมติดตามผลครบ 3 ครั้ง</div>
                                    <div style="font-size: 12px; color: #334155; line-height: 1.45;">ประชุมติดตามผล 3 ครั้ง: ครั้งที่ 1 (21 ม.ค. 69), ครั้งที่ 2 (25 พ.ค. 69), ครั้งที่ 3 (21 ส.ค. 69) (เอกสารหมายเลข 11)</div>
                                </div>
                            </div>

                            <div style="background: #eefbf3; border: 1px solid #86efac; border-radius: 6px; padding: 7px 12px; font-size: 12.5px; color: #166534; font-weight: 700;">
                                ✅ ผลสัมฤทธิ์: ประเมินครบ 3 ภารกิจหลัก และประชุมติดตามผลครบ 3 ครั้งตามเกณฑ์
                            </div>
                        </div>

                        <!-- Right Card: Sub-criterion 2 (3%) -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 16px 18px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4e5f4; padding-bottom: 8px;">
                                <div style="font-size: 14.5px; font-weight: 800; color: #003666; display: flex; align-items: center; gap: 6px;">
                                    <span>📬</span>
                                    <span>ประเด็นที่ 2: การจัดส่งรายงานให้ต้นสังกัดทันเวลา (3%)</span>
                                </div>
                                <span style="font-size: 12px; font-weight: 800; color: #0369a1; background: #e0f2fe; padding: 2px 8px; border-radius: 4px;">น้ำหนัก 3%</span>
                            </div>

                            <div style="display: flex; flex-direction: column; gap: 10px; flex: 1; justify-content: center;">
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #16a34a; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #166534; margin-bottom: 4px;">📅 จัดส่งรายงานสำเร็จ: วันที่ 9 ตุลาคม 2569</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">เงินทุนหมุนเวียนฯ จัดส่งรายงานประเมินผลการควบคุมภายในให้สำนักงาน ก.ค.ศ. ภายในระยะเวลาที่กำหนด โดยจัดส่งในวันที่ 9 ตุลาคม 2569 (เอกสารหมายเลข 12)</div>
                                </div>

                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0284c7; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #003666; margin-bottom: 4px;">⏱️ ทันตามกรอบเวลา 90 วันที่กำหนด</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">ดำเนินการแล้วเสร็จทันตามหลักเกณฑ์กระทรวงการคลังฯ (ภายใน 90 วัน นับแต่วันสิ้นปีบัญชี) เพื่อสำนักงาน ก.ค.ศ. รวบรวมส่ง สป.ศธ. และกระทรวงการคลังตามลำดับ</div>
                                </div>
                            </div>

                            <div style="background: #eefbf3; border: 1px solid #86efac; border-radius: 6px; padding: 7px 12px; font-size: 12.5px; color: #166534; font-weight: 700;">
                                ✅ ผลสัมฤทธิ์: จัดส่งรายงานวันที่ 9 ต.ค. 2569 ทันตามกรอบ 90 วันอย่างสมบูรณ์
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t6-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ มีการประเมินผลการควบคุมภายในครอบคลุม 3 ภารกิจหลัก มีการประชุมติดตามผล 3 ครั้ง และจัดส่งรายงานการประเมินผลให้หน่วยงานต้นสังกัดได้ทันภายในกรอบ 90 วัน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
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

# Replace in text
pattern = r'(<div class="topic-view" id="view-topic-3">[\s\S]*?)(?=\s*</div>\s*<!-- FOOTER BAR -->)'
assert re.search(pattern, text), "Cannot find view-topic-3 to 6 section"

replacement = f"{new_v3}\n\n            <!-- ========================================== -->\n            <!-- VIEW 4: TOPIC 4 กิจกรรมการควบคุมภายใน (5%) -->\n            <!-- ========================================== -->\n            {new_v4}\n\n            <!-- ========================================== -->\n            <!-- VIEW 5: TOPIC 5 สารสนเทศและการสื่อสาร (30%) -->\n            <!-- ========================================== -->\n            {new_v5}\n\n            <!-- ========================================== -->\n            <!-- VIEW 6: TOPIC 6 ติดตามและประเมินผล (5%) -->\n            <!-- ========================================== -->\n            {new_v6}"

text_new = re.sub(pattern, replacement, text, count=1)

# Bump STORAGE_KEY_PREFIX to v3 to ensure completely fresh render
text_new = text_new.replace("const STORAGE_KEY_PREFIX = 'kpi_official_41_v2_Q';", "const STORAGE_KEY_PREFIX = 'kpi_official_41_v3_Q';")
text_new = text_new.replace("const STORAGE_KEY_PREFIX = 'kpi_official_41_Q';", "const STORAGE_KEY_PREFIX = 'kpi_official_41_v3_Q';")

with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text_new)

print("SUCCESS: Updated Views 3, 4, 5, 6 in ตัวชี้วัดที่ 4.1.html!")
