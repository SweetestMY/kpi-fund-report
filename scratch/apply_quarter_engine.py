# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Bump storage key to v4
text = text.replace("const STORAGE_KEY_PREFIX = 'kpi_official_41_v3_Q';", "const STORAGE_KEY_PREFIX = 'kpi_official_41_v4_Q';")

# Quarter defaults and applyQuarterDefault definition
qd_code = """
        /* Quarter Defaults based on Official Documents (Q1, Q2, Q3, Q4) */
        const quarterDefaults41 = {
            1: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 1 (ต.ค. - ธ.ค. 2568)",
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
                ovSumP: "ไตรมาสที่ 1: ดำเนินงานบรรลุเป้าหมายระยะเริ่มต้น ผ่านความเห็นชอบคู่มือและแผนบริหารความเสี่ยงครบถ้วนในไตรมาสที่ 1 (16 ธ.ค. 68), มีระบบรับข้อร้องเรียน 5 ช่องทาง, กำหนดกิจกรรมควบคุม 3 กระบวนงานหลัก อยู่ระหว่างขับเคลื่อนแผนงานและเตรียมการประชุมติดตามผล",
                ovSt1Val: "เริ่มต้น 4 ข้อ",
                ovSt2Val: "ระดับ 3.47 (เบื้องต้น)",
                
                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 3",
                t4ActiveLevel: 3,
                t4ScVal: "ระดับ 3.0000 คะแนน",
                t4ScStars: "⭐⭐⭐",
                t4Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 1):</strong> เงินทุนหมุนเวียนฯ มีการกำหนดกิจกรรมการควบคุม 3 กระบวนงานหลักตามแบบ ปค.5 ครบถ้วน อยู่ระหว่างการรวบรวมจัดทำผัง Work Flow 12 กระบวนงาน ผลการดำเนินงานไตรมาสที่ 1 เทียบเท่าระดับ 3.0000 คะแนน",

                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 1.0000",
                t5P1Badge: "ระดับ 1 (0.2000)",
                t5P2Badge: "ระดับ 1 (0.1000)",
                t5ScVal: "ระดับ 1.0000 คะแนน",
                t5ScStars: "⭐",
                t5P1Achieve: "⏳ ผลสัมฤทธิ์ (ไตรมาส 1): อยู่ระหว่างเริ่มต้นดำเนินกิจกรรมตามแผนบริหารความเสี่ยง (< 50%)",
                t5P2Achieve: "⏳ ผลสัมฤทธิ์ (ไตรมาส 1): ยังไม่ถึงรอบการทบทวนแผนระหว่างปี (กำหนดครั้งที่ 1 ในไตรมาส 2)",
                t5Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 1):</strong> เงินทุนหมุนเวียนฯ อยู่ระหว่างเริ่มต้นดำเนินกิจกรรมตามแผนบริหารความเสี่ยง (< 50%) และยังไม่ถึงรอบการทบทวนแผนระหว่างปี ซึ่งกำหนดครั้งที่ 1 ในไตรมาสที่ 2 ผลการดำเนินงานเทียบเท่าระดับ 1.0000 คะแนน",

                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 1.0000",
                t6P1Badge: "ระดับ 1 (0.0200)",
                t6P2Badge: "N/A (รอผลสิ้นปี)",
                t6ScVal: "ระดับ 1.0000 คะแนน",
                t6ScStars: "⭐",
                t6P2Achieve: "⏳ สถานะ (ไตรมาส 1): อยู่ระหว่างรอบัญชีสิ้นปีงบประมาณเพื่อรวบรวมและจัดส่งรายงานภายใน 90 วัน (N/A)",
                t6Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 1):</strong> มีการแต่งตั้งคณะทำงานจัดทำรายงานผลการควบคุมภายใน (คำสั่งที่ 3/2568) อยู่ระหว่างรอการประชุมติดตามผลครั้งที่ 1 ในไตรมาส 2 และรอผลสิ้นปีงบประมาณสำหรับข้อ 6.2"
            },
            2: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 2 (ต.ค. - มี.ค. 2569)",
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

                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 3",
                t4ActiveLevel: 3,
                t4ScVal: "ระดับ 3.0000 คะแนน",
                t4ScStars: "⭐⭐⭐",
                t4Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 2):</strong> เงินทุนหมุนเวียนฯ มีการกำหนดกิจกรรมการควบคุมของกระบวนงานสำคัญครบ 3 กระบวนงานตามแบบ ปค.5 ครบถ้วน แต่ยังอยู่ระหว่างทบทวนผัง Workflow 12 กระบวนงานให้ครบทั้งระบบ ผลการดำเนินงานไตรมาสที่ 2 เทียบเท่าระดับ 3.0000 คะแนน",

                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 2.3333",
                t5P1Badge: "ระดับ 2 (0.4000)",
                t5P2Badge: "ระดับ 3 (0.3000)",
                t5ScVal: "ระดับ 2.3333 คะแนน",
                t5ScStars: "⭐⭐",
                t5P1Achieve: "⚠️ ผลสัมฤทธิ์ (ไตรมาส 2): ดำเนินกิจกรรมตามแผนได้ร้อยละ 50 - 79 (ระดับ 2)",
                t5P2Achieve: "⚠️ ผลสัมฤทธิ์ (ไตรมาส 2): ทบทวนแผนระหว่างปี ครั้งที่ 1 มติอนุกรรมการฯ 27 มี.ค. 69 (ระดับ 3)",
                t5Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 2):</strong> เงินทุนหมุนเวียนฯ ดำเนินกิจกรรมตามแผนได้ร้อยละ 50 - 79 (ระดับ 2) และได้ดำเนินการทบทวนแผนบริหารความเสี่ยงระหว่างปี ครั้งที่ 1 โดยคณะอนุกรรมการฯ มีมติรับทราบ เมื่อ 27 มี.ค. 69 (ระดับ 3) ผลการดำเนินงานเทียบเท่าระดับ 2.3333 คะแนน",

                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 5 (ข้อ 6.1)",
                t6P1Badge: "ระดับ 5 (0.1000)",
                t6P2Badge: "N/A (รอผลสิ้นปี)",
                t6ScVal: "ระดับ 5.0000 (เฉพาะ 6.1)",
                t6ScStars: "⭐⭐⭐⭐⭐",
                t6P2Achieve: "⏳ สถานะ (ไตรมาส 2): รอส่งรายงานการประเมินผลการควบคุมภายในให้หน่วยงานต้นสังกัดภายใน 90 วันหลังสิ้นปีบัญชี (N/A)",
                t6Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 2):</strong> จัดทำรายงานการประเมินผลการควบคุมภายในครอบคลุมภารกิจหลักครบถ้วน (ข้อ 6.1 ระดับ 5) สำหรับข้อ 6.2 รอส่งรายงานสิ้นปีงบประมาณภายใน 90 วันตามเกณฑ์กระทรวงการคลัง (N/A)"
            },
            3: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 3 (ต.ค. - มิ.ย. 2569)",
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

                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 5",
                t4ActiveLevel: 5,
                t4ScVal: "ระดับ 5.0000 คะแนน",
                t4ScStars: "⭐⭐⭐⭐⭐",
                t4Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 3):</strong> เงินทุนหมุนเวียนฯ จัดทำผัง Work Flow รวม 12 กระบวนงาน ครอบคลุม 3 กระบวนงานหลัก, 2 สนับสนุน, และ 7 กระบวนงานย่อย พร้อมทบทวนสอดคล้องตามแผนปี 2569 ครบถ้วน ผลการดำเนินงานเลื่อนระดับขึ้นเป็น 5.0000 คะแนน",

                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 3.6667",
                t5P1Badge: "ระดับ 3 (0.6000)",
                t5P2Badge: "ระดับ 5 (0.5000)",
                t5ScVal: "ระดับ 3.6667 คะแนน",
                t5ScStars: "⭐⭐⭐⭐",
                t5P1Achieve: "📈 ผลสัมฤทธิ์ (ไตรมาส 3): ดำเนินกิจกรรมตามแผนได้ร้อยละ 80 - 89 (ประเด็น 1 ระดับ 3)",
                t5P2Achieve: "✅ ผลสัมฤทธิ์ (ไตรมาส 3): ทบทวนแผนระหว่างปีครบ 2 ครั้งแล้ว (อนุกรรมการฯ 27 มี.ค. 69 และ กก.บริหารฯ 26 มิ.ย. 69 - ระดับ 5)",
                t5Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 3):</strong> ดำเนินกิจกรรมตามแผนได้ร้อยละ 80 - 89 (ประเด็น 1 ระดับ 3) และทบทวนแผนระหว่างปีครบ 2 ครั้งแล้ว (ไตรมาส 2 วันที่ 27 มี.ค. 69 และไตรมาส 3 วันที่ 26 มิ.ย. 69 โดยคณะกรรมการบริหารฯ ประเด็น 2 ระดับ 5) ผลการดำเนินงานเทียบเท่าระดับ 3.6667 คะแนน",

                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 5 (ข้อ 6.1)",
                t6P1Badge: "ระดับ 5 (0.1000)",
                t6P2Badge: "N/A (รอผลสิ้นปี)",
                t6ScVal: "ระดับ 5.0000 (เฉพาะ 6.1)",
                t6ScStars: "⭐⭐⭐⭐⭐",
                t6P2Achieve: "⏳ สถานะ (ไตรมาส 3): เตรียมรวบรวมและจัดส่งรายงานให้ต้นสังกัดในไตรมาสที่ 4 (N/A)",
                t6Callout: "<strong>สรุปผลการประเมิน (ไตรมาส 3):</strong> จัดทำรายงานประเมินผลการควบคุมภายในครอบคลุมภารกิจหลัก มีการประชุมติดตามผล (ข้อ 6.1 ระดับ 5) และเตรียมจัดส่งรายงานให้ต้นสังกัดในไตรมาส 4 (ข้อ 6.2 รอผลสิ้นปี N/A)"
            },
            4: {
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 4 (ครบปี ต.ค. - ก.ย. 2569)",
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

                t4Badge: "น้ำหนัก 5% | ผลงานระดับ 5",
                t4ActiveLevel: 5,
                t4ScVal: "ระดับ 5.0000 คะแนน",
                t4ScStars: "⭐⭐⭐⭐⭐",
                t4Callout: "<strong>สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ มีการกำหนดกิจกรรมการควบคุมการปฏิบัติงาน (Control Activity) ครอบคลุม 3 กระบวนงานหลักและกระบวนงานย่อยทั้งหมด พร้อมปรับปรุงทบทวนให้สอดคล้องกับแผนปฏิบัติการปี 2569 และผัง Workflow ครบถ้วน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",

                t5Badge: "น้ำหนัก 30% | ผลงานระดับ 5.0000 เต็ม",
                t5P1Badge: "ระดับ 5 (1.0000)",
                t5P2Badge: "ระดับ 5 (0.5000)",
                t5ScVal: "ระดับ 5.0000 คะแนน",
                t5ScStars: "⭐⭐⭐⭐⭐",
                t5P1Achieve: "✅ ผลสัมฤทธิ์: ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมายครบถ้วนทุกด้าน (เอกสารหมายเลข 3)",
                t5P2Achieve: "✅ ผลสัมฤทธิ์: ดำเนินการทบทวนแผนระหว่างปีครบถ้วน 2 ครั้งตามเกณฑ์มาตรฐาน",
                t5Callout: "<strong>สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ ใช้ระบบสารสนเทศสนับสนุนการติดตามการดำเนินกิจกรรมครบ 4 ด้าน 13 กิจกรรม ระดับความรุนแรงของปัจจัยเสี่ยงลดลงตามเป้าหมาย และผ่านการทบทวนความเหมาะสมของแผนระหว่างปีครบ 2 ครั้ง ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",

                t6Badge: "น้ำหนัก 5% | ผลงานระดับ 5.0000 เต็ม",
                t6P1Badge: "ระดับ 5 (0.1000)",
                t6P2Badge: "ระดับ 5 (0.1500)",
                t6ScVal: "ระดับ 5.0000 คะแนน",
                t6ScStars: "⭐⭐⭐⭐⭐",
                t6P2Achieve: "✅ ผลสัมฤทธิ์: จัดส่งรายงานวันที่ 9 ต.ค. 2569 ทันตามกรอบ 90 วันอย่างสมบูรณ์",
                t6Callout: "<strong>สรุปผลการประเมิน:</strong> เงินทุนหมุนเวียนฯ มีการประเมินผลการควบคุมภายในครอบคลุม 3 ภารกิจหลัก มีการประชุมติดตามผล 3 ครั้ง และจัดส่งรายงานการประเมินผลให้หน่วยงานต้นสังกัดได้ทันภายในกรอบ 90 วัน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน"
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

                // View 4
                't4-badge': def.t4Badge, 't4-sc-val': def.t4ScVal, 't4-sc-stars': def.t4ScStars,
                't4-callout': def.t4Callout,

                // View 5
                't5-badge': def.t5Badge, 't5-p1-badge': def.t5P1Badge, 't5-p2-badge': def.t5P2Badge,
                't5-sc-val': def.t5ScVal, 't5-sc-stars': def.t5ScStars, 't5-callout': def.t5Callout,
                't5-p1-achieve': def.t5P1Achieve, 't5-p2-achieve': def.t5P2Achieve,

                // View 6
                't6-badge': def.t6Badge, 't6-p1-badge': def.t6P1Badge, 't6-p2-badge': def.t6P2Badge,
                't6-sc-val': def.t6ScVal, 't6-sc-stars': def.t6ScStars, 't6-callout': def.t6Callout,
                't6-p2-achieve': def.t6P2Achieve
            };

            for (let id in map) {
                const el = document.getElementById(id);
                if (el && map[id] !== undefined) el.innerHTML = map[id];
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
        }
"""

