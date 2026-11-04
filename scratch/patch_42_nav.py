import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read current 4.2
with open("ตัวชี้วัดที่ 4.2.html", "r", encoding="utf-8") as f:
    c = f.read()

# Replace toolbar kpi select
old_select = """                <div class="control-group">
                    <label for="kpiSelect">📑 ตัวชี้วัด:</label>
                    <select id="kpiSelect" class="select-input" onchange="switchKPI(this.value)">
                        <option value="ตัวชี้วัดที่ 1.1.html">1.1 การรับชำระหนี้ต่องวด (10%)</option>
                        <option value="ตัวชี้วัดที่ 1.2.1.html">1.2.1 หนี้ค้างชำระไม่เกิน 1 ปี (7.5%)</option>
                        <option value="ตัวชี้วัดที่ 1.2.2.html">1.2.2 หนี้ค้างชำระเกิน 1 ปี (7.5%)</option>
                        <option value="ตัวชี้วัดที่ 2.1.html">2.1 ค่าใช้จ่ายดำเนินงานต่อรายได้ดอกเบี้ย (5%)</option>
                        <option value="ตัวชี้วัดที่ 2.2.html">2.2 การประเมินผลการบริหารเงินทุนหมุนเวียน (10%)</option>
                        <option value="ตัวชี้วัดที่ 3.1.html">3.1 การสำรวจความพึงพอใจของผู้มีส่วนได้ส่วนเสีย (10%)</option>
                        <option value="ตัวชี้วัดที่ 3.2.html">3.2 การพัฒนาบุคลากรทางการศึกษาด้านวินัยการเงิน (10%)</option>
                        <option value="ตัวชี้วัดที่ 3.3.html">3.3 การจัดเก็บข้อมูลสำหรับประเมินผลลัพธ์ปี 2570 (10%)</option>
                        <option value="ตัวชี้วัดที่ 4.1.html">4.1 การบริหารความเสี่ยงและการควบคุมภายใน (12%)</option>
                        <option value="ตัวชี้วัดที่ 4.2.html" selected>4.2 การตรวจสอบภายใน (4%) (ปัจจุบัน)</option>
                        <option value="ตัวชี้วัดที่ 4.3.html">4.3 การบริหารจัดการสารสนเทศและดิจิทัล (4%)</option>
                        <option value="ตัวชี้วัดที่ 5.1.html">5.1 การประเมินตนเองตามเกณฑ์ Enablers (5%)</option>
                        <option value="ตัวชี้วัดที่ 5.2.html">5.2 การจัดทำแผนปฏิบัติการดิจิทัล (5%)</option>
                        <option value="ตัวชี้วัดที่ 6.1.html">6.1 การเบิกจ่ายงบประมาณ (7%)</option>
                    </select>
                </div>"""

new_select = """                <div class="control-group">
                    <label for="select-kpi-page">📑 ตัวชี้วัด:</label>
                    <select id="select-kpi-page" class="select-input" onchange="navigateToKPI(this.value)" style="font-weight: 600; color: #0a4480; background: #eff6ff;">
                        <option value="1.1">1.1 ร้อยละการรับชำระหนี้</option>
                        <option value="1.2.1">1.2.1 หนี้ไม่เกิน 1 ปี</option>
                        <option value="1.2.2">1.2.2 หนี้เกิน 1 ปี</option>
                        <option value="2.1">2.1 ร้อยละความพึงพอใจฯ</option>
                        <option value="2.2">2.2 ความสำเร็จโครงการเสริมสร้างวินัยฯ</option>
                        <option value="3.1">3.1 ร้อยละเงินอนุมัติให้กู้ยืม</option>
                        <option value="3.2">3.2 ความสำเร็จการแก้ไขปัญหาหนี้สินฯ</option>
                        <option value="3.3">3.3 การจัดเก็บข้อมูลประเมินผลลัพธ์ปี 2570</option>
                        <option value="4.1">4.1 การบริหารความเสี่ยงฯ</option>
                        <option value="4.2" selected>4.2 การตรวจสอบภายใน (ปัจจุบัน)</option>
                        <option value="4.3">4.3 การบริหารจัดการสารสนเทศและดิจิทัล</option>
                        <option value="5.1">5.1 การประเมินตนเองตามเกณฑ์ Enablers</option>
                        <option value="5.2">5.2 การจัดทำแผนปฏิบัติการดิจิทัล</option>
                        <option value="6.1">6.1 การเบิกจ่ายงบประมาณ</option>
                    </select>
                </div>"""

c = c.replace(old_select, new_select)

# Replace switchKPI with navigateToKPI
old_fn = """    function switchKPI(url) {
        if (url && url !== 'ตัวชี้วัดที่ 4.2.html') {
            window.location.href = url;
        }
    }"""

new_fn = """    function navigateToKPI(targetKey) {
        const routes = {
            '1.1': 'ตัวชี้วัดที่ 1.1.html',
            '1.2.1': 'ตัวชี้วัดที่ 1.2.1.html',
            '1.2.2': 'ตัวชี้วัดที่ 1.2.2.html',
            '2.1': 'ตัวชี้วัดที่ 2.1.html',
            '2.2': 'ตัวชี้วัดที่ 2.2.html',
            '3.1': 'ตัวชี้วัดที่ 3.1.html',
            '3.2': 'ตัวชี้วัดที่ 3.2.html',
            '3.3': 'ตัวชี้วัดที่ 3.3.html',
            '4.1': 'ตัวชี้วัดที่ 4.1.html',
            '4.2': 'ตัวชี้วัดที่ 4.2.html',
            '4.3': 'ตัวชี้วัดที่ 4.3.html',
            '5.1': 'ตัวชี้วัดที่ 5.1.html',
            '5.2': 'ตัวชี้วัดที่ 5.2.html',
            '6.1': 'ตัวชี้วัดที่ 6.1.html'
        };
        if (routes[targetKey] && routes[targetKey] !== 'ตัวชี้วัดที่ 4.2.html') {
            window.location.href = routes[targetKey];
        }
    }"""

c = c.replace(old_fn, new_fn)

with open("ตัวชี้วัดที่ 4.2.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Updated ตัวชี้วัดที่ 4.2.html navigateToKPI")
