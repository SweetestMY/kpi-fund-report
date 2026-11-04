# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

old_v2_match = re.search(r'(<div class="topic-view" id="view-topic-2">.*?)(?=\s*<!-- ==========================================\s*-->\s*<!-- VIEW 3:)', text, re.DOTALL)
assert old_v2_match, "view-topic-2 match not found"

new_v2 = """<div class="topic-view" id="view-topic-2">
                <div class="panel-box" style="padding: 18px 22px; justify-content: space-between; gap: 14px;">
                    <div class="panel-title-line">
                        <span contenteditable="true" id="t2-title" style="font-size: 16px; font-weight: 800; color: #003666;">🎯 2. การกำหนดวัตถุประสงค์การบริหารความเสี่ยง (น้ำหนัก 8%) - การจัดทำ/ทบทวนคู่มือ</span>
                        <span contenteditable="true" id="t2-badge" class="panel-title-badge">น้ำหนัก 8% | ผลงานระดับ 5</span>
                    </div>

                    <!-- Progressive Rubric 1-5 -->
                    <div class="rubric-5step-grid">
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div><div contenteditable="true" id="t2-r1" class="rstep-desc">กำหนดผู้รับผิดชอบ/คณะทำงานในการจัดทำ/ทบทวนคู่มือ</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div><div contenteditable="true" id="t2-r2" class="rstep-desc">จัดทำคู่มือแล้วเสร็จ แต่องค์ประกอบยังไม่ครบถ้วน</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div><div contenteditable="true" id="t2-r3" class="rstep-desc">จัดทำคู่มือแล้วเสร็จ โดยมีองค์ประกอบของคู่มือที่ดีครบถ้วน</div></div>
                        <div class="rstep-card"><div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div><div contenteditable="true" id="t2-r4" class="rstep-desc">ครบตามระดับ 3 และผ่านความเห็นชอบคณะกรรมการฯ ในไตรมาส 1</div></div>
                        <div class="rstep-card active-target"><div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div><div contenteditable="true" id="t2-r5" class="rstep-desc">ครบตามระดับ 4 และเผยแพร่คู่มือให้ผู้บริหารและพนักงานในองค์กร</div></div>
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
                                <span contenteditable="true" id="t2-s1-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">ทบทวนคู่มือเดิม</span>
                                <span contenteditable="true" id="t2-s1-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ดำเนินการทบทวนคู่มือการบริหารความเสี่ยงเดิม</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 2</span>
                                <span contenteditable="true" id="t2-s2-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">แต่งตั้งคณะทำงาน</span>
                                <span contenteditable="true" id="t2-s2-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ตั้งคณะทำงานบริหารความเสี่ยงฯ (คำสั่งที่ 3/2568 ลว. 15 ต.ค. 68)</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 3</span>
                                <span contenteditable="true" id="t2-s3-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">จัดประชุมสัมมนา</span>
                                <span contenteditable="true" id="t2-s3-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">12-14 พ.ย. 68 ณ ชลบุรี มีองค์ประกอบคู่มือที่ดีครบถ้วน</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 4</span>
                                <span contenteditable="true" id="t2-s4-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">คณะกรรมการฯ เห็นชอบ</span>
                                <span contenteditable="true" id="t2-s4-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">ผ่านความเห็นชอบ กก.บริหารฯ มติ 8/2568 (16 ธ.ค. 68 ไตรมาส 1)</span>
                            </div>
                            <span class="flow-arrow" style="font-size: 16px;">➔</span>
                            <div class="flow-step-item step-complete" style="padding: 14px 10px;">
                                <span class="flow-step-num" style="font-size: 13px; font-weight: 800;">ขั้นตอนที่ 5</span>
                                <span contenteditable="true" id="t2-s5-t" class="flow-step-title" style="font-size: 13.5px; font-weight: 800; color: #003666; margin: 4px 0;">แจ้งเวียนเผยแพร่</span>
                                <span contenteditable="true" id="t2-s5-d" class="flow-step-desc" style="font-size: 12px; color: #334155; line-height: 1.45;">แจ้งเวียนผู้บริหารและบุคลากรทราบ (ศธ 0206.8/1142 ลว. 25 ธ.ค. 68)</span>
                            </div>
                        </div>
                    </div>

                    <!-- Summary & Score -->
                    <div class="grid-split" style="gap: 14px;">
                        <div class="callout-strip" style="padding: 14px 18px; display: flex; align-items: center;">
                            <div contenteditable="true" id="t2-callout" style="font-size: 13.5px; line-height: 1.6;">
                                <strong style="color: #004b87;">สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ ดำเนินการครบถ้วนทั้ง 5 ขั้นตอน มีคู่มือการบริหารความเสี่ยงที่มีองค์ประกอบที่ดีครบถ้วน ผ่านความเห็นชอบจากคณะกรรมการบริหารฯ ภายในไตรมาสที่ 1 และแจ้งเวียนเผยแพร่ทั่วทั้งองค์กร ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="padding: 14px 22px;">
                            <div>
                                <div contenteditable="true" id="t2-sc-lbl" class="score-lbl" style="font-size: 13.5px;">ผลการดำเนินงานข้อที่ 2 (น้ำหนัก 8%)</div>
                                <div contenteditable="true" id="t2-sc-val" class="big-score-val" style="font-size: 26px;">ระดับ 5.0000 คะแนน</div>
                            </div>
                            <div contenteditable="true" id="t2-sc-stars" class="score-pill-stars" style="font-size: 22px;">⭐⭐⭐⭐⭐</div>
                        </div>
                    </div>
                </div>
            </div>"""

text = text[:old_v2_match.start()] + new_v2 + text[old_v2_match.end():]

with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated view-topic-2 successfully!")
