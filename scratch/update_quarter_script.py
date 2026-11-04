# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# New comprehensive script section
new_quarter_logic = """        const STORAGE_KEY_PREFIX = 'kpi_official_41_v6_Q';

        function getStorageKey(q) {
            return `${STORAGE_KEY_PREFIX}${q}`;
        }

        function showToast(msg) {
            const toast = document.getElementById('toast-notification');
            if (!toast) return;
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 2200);
        }

        /* Quarter Defaults based strictly on Official Documents (Q1, Q2, Q3, Q4) */
        const quarterDefaults41 = {
            1: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 1 (ต.ค. - ธ.ค. 2568)",
                // View 0 (Overview Table)
                ovR1Score: "5.0000", ovR1Weighted: "0.3500",
                ovR2Score: "5.0000", ovR2Weighted: "0.4000",
                ovR3Score: "5.0000", ovR3Weighted: "2.2500",
                ovR4Score: "3.0000", ovR4Weighted: "0.1500",
                ovR5Score: "1.0000", ovR5Weighted: "0.3000",
                ovR6Score: "N/A*", ovR6Weighted: "0.0200",
                ovTotSc: "ระดับ 3.5 (เบื้องต้น)",
                ovTotWeighted: "3.4700",
                ovScVal: "ระดับ 3.4700 คะแนน",
                ovScStars: "⭐⭐⭐",
                ovSumP: "ไตรมาสที่ 1 (ต.ค. - ธ.ค. 2568): ดำเนินงานบรรลุเป้าหมายระยะเริ่มต้น ผ่านความเห็นชอบคู่มือและแผนบริหารความเสี่ยงครบถ้วนในไตรมาสที่ 1 (16 ธ.ค. 68), มีระบบรับข้อร้องเรียน 5 ช่องทาง, กำหนดกิจกรรมควบคุม 3 กระบวนงานหลัก อยู่ระหว่างขับเคลื่อนแผนงานและเตรียมการประชุมติดตามผล",
                ovSt1Val: "เริ่มต้น 4 ข้อ",
                ovSt2Val: "ระดับ 3.47 (เบื้องต้น)",

                // View 4 (กิจกรรมการควบคุมภายใน 5%)
                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 3",
                t4ActiveLevel: 3,
                t4S1D: "กำหนดกิจกรรมควบคุม (Control Activity) ของกระบวนงานสำคัญครบถ้วน 3 กระบวนงานตามแบบ ปค.5 ได้แก่ 1) การจัดสรรเงินให้กู้ยืม 2) การกำกับติดตามหนี้ค้างชำระ และ 3) การบังคับคดีกับลูกหนี้ตามคำพิพากษา (เอกสารหมายเลข 4)",
                t4S2D: "⏳ อยู่ระหว่างดำเนินการ: รวบรวมและจัดทำผัง Work Flow 12 กระบวนงาน (3 สำคัญ, 2 สนับสนุน, 7 ย่อย)",
                t4S3D: "⏳ อยู่ระหว่างดำเนินการ: ทบทวนกิจกรรมควบคุมให้สอดคล้องตามแผนปฏิบัติการประจำปีบัญชี 2569",
                t4Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 1):</strong> เงินทุนหมุนเวียนฯ มีการกำหนดกิจกรรมการควบคุม 3 กระบวนงานหลักตามแบบ ปค.5 ครบถ้วน อยู่ระหว่างการรวบรวมจัดทำผัง Work Flow 12 กระบวนงาน ผลการดำเนินงานไตรมาสที่ 1 เทียบเท่าระดับ 3.0000 คะแนน",
                t4ScVal: "ระดับ 3.0000 คะแนน",
                t4ScStars: "⭐⭐⭐",

                // View 5 (สารสนเทศและการสื่อสาร 30%)
                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 1.0000",
                t5P1Badge: "ระดับ 1 (0.2000)",
                t5P2Badge: "ระดับ 1 (0.1000)",
                t5P1Achieve: "⏳ ผลสัมฤทธิ์ (ไตรมาส 1): อยู่ระหว่างเริ่มต้นดำเนินกิจกรรมตามแผนบริหารความเสี่ยง (< 50% ของแผน)",
                t5P2M1: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">⏳ ครั้งที่ 1 (กำหนดไตรมาสที่ 2)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #64748b; background: #f1f5f9; padding: 1px 6px; border-radius: 4px;">มีนาคม 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">กำหนดเสนอคณะอนุกรรมการบริหารเงินทุนหมุนเวียนฯ เพื่อทบทวนความเหมาะสมของแผนบริหารความเสี่ยงในไตรมาสที่ 2</div>`,
                t5P2M2: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">⏳ ครั้งที่ 2 (กำหนดไตรมาสที่ 3)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #64748b; background: #f1f5f9; padding: 1px 6px; border-radius: 4px;">มิถุนายน 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">กำหนดเสนอคณะกรรมการบริหารเงินทุนหมุนเวียนฯ เพื่อทบทวนความเหมาะสมของแผนบริหารความเสี่ยงในไตรมาสที่ 3</div>`,
                t5P2Achieve: "⏳ ผลสัมฤทธิ์ (ไตรมาส 1): ยังไม่ถึงรอบการทบทวนแผนบริหารความเสี่ยงระหว่างปี",
                t5Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 1):</strong> เงินทุนหมุนเวียนฯ อยู่ระหว่างเริ่มต้นดำเนินกิจกรรมตามแผนบริหารความเสี่ยง (< 50%) และยังไม่ถึงรอบการทบทวนแผนระหว่างปี ผลการดำเนินงานเทียบเท่าระดับ 1.0000 คะแนน",
                t5ScVal: "ระดับ 1.0000 คะแนน",
                t5ScStars: "⭐",

                // View 6 (การติดตามผลและการประเมินผล 5%)
                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 1.0000",
                t6P1Badge: "ระดับ 1 (0.0200)",
                t6P2Badge: "N/A (รอผลสิ้นปี)",
                t6P1Achieve: "⏳ ผลสัมฤทธิ์ (ไตรมาส 1): แต่งตั้งคณะทำงานจัดทำรายงานแล้ว อยู่ระหว่างรอรอบประชุมติดตามผล (ระดับ 1)",
                t6P2Container: `<div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #64748b; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #475569; margin-bottom: 4px;">⏳ อยู่ระหว่างรอบัญชีสิ้นปีงบประมาณ</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">การจัดส่งรายงานการประเมินผลการควบคุมภายใน กำหนดส่งให้หน่วยงานต้นสังกัดภายใน 90 วัน นับแต่วันสิ้นปีบัญชี (สิ้นสุด 30 ก.ย. 69)</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0284c7; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #003666; margin-bottom: 4px;">📅 กำหนดส่งตามเกณฑ์: ต.ค. - ธ.ค. 2569</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">สำนักงาน ก.ค.ศ. จะรวบรวมเพื่อจัดส่งให้ สป.ศธ. และกระทรวงการคลังตามลำดับต่อไป (ผลการประเมินในไตรมาส 1 เป็น N/A)</div>
                                </div>`,
                t6P2Achieve: "⏳ สถานะ (ไตรมาส 1): รอการจัดส่งรายงานเมื่อสิ้นสุดปีงบประมาณภายใน 90 วัน (N/A)",
                t6Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 1):</strong> มีการแต่งตั้งคณะทำงานจัดทำรายงานผลการควบคุมภายใน (คำสั่งที่ 3/2568) อยู่ระหว่างรอการประชุมติดตามผลครั้งที่ 1 ในไตรมาส 2 และรอผลสิ้นปีงบประมาณสำหรับข้อ 6.2",
                t6ScVal: "ระดับ 1.0000 คะแนน",
                t6ScStars: "⭐"
            },
            2: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 2 (ต.ค. - มี.ค. 2569)",
                // View 0 (Overview Table)
                ovR1Score: "5.0000", ovR1Weighted: "0.3500",
                ovR2Score: "5.0000", ovR2Weighted: "0.4000",
                ovR3Score: "5.0000", ovR3Weighted: "2.2500",
                ovR4Score: "3.0000", ovR4Weighted: "0.1500",
                ovR5Score: "2.3333", ovR5Weighted: "0.7000",
                ovR6Score: "N/A (5.0)*", ovR6Weighted: "0.1000",
                ovTotSc: "ระดับ 4 (3.95)",
                ovTotWeighted: "3.9500",
                ovScVal: "ระดับ 3.9500 คะแนน",
                ovScStars: "⭐⭐⭐⭐",
                ovSumP: "ไตรมาสที่ 2 (ตามเอกสารทางการ): บรรลุระดับ 5.0000 ในข้อ 1, 2, 3 และ 6.1; ข้อ 4 อยู่ที่ระดับ 3 (ควบคุม 3 กระบวนงานหลัก); ข้อ 5 ติดตามสารสนเทศได้ 50-79% (ระดับ 2) และทบทวนแผนครั้งที่ 1 (27 มี.ค. 69, ระดับ 3); ข้อ 6.2 รอผลสิ้นปีงบประมาณ (N/A)",
                ovSt1Val: "ก้าวหน้า 5 ข้อ",
                ovSt2Val: "ระดับ 4 (3.9500)",

                // View 4 (กิจกรรมการควบคุมภายใน 5%)
                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 3",
                t4ActiveLevel: 3,
                t4S1D: "กำหนดกิจกรรมควบคุม (Control Activity) ของกระบวนงานสำคัญครบถ้วน 3 กระบวนงานตามแบบ ปค.5 ได้แก่ 1) การจัดสรรเงินให้กู้ยืม 2) การกำกับติดตามหนี้ค้างชำระ และ 3) การบังคับคดีกับลูกหนี้ตามคำพิพากษา (เอกสารหมายเลข 4)",
                t4S2D: "⏳ อยู่ระหว่างดำเนินการ: กำลังจัดทำผัง Work Flow 12 กระบวนงาน (3 สำคัญ, 2 สนับสนุน, 7 ย่อย) ให้ครอบคลุมทุกระบบ",
                t4S3D: "⏳ อยู่ระหว่างดำเนินการ: ทบทวนกิจกรรมควบคุมให้สอดคล้องตามแผนปฏิบัติการปี 2569",
                t4Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 2):</strong> เงินทุนหมุนเวียนฯ มีการกำหนดกิจกรรมการควบคุมของกระบวนงานสำคัญครบ 3 กระบวนงานตามแบบ ปค.5 ครบถ้วน แต่ยังอยู่ระหว่างทบทวนผัง Workflow 12 กระบวนงานให้ครบทั้งระบบ ผลการดำเนินงานไตรมาสที่ 2 เทียบเท่าระดับ 3.0000 คะแนน",
                t4ScVal: "ระดับ 3.0000 คะแนน",
                t4ScStars: "⭐⭐⭐",

                // View 5 (สารสนเทศและการสื่อสาร 30%)
                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 2.3333",
                t5P1Badge: "ระดับ 2 (0.4000)",
                t5P2Badge: "ระดับ 3 (0.3000)",
                t5P1Achieve: "⚠️ ผลสัมฤทธิ์ (ไตรมาส 2): ดำเนินกิจกรรมตามแผนได้ร้อยละ 50 - 79 ของแผน (ระดับ 2)",
                t5P2M1: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">🏛️ ครั้งที่ 1 (ไตรมาสที่ 2)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 1px 6px; border-radius: 4px;">27 มี.ค. 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">คณะอนุกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติรับทราบผลการทบทวนแผนบริหารความเสี่ยง ในคราวประชุมครั้งที่ 3/2569 ครอบคลุม 4 ด้าน พบความเสี่ยงลดลง จึงคงมาตรการเดิม</div>`,
                t5P2M2: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">⏳ ครั้งที่ 2 (กำหนดไตรมาสที่ 3)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #64748b; background: #f1f5f9; padding: 1px 6px; border-radius: 4px;">มิถุนายน 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">อยู่ระหว่างรอการเสนอคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ทบทวนแผนความเสี่ยงต่อเนื่องในไตรมาสที่ 3</div>`,
                t5P2Achieve: "⚠️ ผลสัมฤทธิ์ (ไตรมาส 2): ทบทวนแผนระหว่างปีแล้ว 1 ครั้ง ในไตรมาสที่ 2 มติอนุกรรมการฯ 27 มี.ค. 69 (ระดับ 3)",
                t5Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 2):</strong> เงินทุนหมุนเวียนฯ ดำเนินกิจกรรมตามแผนได้ร้อยละ 50 - 79 (ระดับ 2) และได้ดำเนินการทบทวนแผนบริหารความเสี่ยงระหว่างปี ครั้งที่ 1 โดยคณะอนุกรรมการฯ มีมติรับทราบ เมื่อ 27 มี.ค. 69 (ระดับ 3) ผลการดำเนินงานเทียบเท่าระดับ 2.3333 คะแนน",
                t5ScVal: "ระดับ 2.3333 คะแนน",
                t5ScStars: "⭐⭐",

                // View 6 (การติดตามผลและการประเมินผล 5%)
                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 5 (ข้อ 6.1)",
                t6P1Badge: "ระดับ 5 (0.1000)",
                t6P2Badge: "N/A (รอผลสิ้นปี)",
                t6P1Achieve: "✅ ผลสัมฤทธิ์ (ไตรมาส 2): ประเมินครอบคลุม 3 ภารกิจหลัก และประชุมติดตามผลต่อเนื่อง (ระดับ 5)",
                t6P2Container: `<div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #64748b; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #475569; margin-bottom: 4px;">⏳ อยู่ระหว่างรอบัญชีสิ้นปีงบประมาณ</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">การจัดส่งรายงานการประเมินผลการควบคุมภายใน กำหนดส่งให้หน่วยงานต้นสังกัดภายใน 90 วัน นับแต่วันสิ้นปีบัญชี (สิ้นสุด 30 ก.ย. 69)</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0284c7; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #003666; margin-bottom: 4px;">📅 กำหนดส่งตามเกณฑ์: ต.ค. - ธ.ค. 2569</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">สำนักงาน ก.ค.ศ. จะรวบรวมส่งให้ สป.ศธ. และกระทรวงการคลังตามลำดับต่อไป (ผลการประเมินในไตรมาส 2 จึงเป็น N/A รอผลสิ้นปี)</div>
                                </div>`,
                t6P2Achieve: "⏳ สถานะ (ไตรมาส 2): รอส่งรายงานการประเมินผลการควบคุมภายในให้หน่วยงานต้นสังกัดภายใน 90 วันหลังสิ้นปีบัญชี (N/A)",
                t6Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 2):</strong> จัดทำรายงานการประเมินผลการควบคุมภายในครอบคลุมภารกิจหลักครบถ้วน (ข้อ 6.1 ระดับ 5) สำหรับข้อ 6.2 รอส่งรายงานสิ้นปีงบประมาณภายใน 90 วันตามเกณฑ์กระทรวงการคลัง (N/A)",
                t6ScVal: "ระดับ 5.0000 (เฉพาะ 6.1)",
                t6ScStars: "⭐⭐⭐⭐⭐"
            },
            3: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 3 (ต.ค. - มิ.ย. 2569)",
                // View 0 (Overview Table)
                ovR1Score: "5.0000", ovR1Weighted: "0.3500",
                ovR2Score: "5.0000", ovR2Weighted: "0.4000",
                ovR3Score: "5.0000", ovR3Weighted: "2.2500",
                ovR4Score: "5.0000", ovR4Weighted: "0.2500",
                ovR5Score: "3.6667", ovR5Weighted: "1.1000",
                ovR6Score: "N/A (5.0)*", ovR6Weighted: "0.1000",
                ovTotSc: "ระดับ 4 (4.45)",
                ovTotWeighted: "4.4500",
                ovScVal: "ระดับ 4.4500 คะแนน",
                ovScStars: "⭐⭐⭐⭐",
                ovSumP: "ไตรมาสที่ 3 (ตามเอกสารทางการ): ดำเนินงานก้าวหน้าขึ้นอย่างมีนัยสำคัญ ข้อ 4 บรรลุระดับ 5.0000 (จัดทำผัง 12 Workflows ครบถ้วน); ข้อ 5 ทบทวนแผนครบ 2 ครั้ง (ประเด็น 2 ระดับ 5) และติดตามสารสนเทศได้ 80-89% (ประเด็น 1 ระดับ 3); ข้อ 6.2 อยู่ระหว่างรอส่งรายงานสิ้นปีงบประมาณ (N/A)",
                ovSt1Val: "ก้าวหน้า 5 ข้อ",
                ovSt2Val: "ระดับ 4 (4.4500)",

                // View 4 (กิจกรรมการควบคุมภายใน 5%)
                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 5",
                t4ActiveLevel: 5,
                t4S1D: "กำหนดกิจกรรมควบคุม (Control Activity) ของกระบวนงานสำคัญครบถ้วน 3 กระบวนงานตามแบบ ปค.5 ได้แก่ 1) การจัดสรรเงินให้กู้ยืม 2) การกำกับติดตามหนี้ค้างชำระ และ 3) การบังคับคดีกับลูกหนี้ตามคำพิพากษา (เอกสารหมายเลข 4)",
                t4S2D: "กำหนดขั้นตอนการทำงานอย่างเป็นระบบผ่าน Work Flow รวม 12 กระบวนงาน ครอบคลุม 3 กระบวนงานหลักสำคัญ, 2 กระบวนงานสนับสนุน (ด้านการบริหาร และด้านการเงินและบัญชี), และ 7 กระบวนงานย่อย (เอกสารหมายเลข 6)",
                t4S3D: "ทบทวนกิจกรรมควบคุมให้สอดคล้องตาม Workflow และแผนปฏิบัติการเงินทุนหมุนเวียน ประจำปีบัญชี 2569 ที่กำหนดวงเงินจัดสรรให้กู้ยืม 250 ล้านบาท และการติดตามหนี้ค้างชำระอย่างเคร่งครัด (เอกสารหมายเลข 8)",
                t4Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 3):</strong> เงินทุนหมุนเวียนฯ จัดทำผัง Work Flow รวม 12 กระบวนงาน ครอบคลุม 3 กระบวนงานหลัก, 2 สนับสนุน, และ 7 กระบวนงานย่อย พร้อมทบทวนสอดคล้องตามแผนปี 2569 ครบถ้วน ผลการดำเนินงานเลื่อนระดับขึ้นเป็น 5.0000 คะแนน",
                t4ScVal: "ระดับ 5.0000 คะแนน",
                t4ScStars: "⭐⭐⭐⭐⭐",

                // View 5 (สารสนเทศและการสื่อสาร 30%)
                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 3.6667",
                t5P1Badge: "ระดับ 3 (0.6000)",
                t5P2Badge: "ระดับ 5 (0.5000)",
                t5P1Achieve: "📈 ผลสัมฤทธิ์ (ไตรมาส 3): ดำเนินกิจกรรมตามแผนได้ร้อยละ 80 - 89 ของแผน (ประเด็น 1 ระดับ 3)",
                t5P2M1: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">🏛️ ครั้งที่ 1 (ไตรมาสที่ 2)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 1px 6px; border-radius: 4px;">27 มี.ค. 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">คณะอนุกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติรับทราบผลการทบทวนแผนบริหารความเสี่ยง ในคราวประชุมครั้งที่ 3/2569 ความรุนแรงลดลง จึงคงมาตรการเดิม</div>`,
                t5P2M2: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">🏛️ ครั้งที่ 2 (ไตรมาสที่ 3)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #16a34a; background: #dcfce7; padding: 1px 6px; border-radius: 4px;">26 มิ.ย. 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">คณะกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติรับทราบผลการทบทวนแผนบริหารความเสี่ยง ในคราวประชุมครั้งที่ 3/2569 ความรุนแรงลดลงต่อเนื่อง (เอกสารหมายเลข 3.5)</div>`,
                t5P2Achieve: "✅ ผลสัมฤทธิ์ (ไตรมาส 3): ทบทวนแผนระหว่างปีครบถ้วน 2 ครั้งแล้ว (อนุกรรมการฯ 27 มี.ค. 69 และ กก.บริหารฯ 26 มิ.ย. 69 - ระดับ 5)",
                t5Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 3):</strong> ดำเนินกิจกรรมตามแผนได้ร้อยละ 80 - 89 (ประเด็น 1 ระดับ 3) และทบทวนแผนระหว่างปีครบ 2 ครั้งแล้ว (ไตรมาส 2 วันที่ 27 มี.ค. 69 และไตรมาส 3 วันที่ 26 มิ.ย. 69 โดยคณะกรรมการบริหารฯ ประเด็น 2 ระดับ 5) ผลการดำเนินงานเทียบเท่าระดับ 3.6667 คะแนน",
                t5ScVal: "ระดับ 3.6667 คะแนน",
                t5ScStars: "⭐⭐⭐⭐",

                // View 6 (การติดตามผลและการประเมินผล 5%)
                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 5 (ข้อ 6.1)",
                t6P1Badge: "ระดับ 5 (0.1000)",
                t6P2Badge: "N/A (รอผลสิ้นปี)",
                t6P1Achieve: "✅ ผลสัมฤทธิ์ (ไตรมาส 3): ประเมินครบ 3 ภารกิจหลัก และประชุมติดตามผลต่อเนื่อง (ระดับ 5)",
                t6P2Container: `<div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #64748b; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #475569; margin-bottom: 4px;">⏳ อยู่ระหว่างรอบัญชีสิ้นปีงบประมาณ</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">การจัดส่งรายงานการประเมินผลการควบคุมภายใน กำหนดส่งให้หน่วยงานต้นสังกัดภายใน 90 วัน นับแต่วันสิ้นปีบัญชี (สิ้นสุด 30 ก.ย. 69)</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0284c7; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #003666; margin-bottom: 4px;">📅 กำหนดส่งตามเกณฑ์: ต.ค. - ธ.ค. 2569</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">เตรียมรวบรวมและจัดส่งรายงานให้ต้นสังกัดในไตรมาสที่ 4 ภายใน 90 วัน (ผลการประเมินในไตรมาส 3 จึงเป็น N/A รอผลสิ้นปี)</div>
                                </div>`,
                t6P2Achieve: "⏳ สถานะ (ไตรมาส 3): เตรียมรวบรวมและจัดส่งรายงานให้ต้นสังกัดในไตรมาสที่ 4 (N/A)",
                t6Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 3):</strong> จัดทำรายงานประเมินผลการควบคุมภายในครอบคลุมภารกิจหลัก มีการประชุมติดตามผล (ข้อ 6.1 ระดับ 5) และเตรียมจัดส่งรายงานให้ต้นสังกัดในไตรมาส 4 (ข้อ 6.2 รอผลสิ้นปี N/A)",
                t6ScVal: "ระดับ 5.0000 (เฉพาะ 6.1)",
                t6ScStars: "⭐⭐⭐⭐⭐"
            },
            4: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 4 (ครบปี ต.ค. - ก.ย. 2569)",
                // View 0 (Overview Table)
                ovR1Score: "5.0000", ovR1Weighted: "0.3500",
                ovR2Score: "5.0000", ovR2Weighted: "0.4000",
                ovR3Score: "5.0000", ovR3Weighted: "2.2500",
                ovR4Score: "5.0000", ovR4Weighted: "0.2500",
                ovR5Score: "5.0000", ovR5Weighted: "1.5000",
                ovR6Score: "5.0000", ovR6Weighted: "0.2500",
                ovTotSc: "ระดับ 5",
                ovTotWeighted: "5.0000",
                ovScVal: "ระดับ 5.0000 คะแนน",
                ovScStars: "⭐⭐⭐⭐⭐",
                ovSumP: "งวดสิ้นปีบัญชี 2569: ดำเนินงานบรรลุระดับ 5.0000 ครบถ้วนทั้ง 6 องค์ประกอบ มีคู่มือ แผน Risk Profile ติดตามสารสนเทศ 13 กิจกรรม ทบทวนแผนครบ 2 ครั้ง และส่งรายงานประเมินผลภายในกรอบเวลา 90 วัน",
                ovSt1Val: "ครบ 6 ข้อ",
                ovSt2Val: "ระดับ 5 (เต็ม)",

                // View 4 (กิจกรรมการควบคุมภายใน 5%)
                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 5",
                t4ActiveLevel: 5,
                t4S1D: "กำหนดกิจกรรมควบคุม (Control Activity) ของกระบวนงานสำคัญครบถ้วน 3 กระบวนงานตามแบบ ปค.5 ได้แก่ 1) การจัดสรรเงินให้กู้ยืม 2) การกำกับติดตามหนี้ค้างชำระ และ 3) การบังคับคดีกับลูกหนี้ตามคำพิพากษา (เอกสารหมายเลข 4)",
                t4S2D: "กำหนดขั้นตอนการทำงานอย่างเป็นระบบผ่าน Work Flow รวม 12 กระบวนงาน ครอบคลุม 3 กระบวนงานหลักสำคัญ, 2 กระบวนงานสนับสนุน (ด้านการบริหาร และด้านการเงินและบัญชี), และ 7 กระบวนงานย่อย (เอกสารหมายเลข 6)",
                t4S3D: "ทบทวนกิจกรรมควบคุมให้สอดคล้องตาม Workflow และแผนปฏิบัติการเงินทุนหมุนเวียน ประจำปีบัญชี 2569 ที่กำหนดวงเงินจัดสรรให้กู้ยืม 250 ล้านบาท และการติดตามหนี้ค้างชำระอย่างเคร่งครัด (เอกสารหมายเลข 8)",
                t4Callout: "<strong>สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ มีการกำหนดกิจกรรมการควบคุมการปฏิบัติงาน (Control Activity) ครอบคลุม 3 กระบวนงานหลักและกระบวนงานย่อยทั้งหมด พร้อมปรับปรุงทบทวนให้สอดคล้องกับแผนปฏิบัติการปี 2569 และผัง Workflow ครบถ้วน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",
                t4ScVal: "ระดับ 5.0000 คะแนน",
                t4ScStars: "⭐⭐⭐⭐⭐",

                // View 5 (สารสนเทศและการสื่อสาร 30%)
                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 5.0000 เต็ม",
                t5P1Badge: "ระดับ 5 (1.0000)",
                t5P2Badge: "ระดับ 5 (0.5000)",
                t5P1Achieve: "✅ ผลสัมฤทธิ์: ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมายครบถ้วนทุกด้าน (เอกสารหมายเลข 3)",
                t5P2M1: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">🏛️ ครั้งที่ 1 (ไตรมาสที่ 2)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #0284c7; background: #e0f2fe; padding: 1px 6px; border-radius: 4px;">27 มี.ค. 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">คณะอนุกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติรับทราบผลการทบทวนแผนบริหารความเสี่ยง ในคราวประชุมครั้งที่ 3/2569 ความรุนแรงลดลง จึงคงมาตรการเดิม</div>`,
                t5P2M2: `<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 13.5px; font-weight: 800; color: #003666;">🏛️ ครั้งที่ 2 (ไตรมาสที่ 3)</span>
                            <span style="font-size: 11.5px; font-weight: 700; color: #16a34a; background: #dcfce7; padding: 1px 6px; border-radius: 4px;">26 มิ.ย. 2569</span>
                        </div>
                        <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">คณะกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติรับทราบผลการทบทวนแผนบริหารความเสี่ยง ในคราวประชุมครั้งที่ 3/2569 ความรุนแรงลดลงต่อเนื่อง (เอกสารหมายเลข 3.5)</div>`,
                t5P2Achieve: "✅ ผลสัมฤทธิ์: ดำเนินการทบทวนแผนระหว่างปีครบถ้วน 2 ครั้งตามเกณฑ์มาตรฐาน",
                t5Callout: "<strong>สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ ใช้ระบบสารสนเทศสนับสนุนการติดตามการดำเนินกิจกรรมครบ 4 ด้าน 13 กิจกรรม ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมาย และผ่านการทบทวนความเหมาะสมของแผนระหว่างปีครบ 2 ครั้ง ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",
                t5ScVal: "ระดับ 5.0000 คะแนน",
                t5ScStars: "⭐⭐⭐⭐⭐",

                // View 6 (การติดตามผลและการประเมินผล 5%)
                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 5.0000 เต็ม",
                t6P1Badge: "ระดับ 5 (0.1000)",
                t6P2Badge: "ระดับ 5 (0.1500)",
                t6P1Achieve: "✅ ผลสัมฤทธิ์: ประเมินครบ 3 ภารกิจหลัก และประชุมติดตามผลครบ 3 ครั้งตามเกณฑ์",
                t6P2Container: `<div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #16a34a; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #166534; margin-bottom: 4px;">📅 จัดส่งรายงานสำเร็จ: วันที่ 9 ตุลาคม 2569</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">เงินทุนหมุนเวียนฯ จัดส่งรายงานประเมินผลการควบคุมภายในให้สำนักงาน ก.ค.ศ. ภายในระยะเวลาที่กำหนด โดยจัดส่งในวันที่ 9 ตุลาคม 2569 (เอกสารหมายเลข 12)</div>
                                </div>
                                <div style="background: #ffffff; border: 1px solid #c7ddf2; border-left: 4px solid #0284c7; border-radius: 8px; padding: 12px 14px;">
                                    <div style="font-size: 13.5px; font-weight: 800; color: #003666; margin-bottom: 4px;">⏱️ ทันตามกรอบเวลา 90 วันที่กำหนด</div>
                                    <div style="font-size: 12.5px; color: #334155; line-height: 1.5;">ดำเนินการแล้วเสร็จทันตามหลักเกณฑ์กระทรวงการคลังฯ (ภายใน 90 วัน นับแต่วันสิ้นปีบัญชี) เพื่อสำนักงาน ก.ค.ศ. รวบรวมส่ง สป.ศธ. และกระทรวงการคลังตามลำดับ</div>
                                </div>`,
                t6P2Achieve: "✅ ผลสัมฤทธิ์: จัดส่งรายงานวันที่ 9 ต.ค. 2569 ทันตามกรอบ 90 วันอย่างสมบูรณ์",
                t6Callout: "<strong>สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ มีการประเมินผลการควบคุมภายในครอบคลุม 3 ภารกิจหลัก มีการประชุมติดตามผล 3 ครั้ง และจัดส่งรายงานการประเมินผลให้หน่วยงานต้นสังกัดได้ทันภายในกรอบ 90 วัน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",
                t6ScVal: "ระดับ 5.0000 คะแนน",
                t6ScStars: "⭐⭐⭐⭐⭐"
            }
        };

        function applyQuarterDefault(q) {
            const def = quarterDefaults41[q] || quarterDefaults41[4];

            // 1. Update View 0 Overview Table
            const map = {
                'ov-r1-score': def.ovR1Score, 'ov-r1-weighted': def.ovR1Weighted,
                'ov-r2-score': def.ovR2Score, 'ov-r2-weighted': def.ovR2Weighted,
                'ov-r3-score': def.ovR3Score, 'ov-r3-weighted': def.ovR3Weighted,
                'ov-r4-score': def.ovR4Score, 'ov-r4-weighted': def.ovR4Weighted,
                'ov-r5-score': def.ovR5Score, 'ov-r5-weighted': def.ovR5Weighted,
                'ov-r6-score': def.ovR6Score, 'ov-r6-weighted': def.ovR6Weighted,
                'ov-tot-sc': def.ovTotSc, 'ov-tot-weighted': def.ovTotWeighted,
                'ov-sc-val': def.ovScVal, 'ov-sc-stars': def.ovScStars,
                'ov-sum-p': def.ovSumP,
                'ov-st1-val': def.ovSt1Val, 'ov-st2-val': def.ovSt2Val,

                // View 4 (กิจกรรมการควบคุมภายใน)
                't4-badge': def.t4Badge,
                't4-s1-d': def.t4S1D,
                't4-s2-d': def.t4S2D,
                't4-s3-d': def.t4S3D,
                't4-sc-val': def.t4ScVal,
                't4-sc-stars': def.t4ScStars,
                't4-callout': def.t4Callout,

                // View 5 (สารสนเทศและการสื่อสาร)
                't5-badge': def.t5Badge,
                't5-p1-badge': def.t5P1Badge,
                't5-p2-badge': def.t5P2Badge,
                't5-p1-achieve': def.t5P1Achieve,
                't5-p2-m1': def.t5P2M1,
                't5-p2-m2': def.t5P2M2,
                't5-p2-achieve': def.t5P2Achieve,
                't5-callout': def.t5Callout,
                't5-sc-val': def.t5ScVal,
                't5-sc-stars': def.t5ScStars,

                // View 6 (การติดตามผลและการประเมินผล)
                't6-badge': def.t6Badge,
                't6-p1-badge': def.t6P1Badge,
                't6-p2-badge': def.t6P2Badge,
                't6-p1-achieve': def.t6P1Achieve,
                't6-p2-container': def.t6P2Container,
                't6-p2-achieve': def.t6P2Achieve,
                't6-callout': def.t6Callout,
                't6-sc-val': def.t6ScVal,
                't6-sc-stars': def.t6ScStars
            };

            for (let id in map) {
                const el = document.getElementById(id);
                if (el && map[id] !== undefined) {
                    el.innerHTML = map[id];
                }
            }

            // Update active rubric card in View 4
            if (def.t4ActiveLevel) {
                for (let l = 1; l <= 5; l++) {
                    const card = document.getElementById(`t4-r${l}`)?.closest('.rstep-card');
                    if (card) {
                        if (l === def.t4ActiveLevel) {
                            card.classList.add('active-target');
                        } else {
                            card.classList.remove('active-target');
                        }
                    }
                }
            }

            // Update Pillar item status class in View 4
            const p2Item = document.getElementById('t4-p2-item');
            const p3Item = document.getElementById('t4-p3-item');
            if (p2Item && p3Item) {
                if (q < 3) {
                    p2Item.classList.remove('step-complete');
                    p3Item.classList.remove('step-complete');
                } else {
                    p2Item.classList.add('step-complete');
                    p3Item.classList.add('step-complete');
                }
            }
        }

        /* Switch Sub-Topic View */
        function switchTopicView(topicIndex) {
            activeTopic = topicIndex;

            // 1. Update Tabs styling
            for (let i = 0; i <= 6; i++) {
                const btn = document.getElementById(`tab-btn-${i}`);
                if (btn) {
                    if (i === topicIndex) btn.classList.add('active');
                    else btn.classList.remove('active');
                }
            }

            // 2. Toggle View Visibility
            for (let i = 0; i <= 6; i++) {
                const view = document.getElementById(`view-topic-${i}`);
                if (view) {
                    if (i === topicIndex) view.classList.add('active-view');
                    else view.classList.remove('active-view');
                }
            }

            // 3. Dynamic Sub-heading adjustment
            const subHdr = document.getElementById('hdr-sub-title');
            if (subHdr) {
                if (topicIndex === 0) {
                    subHdr.innerText = "พิจารณาจากผลการดำเนินงาน 6 องค์ประกอบหลักตามกรอบมาตรฐานการควบคุมภายในและการบริหารความเสี่ยง";
                } else if (topicIndex === 1) {
                    subHdr.innerText = "ข้อ 1. สภาพแวดล้อมการควบคุมภายใน (น้ำหนัก 7%) - การจัดให้มีระบบและช่องทางการรับข้อร้องเรียน 5 ช่องทาง";
                } else if (topicIndex === 2) {
                    subHdr.innerText = "ข้อ 2. การกำหนดวัตถุประสงค์การบริหารความเสี่ยง (น้ำหนัก 8%) - การจัดทำ/ทบทวนคู่มือการบริหารความเสี่ยงที่มีองค์ประกอบที่ดีครบถ้วน";
                } else if (topicIndex === 3) {
                    subHdr.innerText = "ข้อ 3. กระบวนการบริหารความเสี่ยง (น้ำหนัก 45%) - การระบุความเสี่ยง 4 ด้าน 8 ปัจจัย และจัดทำ Risk Profile 4 แผนงาน";
                } else if (topicIndex === 4) {
                    subHdr.innerText = "ข้อ 4. กิจกรรมการควบคุมภายใน (น้ำหนัก 5%) - การกำหนด Control Activity ครอบคลุมทุกกระบวนงานสำคัญและกระบวนงานย่อย";
                } else if (topicIndex === 5) {
                    subHdr.innerText = "ข้อ 5. สารสนเทศและการสื่อสาร (น้ำหนัก 30%) - การใช้สารสนเทศติดตาม 13 กิจกรรม และการทบทวนแผนระหว่างปี 2 ครั้ง";
                } else if (topicIndex === 6) {
                    subHdr.innerText = "ข้อ 6. การติดตามผลและการประเมินผล (น้ำหนัก 5%) - การประเมินผลการควบคุมภายใน และส่งรายงานให้ต้นสังกัดใน 90 วัน";
                }
            }

            showToast(`📑 สลับมุมมอง: ${topicNames[topicIndex].replace(/_/g, ' ')}`);
        }

        /* Quick Fiscal Year Updater */
        function quickUpdateFiscalYear(yearVal) {
            saveCurrentQuarter(false);
            showToast(`📅 ปรับปีเป็น ${yearVal} เรียบร้อยแล้ว`);
        }

        /* Per-Quarter State Management */
        function captureCurrentState() {
            const editables = {};
            document.querySelectorAll('#report-canvas [contenteditable="true"]').forEach((el, idx) => {
                const key = el.id || ('ed_' + idx);
                editables[key] = {
                    html: el.innerHTML,
                    style: el.getAttribute('style') || ''
                };
            });

            return {
                fiscalYear: (document.getElementById('select-year') || document.getElementById('fiscal-year-quick')).value,
                activeTopic: activeTopic,
                editables: editables
            };
        }

        function applyCapturedState(state) {
            if (!state) return;

            if (state.editables) {
                document.querySelectorAll('#report-canvas [contenteditable="true"]').forEach((el, idx) => {
                    const key = el.id || ('ed_' + idx);
                    if (state.editables[key]) {
                        el.innerHTML = state.editables[key].html;
                        el.setAttribute('style', state.editables[key].style || '');
                    }
                });
            }

            const rubricLbl = document.getElementById('lbl-meta-rubric');
            if (rubricLbl) {
                const plain = rubricLbl.innerText.replace(/[🎯\s]/g, '');
                if (plain === 'ระดับเกณฑ์:' || plain === 'เกณฑ์:' || plain === 'ระดับเกณฑ์' || plain === 'เกณฑ์') {
                    rubricLbl.innerText = 'เกณฑ์:';
                }
            }

            const lhead5 = document.getElementById('lhead-5');
            if (lhead5 && lhead5.innerText.includes('⭐')) {
                lhead5.innerText = 'ระดับ 5';
            }

            const mainTitle = document.getElementById('hdr-main-title');
            if (mainTitle && mainTitle.style.whiteSpace === 'nowrap') {
                mainTitle.style.whiteSpace = 'normal';
            }

            if (state.fiscalYear) (document.getElementById('select-year') || document.getElementById('fiscal-year-quick')).value = state.fiscalYear;
            if (typeof state.activeTopic !== 'undefined') switchTopicView(state.activeTopic);
        }

        function saveCurrentQuarter(showMsg = true) {
            const state = captureCurrentState();
            localStorage.setItem(getStorageKey(activeQuarter), JSON.stringify(state));
            if (showMsg) {
                showToast(`💾 บันทึกข้อมูล "ไตรมาส ${activeQuarter}" เรียบร้อยแล้ว`);
            }
        }

        function switchQuarter(newQ) {
            newQ = parseInt(newQ);
            if (newQ === activeQuarter) return;

            // Only auto-save if user was actively in Edit Mode
            if (currentAppMode === 'edit') {
                saveCurrentQuarter(false);
            }

            activeQuarter = newQ;
            document.getElementById('quarter-focus').value = newQ;

            // In preview mode or if no customized saved state exists, always apply authentic defaults
            const saved = localStorage.getItem(getStorageKey(activeQuarter));
            if (saved && currentAppMode === 'edit') {
                try {
                    applyCapturedState(JSON.parse(saved));
                } catch(e) {
                    console.error(e);
                    applyQuarterDefault(activeQuarter);
                }
            } else {
                applyQuarterDefault(activeQuarter);
            }

            const badge = document.getElementById('quarter-badge');
            if (badge) {
                badge.innerText = `📂 ข้อมูลแยกเฉพาะ: ไตรมาส ${activeQuarter}`;
            }
            showToast(`📂 สลับมาที่ "ไตรมาส ${activeQuarter}" เรียบร้อยแล้ว`);
        }"""

