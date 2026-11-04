# -*- coding: utf-8 -*-
"""
Builder script for KPI 5.2: การบริหารทรัพยากรบุคคล
"""

html_content = '''<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>แบบฟอร์มรายงานผลตัวชี้วัดที่ 5.2 การบริหารทรัพยากรบุคคล (KPI Presentation Dashboard)</title>
    <!-- Google Fonts: Prompt & Sarabun -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Sarabun:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- html2canvas & jsPDF for Direct Export -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

    <style>
        :root {
            --primary: #004b87;
            --primary-dark: #002647;
            --primary-light: #0077b6;
            --primary-gradient: linear-gradient(135deg, #001f38 0%, #004b87 50%, #0077b6 100%);
            --navy: #00172e;
            --card-border: #9ec5e8;
            --accent-gold: #ffcc00;
            --accent-amber: #d97706;
            --accent-green: #059669;
            --text-dark: #0f172a;
            --text-body: #1e293b;
            --text-muted: #334155;
            --bg-page: #e8f1f8;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Prompt', 'Sarabun', sans-serif;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }

        body {
            background-color: var(--bg-page);
            color: var(--text-dark);
            padding: 16px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* 16:9 Presentation Canvas Container */
        .dashboard-container {
            width: 100%;
            max-width: 1580px;
            background: #ffffff;
            border-radius: 14px;
            box-shadow: 0 10px 30px rgba(0, 38, 71, 0.12);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 1px solid #bfdbfe;
        }

        /* Top Action & Navigation Bar */
        .top-action-bar {
            background: #f8fafc;
            border-bottom: 1px solid #e2e8f0;
            padding: 10px 20px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }

        .nav-controls, .action-buttons {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
        }

        .select-input {
            padding: 6px 12px;
            border-radius: 8px;
            border: 1.5px solid #cbd5e1;
            font-size: 13px;
            font-weight: 500;
            color: var(--navy);
            background: #ffffff;
            outline: none;
            cursor: pointer;
            transition: all 0.2s;
        }

        .select-input:hover, .select-input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(0, 75, 135, 0.15);
        }

        .btn-action {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            border: 1px solid transparent;
            transition: all 0.2s ease;
            text-decoration: none;
            user-select: none;
        }

        .btn-action svg {
            width: 14px;
            height: 14px;
        }

        .btn-save { background: #e0f2fe; color: #0369a1; border-color: #bae6fd; }
        .btn-save:hover { background: #bae6fd; }

        .btn-copy { background: #f1f5f9; color: #334155; border-color: #cbd5e1; }
        .btn-copy:hover { background: #e2e8f0; }

        .btn-png { background: #004b87; color: #ffffff; }
        .btn-png:hover { background: #003666; }

        .btn-pdf { background: #d97706; color: #ffffff; }
        .btn-pdf:hover { background: #b45309; }

        .btn-print { background: #059669; color: #ffffff; }
        .btn-print:hover { background: #047857; }

        .btn-mode-toggle {
            display: inline-flex;
            border-radius: 8px;
            padding: 3px;
            background: #e2e8f0;
            border: 1px solid #cbd5e1;
        }

        .btn-mode-opt {
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            border: none;
            background: transparent;
            color: #475569;
            transition: all 0.2s;
        }

        .btn-mode-opt.active {
            background: #004b87;
            color: #ffffff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.12);
        }

        /* Format Toolbar in Edit Mode */
        .format-toolbar {
            display: none;
            background: #ffffff;
            border-bottom: 2px solid #cbd5e1;
            padding: 6px 20px;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .format-toolbar.show {
            display: flex;
        }

        .tool-btn {
            padding: 4px 8px;
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            border-radius: 5px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            color: #1e293b;
        }

        .tool-btn:hover {
            background: #e2e8f0;
            border-color: #94a3b8;
        }

        /* Subtopic Filter Bar */
        .subtopic-bar {
            background: #ffffff;
            border-bottom: 1.5px solid #dbeafe;
            padding: 8px 20px;
            display: flex;
            align-items: center;
            gap: 8px;
            overflow-x: auto;
        }

        .subtopic-label {
            font-size: 13px;
            font-weight: 700;
            color: var(--navy);
            white-space: nowrap;
            margin-right: 4px;
        }

        .subtopic-tab {
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            color: #475569;
            background: #f1f5f9;
            border: 1px solid #cbd5e1;
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .subtopic-tab:hover {
            background: #e2e8f0;
            color: var(--primary);
        }

        .subtopic-tab.active {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 2px 6px rgba(0, 75, 135, 0.25);
        }

        .subtopic-weight {
            font-size: 11px;
            padding: 2px 7px;
            border-radius: 10px;
            background: rgba(0,0,0,0.08);
        }

        .subtopic-tab.active .subtopic-weight {
            background: rgba(255,255,255,0.25);
            color: #ffffff;
        }

        /* Main Presentation Canvas (16:9 ratio feel) */
        .kpi-canvas {
            padding: 20px 24px;
            background: #ffffff;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        /* Header Banner */
        .header-banner {
            background: var(--primary-gradient);
            border-radius: 12px;
            padding: 16px 24px;
            color: #ffffff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 14px rgba(0, 38, 71, 0.18);
        }

        .banner-left {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .banner-icon {
            width: 48px;
            height: 48px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            backdrop-filter: blur(4px);
        }

        .banner-title-group h1 {
            font-size: 21px;
            font-weight: 700;
            letter-spacing: -0.3px;
            margin-bottom: 4px;
        }

        .banner-title-group p {
            font-size: 13px;
            opacity: 0.9;
            font-family: 'Sarabun', sans-serif;
        }

        .banner-right {
            text-align: right;
            border-left: 2px solid rgba(255, 255, 255, 0.2);
            padding-left: 18px;
        }

        .org-tagline {
            font-size: 11.5px;
            color: #e0f2fe;
            line-height: 1.4;
        }

        /* KPI Metadata Pill Badges */
        .meta-badges-row {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            background: #f8fafc;
            border: 1px solid #dbeafe;
            border-radius: 10px;
            padding: 8px 16px;
            gap: 10px;
        }

        .meta-group {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 8px;
        }

        .pill-badge {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12.5px;
            font-weight: 600;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            color: #1e293b;
        }

        .pill-badge.highlight {
            background: #eff6ff;
            border-color: #93c5fd;
            color: #0369a1;
        }

        .pill-badge.amber {
            background: #fef3c7;
            border-color: #fde68a;
            color: #92400e;
        }

        .rubric-scale {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .rubric-box {
            padding: 3px 7px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            text-align: center;
            background: #e2e8f0;
            color: #475569;
        }

        .rubric-box.active {
            background: var(--primary);
            color: #ffffff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }

        /* Content Views Grid Layout */
        .content-view {
            display: none;
        }

        .content-view.active {
            display: block;
        }

        /* View 0: Two Column Master Overview */
        .overview-grid {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 18px;
        }

        .glass-card {
            background: #ffffff;
            border: 1.5px solid var(--card-border);
            border-radius: 12px;
            padding: 18px;
            box-shadow: 0 4px 12px rgba(0, 38, 71, 0.05);
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .card-header-styled {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
        }

        .card-header-styled h2 {
            font-size: 16px;
            font-weight: 700;
            color: var(--navy);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* KPI Score Hero Card */
        .hero-score-box {
            background: linear-gradient(135deg, #00172e 0%, #003366 100%);
            border-radius: 10px;
            padding: 22px 20px;
            color: #ffffff;
            text-align: center;
            box-shadow: 0 6px 16px rgba(0, 31, 56, 0.25);
            border: 1px solid #1e40af;
        }

        .hero-score-label {
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #93c5fd;
            margin-bottom: 6px;
            font-weight: 600;
        }

        .hero-score-val {
            font-size: 42px;
            font-weight: 800;
            color: #ffcc00;
            line-height: 1.1;
            margin-bottom: 6px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .hero-stars {
            font-size: 20px;
            color: #ffcc00;
            letter-spacing: 3px;
        }

        /* Master Summary Table */
        .summary-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }

        .summary-table th {
            background: #004b87;
            color: #ffffff;
            padding: 8px 10px;
            font-weight: 600;
            text-align: center;
            border: 1px solid #003866;
        }

        .summary-table td {
            padding: 8px 10px;
            border: 1px solid #cbd5e1;
            color: var(--text-body);
        }

        .summary-table tr:nth-child(even) {
            background-color: #f8fafc;
        }

        .summary-table tr:hover {
            background-color: #eff6ff;
        }

        .table-total-row {
            background: #f1f5f9;
            font-weight: 700;
            border-top: 2px solid #004b87 !important;
        }

        .table-total-row td {
            color: var(--navy);
            padding: 10px;
        }

        /* Detail Callout Boxes */
        .callout-box {
            background: #f8fafc;
            border-left: 4px solid var(--primary);
            border-radius: 0 8px 8px 0;
            padding: 12px 16px;
            font-size: 13.5px;
            line-height: 1.5;
            color: var(--text-body);
        }

        .callout-box h4 {
            font-size: 13.5px;
            font-weight: 700;
            color: var(--navy);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .callout-success {
            background: #f0fdf4;
            border-left-color: #16a34a;
        }

        .callout-warning {
            background: #fffbeb;
            border-left-color: #f59e0b;
        }

        .callout-info {
            background: #eff6ff;
            border-left-color: #2563eb;
        }

        /* Metric Mini Cards Grid */
        .metric-cards-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .mini-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px 14px;
            text-align: center;
        }

        .mini-card-title {
            font-size: 11.5px;
            font-weight: 600;
            color: #64748b;
            margin-bottom: 4px;
        }

        .mini-card-val {
            font-size: 20px;
            font-weight: 700;
            color: var(--navy);
        }

        /* Subtopic Views 1 to 3 Layout */
        .subview-container {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        /* Rubric Criteria 5-Step Progress Cards */
        .rubric-grid-5 {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }

        .rubric-card {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 10px 12px;
            font-size: 11.5px;
            line-height: 1.4;
            display: flex;
            flex-direction: column;
            gap: 6px;
            transition: all 0.2s;
        }

        .rubric-card.active {
            background: #fffbeb;
            border: 2px solid #d97706;
            box-shadow: 0 4px 10px rgba(217, 119, 6, 0.15);
        }

        .rubric-card-header {
            font-weight: 700;
            font-size: 12px;
            padding: 3px 8px;
            border-radius: 4px;
            background: #004b87;
            color: #ffffff;
            display: inline-block;
            width: fit-content;
        }

        .rubric-card.active .rubric-card-header {
            background: #d97706;
        }

        /* Workflow Step Timeline */
        .timeline-steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 12px;
            align-items: stretch;
        }

        .step-box {
            background: #f0fdf4;
            border: 1.5px solid #86efac;
            border-radius: 10px;
            padding: 12px 14px;
            position: relative;
        }

        .step-box.primary-step {
            background: #eff6ff;
            border-color: #93c5fd;
        }

        .step-number {
            font-size: 11px;
            font-weight: 700;
            color: #15803d;
            text-transform: uppercase;
            margin-bottom: 2px;
        }

        .step-box.primary-step .step-number {
            color: #1d4ed8;
        }

        .step-title {
            font-size: 13.5px;
            font-weight: 700;
            color: var(--navy);
            margin-bottom: 4px;
        }

        .step-desc {
            font-size: 12px;
            color: #334155;
            line-height: 1.4;
            font-family: 'Sarabun', sans-serif;
        }

        /* Editable Controls */
        [contenteditable="true"] {
            outline: 1.5px dashed #93c5fd !important;
            background-color: #f8fafc !important;
            padding: 2px 4px;
            border-radius: 4px;
        }

        [contenteditable="true"]:focus {
            outline: 2px solid #0284c7 !important;
            background-color: #ffffff !important;
        }

        /* Footer */
        .dashboard-footer {
            background: #f8fafc;
            border-top: 1px solid #e2e8f0;
            padding: 10px 24px;
            font-size: 11.5px;
            color: #64748b;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Toast notification */
        #toast {
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #00172e;
            color: #ffffff;
            padding: 10px 18px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            font-size: 13px;
            font-weight: 500;
            display: none;
            z-index: 9999;
        }

        /* Print Specifics */
        @media print {
            body { padding: 0; background: transparent; }
            .dashboard-container { box-shadow: none; border: none; max-width: 100%; }
            .top-action-bar, .subtopic-bar, .format-toolbar { display: none !important; }
            .content-view { display: block !important; page-break-after: always; }
        }
    </style>
</head>
<body>

    <!-- Main Dashboard Container -->
    <div class="dashboard-container" id="dashboard-container">

        <!-- Top Navigation & Action Controls Bar -->
        <div class="top-action-bar">
            <!-- Left: KPI & Quarter Selectors -->
            <div class="nav-controls">
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="font-size: 12px; font-weight: 700; color: #475569;">📋 ตัวชี้วัด:</span>
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
                        <option value="4.2">4.2 การตรวจสอบภายใน</option>
                        <option value="4.3">4.3 การบริหารจัดการสารสนเทศและดิจิทัล</option>
                        <option value="5.1">5.1 บทบาทคณะกรรมการบริหารทุนหมุนเวียน</option>
                        <option value="5.2" selected>5.2 การบริหารทรัพยากรบุคคล (ปัจจุบัน)</option>
                    </select>
                </div>

                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="font-size: 12px; font-weight: 700; color: #475569;">📊 รายงานถึง:</span>
                    <select id="quarter-focus" class="select-input" onchange="switchQuarter(this.value)">
                        <option value="1">ไตรมาส 1 (ต.ค. - ธ.ค.)</option>
                        <option value="2">ไตรมาส 2 (ต.ค. - มี.ค.)</option>
                        <option value="3">ไตรมาส 3 (ต.ค. - มิ.ย.)</option>
                        <option value="4" selected>ไตรมาส 4 (ครบปี ต.ค. - ก.ย.)</option>
                    </select>
                </div>

                <div class="pill-badge highlight" id="quarter-badge">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                    ไตรมาส 4
                </div>

                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="font-size: 12px; font-weight: 700; color: #475569;">📅 ปี:</span>
                    <select id="select-year" class="select-input" onchange="changeFiscalYear(this.value)">
                        <option value="2568">ปี 2568</option>
                        <option value="2569" selected>ปี 2569</option>
                        <option value="2570">ปี 2570</option>
                    </select>
                </div>
            </div>

            <!-- Right: Preview/Edit Mode & Action Buttons -->
            <div class="action-buttons">
                <!-- Dual Mode Toggle -->
                <div class="btn-mode-toggle">
                    <button class="btn-mode-opt active" id="btn-mode-preview" onclick="setAppMode('preview')">👁️ โหมดนำเสนอ (Preview)</button>
                    <button class="btn-mode-opt" id="btn-mode-edit" onclick="setAppMode('edit')">✏️ โหมดแก้ไขข้อความ (Edit)</button>
                </div>

                <button class="btn-action btn-save" onclick="saveDashboardChanges()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
                    บันทึก
                </button>
                <button class="btn-action btn-copy" onclick="copyDashboardImage()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    คัดลอกภาพ
                </button>
                <button class="btn-action btn-png" onclick="exportDashboardPNG()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                    ส่งออกภาพ (PNG)
                </button>
                <button class="btn-action btn-pdf" onclick="exportDashboardPDF()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                    ส่งออก PDF (เต็มแผ่น)
                </button>
                <button class="btn-action btn-print" onclick="window.print()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
                    พิมพ์ (Print)
                </button>
                <button class="btn-action btn-copy" onclick="toggleFullscreen()">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
                    เต็มจอ
                </button>
            </div>
        </div>

        <!-- Format Toolbar for Edit Mode -->
        <div class="format-toolbar" id="format-toolbar">
            <span style="font-size: 12px; font-weight: 700; color: #475569; margin-right: 4px;">🛠️ เครื่องมือจัดรูปแบบข้อความ:</span>
            <button class="tool-btn" onclick="execCmd('bold')"><b>B</b></button>
            <button class="tool-btn" onclick="execCmd('italic')"><i>I</i></button>
            <button class="tool-btn" onclick="execCmd('underline')"><u>U</u></button>
            <span style="border-left: 1px solid #cbd5e1; height: 18px; margin: 0 4px;"></span>
            <button class="tool-btn" onclick="execCmd('foreColor', '#004b87')">น้ำเงิน</button>
            <button class="tool-btn" onclick="execCmd('foreColor', '#059669')">เขียว</button>
            <button class="tool-btn" onclick="execCmd('foreColor', '#d97706')">ส้ม</button>
            <button class="tool-btn" onclick="execCmd('foreColor', '#dc2626')">แดง</button>
            <span style="border-left: 1px solid #cbd5e1; height: 18px; margin: 0 4px;"></span>
            <button class="tool-btn" onclick="execCmd('hiliteColor', '#fef08a')">ไฮไลต์เหลือง</button>
            <button class="tool-btn" onclick="execCmd('hiliteColor', '#bbf7d0')">ไฮไลต์เขียว</button>
            <button class="tool-btn" onclick="execCmd('hiliteColor', 'transparent')">ล้างไฮไลต์</button>
            <span style="border-left: 1px solid #cbd5e1; height: 18px; margin: 0 4px;"></span>
            <button class="tool-btn" onclick="execCmd('fontSize', '3')">ขนาดปกติ</button>
            <button class="tool-btn" onclick="execCmd('fontSize', '4')">ขนาดใหญ่</button>
            <button class="tool-btn" onclick="execCmd('fontSize', '5')">ขนาดใหญ่พิเศษ</button>
            <span style="border-left: 1px solid #cbd5e1; height: 18px; margin: 0 4px;"></span>
            <button class="tool-btn" onclick="execCmd('undo')">↩ ย้อนกลับ</button>
            <button class="tool-btn" onclick="execCmd('redo')">↪ ทำซ้ำ</button>
        </div>

        <!-- Subtopics Filter Tabs Bar -->
        <div class="subtopic-bar">
            <span class="subtopic-label">📑 ตัวกรองหัวข้อ (Sub-topics):</span>
            <button class="subtopic-tab active" id="tab-v0" onclick="switchTopicView(0)">
                <span>📊 ภาพรวม 2 ข้อ</span>
                <span class="subtopic-weight">100%</span>
            </button>
            <button class="subtopic-tab" id="tab-v1" onclick="switchTopicView(1)">
                <span>1. ปัจจัยพื้นฐาน (Fundamental)</span>
                <span class="subtopic-weight">30%</span>
            </button>
            <button class="subtopic-tab" id="tab-v2" onclick="switchTopicView(2)">
                <span>2.1 แผนปฏิบัติการ HR ประจำปี 2569</span>
                <span class="subtopic-weight">35%</span>
            </button>
            <button class="subtopic-tab" id="tab-v3" onclick="switchTopicView(3)">
                <span>2.2 แผน HR ระยะยาว & ปี 2570</span>
                <span class="subtopic-weight">35%</span>
            </button>
        </div>

        <!-- Main KPI Presentation Canvas -->
        <div class="kpi-canvas" id="kpi-presentation-canvas">

            <!-- Header Banner -->
            <div class="header-banner">
                <div class="banner-left">
                    <div class="banner-icon">👥</div>
                    <div class="banner-title-group">
                        <h1 contenteditable="false" id="editable-banner-title">ด้านที่ 5 การบริหารจัดการทุนหมุนเวียน | ตัวชี้วัดที่ 5.2 การบริหารทรัพยากรบุคคล</h1>
                        <p contenteditable="false" id="editable-banner-sub">พิจารณาผลการดำเนินงาน 2 ข้อ (กรณีที่ 2 ทุนหมุนเวียนที่อยู่ระหว่างพัฒนาการบริหารจัดการ: ปัจจัยพื้นฐาน 30% และแผนบริหารทรัพยากรบุคคล 70%)</p>
                    </div>
                </div>
                <div class="banner-right">
                    <div class="org-tagline">
                        <strong>พัฒนาทรัพยากรบุคคลอย่างมีประสิทธิภาพ</strong><br>
                        สมรรถนะเด่น เสริมสร้างทักษะดิจิทัล & AI สู่การบริการที่เป็นเลิศ
                    </div>
                </div>
            </div>

            <!-- KPI Badges Metadata Row -->
            <div class="meta-badges-row">
                <div class="meta-group">
                    <div class="pill-badge amber">🏷️ ตัวชี้วัด: 5.2 การบริหารทรัพยากรบุคคล</div>
                    <div class="pill-badge">🎯 หน่วยวัด: ระดับคะแนน (1 - 5)</div>
                    <div class="pill-badge amber">⚖️ ค่าน้ำหนัก: ร้อยละ 4 (4%)</div>
                    <div class="pill-badge">📏 ค่าเกณฑ์วัด: เกณฑ์ 5 ระดับ (2 ข้อ)</div>
                </div>
                <div class="rubric-scale">
                    <span style="font-size: 11px; font-weight: 700; color: #475569; margin-right: 4px;">เกณฑ์:</span>
                    <div class="rubric-box">ระดับ 1<br>1.00</div>
                    <div class="rubric-box">ระดับ 2<br>2.00</div>
                    <div class="rubric-box">ระดับ 3<br>3.00</div>
                    <div class="rubric-box">ระดับ 4<br>4.00</div>
                    <div class="rubric-box active">ระดับ 5<br>5.00</div>
                </div>
            </div>

            <!-- ================= VIEW 0: MASTER OVERVIEW ================= -->
            <div class="content-view active" id="view-topic-0">
                <div class="overview-grid">
                    <!-- Left Column: Master Breakdown Table -->
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>📊 ผลการดำเนินงานรวม 2 ข้อ (ตัวชี้วัดที่ 5.2)</h2>
                            <span class="pill-badge highlight" style="font-size: 12px;">น้ำหนักรวม 100%</span>
                        </div>

                        <div style="overflow-x: auto;">
                            <table class="summary-table">
                                <thead>
                                    <tr>
                                        <th style="width: 10%;">ข้อ</th>
                                        <th style="text-align: left; width: 48%;">ประเด็นย่อยที่ใช้พิจารณา</th>
                                        <th style="width: 14%;">น้ำหนัก (%)</th>
                                        <th style="width: 14%;">ระดับคะแนน</th>
                                        <th style="width: 14%;">คะแนนถ่วงน้ำหนัก</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td style="text-align: center; font-weight: 700; color: #004b87;">1</td>
                                        <td><strong>ปัจจัยพื้นฐาน (Fundamental)</strong> - การประเมินผลการปฏิบัติงาน</td>
                                        <td style="text-align: center; font-weight: 600;">30%</td>
                                        <td style="text-align: center; font-weight: 700; color: #059669;" id="tbl-score-1">5.0000</td>
                                        <td style="text-align: right; font-weight: 700;" id="tbl-wscore-1">1.5000</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: center; font-weight: 700; color: #004b87;">2.1</td>
                                        <td><strong>แผนปฏิบัติการ HR ปี 2569</strong> - ดำเนินงาน 3 กิจกรรมครบถ้วน 100%</td>
                                        <td style="text-align: center; font-weight: 600;">35%</td>
                                        <td style="text-align: center; font-weight: 700; color: #059669;" id="tbl-score-2">5.0000</td>
                                        <td style="text-align: right; font-weight: 700;" id="tbl-wscore-2">1.7500</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: center; font-weight: 700; color: #004b87;">2.2</td>
                                        <td><strong>แผน HR ระยะยาว & ปี 2570</strong> - จัดทำ ทบทวน คกก.เห็นชอบ สื่อสารรับทราบ</td>
                                        <td style="text-align: center; font-weight: 600;">35%</td>
                                        <td style="text-align: center; font-weight: 700; color: #059669;" id="tbl-score-3">5.0000</td>
                                        <td style="text-align: right; font-weight: 700;" id="tbl-wscore-3">1.7500</td>
                                    </tr>
                                    <tr class="table-total-row">
                                        <td colspan="2" style="text-align: center; font-weight: 700;">รวมผลการประเมินถ่วงน้ำหนักทั้งหมด</td>
                                        <td style="text-align: center;">100%</td>
                                        <td style="text-align: center; color: #059669;" id="tbl-total-level">ระดับ 5.0</td>
                                        <td style="text-align: right; color: #004b87;" id="tbl-total-wscore">5.0000 คะแนน</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- Summary Connection Callout -->
                        <div class="callout-box callout-info" style="font-size: 12.5px;">
                            💡 <strong>สรุปความเชื่อมโยง:</strong> เงินทุนหมุนเวียนฯ ดำเนินงานด้านทรัพยากรบุคคลบรรลุระดับ 5 ครบทั้ง 2 ข้อ ได้แก่ 1) กำหนดตัวชี้วัดรายบุคคลทุกระดับครบ 2 รอบ นำผลประเมินไปใช้เลื่อนขั้น/ผลตอบแทน และพัฒนาทักษะ AI | 2) ดำเนินงานตามแผนปฏิบัติการฯ ปี 2569 ครบ 3 กิจกรรม (สรรหาพนักงาน, ประเมินผล 2 รอบ, อบรมพัฒนาบุคลากร ณ เขาใหญ่ Pre 86.8% ➔ Post 99.4%) และยกร่างแผน HR ระยะยาว 3 ปี (2570-2572) พร้อมแผนปี 2570 ผ่านความเห็นชอบ คกก.บริหารฯ (28 ส.ค. 69) และสื่อสารแจ้งเวียนเรียบร้อย (30 ก.ย. 69)
                        </div>
                    </div>

                    <!-- Right Column: Hero Score Card & Key Highlights -->
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>🏆 สรุปคะแนนผลการประเมินภาพรวม</h2>
                            <span class="pill-badge" id="score-status-badge" style="background: #fef3c7; color: #92400e; font-weight: 700;">ระดับ 5.0000 (เต็ม)</span>
                        </div>

                        <!-- Hero Score Box -->
                        <div class="hero-score-box">
                            <div class="hero-score-label">ผลการดำเนินงานเทียบเท่า</div>
                            <div class="hero-score-val" id="score-hero-val">ระดับ 5.0000 คะแนน</div>
                            <div class="hero-stars" id="score-hero-stars">★★★★★</div>
                        </div>

                        <!-- Key Achievements Callout -->
                        <div class="callout-box" style="font-size: 13px;">
                            <h4 id="summary-overview-title">🎯 สรุปผลการดำเนินงานสำคัญ:</h4>
                            <p id="summary-overview-desc" style="line-height: 1.55; color: #1e293b;" contenteditable="false">
                                งวดสิ้นปีบัญชี 2569: ดำเนินงานบรรลุเกณฑ์ระดับ 5 ครบถ้วนทุกข้อ บุคลากรทุกคนได้รับการประเมินผล 2 รอบอย่างเป็นระบบ นำผลประเมินไปใช้เลื่อนขั้นเงินเดือนและพัฒนาทักษะดิจิทัล/AI ดำเนินการตามแผนปฏิบัติการฯ 2569 ครบทั้ง 3 กิจกรรมด้วยผลการประเมินความพึงพอใจร้อยละ 88.55 และจัดทำแผน HR ระยะ 3 ปี (2570-2572) ร่วมกับแผนปี 2570 ผ่านความเห็นชอบของคณะกรรมการบริหารเงินทุนหมุนเวียนฯ และแจ้งเวียนหน่วยงานที่เกี่ยวข้องครบถ้วน
                            </p>
                        </div>

                        <!-- Metric Mini Cards -->
                        <div class="metric-cards-grid">
                            <div class="mini-card" style="background: #f0fdf4; border-color: #bbf7d0;">
                                <div class="mini-card-title">ความสำเร็จ</div>
                                <div class="mini-card-val" id="metric-complete-val" style="color: #16a34a;">ครบ 2 ข้อ</div>
                            </div>
                            <div class="mini-card" style="background: #eff6ff; border-color: #bfdbfe;">
                                <div class="mini-card-title">สถานะประเมิน</div>
                                <div class="mini-card-val" id="metric-grade-val" style="color: #0284c7;">ระดับ 5 (เต็ม)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 1: ข้อ 1 ปัจจัยพื้นฐาน (FUNDAMENTAL) ================= -->
            <div class="content-view" id="view-topic-1">
                <div class="subview-container">
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>📋 1. การจัดให้มีปัจจัยพื้นฐาน (Fundamental) ในการบริหารทรัพยากรบุคคล (น้ำหนัก 30%)</h2>
                            <span class="pill-badge" id="v1-score-pill" style="background: #004b87; color: #ffffff;">น้ำหนัก 30% | ผลงานระดับ 5</span>
                        </div>

                        <!-- Rubric Scale Cards -->
                        <div class="rubric-grid-5">
                            <div class="rubric-card" id="v1-rubric-1">
                                <div class="rubric-card-header">ระดับ 1</div>
                                <div>กำหนดตัวชี้วัด แต่ยังอยู่ในช่วงทดลอง และยังไม่ได้นำมาใช้จริง</div>
                            </div>
                            <div class="rubric-card" id="v1-rubric-2">
                                <div class="rubric-card-header">ระดับ 2</div>
                                <div>กำหนดตัวชี้วัดในระดับผู้บริหารระดับสูงของทุนหมุนเวียน และใช้ในการประเมินผล</div>
                            </div>
                            <div class="rubric-card" id="v1-rubric-3">
                                <div class="rubric-card-header">ระดับ 3</div>
                                <div>กำหนดตัวชี้วัดในระดับผู้บริหารระดับสูงและผู้บริหารสายงาน และใช้ในการประเมินผล</div>
                            </div>
                            <div class="rubric-card" id="v1-rubric-4">
                                <div class="rubric-card-header">ระดับ 4</div>
                                <div>กำหนดตัวชี้วัดในบุคลากรทุกระดับของทุนหมุนเวียน และใช้ในการประเมินผล</div>
                            </div>
                            <div class="rubric-card active" id="v1-rubric-5">
                                <div class="rubric-card-header">ระดับ 5 ★</div>
                                <div>ผ่านระดับ 3 หรือ 4 + ใช้ประโยชน์จากผลประเมินพิจารณาผลตอบแทน/เลื่อนขั้น และพัฒนาบุคลากร</div>
                            </div>
                        </div>

                        <!-- Process Workflow Cards -->
                        <div class="timeline-steps">
                            <div class="step-box primary-step">
                                <div class="step-number">รอบการประเมินที่ 1</div>
                                <div class="step-title">ต.ค. 68 - มี.ค. 69 (รอบ 1/69)</div>
                                <div class="step-desc">กำหนดตัวชี้วัด 3 องค์ประกอบ (ผลสัมฤทธิ์, สมรรถนะ, จริยธรรม) ทั้งข้าราชการและพนักงานทุนหมุนเวียน ถ่ายทอดจากผู้บริหารสู่ผู้ปฏิบัติงาน</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">รอบการประเมินที่ 2</div>
                                <div class="step-title">เม.ย. 69 - ก.ย. 69 (รอบ 2/69)</div>
                                <div class="step-desc">ดำเนินการประเมินผลการปฏิบัติงานช่วงเดือนกันยายน 2569 ครบถ้วนตามมาตรฐานสำนักงานปลัดกระทรวงศึกษาธิการ และ ก.ค.ศ.</div>
                            </div>
                            <div class="step-box">
                                <div class="step-number">การใช้ประโยชน์ 1</div>
                                <div class="step-title">เลื่อนขั้น / ผลตอบแทน</div>
                                <div class="step-desc">รอบ 1 ข้าราชการดีเด่น 9 คน ดีมาก 2 คน | รอบ 2 พนักงานทุนหมุนเวียนเลื่อนค่าตอบแทนระดับดีเด่น 13 คน ตามประกาศ สป.ศธ.</div>
                            </div>
                            <div class="step-box">
                                <div class="step-number">การใช้ประโยชน์ 2</div>
                                <div class="step-title">การพัฒนาบุคลากร</div>
                                <div class="step-desc">วิเคราะห์ผลประเมินเพื่อเสริมประสิทธิภาพการทำงานไม่ให้ผิดพลาด และพัฒนาความรู้ความสามารถด้าน AI สนับสนุนการปฏิบัติงาน</div>
                            </div>
                        </div>

                        <!-- 2 Detail Column Cards -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                            <div class="callout-box callout-info" style="font-size: 13px;">
                                <h4 style="color: #0369a1;">📝 การจัดทำระบบประเมินผลรายบุคคล 2 รอบ (ทุกระดับ)</h4>
                                <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                                    <li><strong>ข้าราชการ:</strong> ดำเนินการตามหนังสือ สป.ศธ. (ศธ 0201.4/18894 และ ศธ 0201.4/8970) มี 3 องค์ประกอบ คือ ผลสัมฤทธิ์ของงาน (ตัวชี้วัดรายบุคคล), พฤติกรรมการปฏิบัติราชการ (สมรรถนะ), และประมวลจริยธรรม</li>
                                    <li><strong>พนักงานทุนหมุนเวียน:</strong> ดำเนินการตามหนังสือ ก.ค.ศ. (ศธ 0206.8/30 และ ศธ 0206.8/318) มี 2 องค์ประกอบ คือ ผลสัมฤทธิ์ของงาน และพฤติกรรมสมรรถนะ</li>
                                    <li><strong>การมีส่วนร่วม:</strong> ถ่ายทอดตัวชี้วัดจากผู้บริหารระดับสูง สู่ ผอ.สำนัก หัวหน้างาน และเจ้าหน้าที่ผู้ปฏิบัติงานทุกระดับร่วมกันกำหนด</li>
                                </ul>
                            </div>
                            <div class="callout-box callout-success" style="font-size: 13px;">
                                <h4 style="color: #15803d;">🏆 การนำผลการประเมินไปใช้ประโยชน์ครบ 2 ด้าน (เกณฑ์ระดับ 5)</h4>
                                <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                                    <li><strong>ด้านพิจารณาผลตอบแทน/เลื่อนขั้น:</strong> ข้าราชการได้รับประกาศเลื่อนขั้นเงินเดือนรอบ 1 (ดีเด่น 9 คน, ดีมาก 2 คน) และพนักงานทุนหมุนเวียนได้รับพิจารณาเลื่อนผลตอบแทนสิ้นปีงบประมาณระดับดีเด่น 13 คน</li>
                                    <li><strong>ด้านการพัฒนาบุคลากร:</strong> นำผลการวิเคราะห์ไปจัดทำแผนพัฒนา 2 ทักษะสำคัญ ได้แก่ การปฏิบัติงานราชการอย่างถูกต้องแม่นยำ และการประยุกต์ใช้ AI ในการทำงาน</li>
                                    <li><strong>เอกสารอ้างอิง:</strong> เอกสารหมายเลข 1 ถึง 7 (บันทึกข้อความ, แบบประเมิน, ประกาศผลการปฏิบัติราชการ)</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Bottom Summary Strip -->
                        <div class="hero-score-box" style="padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; text-align: left;">
                            <div>
                                <span style="font-size: 12px; color: #93c5fd; font-weight: 600;">ผลการดำเนินงานข้อ 1 (น้ำหนัก 30%)</span>
                                <div style="font-size: 20px; font-weight: 800; color: #ffcc00;" id="v1-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★★★</span></div>
                            </div>
                            <div style="font-size: 12.5px; color: #e2e8f0; max-width: 65%; text-align: right;" id="v1-bottom-callout">
                                บรรลุเกณฑ์ระดับ 5: บุคลากรทุกระดับจัดทำตัวชี้วัดรายบุคคล นำผลประเมินไปใช้เลื่อนขั้นเงินเดือนและพัฒนาทักษะ AI (คะแนนถ่วงน้ำหนัก 1.5000)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 2: ข้อ 2.1 แผนปฏิบัติการ HR ประจำปี 2569 ================= -->
            <div class="content-view" id="view-topic-2">
                <div class="subview-container">
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>🚀 2.1 การดำเนินงานตามแผนปฏิบัติการด้านการบริหารทรัพยากรบุคคล ประจำปีบัญชี 2569 (น้ำหนัก 35%)</h2>
                            <span class="pill-badge" id="v2-score-pill" style="background: #004b87; color: #ffffff;">น้ำหนัก 35% | ผลงานระดับ 5</span>
                        </div>

                        <!-- Rubric Scale Cards -->
                        <div class="rubric-grid-5">
                            <div class="rubric-card" id="v2-rubric-1">
                                <div class="rubric-card-header">ระดับ 1</div>
                                <div>ดำเนินงานตามแผนปฏิบัติการฯ ได้ร้อยละ 80</div>
                            </div>
                            <div class="rubric-card" id="v2-rubric-2">
                                <div class="rubric-card-header">ระดับ 2</div>
                                <div>ดำเนินงานตามแผนปฏิบัติการฯ ได้ร้อยละ 90</div>
                            </div>
                            <div class="rubric-card" id="v2-rubric-3">
                                <div class="rubric-card-header">ระดับ 3</div>
                                <div>ดำเนินงานตามแผนปฏิบัติการฯ ได้ร้อยละ 100</div>
                            </div>
                            <div class="rubric-card" id="v2-rubric-4">
                                <div class="rubric-card-header">ระดับ 4</div>
                                <div>ดำเนินงานได้ร้อยละ 100 โดยมีผลดีกว่าเป้าหมายครบถ้วน หรือ จัดทำรายงานครอบคลุมปัจจัยสำเร็จ ปัญหา/อุปสรรค ข้อเสนอแนะ</div>
                            </div>
                            <div class="rubric-card active" id="v2-rubric-5">
                                <div class="rubric-card-header">ระดับ 5 ★</div>
                                <div>ดำเนินงานได้ร้อยละ 100 โดยมีผลดีกว่าเป้าหมายครบถ้วน และ จัดทำรายงานครอบคลุมปัจจัยสำเร็จ ปัญหา/อุปสรรค ข้อเสนอแนะ</div>
                            </div>
                        </div>

                        <!-- 3 Main Action Plan Activities -->
                        <div class="timeline-steps">
                            <div class="step-box primary-step">
                                <div class="step-number">กิจกรรมที่ 1</div>
                                <div class="step-title">การสรรหาและบรรจุอัตรากำลัง</div>
                                <div class="step-desc">เปิดรับสมัครพนักงานทุนหมุนเวียน 2 อัตรา ได้แก่ นักวิชาการคอมพิวเตอร์ (เริ่มงาน 2 ก.พ. 69) และนิติกร (เริ่มงาน 15 มิ.ย. 69) เพื่อเสริมศักยภาพงาน</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">กิจกรรมที่ 2</div>
                                <div class="step-title">การประเมินผลปฏิบัติงาน 2 รอบ</div>
                                <div class="step-desc">จัดทำและปรับปรุงตัวชี้วัดรายบุคคลรอบ 1 และรอบ 2 อย่างเป็นระบบ ครอบคลุมทั้งข้าราชการและพนักงานทุนหมุนเวียนทุกระดับ</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">กิจกรรมที่ 3</div>
                                <div class="step-title">ประชุมเชิงปฏิบัติการพัฒนาบุคลากร</div>
                                <div class="step-desc">จัดประชุม 18-20 ธ.ค. 68 ณ เขาใหญ่ นครราชสีมา (25 คน) หัวข้อการสื่อสาร เทคนิคทวงหนี้ เจรจาต่อรอง ทักษะดิจิทัล และทีมงานสู่ความเป็นเลิศ</div>
                            </div>
                        </div>

                        <!-- Performance & Training Evaluation Grid -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                            <div class="callout-box callout-success" style="font-size: 13px;">
                                <h4 style="color: #15803d;">📈 ผลสัมฤทธิ์การพัฒนาบุคลากร (ดีกว่าเป้าหมายที่กำหนด)</h4>
                                <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                                    <li><strong>การทดสอบความรู้ (Pre-Post Test):</strong> ค่าเฉลี่ยก่อนการอบรม 17.36 คะแนน (86.80%) ➔ หลังการอบรมเพิ่มขึ้นเป็น <strong>19.88 คะแนน (99.40%)</strong> เพิ่มขึ้นเฉลี่ย 2.52 คะแนน (12.60%)</li>
                                    <li><strong>ผู้ผ่านเกณฑ์พัฒนา:</strong> ผู้เข้าอบรม 20 จาก 25 คน (ร้อยละ 80.00) มีคะแนนหลังอบรมสูงขึ้น บรรลุตามเกณฑ์ตัวชี้วัดโครงการ (ไม่น้อยกว่า 80%)</li>
                                    <li><strong>คะแนนเต็ม 20:</strong> มีผู้ได้คะแนนเต็ม 20 คะแนนถึง 22 คน (ร้อยละ 88.00) และได้ 19 คะแนน 3 คน (ร้อยละ 12.00)</li>
                                </ul>
                            </div>
                            <div class="callout-box callout-info" style="font-size: 13px;">
                                <h4 style="color: #0369a1;">📊 ความพึงพอใจและรายงานผลครบถ้วน (เกณฑ์ระดับ 5)</h4>
                                <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                                    <li><strong>ความพึงพอใจภาพรวม:</strong> อยู่ในระดับมากที่สุด ค่าเฉลี่ย <strong>4.43 (S.D. = 0.80, ร้อยละ 88.55)</strong> โดยด้านการบรรยาย/ฝึกปฏิบัติได้ค่าเฉลี่ยสูงสุด 4.62 (92.40%)</li>
                                    <li><strong>รายงานผลครอบคลุมองค์ประกอบครบถ้วน:</strong> จัดทำรายงานวิเคราะห์ปัจจัยสำเร็จ, ปัญหาอุปสรรค, และข้อเสนอแนะในการปฏิบัติงานจริง</li>
                                    <li><strong>เอกสารอ้างอิง:</strong> เอกสารหมายเลข 8 ถึง 12 (แผนปฏิบัติการ HR ปี 2569, ประกาศสรรหา, อนุมัติโครงการ, รายงานผลโครงการ)</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Bottom Summary Strip -->
                        <div class="hero-score-box" style="padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; text-align: left;">
                            <div>
                                <span style="font-size: 12px; color: #93c5fd; font-weight: 600;">ผลการดำเนินงานข้อ 2.1 (น้ำหนัก 35%)</span>
                                <div style="font-size: 20px; font-weight: 800; color: #ffcc00;" id="v2-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★★★</span></div>
                            </div>
                            <div style="font-size: 12.5px; color: #e2e8f0; max-width: 65%; text-align: right;" id="v2-bottom-callout">
                                บรรลุเกณฑ์ระดับ 5: ดำเนินการตามแผนฯ ครบ 100% ผลการอบรมดีกว่าเป้าหมาย (99.40%) และจัดทำรายงานครบทุกองค์ประกอบ (คะแนนถ่วงน้ำหนัก 1.7500)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 3: ข้อ 2.2 แผน HR ระยะยาว & ปี 2570 ================= -->
            <div class="content-view" id="view-topic-3">
                <div class="subview-container">
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>📑 2.2 การจัดทำ/ทบทวนแผนการบริหารทรัพยากรบุคคล (ระยะยาว) และแผนปฏิบัติการด้านการบริหารทรัพยากรบุคคลประจำปี 2570 (น้ำหนัก 35%)</h2>
                            <span class="pill-badge" id="v3-score-pill" style="background: #004b87; color: #ffffff;">น้ำหนัก 35% | ผลงานระดับ 5</span>
                        </div>

                        <!-- Rubric Scale Cards -->
                        <div class="rubric-grid-5">
                            <div class="rubric-card" id="v3-rubric-1">
                                <div class="rubric-card-header">ระดับ 1</div>
                                <div>มีความคืบหน้าร้อยละ 80 ของการจัดทำ/ทบทวนแผนระยะยาว และแผนปฏิบัติการฯ ปี 2570</div>
                            </div>
                            <div class="rubric-card" id="v3-rubric-2">
                                <div class="rubric-card-header">ระดับ 2</div>
                                <div>จัดทำ/ทบทวนแผนระยะยาว หรือ แผนปฏิบัติการฯ ปี 2570 ได้แล้วเสร็จภายในปีบัญชี</div>
                            </div>
                            <div class="rubric-card" id="v3-rubric-3">
                                <div class="rubric-card-header">ระดับ 3</div>
                                <div>จัดทำ/ทบทวนแผนระยะยาว และ แผนปฏิบัติการฯ ปี 2570 ได้แล้วเสร็จภายในปีบัญชี</div>
                            </div>
                            <div class="rubric-card" id="v3-rubric-4">
                                <div class="rubric-card-header">ระดับ 4</div>
                                <div>จัดทำแผนทั้ง 2 ฉบับเสร็จสิ้นภายในปีบัญชี และได้รับความเห็นชอบจากคณะกรรมการบริหารทุนหมุนเวียน</div>
                            </div>
                            <div class="rubric-card active" id="v3-rubric-5">
                                <div class="rubric-card-header">ระดับ 5 ★</div>
                                <div>แผนทั้ง 2 ฉบับเสร็จสิ้น + คกก.บริหารฯ เห็นชอบ + สื่อสารให้ผู้บริหารและหน่วยงานภายในรับทราบภายในปี 2569</div>
                            </div>
                        </div>

                        <!-- 4 Step Implementation Flow -->
                        <div class="timeline-steps">
                            <div class="step-box">
                                <div class="step-number">ขั้นตอนที่ 1</div>
                                <div class="step-title">ทบทวน & ศึกษาบริบท</div>
                                <div class="step-desc">ศึกษาบริบทที่เกี่ยวข้องของแผนบริหารทรัพยากรบุคคลระยะยาวเดิม (2569-2571) และแผนปี 2569 เพื่อกำหนดกรอบทิศทาง</div>
                            </div>
                            <div class="step-box">
                                <div class="step-number">ขั้นตอนที่ 2</div>
                                <div class="step-title">ยกร่างแผนทั้ง 2 ฉบับ</div>
                                <div class="step-desc">ยกร่างแผน HR ระยะ 3 ปี (พ.ศ. 2570 - 2572) และแผนปฏิบัติการด้าน HR ประจำปีบัญชี 2570 ให้สอดคล้องกับแผนยุทธศาสตร์องค์กร</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">ขั้นตอนที่ 3 (มติ คกก.)</div>
                                <div class="step-title">คกก.บริหารฯ เห็นชอบ</div>
                                <div class="step-desc">การประชุม คกก.บริหารเงินทุนหมุนเวียนฯ ครั้งที่ 5/2569 เมื่อวันที่ <strong>28 ส.ค. 2569</strong> มีมติเห็นชอบแผนทั้ง 2 ฉบับอย่างเป็นเอกฉันท์</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">ขั้นตอนที่ 4 (สื่อสาร)</div>
                                <div class="step-title">แจ้งเวียนรับทราบครบถ้วน</div>
                                <div class="step-desc">มีหนังสือแจ้งเวียนให้ผู้บริหารและหน่วยงานภายในรับทราบ ตามหนังสือ ศธ 0206.8/716 ลงวันที่ <strong>30 กันยายน 2569</strong></div>
                            </div>
                        </div>

                        <!-- Detail Cards -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                            <div class="callout-box callout-info" style="font-size: 13px;">
                                <h4 style="color: #0369a1;">📘 รายละเอียดแผน HR ทั้ง 2 ฉบับที่จัดทำแล้วเสร็จ</h4>
                                <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                                    <li><strong>แผนการบริหารทรัพยากรบุคคล ระยะ 3 ปี (พ.ศ. 2570 - 2572):</strong> กำหนดกรอบการพัฒนาขีดความสามารถบุคลากร, การบริหารอัตรากำลัง, วัฒนธรรมองค์กร, และการปรับตัวสู่เทคโนโลยีดิจิทัลและ AI</li>
                                    <li><strong>แผนปฏิบัติการด้านการบริหารทรัพยากรบุคคล ประจำปีบัญชี 2570:</strong> กำหนดโครงการ กิจกรรม เป้าหมายตัวชี้วัด กรอบระยะเวลา และงบประมาณรองรับการพัฒนาบุคลากรอย่างเป็นรูปธรรม</li>
                                    <li><strong>ความสอดคล้อง:</strong> เชื่อมโยงกับแผนปฏิบัติการระยะยาว 3 ปี (2570-2572) ของเงินทุนหมุนเวียนที่ได้รับอนุมัติจากกรมบัญชีกลาง</li>
                                </ul>
                            </div>
                            <div class="callout-box callout-success" style="font-size: 13px;">
                                <h4 style="color: #15803d;">🏆 การบรรลุเกณฑ์ระดับ 5 อย่างสมบูรณ์</h4>
                                <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                                    <li><strong>ได้รับความเห็นชอบจาก คกก.บริหารฯ:</strong> มติที่ประชุมครั้งที่ 5/2569 เมื่อ 28 ส.ค. 69 เห็นชอบแผนทั้ง 2 ฉบับ (เอกสารหมายเลข 13)</li>
                                    <li><strong>สื่อสารให้ผู้บริหารและหน่วยงานภายในรับทราบ:</strong> จัดทำบันทึกข้อความแจ้งเวียน ที่ ศธ 0206.8/716 ลงวันที่ 30 กันยายน 2569 ภายในปีบัญชี 2569 ครบถ้วน (เอกสารหมายเลข 16)</li>
                                    <li><strong>สรุปผลการประเมิน:</strong> บรรลุตามเงื่อนไขระดับ 5 ครบถ้วน 100% คิดเป็นระดับ 5.0000 คะแนน</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Bottom Summary Strip -->
                        <div class="hero-score-box" style="padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; text-align: left;">
                            <div>
                                <span style="font-size: 12px; color: #93c5fd; font-weight: 600;">ผลการดำเนินงานข้อ 2.2 (น้ำหนัก 35%)</span>
                                <div style="font-size: 20px; font-weight: 800; color: #ffcc00;" id="v3-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★★★</span></div>
                            </div>
                            <div style="font-size: 12.5px; color: #e2e8f0; max-width: 65%; text-align: right;" id="v3-bottom-callout">
                                บรรลุเกณฑ์ระดับ 5: จัดทำแผนทั้ง 2 ฉบับ คกก.บริหารฯ เห็นชอบ (28 ส.ค. 69) และสื่อสารแจ้งเวียนภายในปี 2569 (30 ก.ย. 69) (คะแนนถ่วงน้ำหนัก 1.7500)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Dashboard Footer -->
        <div class="dashboard-footer">
            <div>สำนักงานคณะกรรมการข้าราชการครูและบุคลากรทางการศึกษา (ก.ค.ศ.) | สำนักบริหารเงินทุนหมุนเวียนเพื่อแก้ไขปัญหาหนี้สินข้าราชการครู</div>
            <div>คุณภาพการบริหาร เพื่อครู เพื่ออนาคตการศึกษาไทย</div>
        </div>

    </div>

    <!-- Toast Notification Element -->
    <div id="toast">บันทึกข้อมูลเรียบร้อยแล้ว</div>

    <!-- Application JavaScript Logic -->
    <script>
        /* State Management */
        let activeQuarter = 4;
        let activeTopic = 0;
        let currentAppMode = 'preview'; // 'preview' or 'edit'

        const topicNames = [
            'ภาพรวม 2 ข้อ',
            '1. ปัจจัยพื้นฐาน HR',
            '2.1 แผนปฏิบัติการ HR ปี 69',
            '2.2 แผน HR ระยะยาว & ปี 70'
        ];

        /* KPI Routes Navigation */
        function navigateToKPI(kpiValue) {
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
                '5.2': 'ตัวชี้วัดที่ 5.2.html'
            };
            if (routes[kpiValue]) {
                window.location.href = routes[kpiValue];
            }
        }

        /* Subtopics Switching Logic */
        function switchTopicView(topicIndex) {
            activeTopic = topicIndex;
            for (let i = 0; i <= 3; i++) {
                const tab = document.getElementById(`tab-v${i}`);
                const view = document.getElementById(`view-topic-${i}`);
                if (tab) tab.classList.toggle('active', i === topicIndex);
                if (view) view.classList.toggle('active', i === topicIndex);
            }
        }

        /* Official Data Model for Each Quarter */
        const quarterDefaults = {
            1: {
                heroScore: 'ระดับ 1.6000 คะแนน',
                heroStars: '★☆☆☆☆',
                statusBadge: 'ระดับ 1.60 (เบื้องต้น)',
                completeVal: 'เริ่มต้น 2 ข้อ',
                gradeVal: 'ระดับ 1.60 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 1: จัดทำและปรับปรุงตัวชี้วัดรายบุคคลรอบที่ 1 ทั้งข้าราชการและพนักงานทุนหมุนเวียน จัดประชุมเชิงปฏิบัติการพัฒนาประสิทธิภาพการปฏิบัติงาน (18-20 ธ.ค. 68 ณ เขาใหญ่) และเปิดรับสมัครพนักงานทุนหมุนเวียน 2 อัตรา ส่วนแผน HR ระยะยาวและปี 2570 อยู่ระหว่างเตรียมการทบทวนบริบท',
                table: {
                    s1: '3.0000', ws1: '0.9000',
                    s2: '2.0000', ws2: '0.7000',
                    s3: 'N/A', ws3: '0.0000',
                    totLevel: 'ระดับ 1.60 (เบื้องต้น)', totWScore: '1.6000 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงานระดับ 3',
                    activeRubric: 3,
                    bottomVal: 'ระดับ 3.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★☆☆</span>',
                    bottomCallout: 'ไตรมาส 1: กำหนดตัวชี้วัดรายบุคคลรอบที่ 1 ถ่ายทอดจากผู้บริหารสู่บุคลากรทุกระดับเพื่อใช้ประเมินผล (คะแนนถ่วงน้ำหนัก 0.9000)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 2',
                    activeRubric: 2,
                    bottomVal: 'ระดับ 2.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★☆☆☆</span>',
                    bottomCallout: 'ไตรมาส 1: ดำเนินการจัดประชุมเชิงปฏิบัติการพัฒนาบุคลากร (18-20 ธ.ค. 68) และประกาศรับสมัครพนักงานทุนหมุนเวียน (คะแนนถ่วงน้ำหนัก 0.7000)'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | อยู่ระหว่างเตรียมการ (N/A)',
                    activeRubric: 1,
                    bottomVal: 'N/A (เตรียมการทบทวนบริบท)',
                    bottomCallout: 'ไตรมาส 1: อยู่ระหว่างเตรียมการทบทวนและศึกษาบริบทของแผน HR ระยะยาวเดิม (2569-2571) (คะแนนถ่วงน้ำหนัก 0.0000)'
                }
            },
            2: {
                heroScore: 'ระดับ 2.2500 คะแนน',
                heroStars: '★★☆☆☆',
                statusBadge: 'ระดับ 2.25 (เบื้องต้น)',
                completeVal: 'ผ่านเกณฑ์ 2 ข้อ',
                gradeVal: 'ระดับ 2.25 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 2: ประเมินผลการปฏิบัติงานรอบที่ 1 (ต.ค. 68 - มี.ค. 69) ครอบคลุมบุคลากรทุกระดับ รับรายงานตัวนักวิชาการคอมพิวเตอร์ (2 ก.พ. 69) เปิดรับสมัครนิติกร ดำเนินการตามแผนปฏิบัติการฯ ได้ร้อยละ 100 ในกิจกรรมที่กำหนด (ระดับ 3) และอยู่ระหว่างทบทวนศึกษาบริบทเพื่อยกร่างแผน HR ระยะยาวและปี 2570',
                table: {
                    s1: '4.0000', ws1: '1.2000',
                    s2: '3.0000', ws2: '1.0500',
                    s3: 'N/A', ws3: '0.0000',
                    totLevel: 'ระดับ 2.25 (เบื้องต้น)', totWScore: '2.2500 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงานระดับ 4',
                    activeRubric: 4,
                    bottomVal: 'ระดับ 4.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★★☆</span>',
                    bottomCallout: 'ไตรมาส 2: ประเมินผลการปฏิบัติงานรอบที่ 1 เสร็จสิ้นในบุคลากรทุกระดับของทุนหมุนเวียน (คะแนนถ่วงน้ำหนัก 1.2000)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 3',
                    activeRubric: 3,
                    bottomVal: 'ระดับ 3.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★☆☆</span>',
                    bottomCallout: 'ไตรมาส 2: ดำเนินงานตามแผนปฏิบัติการฯ ได้ร้อยละ 100 ตามกิจกรรมที่กำหนดในรอบไตรมาส (คะแนนถ่วงน้ำหนัก 1.0500)'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | อยู่ระหว่างทบทวนบริบท (N/A)',
                    activeRubric: 1,
                    bottomVal: 'N/A (อยู่ระหว่างทบทวนบริบท)',
                    bottomCallout: 'ไตรมาส 2: อยู่ในขั้นตอนการทบทวน ศึกษาบริบทที่เกี่ยวข้องของแผน HR ระยะยาวเดิมและแผนปี 2569 (คะแนนถ่วงน้ำหนัก 0.0000)'
                }
            },
            3: {
                heroScore: 'ระดับ 2.2500 คะแนน',
                heroStars: '★★☆☆☆',
                statusBadge: 'ระดับ 2.25 (เบื้องต้น)',
                completeVal: 'ผ่านเกณฑ์ 2 ข้อ',
                gradeVal: 'ระดับ 2.25 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 3: ข้าราชการได้รับการประกาศเลื่อนขั้นรอบ 1 (ดีเด่น 9 คน ดีมาก 2 คน) นิติกรเริ่มงาน (15 มิ.ย. 69) ดำเนินงานตามแผนปฏิบัติการฯ ได้ร้อยละ 100 (ระดับ 3) ยกร่างแผน HR ระยะ 3 ปี (2570-2572) และแผนปี 2570 แล้วเสร็จ โดยเตรียมเสนอ คกก.บริหารฯ พิจารณาให้ความเห็นชอบในเดือนสิงหาคม 2569',
                table: {
                    s1: '4.0000', ws1: '1.2000',
                    s2: '3.0000', ws2: '1.0500',
                    s3: 'N/A', ws3: '0.0000',
                    totLevel: 'ระดับ 2.25 (เบื้องต้น)', totWScore: '2.2500 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงานระดับ 4',
                    activeRubric: 4,
                    bottomVal: 'ระดับ 4.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★★☆</span>',
                    bottomCallout: 'ไตรมาส 3: นำผลประเมินรอบ 1 ไปใช้เลื่อนขั้นข้าราชการ และอยู่ระหว่างเตรียมประเมินผลรอบ 2 ในเดือน ก.ย. 69 (คะแนนถ่วงน้ำหนัก 1.2000)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 3',
                    activeRubric: 3,
                    bottomVal: 'ระดับ 3.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★★★☆☆</span>',
                    bottomCallout: 'ไตรมาส 3: ดำเนินงานตามแผนปฏิบัติการฯ ได้ร้อยละ 100 โดยรับบรรจุนิติกร และอยู่ระหว่างสรุปรายงานผล (คะแนนถ่วงน้ำหนัก 1.0500)'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | ยกร่างแล้วเสร็จ รอเสนอ คกก. (N/A)',
                    activeRubric: 2,
                    bottomVal: 'N/A (ยกร่างเสร็จ รอเสนอ คกก.)',
                    bottomCallout: 'ไตรมาส 3: ยกร่างแผน HR 3 ปี และแผนปี 2570 แล้วเสร็จ โดยเตรียมเสนอคณะกรรมการบริหารฯ ในเดือน ส.ค. 69 (คะแนนถ่วงน้ำหนัก 0.0000)'
                }
            },
            4: {
                heroScore: 'ระดับ 5.0000 คะแนน',
                heroStars: '★★★★★',
                statusBadge: 'ระดับ 5.0000 (เต็ม)',
                completeVal: 'ครบ 2 ข้อ',
                gradeVal: 'ระดับ 5 (เต็ม)',
                summaryDesc: 'งวดสิ้นปีบัญชี 2569: ดำเนินงานบรรลุเกณฑ์ระดับ 5 ครบถ้วนทุกข้อ บุคลากรทุกคนได้รับการประเมินผล 2 รอบอย่างเป็นระบบ นำผลประเมินไปใช้เลื่อนขั้นเงินเดือนและพัฒนาทักษะดิจิทัล/AI ดำเนินการตามแผนปฏิบัติการฯ 2569 ครบทั้ง 3 กิจกรรมด้วยผลการประเมินความพึงพอใจร้อยละ 88.55 และจัดทำแผน HR ระยะ 3 ปี (2570-2572) ร่วมกับแผนปี 2570 ผ่านความเห็นชอบของคณะกรรมการบริหารเงินทุนหมุนเวียนฯ และแจ้งเวียนหน่วยงานที่เกี่ยวข้องครบถ้วน',
                table: {
                    s1: '5.0000', ws1: '1.5000',
                    s2: '5.0000', ws2: '1.7500',
                    s3: '5.0000', ws3: '1.7500',
                    totLevel: 'ระดับ 5.0', totWScore: '5.0000 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'บรรลุเกณฑ์ระดับ 5: บุคลากรทุกระดับจัดทำตัวชี้วัดรายบุคคล นำผลประเมินไปใช้เลื่อนขั้นเงินเดือนและพัฒนาทักษะ AI (คะแนนถ่วงน้ำหนัก 1.5000)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'บรรลุเกณฑ์ระดับ 5: ดำเนินการตามแผนฯ ครบ 100% ผลการอบรมดีกว่าเป้าหมาย (99.40%) และจัดทำรายงานครบทุกองค์ประกอบ (คะแนนถ่วงน้ำหนัก 1.7500)'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'บรรลุเกณฑ์ระดับ 5: จัดทำแผนทั้ง 2 ฉบับ คกก.บริหารฯ เห็นชอบ (28 ส.ค. 69) และสื่อสารแจ้งเวียนภายในปี 2569 (30 ก.ย. 69) (คะแนนถ่วงน้ำหนัก 1.7500)'
                }
            }
        };

        /* Switch Quarter Logic */
        function changeFiscalYear(yr) {
            showToast(`เลือกดูข้อมูลปีงบประมาณ ${yr}`);
        }

        function switchQuarter(qNum) {
            activeQuarter = parseInt(qNum);
            const qSelect = document.getElementById('quarter-focus');
            if (qSelect) qSelect.value = activeQuarter;

            const qBadge = document.getElementById('quarter-badge');
            if (qBadge) {
                qBadge.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg> ไตรมาส ${activeQuarter}`;
            }

            // Apply official data directly in preview mode
            applyQuarterData(activeQuarter);

            // In edit mode only, load custom edits from localStorage
            if (currentAppMode === 'edit') {
                const saved = localStorage.getItem(getStorageKey(activeQuarter));
                if (saved) {
                    try {
                        const parsed = JSON.parse(saved);
                        loadCustomEdits(parsed);
                    } catch (e) {
                        console.error("Failed to parse saved quarter data", e);
                    }
                }
            }

            showToast(`สลับข้อมูลเป็นไตรมาสที่ ${activeQuarter} เรียบร้อยแล้ว`);
        }

        function applyQuarterData(q) {
            const data = quarterDefaults[q] || quarterDefaults[4];

            // 1. Overview Elements
            const heroScore = document.getElementById('score-hero-val');
            if (heroScore) heroScore.innerText = data.heroScore;

            const heroStars = document.getElementById('score-hero-stars');
            if (heroStars) heroStars.innerText = data.heroStars;

            const statusBadge = document.getElementById('score-status-badge');
            if (statusBadge) statusBadge.innerText = data.statusBadge;

            const metricComp = document.getElementById('metric-complete-val');
            if (metricComp) metricComp.innerText = data.completeVal;

            const metricGrade = document.getElementById('metric-grade-val');
            if (metricGrade) metricGrade.innerText = data.gradeVal;

            const sumDesc = document.getElementById('summary-overview-desc');
            if (sumDesc) sumDesc.innerText = data.summaryDesc;

            // Overview Table
            document.getElementById('tbl-score-1').innerText = data.table.s1;
            document.getElementById('tbl-wscore-1').innerText = data.table.ws1;
            document.getElementById('tbl-score-2').innerText = data.table.s2;
            document.getElementById('tbl-wscore-2').innerText = data.table.ws2;
            document.getElementById('tbl-score-3').innerText = data.table.s3;
            document.getElementById('tbl-wscore-3').innerText = data.table.ws3;
            document.getElementById('tbl-total-level').innerText = data.table.totLevel;
            document.getElementById('tbl-total-wscore').innerText = data.table.totWScore;

            // 2. View 1 Updates
            document.getElementById('v1-score-pill').innerText = data.v1.scorePill;
            document.getElementById('v1-bottom-val').innerHTML = data.v1.bottomVal;
            document.getElementById('v1-bottom-callout').innerText = data.v1.bottomCallout;
            updateRubricHighlight('v1', data.v1.activeRubric);

            // 3. View 2 Updates
            document.getElementById('v2-score-pill').innerText = data.v2.scorePill;
            document.getElementById('v2-bottom-val').innerHTML = data.v2.bottomVal;
            document.getElementById('v2-bottom-callout').innerText = data.v2.bottomCallout;
            updateRubricHighlight('v2', data.v2.activeRubric);

            // 4. View 3 Updates
            document.getElementById('v3-score-pill').innerText = data.v3.scorePill;
            document.getElementById('v3-bottom-val').innerHTML = data.v3.bottomVal;
            document.getElementById('v3-bottom-callout').innerText = data.v3.bottomCallout;
            updateRubricHighlight('v3', data.v3.activeRubric);
        }

        function updateRubricHighlight(prefix, activeNum) {
            for (let i = 1; i <= 5; i++) {
                const el = document.getElementById(`${prefix}-rubric-${i}`);
                if (el) {
                    if (i === activeNum) {
                        el.classList.add('active');
                        const header = el.querySelector('.rubric-card-header');
                        if (header && !header.innerText.includes('★')) {
                            header.innerText = header.innerText.trim() + ' ★';
                        }
                    } else {
                        el.classList.remove('active');
                        const header = el.querySelector('.rubric-card-header');
                        if (header) {
                            header.innerText = header.innerText.replace('★', '').trim();
                        }
                    }
                }
            }
        }

        /* Dual Mode Toggle (Preview vs Edit) */
        function setAppMode(mode) {
            currentAppMode = mode;
            const btnPreview = document.getElementById('btn-mode-preview');
            const btnEdit = document.getElementById('btn-mode-edit');
            const toolbar = document.getElementById('format-toolbar');

            const isEdit = (mode === 'edit');
            btnPreview.classList.toggle('active', !isEdit);
            btnEdit.classList.toggle('active', isEdit);
            toolbar.classList.toggle('show', isEdit);

            // Toggle editable attributes on targeted elements
            const editables = document.querySelectorAll('[contenteditable]');
            editables.forEach(el => {
                el.contentEditable = isEdit ? 'true' : 'false';
            });

            if (!isEdit) {
                applyQuarterData(activeQuarter);
            }

            showToast(isEdit ? 'เข้าสู่โหมดแก้ไขข้อความ (Edit Mode)' : 'เข้าสู่โหมดนำเสนอ (Preview Mode)');
        }

        /* Rich Text Formatting Command */
        function execCmd(command, value = null) {
            if (currentAppMode !== 'edit') return;
            document.execCommand(command, false, value);
        }

        /* LocalStorage Persistence */
        function getStorageKey(q) {
            return `kpi_52_custom_q${q}`;
        }

        function saveDashboardChanges() {
            const dataToSave = {
                heroScore: document.getElementById('score-hero-val').innerText,
                summaryDesc: document.getElementById('summary-overview-desc').innerHTML,
                bannerTitle: document.getElementById('editable-banner-title').innerHTML,
                bannerSub: document.getElementById('editable-banner-sub').innerHTML
            };

            localStorage.setItem(getStorageKey(activeQuarter), JSON.stringify(dataToSave));
            showToast(`บันทึกการแก้ไขของไตรมาส ${activeQuarter} สำเร็จแล้ว`);
        }

        function loadCustomEdits(saved) {
            if (saved.heroScore) document.getElementById('score-hero-val').innerText = saved.heroScore;
            if (saved.summaryDesc) document.getElementById('summary-overview-desc').innerHTML = saved.summaryDesc;
            if (saved.bannerTitle) document.getElementById('editable-banner-title').innerHTML = saved.bannerTitle;
            if (saved.bannerSub) document.getElementById('editable-banner-sub').innerHTML = saved.bannerSub;
        }

        /* Toast Popup Utility */
        function showToast(msg) {
            const toast = document.getElementById('toast');
            toast.innerText = msg;
            toast.style.display = 'block';
            setTimeout(() => {
                toast.style.display = 'none';
            }, 2500);
        }

        /* Fullscreen Toggle */
        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(err => {
                    alert(`Error attempting fullscreen: ${err.message}`);
                });
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                }
            }
        }

        /* Clipboard Copy */
        async function copyDashboardImage() {
            showToast("กำลังประมวลผลคัดลอกภาพ...");
            try {
                const element = document.getElementById('kpi-presentation-canvas');
                const canvas = await html2canvas(element, { scale: 2, useCORS: true });
                canvas.toBlob(blob => {
                    navigator.clipboard.write([
                        new ClipboardItem({ 'image/png': blob })
                    ]).then(() => {
                        showToast("คัดลอกภาพลง Clipboard สำเร็จแล้ว!");
                    }).catch(err => {
                        console.error("Clipboard write error:", err);
                        showToast("ไม่สามารถคัดลอกลง Clipboard ได้โดยตรง");
                    });
                });
            } catch (err) {
                console.error("Capture error:", err);
                showToast("เกิดข้อผิดพลาดในการจับภาพ");
            }
        }

        /* Direct PNG Export */
        async function exportDashboardPNG() {
            showToast("กำลังสร้างไฟล์ PNG...");
            try {
                const element = document.getElementById('kpi-presentation-canvas');
                const canvas = await html2canvas(element, { scale: 2, useCORS: true });
                const link = document.createElement('a');
                link.download = `รายงานตัวชี้วัดที่_5.2_ไตรมาส${activeQuarter}_${topicNames[activeTopic]}.png`;
                link.href = canvas.toDataURL('image/png');
                link.click();
                showToast("ดาวน์โหลดไฟล์ภาพ PNG สำเร็จแล้ว");
            } catch (error) {
                console.error("PNG Export error:", error);
                showToast("เกิดข้อผิดพลาดในการส่งออกภาพ");
            }
        }

        /* Direct Full-Page PDF Export */
        async function exportDashboardPDF() {
            showToast("กำลังสร้างไฟล์ PDF...");
            try {
                const element = document.getElementById('kpi-presentation-canvas');
                const canvas = await html2canvas(element, { scale: 2, useCORS: true });
                const imgData = canvas.toDataURL('image/png');
                const { jsPDF } = window.jspdf;

                const pdfWidth = canvas.width;
                const pdfHeight = canvas.height;
                const orientation = pdfWidth > pdfHeight ? 'landscape' : 'portrait';

                const pdf = new jsPDF({
                    orientation: orientation,
                    unit: 'px',
                    format: [pdfWidth, pdfHeight]
                });

                pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
                pdf.save(`รายงานตัวชี้วัดที่_5.2_ไตรมาส${activeQuarter}_${topicNames[activeTopic]}.pdf`);
                showToast("ดาวน์โหลดไฟล์ PDF เรียบร้อยแล้ว");
            } catch (error) {
                console.error("PDF Export error:", error);
                showToast("เกิดข้อผิดพลาดในการสร้างไฟล์ PDF");
            }
        }

        /* Initial Setup on Page Load */
        window.addEventListener('DOMContentLoaded', () => {
            switchQuarter(4);
            switchTopicView(0);
        });
    </script>
</body>
</html>
'''

with open('ตัวชี้วัดที่ 5.2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS_BUILD_52")