# Replace switchQuarter with the enhanced version that calls applyQuarterDefault
old_switch = """        function switchQuarter(newQ) {
            newQ = parseInt(newQ);
            if (newQ === activeQuarter) return;

            saveCurrentQuarter(false);
            activeQuarter = newQ;
            document.getElementById('quarter-focus').value = newQ;

            const saved = localStorage.getItem(getStorageKey(activeQuarter));
            if (saved) {
                try {
                    applyCapturedState(JSON.parse(saved));
                } catch(e) {
                    console.error(e);
                }
            } else {
                // If quarter has no saved state yet, ensure clean standard labels
                const rubricLbl = document.getElementById('lbl-meta-rubric');
                if (rubricLbl) rubricLbl.innerText = 'เกณฑ์:';
                const lhead5 = document.getElementById('lhead-5');
                if (lhead5) lhead5.innerText = 'ระดับ 5';
            }

            document.getElementById('quarter-badge').innerText = `📂 ข้อมูลแยกเฉพาะ: ไตรมาส ${activeQuarter}`;
            showToast(`📂 สลับมาที่ "ไตรมาส ${activeQuarter}" เรียบร้อยแล้ว`);
        }"""

new_switch = """        function switchQuarter(newQ) {
            newQ = parseInt(newQ);
            if (newQ === activeQuarter) return;

            saveCurrentQuarter(false);
            activeQuarter = newQ;
            document.getElementById('quarter-focus').value = newQ;

            const saved = localStorage.getItem(getStorageKey(activeQuarter));
            if (saved) {
                try {
                    applyCapturedState(JSON.parse(saved));
                } catch(e) {
                    console.error(e);
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

# Insert qd_code right before switchQuarter
assert old_switch in text, "old_switch not found in text"

text = text.replace(old_switch, qd_code + "\n" + new_switch)

# Update window.onload
old_onload_pattern = r'window\.onload\s*=\s*function\(\)\s*\{[\s\S]*?(?=document\.getElementById\(\'quarter-badge\'\)\.innerText)'
new_onload = """window.onload = function() {
            activeQuarter = parseInt(document.getElementById('quarter-focus').value) || 4;
            const saved = localStorage.getItem(getStorageKey(activeQuarter));
            if (saved) {
                try {
                    applyCapturedState(JSON.parse(saved));
                } catch(e) {
                    console.error(e);
                }
            } else {
                applyQuarterDefault(activeQuarter);
            }
            """

text = re.sub(old_onload_pattern, new_onload, text)

with open('ตัวชี้วัดที่ 4.1.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Embedded quarterDefaults41 and updated switchQuarter and window.onload!")