# Replace from STORAGE_KEY_PREFIX to resetCurrentQuarter
start_pos = text.find("const STORAGE_KEY_PREFIX = 'kpi_official_41_v")
end_pos = text.find("function resetCurrentQuarter")
assert start_pos != -1 and end_pos != -1, "Could not find storage code block"

text = text[:start_pos] + new_quarter_logic + "\n\n        " + text[end_pos:]

# Also update window.onload to purge legacy cache and apply default properly
onload_replacement = """window.onload = function() {
            // Auto-purge any stale legacy cache from previous versions
            try {
                for (let i = 0; i < localStorage.length; i++) {
                    const k = localStorage.key(i);
                    if (k && k.startsWith('kpi_official_41_') && !k.startsWith('kpi_official_41_v6_')) {
                        localStorage.removeItem(k);
                    }
                }
            } catch(e) { console.warn(e); }

            activeQuarter = parseInt(document.getElementById('quarter-focus').value) || 4;
            const saved = localStorage.getItem(getStorageKey(activeQuarter));
            if (saved && currentAppMode === 'edit') {
                try {
                    applyCapturedState(JSON.parse(saved));
                } catch(e) {
                    console.error(e);
                    applyQuarterDefault(activeQuarter);
                }
            } else {
                applyQuarterDefault(activeQuarter);
            }

            document.getElementById('quarter-badge').innerText = `📂 ข้อมูลแยกเฉพาะ: ไตรมาส ${activeQuarter}`;
        };"""

onload_start = text.find("window.onload = function()")
onload_end = text.find("};", onload_start) + 2
assert onload_start != -1 and onload_end != -1, "Could not find window.onload block"

text = text[:onload_start] + onload_replacement + text[onload_end:]

with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Full quarterly script updated!")
