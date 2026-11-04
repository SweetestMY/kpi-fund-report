import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read 4.1 to extract the style block
with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text41 = f.read()

style_start = text41.find('<style>')
style_end = text41.find('</style>') + len('</style>')
style_block = text41[style_start:style_end]

html_42 = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>แบบฟอร์มรายงานผลตัวชี้วัดที่ 4.2 การตรวจสอบภายใน (KPI Presentation Dashboard)</title>
    <!-- Google Fonts: Prompt & Sarabun -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Sarabun:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- html2canvas -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

{style_block}
</head>
<body class="app-mode-preview">

    <!-- RESPONSIVE 16:9 SLIDE PAGE WRAPPER (PREVENTS OVERFLOW & CLIPPING) -->
    <div class="page-wrapper">

        <!-- TOP CONTROL TOOLBARS (WITH DUAL MODE SWITCHER) -->
        <div class="toolbar-container">
            <!-- 1. Primary Action Ribbon -->
            <div class="toolbar-ribbon">
                <div class="ribbon-left">
                    <!-- KPI Quick Switcher (Strictly 1.1 to 4.2 only) -->
                    <div class="control-item">
                        <span>📑 ตัวชี้วัด:</span>
                        <select id="select-kpi-page" class="select-input" onchange="navigateToKPI(this.value)" style="font-weight: 600; color: #0a4480; background: #eff6ff;">
                            <option value="1.1">1.1 ร้อยละการรับชำระหนี้</option>
                            <option value="1.2.1">1.2.1 หหนี้ไม่เกิน 1 ปี</option>
                            <option value="1.2.2">1.2.2 หนี้เกิน 1 ปี</option>
                            <option value="2.1">2.1 ร้อยละความพึงพอใจฯ</option>
                            <option value="2.2">2.2 ความสำเร็จโครงการเสริมสร้างวินัยฯ</option>
                            <option value="3.1">3.1 ร้อยละเงินอนุมัติให้กู้ยืม</option>
                            <option value="3.2">3.2 ความสำเร็จการแก้ไขปัญหาหนี้สินฯ</option>
                            <option value="3.3">3.3 การจัดเก็บข้อมูลประเมินผลลัพธ์ปี 2570</option>
                            <option value="4.1">4.1 การบริหารความเสี่ยงฯ</option>
                            <option value="4.2" selected>4.2 การตรวจสอบภายใน (ปัจจุบัน)</option>
                        </select>
                    </div>

                    <!-- Quarter Selector -->
                    <div class="control-item">
                        <span>📊 รายงานถึง:</span>
                        <select id="quarter-focus" class="select-input" onchange="switchQuarter(this.value)">
                            <option value="1">ไตรมาส 1 (ต.ค. - ธ.ค.)</option>
                            <option value="2">ไตรมาส 2 (ต.ค. - มี.ค.)</option>
                            <option value="3">ไตรมาส 3 (ต.ค. - มิ.ย.)</option>
                            <option value="4" selected>ไตรมาส 4 (ครบปี ต.ค. - ก.ย.)</option>
                        </select>
                    </div>

                    <span id="quarter-badge" class="quarter-active-badge">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                        ไตรมาส 4
                    </span>

                    <!-- Fiscal Year Selector -->
                    <div class="control-item" style="margin-left: 4px;">
                        <span>📅 ปี:</span>
                        <select id="select-year" class="select-input" onchange="changeFiscalYear(this.value)">
                            <option value="2568">ปี 2568</option>
                            <option value="2569" selected>ปี 2569</option>
                            <option value="2570">ปี 2570</option>
                        </select>
                    </div>
                </div>

                <!-- 2. Dual Mode Segmented Switcher (Center of Ribbon) -->
                <div class="ribbon-center">
                    <div class="mode-segmented-control">
                        <button class="mode-btn active" id="btn-mode-preview" onclick="setAppMode('preview')" title="โหมดนำเสนอ สะอาดตา ไร้เครื่องมือจัดฟอร์ม">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                            โหมดนำเสนอ (Preview)
                        </button>
                        <button class="mode-btn" id="btn-mode-edit" onclick="setAppMode('edit')" title="โหมดแก้ไขข้อความ เปิดแถบเครื่องมือจัดฟอร์มแบบจัดเต็ม">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
                            โหมดแก้ไขข้อความ (Edit)
                        </button>
                    </div>
                </div>

                <div class="ribbon-right">
                    <!-- Save Current Quarter -->
                    <button class="btn btn-outline" onclick="saveCurrentQuarter(true)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
                        บันทึก
                    </button>

                    <!-- Copy Image to Clipboard -->
                    <button class="btn btn-outline" onclick="copyImageToClipboard()" title="คัดลอกรูปภาพลงคลิปบอร์ดทันที (นำไปกด Ctrl+V วางใน PowerPoint หรือ LINE ได้เลย)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                        คัดลอกภาพ
                    </button>

                    <!-- Export PNG -->
                    <button class="btn btn-primary" onclick="exportToImage()" title="ส่งออกเป็นรูปภาพ PNG คุณภาพสูง">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                        ส่งออกภาพ (PNG)
                    </button>

                    <!-- Export Direct PDF (Full Bleed) -->
                    <button class="btn btn-warning" style="background: linear-gradient(135deg, #d97706, #b45309); color: white; border: none; font-weight: 600;" onclick="exportToPDF()" title="ดาวน์โหลดไฟล์ PDF คุณภาพสูง สัดส่วนเต็มแผ่นเหมือนรูปภาพ 100% ไร้ขอบขาว">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        ส่งออก PDF (เต็มแผ่น)
                    </button>

                    <!-- Print Browser Dialog -->
                    <button class="btn btn-success" onclick="window.print()" title="เปิดหน้าต่างสั่งพิมพ์ของเบราว์เซอร์ (ปรับพอดีหน้า A4 แนวนอนอัตโนมัติ ไม่ตกขอบ)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
                        พิมพ์ (Print)
                    </button>

                    <!-- Fullscreen Presentation Toggle -->
                    <button class="btn btn-outline" id="btn-fullscreen" onclick="toggleFullscreen()" title="โหมดนำเสนอเต็มหน้าจอ (สำหรับจอโปรเจกเตอร์/ทีวี)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
                        เต็มจอ
                    </button>
                </div>
            </div>

            <!-- Formatting Toolbar for Edit Mode -->
            <div class="format-toolbar" id="format-toolbar" style="display: none; background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 6px 14px; gap: 8px; align-items: center; box-shadow: 0 2px 6px rgba(0, 40, 85, 0.05);">
                <span style="font-size: 12px; font-weight: 700; color: #1e3a8a; margin-right: 4px;">🛠️ จัดรูปแบบ:</span>
                <button class="btn-fmt" onclick="formatDoc('bold')" title="ตัวหนา"><b>B</b></button>
                <button class="btn-fmt" onclick="formatDoc('italic')" title="ตัวเอียง"><i>I</i></button>
                <button class="btn-fmt" onclick="formatDoc('underline')" title="ขีดเส้นใต้"><u>U</u></button>
                <div style="width: 1px; height: 16px; background: #cbd5e1; margin: 0 4px;"></div>
                <button class="btn-fmt" onclick="changeFontSize(1)" title="ขยายตัวหนังสือ">A+</button>
                <button class="btn-fmt" onclick="changeFontSize(-1)" title="ลดขนาดตัวหนังสือ">A-</button>
                <div style="width: 1px; height: 16px; background: #cbd5e1; margin: 0 4px;"></div>
                <input type="color" onchange="formatDoc('foreColor', this.value)" title="เปลี่ยนสีข้อความ" style="width: 24px; height: 24px; border: none; cursor: pointer; border-radius: 4px;">
                <span style="font-size: 11.5px; color: #64748b; margin-left: 8px;">คลิกข้อความใดก็ได้บนการ์ดเพื่อพิมพ์แก้ไข</span>
            </div>

            <!-- Sub-topic Interactive Filter Tab Bar -->
            <div class="filter-tabs-bar" style="background: #ffffff; border: 1px solid rgba(188, 219, 242, 0.85); border-radius: 10px; padding: 6px 14px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <div class="filter-tab-title" style="font-size: 12.5px; font-weight: 700; color: #004b87; margin-right: 4px;">
                    <span>📑 ตัวกรองหัวข้อ (Sub-topics):</span>
                </div>
                <button class="tab-btn active" id="tab-btn-0" onclick="switchTopicView(0)">
                    <span>📊 ภาพรวมสรุป 3 ข้อ</span>
                    <span class="tab-pct" style="background: #005691; color: white; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">100%</span>
                </button>
                <button class="tab-btn" id="tab-btn-1" onclick="switchTopicView(1)">
                    <span>1. การปฏิบัติงานตรวจสอบภายใน</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">45%</span>
                </button>
                <button class="tab-btn" id="tab-btn-2" onclick="switchTopicView(2)">
                    <span>2. การประชุมปิดการตรวจสอบ</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">15%</span>
                </button>
                <button class="tab-btn" id="tab-btn-3" onclick="switchTopicView(3)">
                    <span>3. การปฏิบัติงานตามข้อเสนอแนะ</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">40%</span>
                </button>
            </div>
        </div>

        <!-- 16:9 EXECUTIVE DASHBOARD PRESENTATION FRAME -->
        <div class="dashboard-container" id="report-canvas">

            <!-- HEADER BANNER -->
            <div class="header-banner">
                <div class="header-left">
                    <div class="header-icon-box">🛡️</div>
                    <div class="header-titles">
                        <div contenteditable="true" id="hdr-main-title" class="main-heading">ด้านที่ 4 การบริหารจัดการทุนหมุนเวียน | ตัวชี้วัดที่ 4.2 การตรวจสอบภายใน</div>
                        <div contenteditable="true" id="hdr-sub-title" class="sub-heading">กรณีที่ 3 ทุนหมุนเวียนที่ใช้หน่วยงานตรวจสอบภายในจากหน่วยงานต้นสังกัด พิจารณาผลการดำเนินงาน 3 ประเด็นย่อย</div>
                    </div>
                </div>
                <div contenteditable="true" id="hdr-slogan" class="header-slogan">
                    บริหารอย่างมีประสิทธิภาพ<br>โปร่งใส เพื่อการพัฒนาที่ยั่งยืน
                </div>
            </div>

            <!-- KPI METADATA STRIP -->
            <div class="meta-strip">
                <div class="meta-pills-left">
                    <div class="meta-pill">
                        <span contenteditable="true" id="lbl-meta-code" class="pill-lbl">📋 ตัวชี้วัด:</span>
                        <span contenteditable="true" id="meta-code" class="pill-val">4.2 การตรวจสอบภายใน</span>
                    </div>
                    <div class="meta-pill">
                        <span contenteditable="true" id="lbl-meta-unit" class="pill-lbl">🎯 หน่วยวัด:</span>
                        <span contenteditable="true" id="meta-unit" class="pill-val">ระดับคะแนน (1 - 5)</span>
                    </div>
                    <div class="meta-pill">
                        <span contenteditable="true" id="lbl-meta-weight" class="pill-lbl">⚖️ ค่าน้ำหนัก:</span>
                        <span contenteditable="true" id="meta-weight" class="pill-val">ร้อยละ 4</span>
                    </div>
                    <div class="meta-pill">
                        <span contenteditable="true" id="lbl-meta-criteria" class="pill-lbl">📏 ค่าเกณฑ์วัด:</span>
                        <span contenteditable="true" id="meta-criteria" class="pill-val">เกณฑ์ 5 ระดับ (กรณีที่ 3)</span>
                    </div>
                </div>

                <!-- Rubric Levels: 1, 2, 3, 4, 5 -->
                <div class="meta-levels-group">
                    <span contenteditable="true" id="lbl-meta-rubric" class="rubric-lbl">เกณฑ์:</span>
                    <div class="level-chip chip-l1">
                        <div contenteditable="true" id="lhead-1" class="l-head">ระดับ 1</div>
                        <div contenteditable="true" id="lvl-1" class="l-val">1.00</div>
                    </div>
                    <div class="level-chip chip-l2">
                        <div contenteditable="true" id="lhead-2" class="l-head">ระดับ 2</div>
                        <div contenteditable="true" id="lvl-2" class="l-val">2.00</div>
                    </div>
                    <div class="level-chip chip-l3">
                        <div contenteditable="true" id="lhead-3" class="l-head">ระดับ 3</div>
                        <div contenteditable="true" id="lvl-3" class="l-val">3.00</div>
                    </div>
                    <div class="level-chip chip-l4">
                        <div contenteditable="true" id="lhead-4" class="l-head">ระดับ 4</div>
                        <div contenteditable="true" id="lvl-4" class="l-val">4.00</div>
                    </div>
                    <div class="level-chip chip-l5">
                        <div contenteditable="true" id="lhead-5" class="l-head">ระดับ 5</div>
                        <div contenteditable="true" id="lvl-5" class="l-val">5.00</div>
                    </div>
                </div>
            </div>

            <!-- SLIDE CONTENT CONTAINER -->
            <div class="slide-content">

                <!-- ========================================== -->
                <!-- VIEW 0: EXECUTIVE SUMMARY / OVERVIEW (ภาพรวม 3 ข้อ) -->
                <!-- ========================================== -->
                <div class="topic-view active-view" id="view-topic-0">
                    <div class="grid-split" style="grid-template-columns: 1.35fr 1fr; gap: 18px; flex: 1;">
                        
                        <!-- Left: Summary Table of 3 Sub-issues -->
                        <div class="panel-box" style="padding: 22px 24px; justify-content: space-between; gap: 16px;">
                            <div class="panel-title-line" style="margin-bottom: 2px;">
                                <span contenteditable="true" id="ov-t1" style="font-size: 17px; font-weight: 800; color: #003666;">📊 ผลการดำเนินงานรวม 3 ประเด็นย่อย (ตัวชี้วัดที่ 4.2)</span>
                                <span contenteditable="true" id="ov-t1-sub" class="panel-title-badge" style="font-size: 13.5px; padding: 5px 12px;">น้ำหนักรวม 100% (ในมิติ 4%)</span>
                            </div>

                            <div style="overflow-x: auto; flex: 1; display: flex; flex-direction: column; justify-content: center;">
                                <table class="overview-kpi-table" style="font-size: 15.5px; height: 100%;">
                                    <thead>
                                        <tr>
                                            <th contenteditable="true" id="ov-th-1" style="width: 55px; font-size: 15.5px; padding: 14px 8px;">ข้อ</th>
                                            <th contenteditable="true" id="ov-th-2" style="font-size: 15.5px; padding: 14px 14px; text-align: left;">ประเด็นย่อยที่ใช้พิจารณา</th>
                                            <th contenteditable="true" id="ov-th-3" style="width: 110px; font-size: 15.5px; padding: 14px 8px;">น้ำหนัก (%)</th>
                                            <th contenteditable="true" id="ov-th-4" style="width: 120px; font-size: 15.5px; padding: 14px 8px;">ระดับคะแนน</th>
                                            <th contenteditable="true" id="ov-th-5" style="width: 140px; font-size: 15.5px; padding: 14px 12px;">คะแนนถ่วงน้ำหนัก</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr onclick="switchTopicView(1)" style="cursor: pointer;">
                                            <td contenteditable="true" id="ov-r1-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 16px 8px;">1</td>
                                            <td contenteditable="true" id="ov-r1-name" style="font-size: 15.5px; font-weight: 600; padding: 16px 14px;">การปฏิบัติงานตรวจสอบภายใน</td>
                                            <td contenteditable="true" id="ov-r1-w" style="text-align: center; font-weight: 700; font-size: 15.5px; padding: 16px 8px;">45%</td>
                                            <td contenteditable="true" id="ov-r1-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 16px 8px;">5.0000</td>
                                            <td contenteditable="true" id="ov-r1-weighted" style="text-align: right; font-weight: 700; font-size: 16px; padding: 16px 16px;">2.2500</td>
                                        </tr>
                                        <tr onclick="switchTopicView(2)" style="cursor: pointer;">
                                            <td contenteditable="true" id="ov-r2-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 16px 8px;">2</td>
                                            <td contenteditable="true" id="ov-r2-name" style="font-size: 15.5px; font-weight: 600; padding: 16px 14px;">การประชุมปิดการตรวจสอบ</td>
                                            <td contenteditable="true" id="ov-r2-w" style="text-align: center; font-weight: 700; font-size: 15.5px; padding: 16px 8px;">15%</td>
                                            <td contenteditable="true" id="ov-r2-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 16px 8px;">5.0000</td>
                                            <td contenteditable="true" id="ov-r2-weighted" style="text-align: right; font-weight: 700; font-size: 16px; padding: 16px 16px;">0.7500</td>
                                        </tr>
                                        <tr onclick="switchTopicView(3)" style="cursor: pointer;">
                                            <td contenteditable="true" id="ov-r3-no" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 16px 8px;">3</td>
                                            <td contenteditable="true" id="ov-r3-name" style="font-size: 15.5px; font-weight: 600; padding: 16px 14px;">การปฏิบัติงานตามข้อเสนอแนะ</td>
                                            <td contenteditable="true" id="ov-r3-w" style="text-align: center; font-weight: 700; font-size: 15.5px; padding: 16px 8px;">40%</td>
                                            <td contenteditable="true" id="ov-r3-score" style="text-align: center; font-weight: 800; font-size: 16px; color: #005691; padding: 16px 8px;">5.0000</td>
                                            <td contenteditable="true" id="ov-r3-weighted" style="text-align: right; font-weight: 700; font-size: 16px; padding: 16px 16px;">2.0000</td>
                                        </tr>
                                        <tr class="total-row" style="background: #eef7ff; border-top: 2.5px solid #004b87;">
                                            <td colspan="2" contenteditable="true" id="ov-tot-lbl" style="text-align: center; font-weight: 800; font-size: 16.5px; color: #003666; padding: 16px 14px;">รวมผลการประเมินถ่วงน้ำหนักทั้งหมด</td>
                                            <td contenteditable="true" id="ov-tot-w" style="text-align: center; font-weight: 800; font-size: 16px; color: #003666; padding: 16px 8px;">100%</td>
                                            <td contenteditable="true" id="ov-tot-sc" style="text-align: center; font-weight: 800; font-size: 17px; color: #047857; padding: 16px 8px;">ระดับ 5</td>
                                            <td contenteditable="true" id="ov-tot-weighted" style="text-align: right; font-weight: 800; font-size: 18.5px; color: #047857; padding: 16px 16px;">5.0000 คะแนน</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>

                            <!-- Context Note on Case 3 -->
                            <div style="background: #f1f8fc; border-left: 4px solid #005691; border-radius: 6px; padding: 10px 14px; font-size: 13.5px; color: #0f2d4a; line-height: 1.5;">
                                💡 <b>กรณีที่ 3 ทุนหมุนเวียนที่ใช้หน่วยงานตรวจสอบภายในจากหน่วยงานต้นสังกัด:</b> ได้รับการแต่งตั้งผู้ตรวจสอบภายในของสำนักงาน ก.ค.ศ. เป็นผู้ตรวจสอบภายในของเงินทุนหมุนเวียนฯ (มติ คกก.บริหารฯ 28 ธ.ค. 65) และมีกฎบัตรการตรวจสอบภายใน (มติ 30 เม.ย. 67)
                            </div>
                        </div>

                        <!-- Right: Executive Scorecard & Highlights -->
                        <div class="panel-box" style="padding: 22px 24px; justify-content: space-between; gap: 16px;">
                            <div class="panel-title-line">
                                <span contenteditable="true" id="ov-t2" style="font-size: 17px; font-weight: 800; color: #003666;">🏆 สรุปคะแนนผลการประเมินภาพรวม</span>
                                <span contenteditable="true" id="ov-badge" class="panel-title-badge" style="background: #ecfdf5; color: #065f46; border-color: #a7f3d0;">ระดับคะแนนสูงสุด</span>
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
                                    ได้รับการตรวจสอบจากผู้ตรวจสอบภายในต้นสังกัดครบถ้วนตามแผน 2 ครั้ง มีการประชุมปิดการตรวจสอบร่วมกันระหว่างผู้บริหารและผู้ตรวจสอบภายใน ปฏิบัติตามข้อสังเกตและข้อเสนอแนะครบถ้วนทุกข้อ โดย คกก.บริหารเงินทุนหมุนเวียนฯ ได้มอบนโยบายการปฏิบัติงานที่สอดคล้องกับรายงานผลการตรวจสอบ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี
                                </div>
                            </div>

                            <!-- Two Bottom Achievement Status Badges -->
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                                <div style="background: #ecfdf5; border: 1.5px solid #86efac; border-radius: 10px; padding: 14px 16px; text-align: center;">
                                    <div contenteditable="true" id="ov-st1-lbl" style="font-size: 13.5px; color: #065f46; font-weight: 700;">ความสำเร็จ</div>
                                    <div contenteditable="true" id="ov-st1-val" style="font-size: 24px; font-weight: 800; color: #047857; margin-top: 4px;">ครบ 3 ประเด็น</div>
                                </div>
                                <div style="background: #eff6ff; border: 1.5px solid #93c5fd; border-radius: 10px; padding: 14px 16px; text-align: center;">
                                    <div contenteditable="true" id="ov-st2-lbl" style="font-size: 13.5px; color: #1e40af; font-weight: 700;">สถานะประเมิน</div>
                                    <div contenteditable="true" id="ov-st2-val" style="font-size: 24px; font-weight: 800; color: #1d4ed8; margin-top: 4px;">ระดับ 5 (เต็ม)</div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- ========================================== -->
                <!-- VIEW 1: TOPIC 1 การปฏิบัติงานตรวจสอบภายใน (45%) -->
                <!-- ========================================== -->
                <div class="topic-view" id="view-topic-1">
                    <div class="panel-box" style="padding: 20px 24px; gap: 16px;">
                        <div class="panel-title-line">
                            <span contenteditable="true" id="t1-title" style="font-size: 16.5px; font-weight: 800; color: #003666;">🔍 1. การปฏิบัติงานตรวจสอบภายใน (น้ำหนัก 45%) - การตรวจสอบและรายงานผลต่อคณะกรรมการ</span>
                            <span contenteditable="true" id="t1-badge" class="panel-title-badge">น้ำหนัก 45% | ผลงานระดับ 5</span>
                        </div>

                        <!-- Progressive Rubric 1-5 -->
                        <div class="rubric-5step-grid">
                            <div class="rstep-card" id="t1-r1-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div>
                                <div contenteditable="true" id="t1-r1" class="rstep-desc">ประสานงานกับหน่วยตรวจต้นสังกัด แต่ไม่ได้รับการตรวจสอบจากผู้ตรวจสอบภายใน</div>
                            </div>
                            <div class="rstep-card" id="t1-r2-card" style="opacity: 0.45;">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div>
                                <div contenteditable="true" id="t1-r2" class="rstep-desc" style="text-align: center; padding-top: 10px;">-</div>
                            </div>
                            <div class="rstep-card" id="t1-r3-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div>
                                <div contenteditable="true" id="t1-r3" class="rstep-desc">ได้รับการตรวจสอบ ได้รับรายงานผล และนำเสนอรายงานผลต่อคณะกรรมการบริหารฯ รับทราบ</div>
                            </div>
                            <div class="rstep-card" id="t1-r4-card" style="opacity: 0.45;">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div>
                                <div contenteditable="true" id="t1-r4" class="rstep-desc" style="text-align: center; padding-top: 10px;">-</div>
                            </div>
                            <div class="rstep-card active-target" id="t1-r5-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div>
                                <div contenteditable="true" id="t1-r5" class="rstep-desc">ได้รับการตรวจสอบ นำเสนอรายงานต่อคณะกรรมการบริหารฯ และ<b>คณะกรรมการฯ ได้มอบนโยบายการปฏิบัติงานที่สอดคล้องกับรายงานผลการตรวจสอบ</b></div>
                            </div>
                        </div>

                        <!-- 3 Strategic Flow Steps -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 18px 20px;">
                            <div contenteditable="true" id="t1-flow-h" style="font-size: 15px; font-weight: 800; color: #004b87; margin-bottom: 12px;">
                                📌 การดำเนินงาน 3 ขั้นตอนหลักตามเอกสารทางการ ก.ค.ศ.:
                            </div>
                            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;">
                                <div class="channel-card" id="t1-s1-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ขั้นตอนที่ 1</span>
                                    <span contenteditable="true" id="t1-s1-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">แต่งตั้งผู้ตรวจ & จัดทำกฎบัตร</span>
                                    <span contenteditable="true" id="t1-s1-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        • มติ คกก.บริหารฯ ครั้งที่ 8/2565 (28 ธ.ค. 65) แต่งตั้งผู้ตรวจสอบภายในของสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>
                                        • มติ คกก.บริหารฯ ครั้งที่ 3/2567 (30 เม.ย. 67) เห็นชอบกฎบัตรการตรวจสอบภายใน และทบทวนสอบทานทุกปี
                                    </span>
                                </div>
                                <div class="channel-card" id="t1-s2-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ขั้นตอนที่ 2</span>
                                    <span contenteditable="true" id="t1-s2-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">แผนตรวจสอบ 2 ครั้ง ประจำปี 69</span>
                                    <span contenteditable="true" id="t1-s2-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        • <b>ครั้งที่ 1 (รายงานการเงิน):</b> ดำเนินการ เม.ย. - ก.ค. 69 ประชุมปิดตรวจ 10 ก.ย. 69 และเสนอรายงานสำเร็จ<br>
                                        • <b>ครั้งที่ 2 (เงินนอกงบประมาณ):</b> ดำเนินการ ก.ย. 69 สรุปผลการตรวจสอบเรียบร้อยตามแผน
                                    </span>
                                </div>
                                <div class="channel-card" id="t1-s3-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ขั้นตอนที่ 3</span>
                                    <span contenteditable="true" id="t1-s3-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">เสนอ คกก. & มอบนโยบาย</span>
                                    <span contenteditable="true" id="t1-s3-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        เสนอรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 เมื่อ <b>30 กันยายน 2569</b> โดยคณะกรรมการฯ ได้มอบนโยบายและข้อสังเกตในการปฏิบัติงานสอดคล้องกับรายงานผล
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Execution Details & Scorecard -->
                        <div class="grid-split" style="gap: 16px;">
                            <div style="background: #ffffff; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 14px 18px; font-size: 13.5px; display: flex; flex-direction: column; gap: 8px; justify-content: center;">
                                <div contenteditable="true" id="t1-rep-h" style="font-weight: 800; color: #004b87; font-size: 14.5px;">📄 เอกสารและหลักฐานอ้างอิงสำคัญ:</div>
                                <div contenteditable="true" id="t1-ev-1" style="color: #0f172a;">• <b>เอกสารหมายเลข 1:</b> แผนการตรวจสอบประจำปีงบประมาณ พ.ศ. 2569 ของผู้ตรวจสอบภายใน สำนักงาน ก.ค.ศ.</div>
                                <div contenteditable="true" id="t1-ev-2" style="color: #0f172a;">• <b>เอกสารหมายเลข 2:</b> รายงานการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ (10 กันยายน 2569)</div>
                                <div contenteditable="true" id="t1-ev-3" style="color: #0f172a;">• <b>เอกสารหมายเลข 3:</b> รายงานผลการตรวจสอบการจัดทำรายงานการเงินของเงินทุนหมุนเวียนฯ โดยผู้ตรวจสอบภายใน</div>
                                <div contenteditable="true" id="t1-ev-4" style="color: #0f172a;">• <b>เอกสารหมายเลข 4:</b> รายงานการประชุมคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 เมื่อวันที่ 30 กันยายน 2569</div>
                                <div contenteditable="true" id="t1-callout" style="background: #ecfdf5; border-left: 4px solid #059669; padding: 6px 12px; border-radius: 4px; font-weight: 600; color: #065f46; margin-top: 4px;">
                                    สรุปผลการประเมิน: ทุนหมุนเวียนได้รับการตรวจสอบภายใน รายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ และคณะกรรมการฯ ได้มอบนโยบายการปฏิบัติงาน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                                </div>
                            </div>
                            <div class="big-score-box" style="padding: 22px 24px;">
                                <div>
                                    <div contenteditable="true" id="t1-sc-lbl" class="score-lbl" style="font-size: 15px;">ผลการดำเนินงานข้อที่ 1 (น้ำหนัก 45%)</div>
                                    <div contenteditable="true" id="t1-sc-val" class="big-score-val" style="font-size: 32px; font-weight: 900; color: #ffdd00;">ระดับ 5.0000 คะแนน</div>
                                </div>
                                <div contenteditable="true" id="t1-sc-stars" class="score-pill-stars" style="font-size: 26px;">⭐⭐⭐⭐⭐</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ========================================== -->
                <!-- VIEW 2: TOPIC 2 การประชุมปิดการตรวจสอบ (15%) -->
                <!-- ========================================== -->
                <div class="topic-view" id="view-topic-2">
                    <div class="panel-box" style="padding: 20px 24px; gap: 16px;">
                        <div class="panel-title-line">
                            <span contenteditable="true" id="t2-title" style="font-size: 16.5px; font-weight: 800; color: #003666;">🤝 2. การประชุมปิดการตรวจสอบ (น้ำหนัก 15%) - การมีส่วนร่วมของผู้บริหารและกำหนดแนวทางแก้ไข</span>
                            <span contenteditable="true" id="t2-badge" class="panel-title-badge">น้ำหนัก 15% | ผลงานระดับ 5</span>
                        </div>

                        <!-- Progressive Rubric 1-5 -->
                        <div class="rubric-5step-grid">
                            <div class="rstep-card" id="t2-r1-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div>
                                <div contenteditable="true" id="t2-r1" class="rstep-desc">ประสานงานกับหน่วยตรวจ แต่ไม่ได้รับการตรวจสอบจากผู้ตรวจสอบภายในต้นสังกัด</div>
                            </div>
                            <div class="rstep-card" id="t2-r2-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div>
                                <div contenteditable="true" id="t2-r2" class="rstep-desc">มีการประชุมปิดการตรวจสอบ แต่ไม่ครบทุกเรื่อง/ครั้งที่ได้รับการตรวจสอบ</div>
                            </div>
                            <div class="rstep-card" id="t2-r3-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div>
                                <div contenteditable="true" id="t2-r3" class="rstep-desc">ผู้บริหารทุนหมุนเวียนเข้าร่วมประชุมปิดการตรวจสอบ ครบทุกเรื่อง/ครั้งที่ได้รับการตรวจสอบ</div>
                            </div>
                            <div class="rstep-card" id="t2-r4-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div>
                                <div contenteditable="true" id="t2-r4" class="rstep-desc">ผู้บริหารเข้าร่วมประชุมปิดตรวจครบทุกครั้ง และกำหนดแนวทางแก้ไขได้อย่างชัดเจน แต่ไม่ครบทุกข้อเสนอแนะ</div>
                            </div>
                            <div class="rstep-card active-target" id="t2-r5-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div>
                                <div contenteditable="true" id="t2-r5" class="rstep-desc">ผู้บริหารเข้าร่วมประชุมปิดตรวจครบทุกครั้ง และ<b>กำหนดแนวทางแก้ไขการปฏิบัติงานตามข้อเสนอแนะได้อย่างชัดเจน และครบถ้วนทุกข้อเสนอแนะ</b></div>
                            </div>
                        </div>

                        <!-- 3 Pillars -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 18px 20px;">
                            <div contenteditable="true" id="t2-flow-h" style="font-size: 15px; font-weight: 800; color: #004b87; margin-bottom: 12px;">
                                📌 กระบวนการประชุมปิดตรวจและกำหนดแนวทางแก้ไข:
                            </div>
                            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;">
                                <div class="channel-card" id="t2-s1-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ประเด็นที่ 1</span>
                                    <span contenteditable="true" id="t2-s1-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">ผู้บริหารเข้าร่วมครบทุกครั้ง</span>
                                    <span contenteditable="true" id="t2-s1-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียน พร้อมด้วยหัวหน้ากลุ่ม และเจ้าหน้าที่ผู้เกี่ยวข้อง ได้เข้าร่วมการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 เมื่อวันที่ <b>10 กันยายน 2569</b> ครบถ้วนทุกครั้ง
                                    </span>
                                </div>
                                <div class="channel-card" id="t2-s2-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ประเด็นที่ 2</span>
                                    <span contenteditable="true" id="t2-s2-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">กำหนดแนวทางแก้ไขชัดเจน</span>
                                    <span contenteditable="true" id="t2-s2-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        ผู้ตรวจสอบภายในรายงานข้อตรวจพบ ข้อสังเกต และข้อเสนอแนะ โดยเงินทุนหมุนเวียนฯ ได้กำหนดแนวทางและดำเนินการปรับปรุงการปฏิบัติงานตามข้อเสนอแนะแล้วเสร็จอย่างชัดเจน ครบถ้วนทุกข้อเสนอแนะ
                                    </span>
                                </div>
                                <div class="channel-card" id="t2-s3-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ประเด็นที่ 3</span>
                                    <span contenteditable="true" id="t2-s3-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">รายงานผลต่อผู้บริหาร & คกก.</span>
                                    <span contenteditable="true" id="t2-s3-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        จัดทำรายงานผลการตรวจสอบรายงานการเงินเสนอต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ในคราวประชุมครั้งที่ 6/2569 เมื่อวันที่ 30 กันยายน 2569 ครบถ้วนสมบูรณ์
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Execution Details & Scorecard -->
                        <div class="grid-split" style="gap: 16px;">
                            <div style="background: #ffffff; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 14px 18px; font-size: 13.5px; display: flex; flex-direction: column; gap: 8px; justify-content: center;">
                                <div contenteditable="true" id="t2-rep-h" style="font-weight: 800; color: #004b87; font-size: 14.5px;">📄 เอกสารและหลักฐานอ้างอิง:</div>
                                <div contenteditable="true" id="t2-ev-1" style="color: #0f172a;">• <b>เอกสารหมายเลข 2:</b> รายงานการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 เมื่อวันที่ 10 กันยายน 2569</div>
                                <div contenteditable="true" id="t2-ev-2" style="color: #0f172a;">• <b>เอกสารหมายเลข 3:</b> รายงานผลการตรวจสอบการจัดทำรายงานการเงินของเงินทุนหมุนเวียนฯ โดยผู้ตรวจสอบภายใน</div>
                                <div contenteditable="true" id="t2-callout" style="background: #ecfdf5; border-left: 4px solid #059669; padding: 6px 12px; border-radius: 4px; font-weight: 600; color: #065f46; margin-top: 4px;">
                                    สรุปผลการประเมิน: ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียนเข้าร่วมประชุมปิดการตรวจสอบครบทุกครั้ง และกำหนดแนวทางแก้ไขตามข้อเสนอแนะได้ชัดเจนและครบถ้วนทุกข้อเสนอแนะ ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                                </div>
                            </div>
                            <div class="big-score-box" style="padding: 22px 24px;">
                                <div>
                                    <div contenteditable="true" id="t2-sc-lbl" class="score-lbl" style="font-size: 15px;">ผลการดำเนินงานข้อที่ 2 (น้ำหนัก 15%)</div>
                                    <div contenteditable="true" id="t2-sc-val" class="big-score-val" style="font-size: 32px; font-weight: 900; color: #ffdd00;">ระดับ 5.0000 คะแนน</div>
                                </div>
                                <div contenteditable="true" id="t2-sc-stars" class="score-pill-stars" style="font-size: 26px;">⭐⭐⭐⭐⭐</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ========================================== -->
                <!-- VIEW 3: TOPIC 3 การปฏิบัติงานตามข้อเสนอแนะ (40%) -->
                <!-- ========================================== -->
                <div class="topic-view" id="view-topic-3">
                    <div class="panel-box" style="padding: 20px 24px; gap: 16px;">
                        <div class="panel-title-line">
                            <span contenteditable="true" id="t3-title" style="font-size: 16.5px; font-weight: 800; color: #003666;">⚡ 3. การปฏิบัติงานตามข้อเสนอแนะ (น้ำหนัก 40%) - การแก้ไขปรับปรุงและการไม่เกิดข้อตรวจพบผิดซ้ำ</span>
                            <span contenteditable="true" id="t3-badge" class="panel-title-badge">น้ำหนัก 40% | ผลงานระดับ 5</span>
                        </div>

                        <!-- Progressive Rubric 1-5 -->
                        <div class="rubric-5step-grid">
                            <div class="rstep-card" id="t3-r1-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 1</span></div>
                                <div contenteditable="true" id="t3-r1" class="rstep-desc">ปฏิบัติงานตามข้อเสนอแนะ แต่แก้ไขแล้วเสร็จช้ากว่าระยะเวลาที่กำหนด</div>
                            </div>
                            <div class="rstep-card" id="t3-r2-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 2</span></div>
                                <div contenteditable="true" id="t3-r2" class="rstep-desc">ปฏิบัติตามข้อเสนอแนะตามระยะเวลาที่กำหนด แต่ไม่ครบถ้วนทุกข้อเสนอแนะ</div>
                            </div>
                            <div class="rstep-card" id="t3-r3-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 3</span></div>
                                <div contenteditable="true" id="t3-r3" class="rstep-desc">ปฏิบัติตามข้อเสนอแนะตามเวลาที่กำหนด และรายงานผลการแก้ไขต่อที่ประชุมคณะกรรมการบริหารฯ เพื่อพิจารณา</div>
                            </div>
                            <div class="rstep-card" id="t3-r4-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 4</span></div>
                                <div contenteditable="true" id="t3-r4" class="rstep-desc">ผลการตรวจสอบของทุนหมุนเวียนในรอบ 2 ปี ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</div>
                            </div>
                            <div class="rstep-card active-target" id="t3-r5-card">
                                <div class="rstep-head"><span class="rstep-num">ระดับ 5 ⭐</span></div>
                                <div contenteditable="true" id="t3-r5" class="rstep-desc"><b>ผลการตรวจสอบของทุนหมุนเวียนในรอบ 3 ปี ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</b></div>
                            </div>
                        </div>

                        <!-- 3 Pillars -->
                        <div style="background: #f8fbfe; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 18px 20px;">
                            <div contenteditable="true" id="t3-flow-h" style="font-size: 15px; font-weight: 800; color: #004b87; margin-bottom: 12px;">
                                📌 การแก้ไขข้อตรวจพบและคุณภาพการกำกับดูแลต่อเนื่อง 3 ปี:
                            </div>
                            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;">
                                <div class="channel-card" id="t3-s1-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ด้านที่ 1</span>
                                    <span contenteditable="true" id="t3-s1-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">แก้ไขตามเวลาที่กำหนด</span>
                                    <span contenteditable="true" id="t3-s1-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        การตรวจสอบครั้งที่ 1 พบข้อสังเกตให้ตรวจปรับปรุงรายการบัญชี เงินทุนหมุนเวียนฯ ได้ตรวจปรับปรุงรายการบัญชีโดยเร็ว ณ วันที่ตรวจพบ พร้อมทั้งจัดทำรายละเอียดประกอบการปรับปรุงรายการบัญชีเรียบร้อยทันเวลา
                                    </span>
                                </div>
                                <div class="channel-card" id="t3-s2-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ด้านที่ 2</span>
                                    <span contenteditable="true" id="t3-s2-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">รายงานการแก้ไขเรียบร้อย</span>
                                    <span contenteditable="true" id="t3-s2-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        ผู้ตรวจสอบภายในได้บันทึกการดำเนินการแก้ไขไว้ในรายงานผล และรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 (30 ก.ย. 69) รับทราบเรียบร้อย
                                    </span>
                                </div>
                                <div class="channel-card" id="t3-s3-card" style="padding: 14px 16px; background: #ffffff; border: 1.5px solid #b9d8f2; border-radius: 10px; display: flex; flex-direction: column; gap: 6px;">
                                    <span style="font-size: 12px; font-weight: 800; color: #059669; background: #dcfce7; padding: 2px 8px; border-radius: 10px; align-self: flex-start;">ด้านที่ 3</span>
                                    <span contenteditable="true" id="t3-s3-t" style="font-size: 14.5px; font-weight: 800; color: #003666;">ไม่มีข้อตรวจพบผิดซ้ำในรอบ 3 ปี</span>
                                    <span contenteditable="true" id="t3-s3-d" style="font-size: 13px; color: #334155; line-height: 1.55;">
                                        ผลการตรวจสอบภายในของเงินทุนหมุนเวียนฯ ในรอบ 3 ปีบัญชีที่ผ่านมา <b>ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</b> แสดงถึงประสิทธิภาพและความต่อเนื่องในการควบคุมและปรับปรุงการปฏิบัติงาน
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Execution Details & Scorecard -->
                        <div class="grid-split" style="gap: 16px;">
                            <div style="background: #ffffff; border: 1.5px solid #a3c7e8; border-radius: 12px; padding: 14px 18px; font-size: 13.5px; display: flex; flex-direction: column; gap: 8px; justify-content: center;">
                                <div contenteditable="true" id="t3-rep-h" style="font-weight: 800; color: #004b87; font-size: 14.5px;">📄 เอกสารและหลักฐานอ้างอิง:</div>
                                <div contenteditable="true" id="t3-ev-1" style="color: #0f172a;">• <b>เอกสารหมายเลข 2:</b> รายงานการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 (10 กันยายน 2569)</div>
                                <div contenteditable="true" id="t3-ev-2" style="color: #0f172a;">• <b>เอกสารหมายเลข 3:</b> รายงานผลการตรวจสอบการจัดทำรายงานการเงินของเงินทุนหมุนเวียนฯ โดยผู้ตรวจสอบภายใน</div>
                                <div contenteditable="true" id="t3-ev-3" style="color: #0f172a;">• <b>เอกสารหมายเลข 4:</b> รายงานการประชุมคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 เมื่อวันที่ 30 กันยายน 2569</div>
                                <div contenteditable="true" id="t3-callout" style="background: #ecfdf5; border-left: 4px solid #059669; padding: 6px 12px; border-radius: 4px; font-weight: 600; color: #065f46; margin-top: 4px;">
                                    สรุปผลการประเมิน: มีการปฏิบัติตามข้อเสนอแนะของผู้ตรวจสอบภายในแล้วเสร็จตามกำหนด รายงานต่อคณะกรรมการบริหารฯ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                                </div>
                            </div>
                            <div class="big-score-box" style="padding: 22px 24px;">
                                <div>
                                    <div contenteditable="true" id="t3-sc-lbl" class="score-lbl" style="font-size: 15px;">ผลการดำเนินงานข้อที่ 3 (น้ำหนัก 40%)</div>
                                    <div contenteditable="true" id="t3-sc-val" class="big-score-val" style="font-size: 32px; font-weight: 900; color: #ffdd00;">ระดับ 5.0000 คะแนน</div>
                                </div>
                                <div contenteditable="true" id="t3-sc-stars" class="score-pill-stars" style="font-size: 26px;">⭐⭐⭐⭐⭐</div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- DASHBOARD FOOTER -->
            <div class="dashboard-footer" style="background: #ffffff; border-top: 1px solid #d4e4f2; padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; color: #475569; font-weight: 600;">
                <div>สำนักงานคณะกรรมการข้าราชการครูและบุคลากรทางการศึกษา (ก.ค.ศ.) | สำนักบริหารเงินทุนหมุนเวียนเพื่อแก้ไขปัญหาหนี้สินข้าราชการครู</div>
                <div>คุณภาพการบริหาร เพื่อครู เพื่ออนาคตการศึกษาไทย</div>
            </div>

        </div>

    </div>

    <!-- TOAST NOTIFICATION -->
    <div id="toast-notification" class="toast-notification">บันทึกข้อมูลเรียบร้อยแล้ว</div>

    <script>
        let lastFocusedElement = null;
        let activeQuarter = 4;
        let activeTopic = 0; // 0=Overview, 1..3=Topics 1..3
        let currentAppMode = 'preview';

        const topicNames = {{
            0: "ภาพรวมสรุป_3_ข้อ",
            1: "ข้อ_1_การปฏิบัติงานตรวจสอบภายใน",
            2: "ข้อ_2_การประชุมปิดการตรวจสอบ",
            3: "ข้อ_3_การปฏิบัติงานตามข้อเสนอแนะ"
        }};

        const STORAGE_KEY_PREFIX = 'kpi_official_42_v2_Q';

        function getStorageKey(q) {{
            return `${{STORAGE_KEY_PREFIX}}${{q}}`;
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast-notification');
            if (!toast) return;
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2200);
        }}

        /* Navigation Switcher strictly for 1.1 to 4.2 */
        function navigateToKPI(targetKey) {{
            const routes = {{
                '1.1': 'ตัวชี้วัดที่ 1.1.html',
                '1.2.1': 'ตัวชี้วัดที่ 1.2.1.html',
                '1.2.2': 'ตัวชี้วัดที่ 1.2.2.html',
                '2.1': 'ตัวชี้วัดที่ 2.1.html',
                '2.2': 'ตัวชี้วัดที่ 2.2.html',
                '3.1': 'ตัวชี้วัดที่ 3.1.html',
                '3.2': 'ตัวชี้วัดที่ 3.2.html',
                '3.3': 'ตัวชี้วัดที่ 3.3.html',
                '4.1': 'ตัวชี้วัดที่ 4.1.html',
                '4.2': 'ตัวชี้วัดที่ 4.2.html'
            }};
            if (routes[targetKey] && routes[targetKey] !== 'ตัวชี้วัดที่ 4.2.html') {{
                window.location.href = routes[targetKey];
            }}
        }}

        /* Quarter Defaults based strictly on Official Documents (Q1, Q2, Q3, Q4) */
        const quarterDefaults42 = {{
            1: {{
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 1 (ต.ค. - ธ.ค. 2568)",
                // View 0
                ovR1Score: "N/A", ovR1Weighted: "-",
                ovR2Score: "N/A", ovR2Weighted: "-",
                ovR3Score: "N/A", ovR3Weighted: "-",
                ovTotSc: "N/A", ovTotWeighted: "N/A (รอผลตรวจสอบ)",
                ovBadge: "อยู่ระหว่างดำเนินการ",
                ovBadgeStyle: "background: #fff7ed; color: #c2410c; border: 1px solid #ffedd5;",
                ovScVal: "N/A (รอผลการตรวจสอบ)",
                ovScStars: "⏳",
                ovSumP: "ไตรมาสที่ 1 (ต.ค. - ธ.ค. 2568): เงินทุนหมุนเวียนฯ อยู่ระหว่างประสานงานกับหน่วยตรวจสอบภายในของสำนักงาน ก.ค.ศ. (หน่วยงานต้นสังกัด) เพื่อจัดเตรียมข้อมูลและรายงานการเงินตามกรอบแผนการตรวจสอบประจำปีบัญชี 2569",
                ovSt1Val: "เตรียมการ",
                ovSt2Val: "N/A (รอผล)",

                // View 1
                t1Badge: "น้ำหนัก 45% | อยู่ระหว่างเตรียมการ (N/A)",
                t1ActiveRubric: 1,
                t1S1D: "• มติ คกก.บริหารฯ ครั้งที่ 8/2565 แต่งตั้งผู้ตรวจสอบภายในสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>• มีกฎบัตรการตรวจสอบภายในเป็นกรอบการปฏิบัติงาน",
                t1S2D: "• อยู่ระหว่างจัดเตรียมรายงานการเงินและเอกสารประกอบ เพื่อเตรียมจัดส่งให้หน่วยตรวจสอบภายในตามแผนงาน",
                t1S3D: "• ยังไม่ถึงรอบการประชุมรายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ (กำหนดช่วงท้ายปีงบประมาณ)",
                t1Callout: "สรุปผลการประเมิน (ไตรมาส 1): อยู่ระหว่างเตรียมการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน ผลการดำเนินงานยังไม่ถึงรอบการประเมิน (N/A)",
                t1ScVal: "N/A", t1ScStars: "⏳",

                // View 2
                t2Badge: "น้ำหนัก 15% | อยู่ระหว่างรอการตรวจสอบ (N/A)",
                t2ActiveRubric: 1,
                t2S1D: "• ผู้บริหารและเจ้าหน้าที่อยู่ระหว่างประสานงานกำหนดการตรวจสอบกับหน่วยตรวจสอบภายในต้นสังกัด",
                t2S2D: "• ยังไม่ถึงรอบการประชุมปิดการตรวจสอบรายงานการเงิน",
                t2S3D: "• ยังไม่มีการจัดทำรายงานผลการประชุมปิดตรวจเสนอคณะกรรมการบริหารฯ",
                t2Callout: "สรุปผลการประเมิน (ไตรมาส 1): อยู่ระหว่างรอบัญชีและการเข้าตรวจสอบของผู้ตรวจสอบภายใน (N/A)",
                t2ScVal: "N/A", t2ScStars: "⏳",

                // View 3
                t3Badge: "น้ำหนัก 40% | อยู่ระหว่างรอผลการตรวจสอบ (N/A)",
                t3ActiveRubric: 1,
                t3S1D: "• อยู่ระหว่างรอรับข้อสังเกตและข้อเสนอแนะจากผู้ตรวจสอบภายในประจำปี 2569",
                t3S2D: "• เตรียมความพร้อมระบบบัญชีและการจัดทำรายละเอียดประกอบเพื่อรองรับการตรวจสอบ",
                t3S3D: "• สถิติย้อนหลังในรอบ 3 ปีที่ผ่านมาไม่มีประเด็นข้อตรวจพบผิดซ้ำ (รอการตรวจสอบรอบปี 2569)",
                t3Callout: "สรุปผลการประเมิน (ไตรมาส 1): อยู่ระหว่างรอรับรายงานผลการตรวจสอบและข้อเสนอแนะ (N/A)",
                t3ScVal: "N/A", t3ScStars: "⏳"
            }},
            2: {{
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 2 (ต.ค. 2568 - มี.ค. 2569)",
                // View 0
                ovR1Score: "N/A", ovR1Weighted: "-",
                ovR2Score: "N/A", ovR2Weighted: "-",
                ovR3Score: "N/A", ovR3Weighted: "-",
                ovTotSc: "N/A", ovTotWeighted: "N/A (รอผลตรวจสอบ)",
                ovBadge: "อยู่ระหว่างดำเนินการ",
                ovBadgeStyle: "background: #fff7ed; color: #c2410c; border: 1px solid #ffedd5;",
                ovScVal: "N/A (รอผลการตรวจสอบ)",
                ovScStars: "⏳",
                ovSumP: "ไตรมาสที่ 2 (ต.ค. 2568 - มี.ค. 2569): ทุนหมุนเวียนอยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายในของสำนักงาน ก.ค.ศ. ตามแผนการตรวจสอบประจำปีบัญชี 2569",
                ovSt1Val: "จัดส่งรายงานการเงิน",
                ovSt2Val: "N/A (รอผล)",

                // View 1
                t1Badge: "น้ำหนัก 45% | อยู่ระหว่างส่งรายงานการเงิน (N/A)",
                t1ActiveRubric: 1,
                t1S1D: "• มติ คกก.บริหารฯ ครั้งที่ 8/2565 แต่งตั้งผู้ตรวจสอบภายในสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>• มีกฎบัตรการตรวจสอบภายในเป็นกรอบการปฏิบัติงาน",
                t1S2D: "• เงินทุนหมุนเวียนฯ อยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายในเพื่อเข้าปฏิบัติงานตรวจสอบ",
                t1S3D: "• ยังไม่ถึงรอบการประชุมรายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ",
                t1Callout: "สรุปผลการประเมิน (ไตรมาส 2): ตามเอกสารทางการ ทุนหมุนเวียนอยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน (N/A)",
                t1ScVal: "N/A", t1ScStars: "⏳",

                // View 2
                t2Badge: "น้ำหนัก 15% | อยู่ระหว่างส่งรายงานการเงิน (N/A)",
                t2ActiveRubric: 1,
                t2S1D: "• ประสานงานกับผู้ตรวจสอบภายในอย่างต่อเนื่องในการจัดส่งข้อมูลรายงานการเงิน",
                t2S2D: "• อยู่ระหว่างดำเนินการตรวจสอบรายงานการเงิน ยังไม่ถึงรอบการประชุมปิดการตรวจสอบ",
                t2S3D: "• ยังไม่มีรายงานผลเสนอคณะกรรมการบริหารฯ ในไตรมาสที่ 2",
                t2Callout: "สรุปผลการประเมิน (ไตรมาส 2): อยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน ยังไม่มีการประชุมปิดการตรวจสอบ (N/A)",
                t2ScVal: "N/A", t2ScStars: "⏳",

                // View 3
                t3Badge: "น้ำหนัก 40% | อยู่ระหว่างส่งรายงานการเงิน (N/A)",
                t3ActiveRubric: 1,
                t3S1D: "• อยู่ระหว่างส่งรายงานการเงิน ยังไม่มีข้อเสนอแนะจากการตรวจสอบรอบปีบัญชี 2569",
                t3S2D: "• กำกับติดตามการบันทึกบัญชีให้เป็นไปตามระเบียบอย่างเคร่งครัด",
                t3S3D: "• สถิติย้อนหลังในรอบ 3 ปีที่ผ่านมาไม่มีประเด็นข้อตรวจพบผิดซ้ำ",
                t3Callout: "สรุปผลการประเมิน (ไตรมาส 2): เงินทุนหมุนเวียนฯ อยู่ระหว่างจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน (N/A)",
                t3ScVal: "N/A", t3ScStars: "⏳"
            }},
            3: {{
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 3 (ต.ค. 2568 - มิ.ย. 2569)",
                // View 0
                ovR1Score: "N/A", ovR1Weighted: "-",
                ovR2Score: "N/A", ovR2Weighted: "-",
                ovR3Score: "N/A", ovR3Weighted: "-",
                ovTotSc: "N/A", ovTotWeighted: "N/A (รอผลตรวจสอบ)",
                ovBadge: "อยู่ระหว่างการตรวจสอบ",
                ovBadgeStyle: "background: #eff6ff; color: #1d4ed8; border: 1px solid #dbeafe;",
                ovScVal: "N/A (รอผลการตรวจสอบ)",
                ovScStars: "⏳",
                ovSumP: "ไตรมาสที่ 3 (ต.ค. 2568 - มิ.ย. 2569): หน่วยตรวจสอบภายในของสำนักงาน ก.ค.ศ. อยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ตามแผนงานประจำปีบัญชี 2569",
                ovSt1Val: "อยู่ระหว่างตรวจสอบ",
                ovSt2Val: "N/A (รอผล)",

                // View 1
                t1Badge: "น้ำหนัก 45% | ผู้ตรวจอยู่ระหว่างตรวจสอบ (N/A)",
                t1ActiveRubric: 1,
                t1S1D: "• มีคำสั่งแต่งตั้งและกฎบัตรการตรวจสอบภายในครบถ้วน",
                t1S2D: "• <b>ผู้ตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงิน</b>ของเงินทุนหมุนเวียนฯ (เม.ย. - ก.ค. 69)",
                t1S3D: "• รอการสรุปผลและรายงานต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ในช่วงไตรมาสที่ 4",
                t1Callout: "สรุปผลการประเมิน (ไตรมาส 3): ตามเอกสารทางการ หน่วยตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ (N/A)",
                t1ScVal: "N/A", t1ScStars: "⏳",

                // View 2
                t2Badge: "น้ำหนัก 15% | อยู่ระหว่างตรวจสอบรายงานการเงิน (N/A)",
                t2ActiveRubric: 1,
                t2S1D: "• หน่วยตรวจสอบภายในอยู่ระหว่างตรวจสอบเอกสารและรายการทางการเงิน",
                t2S2D: "• มีกำหนดการจัดประชุมปิดการตรวจสอบในช่วงไตรมาสที่ 4 หลังการตรวจสอบรายงานการเงินแล้วเสร็จ",
                t2S3D: "• อยู่ระหว่างเตรียมข้อมูลสรุปสำหรับนำเสนอผู้บริหาร",
                t2Callout: "สรุปผลการประเมิน (ไตรมาส 3): หน่วยตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ยังไม่ถึงรอบการประชุมปิดตรวจ (N/A)",
                t2ScVal: "N/A", t2ScStars: "⏳",

                // View 3
                t3Badge: "น้ำหนัก 40% | อยู่ระหว่างตรวจสอบรายงานการเงิน (N/A)",
                t3ActiveRubric: 1,
                t3S1D: "• เจ้าหน้าที่ให้ข้อมูลและร่วมประสานงานกับผู้ตรวจสอบภายในอย่างใกล้ชิดระหว่างการตรวจสอบ",
                t3S2D: "• เตรียมพร้อมแนวทางการปรับปรุงรายการบัญชีทันทีหากได้รับข้อสังเกตเบื้องต้น",
                t3S3D: "• สถิติย้อนหลังในรอบ 3 ปีที่ผ่านมาไม่มีประเด็นข้อตรวจพบผิดซ้ำ",
                t3Callout: "สรุปผลการประเมิน (ไตรมาส 3): หน่วยตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ (N/A)",
                t3ScVal: "N/A", t3ScStars: "⏳"
            }},
            4: {{
                badgeText: "📂 ข้อมูลแยกเฉพาะ: ไตรมาส 4 (ครบปี ต.ค. - ก.ย. 2569)",
                // View 0
                ovR1Score: "5.0000", ovR1Weighted: "2.2500",
                ovR2Score: "5.0000", ovR2Weighted: "0.7500",
                ovR3Score: "5.0000", ovR3Weighted: "2.0000",
                ovTotSc: "ระดับ 5", ovTotWeighted: "5.0000 คะแนน",
                ovBadge: "ระดับคะแนนสูงสุด",
                ovBadgeStyle: "background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0;",
                ovScVal: "ระดับ 5.0000 คะแนน",
                ovScStars: "⭐⭐⭐⭐⭐",
                ovSumP: "ได้รับการตรวจสอบจากผู้ตรวจสอบภายในต้นสังกัดครบถ้วนตามแผน 2 ครั้ง มีการประชุมปิดการตรวจสอบร่วมกันระหว่างผู้บริหารและผู้ตรวจสอบภายใน ปฏิบัติตามข้อสังเกตและข้อเสนอแนะครบถ้วนทุกข้อ โดย คกก.บริหารเงินทุนหมุนเวียนฯ ได้มอบนโยบายการปฏิบัติงานที่สอดคล้องกับรายงานผลการตรวจสอบ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี",
                ovSt1Val: "ครบ 3 ประเด็น",
                ovSt2Val: "ระดับ 5 (เต็ม)",

                // View 1
                t1Badge: "น้ำหนัก 45% | ผลงานระดับ 5",
                t1ActiveRubric: 5,
                t1S1D: "• มติ คกก.บริหารฯ ครั้งที่ 8/2565 (28 ธ.ค. 65) แต่งตั้งผู้ตรวจสอบภายในของสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>• มติ คกก.บริหารฯ ครั้งที่ 3/2567 (30 เม.ย. 67) เห็นชอบกฎบัตรการตรวจสอบภายใน และทบทวนสอบทานทุกปี",
                t1S2D: "• <b>ครั้งที่ 1 (รายงานการเงิน):</b> ดำเนินการ เม.ย. - ก.ค. 69 ประชุมปิดตรวจ 10 ก.ย. 69 และเสนอรายงานสำเร็จ<br>• <b>ครั้งที่ 2 (เงินนอกงบประมาณ):</b> ดำเนินการ ก.ย. 69 สรุปผลการตรวจสอบเรียบร้อยตามแผน",
                t1S3D: "เสนอรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 เมื่อ <b>30 กันยายน 2569</b> โดยคณะกรรมการฯ ได้มอบนโยบายและข้อสังเกตในการปฏิบัติงานสอดคล้องกับรายงานผล",
                t1Callout: "สรุปผลการประเมิน: ทุนหมุนเวียนได้รับการตรวจสอบภายใน รายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ และคณะกรรมการฯ ได้มอบนโยบายการปฏิบัติงาน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",
                t1ScVal: "ระดับ 5.0000 คะแนน", t1ScStars: "⭐⭐⭐⭐⭐",

                // View 2
                t2Badge: "น้ำหนัก 15% | ผลงานระดับ 5",
                t2ActiveRubric: 5,
                t2S1D: "ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียน พร้อมด้วยหัวหน้ากลุ่ม และเจ้าหน้าที่ผู้เกี่ยวข้อง ได้เข้าร่วมการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 เมื่อวันที่ <b>10 กันยายน 2569</b> ครบถ้วนทุกครั้ง",
                t2S2D: "ผู้ตรวจสอบภายในรายงานข้อตรวจพบ ข้อสังเกต และข้อเสนอแนะ โดยเงินทุนหมุนเวียนฯ ได้กำหนดแนวทางและดำเนินการปรับปรุงการปฏิบัติงานตามข้อเสนอแนะแล้วเสร็จอย่างชัดเจน ครบถ้วนทุกข้อเสนอแนะ",
                t2S3D: "จัดทำรายงานผลการตรวจสอบรายงานการเงินเสนอต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ในคราวประชุมครั้งที่ 6/2569 เมื่อวันที่ 30 กันยายน 2569 ครบถ้วนสมบูรณ์",
                t2Callout: "สรุปผลการประเมิน: ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียนเข้าร่วมประชุมปิดการตรวจสอบครบทุกครั้ง และกำหนดแนวทางแก้ไขตามข้อเสนอแนะได้ชัดเจนและครบถ้วนทุกข้อเสนอแนะ ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",
                t2ScVal: "ระดับ 5.0000 คะแนน", t2ScStars: "⭐⭐⭐⭐⭐",

                // View 3
                t3Badge: "น้ำหนัก 40% | ผลงานระดับ 5",
                t3ActiveRubric: 5,
                t3S1D: "การตรวจสอบครั้งที่ 1 พบข้อสังเกตให้ตรวจปรับปรุงรายการบัญชี เงินทุนหมุนเวียนฯ ได้ตรวจปรับปรุงรายการบัญชีโดยเร็ว ณ วันที่ตรวจพบ พร้อมทั้งจัดทำรายละเอียดประกอบการปรับปรุงรายการบัญชีเรียบร้อยทันเวลา",
                t3S2D: "ผู้ตรวจสอบภายในได้บันทึกการดำเนินการแก้ไขไว้ในรายงานผล และรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 (30 ก.ย. 69) รับทราบเรียบร้อย",
                t3S3D: "ผลการตรวจสอบภายในของเงินทุนหมุนเวียนฯ ในรอบ 3 ปีบัญชีที่ผ่านมา <b>ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</b> แสดงถึงประสิทธิภาพและความต่อเนื่องในการควบคุมและปรับปรุงการปฏิบัติงาน",
                t3Callout: "สรุปผลการประเมิน: มีการปฏิบัติตามข้อเสนอแนะของผู้ตรวจสอบภายในแล้วเสร็จตามกำหนด รายงานต่อคณะกรรมการบริหารฯ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน",
                t3ScVal: "ระดับ 5.0000 คะแนน", t3ScStars: "⭐⭐⭐⭐⭐"
            }}
        }};

        function switchQuarter(quarterNum) {{
            quarterNum = parseInt(quarterNum, 10);
            if (quarterNum < 1 || quarterNum > 4) quarterNum = 4;

            // In Edit Mode, save current changes first
            if (currentAppMode === 'edit') {{
                saveCurrentQuarter(false);
            }}

            activeQuarter = quarterNum;
            const qSelect = document.getElementById('quarter-focus');
            if (qSelect) qSelect.value = activeQuarter;

            const qBadge = document.getElementById('quarter-badge');
            if (qBadge) {{
                qBadge.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg> ไตรมาส ${{activeQuarter}}`;
            }}

            // If in edit mode and user saved custom edits, load them. In preview mode, always apply pristine official defaults.
            const savedState = localStorage.getItem(getStorageKey(activeQuarter));
            if (currentAppMode === 'edit' && savedState) {{
                try {{
                    applyCapturedState(JSON.parse(savedState));
                }} catch(e) {{
                    applyQuarterDefault(activeQuarter);
                }}
            }} else {{
                applyQuarterDefault(activeQuarter);
            }}

            showToast(`📊 สลับมาที่ "ไตรมาส ${{activeQuarter}}" เรียบร้อยแล้ว`);
        }}

        function applyQuarterDefault(q) {{
            const d = quarterDefaults42[q];
            if (!d) return;

            // View 0
            setElText('ov-r1-score', d.ovR1Score);
            setElText('ov-r1-weighted', d.ovR1Weighted);
            setElText('ov-r2-score', d.ovR2Score);
            setElText('ov-r2-weighted', d.ovR2Weighted);
            setElText('ov-r3-score', d.ovR3Score);
            setElText('ov-r3-weighted', d.ovR3Weighted);
            setElText('ov-tot-sc', d.ovTotSc);
            setElText('ov-tot-weighted', d.ovTotWeighted);
            
            const ovBadge = document.getElementById('ov-badge');
            if (ovBadge) {{
                ovBadge.textContent = d.ovBadge;
                ovBadge.setAttribute('style', d.ovBadgeStyle);
            }}

            setElText('ov-sc-val', d.ovScVal);
            setElText('ov-sc-stars', d.ovScStars);
            setElText('ov-sum-p', d.ovSumP);
            setElText('ov-st1-val', d.ovSt1Val);
            setElText('ov-st2-val', d.ovSt2Val);

            // View 1
            setElText('t1-badge', d.t1Badge);
            setElHtml('t1-s1-d', d.t1S1D);
            setElHtml('t1-s2-d', d.t1S2D);
            setElHtml('t1-s3-d', d.t1S3D);
            setElText('t1-callout', d.t1Callout);
            setElText('t1-sc-val', d.t1ScVal);
            setElText('t1-sc-stars', d.t1ScStars);
            highlightRubric(1, d.t1ActiveRubric);

            // View 2
            setElText('t2-badge', d.t2Badge);
            setElHtml('t2-s1-d', d.t2S1D);
            setElHtml('t2-s2-d', d.t2S2D);
            setElHtml('t2-s3-d', d.t2S3D);
            setElText('t2-callout', d.t2Callout);
            setElText('t2-sc-val', d.t2ScVal);
            setElText('t2-sc-stars', d.t2ScStars);
            highlightRubric(2, d.t2ActiveRubric);

            // View 3
            setElText('t3-badge', d.t3Badge);
            setElHtml('t3-s1-d', d.t3S1D);
            setElHtml('t3-s2-d', d.t3S2D);
            setElHtml('t3-s3-d', d.t3S3D);
            setElText('t3-callout', d.t3Callout);
            setElText('t3-sc-val', d.t3ScVal);
            setElText('t3-sc-stars', d.t3ScStars);
            highlightRubric(3, d.t3ActiveRubric);
        }}

        function highlightRubric(topicNum, level) {{
            for (let l = 1; l <= 5; l++) {{
                const card = document.getElementById(`t${{topicNum}}-r${{l}}-card`);
                if (card) {{
                    if (l === level) {{
                        card.classList.add('active-target');
                    }} else {{
                        card.classList.remove('active-target');
                    }}
                }}
            }}
        }}

        function setElText(id, text) {{
            const el = document.getElementById(id);
            if (el) el.textContent = text;
        }}

        function setElHtml(id, html) {{
            const el = document.getElementById(id);
            if (el) el.innerHTML = html;
        }}

        function switchTopicView(topicIndex) {{
            activeTopic = topicIndex;

            // 1. Update Tabs styling
            for (let i = 0; i <= 3; i++) {{
                const btn = document.getElementById(`tab-btn-${{i}}`);
                if (btn) {{
                    if (i === topicIndex) btn.classList.add('active');
                    else btn.classList.remove('active');
                }}
            }}

            // 2. Toggle View Visibility
            for (let i = 0; i <= 3; i++) {{
                const view = document.getElementById(`view-topic-${{i}}`);
                if (view) {{
                    if (i === topicIndex) view.classList.add('active-view');
                    else view.classList.remove('active-view');
                }}
            }}

            // 3. Dynamic Sub-heading adjustment
            const subHdr = document.getElementById('hdr-sub-title');
            if (subHdr) {{
                if (topicIndex === 0) {{
                    subHdr.innerText = "กรณีที่ 3 ทุนหมุนเวียนที่ใช้หน่วยงานตรวจสอบภายในจากหน่วยงานต้นสังกัด พิจารณาผลการดำเนินงาน 3 ประเด็นย่อย";
                }} else if (topicIndex === 1) {{
                    subHdr.innerText = "ข้อ 1. การปฏิบัติงานตรวจสอบภายใน (น้ำหนัก 45%) - การตรวจสอบและรายงานผลต่อคณะกรรมการบริหารฯ";
                }} else if (topicIndex === 2) {{
                    subHdr.innerText = "ข้อ 2. การประชุมปิดการตรวจสอบ (น้ำหนัก 15%) - การมีส่วนร่วมของผู้บริหารและกำหนดแนวทางแก้ไข";
                }} else if (topicIndex === 3) {{
                    subHdr.innerText = "ข้อ 3. การปฏิบัติงานตามข้อเสนอแนะ (น้ำหนัก 40%) - การแก้ไขปรับปรุงและการไม่เกิดข้อตรวจพบผิดซ้ำในรอบ 3 ปี";
                }}
            }}

            showToast(`📑 สลับมุมมอง: ${{topicNames[topicIndex].replace(/_/g, ' ')}}`);
        }}

        function setAppMode(mode) {{
            currentAppMode = mode;
            const btnPrev = document.getElementById('btn-mode-preview');
            const btnEdit = document.getElementById('btn-mode-edit');
            const fmtBar = document.getElementById('format-toolbar');

            if (mode === 'edit') {{
                document.body.classList.remove('app-mode-preview');
                document.body.classList.add('app-mode-edit');
                btnEdit.classList.add('active');
                btnPrev.classList.remove('active');
                if (fmtBar) fmtBar.style.display = 'flex';
                showToast("✏️ เปิดโหมดแก้ไขข้อความ: สามารถคลิกพิมพ์บนการ์ดได้ทันที");
            }} else {{
                document.body.classList.remove('app-mode-edit');
                document.body.classList.add('app-mode-preview');
                btnPrev.classList.add('active');
                btnEdit.classList.remove('active');
                if (fmtBar) fmtBar.style.display = 'none';
                showToast("👁️ เปิดโหมดนำเสนอ: สะอาดตา ไร้เครื่องมือ");
            }}
        }}

        function formatDoc(cmd, val = null) {{
            if (currentAppMode !== 'edit') {{
                showToast("⚠️ กรุณากดปุ่ม 'โหมดแก้ไขข้อความ' ด้านบนก่อนจัดรูปแบบ");
                return;
            }}
            document.execCommand(cmd, false, val);
        }}

        function changeFontSize(delta) {{
            if (currentAppMode !== 'edit') {{
                showToast("⚠️ กรุณากดปุ่ม 'โหมดแก้ไขข้อความ' ก่อนปรับขนาด");
                return;
            }}
            const sel = window.getSelection();
            if (!sel || !sel.rangeCount) return;
            const range = sel.getRangeAt(0);
            let parent = range.commonAncestorContainer;
            if (parent.nodeType === 3) parent = parent.parentNode;
            if (parent && parent.getAttribute && parent.getAttribute('contenteditable') === 'true') {{
                let currSize = parseFloat(window.getComputedStyle(parent).fontSize);
                parent.style.fontSize = (currSize + delta) + 'px';
            }}
        }}

        function saveCurrentQuarter(showFeedback = true) {{
            if (currentAppMode !== 'edit') {{
                if (showFeedback) showToast("💾 บันทึกสำเร็จ (ระบบพร้อมนำเสนอ)");
                return;
            }}
            const state = captureCurrentState();
            localStorage.setItem(getStorageKey(activeQuarter), JSON.stringify(state));
            if (showFeedback) showToast(`💾 บันทึกข้อมูลไตรมาส ${{activeQuarter}} เรียบร้อยแล้ว`);
        }}

        function captureCurrentState() {{
            const editables = {{}};
            document.querySelectorAll('#report-canvas [contenteditable="true"]').forEach((el, idx) => {{
                const key = el.id || ('ed_' + idx);
                editables[key] = {{
                    html: el.innerHTML,
                    style: el.getAttribute('style') || ''
                }};
            }});
            return {{
                activeTopic: activeTopic,
                editables: editables
            }};
        }}

        function applyCapturedState(state) {{
            if (!state || !state.editables) return;
            document.querySelectorAll('#report-canvas [contenteditable="true"]').forEach((el, idx) => {{
                const key = el.id || ('ed_' + idx);
                if (state.editables[key]) {{
                    el.innerHTML = state.editables[key].html;
                    if (state.editables[key].style) {{
                        el.setAttribute('style', state.editables[key].style);
                    }}
                }}
            }});
        }}

        function changeFiscalYear(val) {{
            showToast(`📅 เปลี่ยนปีงบประมาณเป็น ${{val}}`);
        }}

        async function copyImageToClipboard() {{
            showToast("กำลังประมวลผลคัดลอกรูปภาพ...");
            const target = document.getElementById('report-canvas');
            try {{
                const canvas = await html2canvas(target, {{ scale: 2, useCORS: true }});
                canvas.toBlob(async blob => {{
                    try {{
                        await navigator.clipboard.write([
                            new ClipboardItem({{ 'image/png': blob }})
                        ]);
                        showToast("📋 คัดลอกภาพสไลด์ลงคลิปบอร์ดแล้ว! กด Ctrl+V ได้เลย");
                    }} catch(e) {{
                        exportToImage();
                    }}
                }});
            }} catch(err) {{
                alert("เกิดข้อผิดพลาดในการคัดลอกภาพ กรุณาใช้ปุ่ม ส่งออกภาพ (PNG)");
            }}
        }}

        async function exportToImage() {{
            showToast("กำลังสร้างไฟล์ PNG...");
            const target = document.getElementById('report-canvas');
            try {{
                const canvas = await html2canvas(target, {{ scale: 2, useCORS: true }});
                const link = document.createElement('a');
                link.download = `ตัวชี้วัดที่_4.2_การตรวจสอบภายใน_Q${{activeQuarter}}.png`;
                link.href = canvas.toDataURL('image/png');
                link.click();
                showToast("🖼️ ดาวน์โหลดภาพ PNG คุณภาพสูงเรียบร้อยแล้ว");
            }} catch(e) {{
                alert("เกิดข้อผิดพลาดในการส่งออกภาพ");
            }}
        }}

        async function exportToPDF() {{
            showToast("กำลังจัดทำเอกสาร PDF เต็มแผ่น...");
            const target = document.getElementById('report-canvas');
            try {{
                const canvas = await html2canvas(target, {{ scale: 2, useCORS: true }});
                const imgData = canvas.toDataURL('image/png');
                const {{ jsPDF }} = window.jspdf;
                const pdf = new jsPDF({{
                    orientation: 'landscape',
                    unit: 'mm',
                    format: 'a4'
                }});
                const pdfWidth = pdf.internal.pageSize.getWidth();
                const pdfHeight = pdf.internal.pageSize.getHeight();
                pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
                pdf.save(`ตัวชี้วัดที่_4.2_การตรวจสอบภายใน_Q${{activeQuarter}}.pdf`);
                showToast("📄 ดาวน์โหลดไฟล์ PDF สัดส่วนเต็มแผ่นเรียบร้อยแล้ว");
            }} catch(e) {{
                window.print();
            }}
        }}

        function toggleFullscreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen().catch(err => {{
                    alert(`Error attempting to enable full-screen mode: ${{err.message}}`);
                }});
            }} else {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }}
            }}
        }}

        window.onload = function() {{
            applyQuarterDefault(activeQuarter);
            switchTopicView(0);
        }};
    </script>
</body>
</html>
"""

with open('ตัวชี้วัดที่ 4.2.html', 'w', encoding='utf-8') as f:
    f.write(html_42)

print("SUCCESS: Generated ตัวชี้วัดที่ 4.2.html faithfully with exact 4.1 styling!")
