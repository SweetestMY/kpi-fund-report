# -*- coding: utf-8 -*-
"""
Builder script for KPI 5.1: บทบาทคณะกรรมการบริหารทุนหมุนเวียน
"""

html_content = '''<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>แบบฟอร์มรายงานผลตัวชี้วัดที่ 5.1 บทบาทคณะกรรมการบริหารทุนหมุนเวียน (KPI Presentation Dashboard)</title>
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
            overflow-x: auto;
            box-sizing: border-box;
        }

        .page-wrapper {
            max-width: 1560px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .toolbar-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
            position: sticky;
            top: 10px;
            z-index: 1000;
        }

        .toolbar-ribbon {
            background: #ffffff;
            border: 1px solid rgba(188, 219, 242, 0.85);
            border-radius: 12px;
            padding: 8px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 14px rgba(0, 40, 85, 0.08);
            gap: 12px;
            flex-wrap: wrap;
        }

        .ribbon-left, .ribbon-center, .ribbon-right {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .control-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 13px;
            font-weight: 600;
            color: #004b87;
        }

        .select-input {
            padding: 5px 10px;
            border-radius: 6px;
            border: 1px solid #9ec5e8;
            background: #ffffff;
            font-size: 13px;
            font-weight: 500;
            color: #0f172a;
            cursor: pointer;
            outline: none;
            transition: all 0.2s;
        }

        .select-input:hover, .select-input:focus {
            border-color: #004b87;
            box-shadow: 0 0 0 2px rgba(0, 75, 135, 0.15);
        }

        .quarter-active-badge {
            background: #e0f2fe;
            color: #0369a1;
            padding: 3px 9px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            border: 1px solid #bae6fd;
        }

        .mode-segmented-control {
            display: flex;
            background: #f1f5f9;
            padding: 3px;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            gap: 2px;
        }

        .mode-btn {
            border: none;
            background: transparent;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 12.5px;
            font-weight: 600;
            color: #475569;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.2s;
        }

        .mode-btn.active {
            background: #004b87;
            color: #ffffff;
            box-shadow: 0 2px 6px rgba(0, 75, 135, 0.25);
        }

        .btn {
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 12.5px;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: none;
            transition: all 0.2s;
        }

        .btn-outline {
            background: #ffffff;
            color: #004b87;
            border: 1px solid #9ec5e8;
        }
        .btn-outline:hover {
            background: #f0f7ff;
            border-color: #004b87;
        }

        .btn-primary {
            background: #004b87;
            color: #ffffff;
        }
        .btn-primary:hover {
            background: #003661;
        }

        .btn-success {
            background: #059669;
            color: #ffffff;
        }
        .btn-success:hover {
            background: #047857;
        }

        .btn-warning {
            background: #d97706;
            color: #ffffff;
        }
        .btn-warning:hover {
            background: #b45309;
        }

        .btn-fmt {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 4px;
            padding: 3px 8px;
            font-size: 12px;
            font-weight: 600;
            color: #1e293b;
            cursor: pointer;
        }
        .btn-fmt:hover {
            background: #e2e8f0;
        }

        .tab-btn {
            border: 1px solid #9ec5e8;
            background: #f8fbfe;
            padding: 6px 13px;
            border-radius: 8px;
            font-size: 12.5px;
            font-weight: 600;
            color: #004b87;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.2s;
            white-space: nowrap;
        }

        .tab-btn:hover {
            background: #e0f2fe;
            border-color: #0284c7;
        }

        .tab-btn.active {
            background: #004b87;
            color: #ffffff;
            border-color: #003661;
            box-shadow: 0 3px 8px rgba(0, 75, 135, 0.25);
        }

        .tab-btn.active .tab-pct {
            background: rgba(255, 255, 255, 0.25) !important;
            color: #ffffff !important;
        }

        /* 16:9 Presentation Frame */
        .dashboard-container {
            background: #ffffff;
            border-radius: 14px;
            border: 1px solid rgba(188, 219, 242, 0.9);
            box-shadow: 0 6px 20px rgba(0, 40, 85, 0.08);
            padding: 22px 26px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            min-height: 820px;
            position: relative;
        }

        /* Header Banner */
        .header-banner {
            background: var(--primary-gradient);
            border-radius: 12px;
            padding: 14px 22px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(0, 31, 56, 0.25);
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .header-icon-box {
            font-size: 28px;
            background: rgba(255, 255, 255, 0.12);
            width: 52px;
            height: 52px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .main-heading {
            font-size: 20px;
            font-weight: 700;
            letter-spacing: -0.2px;
            color: #ffffff;
        }

        .sub-heading {
            font-size: 13.5px;
            color: #bae6fd;
            font-weight: 400;
            margin-top: 2px;
        }

        .header-right-tag {
            text-align: right;
            font-size: 12.5px;
            font-style: italic;
            color: #e0f2fe;
            line-height: 1.4;
        }

        /* KPI Metadata Bar */
        .kpi-meta-strip {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #f8fbfe;
            border: 1px solid #bfdbfe;
            border-radius: 10px;
            padding: 9px 18px;
            gap: 12px;
            flex-wrap: wrap;
        }

        .meta-pills-group {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .meta-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 13px;
            font-weight: 600;
            color: #1e3a8a;
            background: #ffffff;
            padding: 4px 12px;
            border-radius: 20px;
            border: 1px solid #cbd5e1;
        }

        .meta-pill .val {
            color: #0f172a;
            font-weight: 700;
        }

        .meta-pill-accent {
            background: #fef3c7;
            border-color: #fde68a;
            color: #92400e;
        }

        .rubric-target-inline {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .target-scale-box {
            display: flex;
            align-items: center;
            gap: 3px;
        }

        .target-step-cell {
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            text-align: center;
            background: #f1f5f9;
            color: #475569;
            border: 1px solid #cbd5e1;
            line-height: 1.2;
        }

        .target-step-cell.active-target {
            background: #0284c7;
            color: #ffffff;
            border-color: #0369a1;
            box-shadow: 0 1px 4px rgba(2, 132, 199, 0.3);
        }

        /* Content Views */
        .content-view {
            display: none;
            flex-direction: column;
            gap: 16px;
            animation: fadeIn 0.25s ease-in-out;
        }

        .content-view.active {
            display: flex;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(3px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* View 0: Overview 2 Columns Layout */
        .overview-grid {
            display: grid;
            grid-template-columns: 1.35fr 1fr;
            gap: 20px;
            align-items: stretch;
        }

        .card-panel {
            background: #ffffff;
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            box-shadow: 0 2px 8px rgba(0, 40, 85, 0.04);
        }

        .panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e0f2fe;
            padding-bottom: 10px;
        }

        .panel-title {
            font-size: 16px;
            font-weight: 700;
            color: #004b87;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Overview Table */
        .data-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            overflow: hidden;
            font-size: 13.5px;
        }

        .data-table th {
            background: #004b87;
            color: #ffffff;
            font-weight: 600;
            padding: 10px 12px;
            text-align: center;
            border-bottom: 1px solid #002647;
        }

        .data-table th:first-child { text-align: center; }
        .data-table th:nth-child(2) { text-align: left; }

        .data-table td {
            padding: 9px 12px;
            border-bottom: 1px solid #e2e8f0;
            color: var(--text-body);
        }

        .data-table tr:last-child td {
            border-bottom: none;
        }

        .data-table tbody tr {
            cursor: pointer;
            transition: background 0.15s;
        }

        .data-table tbody tr:hover {
            background: #f0f7ff;
        }

        .data-table tfoot tr {
            background: #f8fafc;
            font-weight: 700;
        }

        .data-table tfoot td {
            padding: 11px 12px;
            border-top: 2px solid #cbd5e1;
            color: #004b87;
        }

        /* Right Big Score Card */
        .score-hero-box {
            background: linear-gradient(135deg, #001f38 0%, #003661 100%);
            border-radius: 12px;
            padding: 22px 20px;
            color: #ffffff;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 8px;
            box-shadow: 0 4px 14px rgba(0, 31, 56, 0.2);
            border: 1px solid #004b87;
        }

        .score-hero-label {
            font-size: 14.5px;
            color: #bae6fd;
            font-weight: 500;
        }

        .score-hero-number {
            font-size: 38px;
            font-weight: 800;
            color: var(--accent-gold);
            letter-spacing: -0.5px;
            line-height: 1.1;
        }

        .stars-container {
            color: #facc15;
            font-size: 18px;
            letter-spacing: 3px;
        }

        .summary-card-inner {
            background: #f8fbfe;
            border: 1px solid #bfdbfe;
            border-radius: 10px;
            padding: 14px 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .summary-inner-title {
            font-size: 14px;
            font-weight: 700;
            color: #004b87;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .summary-inner-desc {
            font-size: 13.5px;
            color: #1e293b;
            line-height: 1.6;
        }

        .status-pills-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .status-metric-card {
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 8px;
            padding: 12px 14px;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .status-metric-label {
            font-size: 12px;
            font-weight: 600;
            color: #166534;
        }

        .status-metric-val {
            font-size: 18px;
            font-weight: 800;
            color: #15803d;
        }

        /* Subtopic Views: Rubric Scales Row */
        .rubric-strip {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
            margin-bottom: 4px;
        }

        .rubric-cell {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 10px 12px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            font-size: 12px;
            line-height: 1.45;
            color: #334155;
            transition: all 0.2s;
        }

        .rubric-cell .level-badge {
            font-size: 12px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 4px;
            display: inline-block;
            width: fit-content;
            background: #e2e8f0;
            color: #1e293b;
        }

        .rubric-cell.active {
            background: #eff6ff;
            border: 2px solid #004b87;
            box-shadow: 0 3px 10px rgba(0, 75, 135, 0.15);
        }

        .rubric-cell.active .level-badge {
            background: #004b87;
            color: #ffffff;
        }

        .rubric-cell.achieved-gold {
            background: #fffbeb;
            border: 2px solid #d97706;
            box-shadow: 0 3px 10px rgba(217, 119, 6, 0.2);
        }

        .rubric-cell.achieved-gold .level-badge {
            background: #d97706;
            color: #ffffff;
        }

        /* Detail Work Cards */
        .subview-grid-cards {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }

        .work-card {
            background: #ffffff;
            border: 1px solid var(--card-border);
            border-radius: 10px;
            padding: 16px 18px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            box-shadow: 0 2px 6px rgba(0, 40, 85, 0.03);
        }

        .work-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1.5px solid #e0f2fe;
            padding-bottom: 8px;
        }

        .work-card-title {
            font-size: 15px;
            font-weight: 700;
            color: #004b87;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .work-card-body {
            font-size: 13.5px;
            color: #1e293b;
            line-height: 1.6;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        /* Milestone Flow Steps */
        .milestone-stepper {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            background: #f8fbfe;
            border: 1px solid #bfdbfe;
            border-radius: 10px;
            padding: 12px 16px;
            flex-wrap: wrap;
        }

        .step-item {
            flex: 1;
            min-width: 130px;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 9px 12px;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 3px;
        }

        .step-item.step-complete {
            background: #f0fdf4;
            border-color: #86efac;
        }

        .step-title {
            font-size: 12.5px;
            font-weight: 700;
            color: #004b87;
        }

        .step-sub {
            font-size: 11.5px;
            color: #475569;
        }

        .step-arrow {
            color: #94a3b8;
            font-size: 16px;
            font-weight: 700;
        }

        /* Bottom Score Strip */
        .bottom-score-strip {
            background: linear-gradient(135deg, #001f38 0%, #003661 100%);
            border-radius: 10px;
            padding: 14px 22px;
            color: #ffffff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid #004b87;
            box-shadow: 0 4px 12px rgba(0, 31, 56, 0.15);
        }

        .bottom-score-left {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .bottom-score-label {
            font-size: 13px;
            color: #bae6fd;
            font-weight: 500;
        }

        .bottom-score-value {
            font-size: 24px;
            font-weight: 800;
            color: var(--accent-gold);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        /* Toast Notification */
        .toast {
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #0f172a;
            color: #ffffff;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 13.5px;
            font-weight: 500;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
            opacity: 0;
            transform: translateY(10px);
            transition: all 0.3s;
            pointer-events: none;
            z-index: 9999;
        }

        .toast.show {
            opacity: 1;
            transform: translateY(0);
        }

        /* Footer */
        .dashboard-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #cbd5e1;
            padding-top: 10px;
            font-size: 12px;
            color: #64748b;
        }

        /* Edit Mode Styles */
        body.app-mode-edit [contenteditable="true"] {
            outline: 1.5px dashed #38bdf8 !important;
            outline-offset: 2px;
            cursor: text;
        }

        body.app-mode-edit [contenteditable="true"]:hover {
            background-color: rgba(224, 242, 254, 0.4);
        }

        body.app-mode-edit [contenteditable="true"]:focus {
            outline: 2px solid #0284c7 !important;
            background-color: #ffffff;
        }

        body.app-mode-preview [contenteditable="true"] {
            outline: none !important;
            cursor: default;
        }

        @media print {
            body { background: #ffffff; padding: 0; }
            .toolbar-container { display: none !important; }
            .dashboard-container { box-shadow: none; border: none; padding: 0; }
        }
    </style>
</head>
<body class="app-mode-preview">

    <div class="page-wrapper">

        <!-- TOOLBAR RIBBON -->
        <div class="toolbar-container">
            <div class="toolbar-ribbon">
                <div class="ribbon-left">
                    <!-- KPI Selector: strictly 1.1 through 5.1 only -->
                    <div class="control-item">
                        <span>📑 ตัวชี้วัด:</span>
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
                            <option value="5.1" selected>5.1 บทบาทคณะกรรมการบริหารทุนหมุนเวียน (ปัจจุบัน)</option>
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

                    <!-- Year Selector -->
                    <div class="control-item" style="margin-left: 4px;">
                        <span>📅 ปี:</span>
                        <select id="select-year" class="select-input" onchange="changeFiscalYear(this.value)">
                            <option value="2568">ปี 2568</option>
                            <option value="2569" selected>ปี 2569</option>
                            <option value="2570">ปี 2570</option>
                        </select>
                    </div>
                </div>

                <!-- Dual Mode Segmented Control -->
                <div class="ribbon-center">
                    <div class="mode-segmented-control">
                        <button class="mode-btn active" id="btn-mode-preview" onclick="setAppMode('preview')" title="โหมดนำเสนอ สะอาดตา ไร้เครื่องมือจัดฟอร์ม">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                            โหมดนำเสนอ (Preview)
                        </button>
                        <button class="mode-btn" id="btn-mode-edit" onclick="setAppMode('edit')" title="โหมดแก้ไขข้อความ เปิดแถบเครื่องมือจัดฟอร์ม">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
                            โหมดแก้ไขข้อความ (Edit)
                        </button>
                    </div>
                </div>

                <div class="ribbon-right">
                    <button class="btn btn-outline" onclick="saveCurrentQuarter(true)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
                        บันทึก
                    </button>
                    <button class="btn btn-outline" onclick="copyImageToClipboard()" title="คัดลอกรูปภาพลงคลิปบอร์ดทันที">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                        คัดลอกภาพ
                    </button>
                    <button class="btn btn-primary" onclick="exportToImage()" title="ส่งออกเป็นรูปภาพ PNG">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                        ส่งออกภาพ (PNG)
                    </button>
                    <button class="btn btn-warning" onclick="exportToPDF()" title="ดาวน์โหลดไฟล์ PDF เต็มแผ่น">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        ส่งออก PDF (เต็มแผ่น)
                    </button>
                    <button class="btn btn-success" onclick="window.print()" title="พิมพ์">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
                        พิมพ์ (Print)
                    </button>
                    <button class="btn btn-outline" id="btn-fullscreen" onclick="toggleFullscreen()" title="เต็มจอ">
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
                    <span>📊 ภาพรวม 5 ข้อ</span>
                    <span class="tab-pct" style="background: #005691; color: white; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">100%</span>
                </button>
                <button class="tab-btn" id="tab-btn-1" onclick="switchTopicView(1)">
                    <span>1. แผนระยะยาว &amp; ปี 70</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">30%</span>
                </button>
                <button class="tab-btn" id="tab-btn-2" onclick="switchTopicView(2)">
                    <span>2. การประชุม คกก.</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">10%</span>
                </button>
                <button class="tab-btn" id="tab-btn-3" onclick="switchTopicView(3)">
                    <span>3. ติดตามผลงาน 5 ด้าน</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">35%</span>
                </button>
                <button class="tab-btn" id="tab-btn-4" onclick="switchTopicView(4)">
                    <span>4. ประเมินผลผู้บริหาร</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">20%</span>
                </button>
                <button class="tab-btn" id="tab-btn-5" onclick="switchTopicView(5)">
                    <span>5. การเปิดเผยข้อมูล 10 ด้าน</span>
                    <span class="tab-pct" style="background: #e0f2fe; color: #004b87; padding: 1px 6px; border-radius: 10px; font-size: 11px; margin-left: 4px;">5%</span>
                </button>
            </div>
        </div>

        <!-- 16:9 PRESENTATION FRAME CANVAS -->
        <div class="dashboard-container" id="report-canvas">

            <!-- HEADER BANNER -->
            <div class="header-banner">
                <div class="header-left">
                    <div class="header-icon-box">🏛️</div>
                    <div class="header-titles">
                        <div contenteditable="true" id="hdr-main-title" class="main-heading">ด้านที่ 5 การบริหารจัดการทุนหมุนเวียน | ตัวชี้วัดที่ 5.1 บทบาทคณะกรรมการบริหารทุนหมุนเวียน</div>
                        <div contenteditable="true" id="hdr-sub-title" class="sub-heading">พิจารณาผลการดำเนินงาน 5 ข้อ (การจัดทำแผน, การประชุม, การติดตามผลงาน 5 ด้าน, การประเมินผลผู้บริหาร และการเปิดเผยข้อมูล)</div>
                    </div>
                </div>
                <div class="header-right-tag">
                    <div>กำกับดูแลอย่างมีธรรมาภิบาล</div>
                    <div>โปร่งใส คุ้มค่า เพื่อการพัฒนาที่ยั่งยืน</div>
                </div>
            </div>

            <!-- KPI METADATA STRIP -->
            <div class="kpi-meta-strip">
                <div class="meta-pills-group">
                    <div class="meta-pill">
                        <span>🏷️ ตัวชี้วัด:</span>
                        <span class="val">5.1 บทบาทคณะกรรมการบริหาร</span>
                    </div>
                    <div class="meta-pill">
                        <span>🎯 หน่วยวัด:</span>
                        <span class="val">ระดับคะแนน (1 - 5)</span>
                    </div>
                    <div class="meta-pill meta-pill-accent">
                        <span>⚖️ ค่าน้ำหนัก:</span>
                        <span class="val">ร้อยละ 4 (4%)</span>
                    </div>
                    <div class="meta-pill">
                        <span>📐 ค่าเกณฑ์วัด:</span>
                        <span class="val">เกณฑ์ 5 ระดับ (5 ข้อ)</span>
                    </div>
                </div>

                <div class="rubric-target-inline">
                    <span style="font-size: 12px; font-weight: 700; color: #1e3a8a; margin-right: 2px;">เกณฑ์:</span>
                    <div class="target-scale-box">
                        <div class="target-step-cell">ระดับ 1<br>1.00</div>
                        <div class="target-step-cell">ระดับ 2<br>2.00</div>
                        <div class="target-step-cell">ระดับ 3<br>3.00</div>
                        <div class="target-step-cell">ระดับ 4<br>4.00</div>
                        <div class="target-step-cell active-target">ระดับ 5<br>5.00</div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 0: ภาพรวมสรุป 5 ข้อ (6 ประเด็นย่อย) ================= -->
            <div class="content-view active" id="view-topic-0">
                <div class="overview-grid">
                    <!-- Left: Table Card -->
                    <div class="card-panel">
                        <div class="panel-header">
                            <div class="panel-title">
                                <span>📊 ผลการดำเนินงานรวม 5 ข้อ (ตัวชี้วัดที่ 5.1)</span>
                            </div>
                            <span class="tab-pct" style="background: #004b87; color: white; padding: 3px 8px; border-radius: 12px; font-size: 12px; font-weight: 700;">น้ำหนักรวม 100%</span>
                        </div>

                        <table class="data-table">
                            <thead>
                                <tr>
                                    <th style="width: 10%;">ข้อ</th>
                                    <th style="width: 50%;">ประเด็นย่อยที่ใช้พิจารณา</th>
                                    <th style="width: 14%;">น้ำหนัก (%)</th>
                                    <th style="width: 13%;">ระดับคะแนน</th>
                                    <th style="width: 13%;">คะแนนถ่วงน้ำหนัก</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr onclick="switchTopicView(1)" title="คลิกเพื่อดูรายละเอียดข้อ 1.1">
                                    <td style="text-align: center; font-weight: 700; color: #004b87;">1.1</td>
                                    <td>การกำหนดทิศทางยุทธศาสตร์และเป้าประสงค์</td>
                                    <td style="text-align: center; font-weight: 600;">15%</td>
                                    <td style="text-align: center; font-weight: 700; color: #004b87;" id="tbl-score-1">5.0000</td>
                                    <td style="text-align: center; font-weight: 700; color: #0284c7;" id="tbl-wscore-1">0.7500</td>
                                </tr>
                                <tr onclick="switchTopicView(1)" title="คลิกเพื่อดูรายละเอียดข้อ 1.2">
                                    <td style="text-align: center; font-weight: 700; color: #004b87;">1.2</td>
                                    <td>การจัดทำ/ทบทวนแผนระยะยาว (3-5 ปี) และแผนปี 2570</td>
                                    <td style="text-align: center; font-weight: 600;">15%</td>
                                    <td style="text-align: center; font-weight: 700; color: #004b87;" id="tbl-score-2">5.0000</td>
                                    <td style="text-align: center; font-weight: 700; color: #0284c7;" id="tbl-wscore-2">0.7500</td>
                                </tr>
                                <tr onclick="switchTopicView(2)" title="คลิกเพื่อดูรายละเอียดข้อ 2">
                                    <td style="text-align: center; font-weight: 700; color: #004b87;">2</td>
                                    <td>การเข้าร่วมประชุมของคณะกรรมการบริหารฯ (ไม่น้อยกว่า 80%)</td>
                                    <td style="text-align: center; font-weight: 600;">10%</td>
                                    <td style="text-align: center; font-weight: 700; color: #004b87;" id="tbl-score-3">5.0000</td>
                                    <td style="text-align: center; font-weight: 700; color: #0284c7;" id="tbl-wscore-3">0.5000</td>
                                </tr>
                                <tr onclick="switchTopicView(3)" title="คลิกเพื่อดูรายละเอียดข้อ 3">
                                    <td style="text-align: center; font-weight: 700; color: #004b87;">3</td>
                                    <td>การติดตามผลการปฏิบัติงานที่สำคัญครบถ้วน 5 ด้าน</td>
                                    <td style="text-align: center; font-weight: 600;">35%</td>
                                    <td style="text-align: center; font-weight: 700; color: #004b87;" id="tbl-score-4">5.0000</td>
                                    <td style="text-align: center; font-weight: 700; color: #0284c7;" id="tbl-wscore-4">1.7500</td>
                                </tr>
                                <tr onclick="switchTopicView(4)" title="คลิกเพื่อดูรายละเอียดข้อ 4">
                                    <td style="text-align: center; font-weight: 700; color: #004b87;">4</td>
                                    <td>การจัดให้มีระบบประเมินผลผู้บริหารและผูกโยงแรงจูงใจ</td>
                                    <td style="text-align: center; font-weight: 600;">20%</td>
                                    <td style="text-align: center; font-weight: 700; color: #004b87;" id="tbl-score-5">5.0000</td>
                                    <td style="text-align: center; font-weight: 700; color: #0284c7;" id="tbl-wscore-5">1.0000</td>
                                </tr>
                                <tr onclick="switchTopicView(5)" title="คลิกเพื่อดูรายละเอียดข้อ 5">
                                    <td style="text-align: center; font-weight: 700; color: #004b87;">5</td>
                                    <td>การเปิดเผยข้อมูลสารสนเทศครบถ้วน 10 ประเด็นขึ้นไป</td>
                                    <td style="text-align: center; font-weight: 600;">5%</td>
                                    <td style="text-align: center; font-weight: 700; color: #004b87;" id="tbl-score-6">5.0000</td>
                                    <td style="text-align: center; font-weight: 700; color: #0284c7;" id="tbl-wscore-6">0.2500</td>
                                </tr>
                            </tbody>
                            <tfoot>
                                <tr>
                                    <td colspan="2" style="text-align: center; font-weight: 700;">รวมผลการประเมินถ่วงน้ำหนักทั้งหมด</td>
                                    <td style="text-align: center; font-weight: 800;">100%</td>
                                    <td style="text-align: center; font-weight: 800; color: #004b87;" id="tbl-total-level">ระดับ 5.0</td>
                                    <td style="text-align: center; font-weight: 800; color: #059669;" id="tbl-total-wscore">5.0000 คะแนน</td>
                                </tr>
                            </tfoot>
                        </table>

                        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #166534; line-height: 1.5;">
                            <b>💡 สรุปความเชื่อมโยง:</b> คกก.บริหารฯ ทำหน้าที่กำกับดูแลครบถ้วน 5 ข้อ ได้แก่ เห็นชอบแผนยุทธศาสตร์ 3 ปีและแผนปี 2570 (ผ่านมติ 23 ก.ค. 69 และ กรมบัญชีกลางอนุมัติ 30 ก.ย. 69) | ประชุม 7 ครั้ง เข้าร่วมเกิน 80% ถึง 85.71% | ติดตามผลงาน 5 ด้านรายไตรมาสต่อเนื่อง | ประเมินผลผู้บริหาร 94.60% ผูกโยงแรงจูงใจ | เปิดเผยข้อมูลครบ 10 ประเด็นบนเว็บไซต์
                        </div>
                    </div>

                    <!-- Right: Big Score Card & Achievement -->
                    <div class="card-panel">
                        <div class="panel-header">
                            <div class="panel-title">
                                <span>🏆 สรุปคะแนนผลการประเมินภาพรวม</span>
                            </div>
                            <span id="score-status-badge" style="background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 12px; font-size: 11.5px; font-weight: 700; border: 1px solid #fde68a;">ระดับ 5.0000 (เต็ม)</span>
                        </div>

                        <!-- Big Score Hero -->
                        <div class="score-hero-box">
                            <div class="score-hero-label" id="score-hero-label">ผลการดำเนินงานเทียบเท่า</div>
                            <div class="score-hero-number" id="score-hero-val">ระดับ 5.0000 คะแนน</div>
                            <div class="stars-container" id="score-hero-stars">★★★★★</div>
                        </div>

                        <!-- Executive Key Summary -->
                        <div class="summary-card-inner">
                            <div class="summary-inner-title">
                                <span>🎯 สรุปผลการดำเนินงานสำคัญ:</span>
                            </div>
                            <div contenteditable="true" id="summary-overview-desc" class="summary-inner-desc">
                                คณะกรรมการบริหารเงินทุนหมุนเวียนฯ ปฏิบัติหน้าที่กำกับดูแลบรรลุเกณฑ์ระดับ 5 ครบถ้วนทุกข้อ ได้แก่ การกำหนดทิศทางยุทธศาสตร์และแผนปฏิบัติการระยะยาว 3 ปี (2570-2572) และแผนปี 2570 มีคุณภาพครบถ้วน, การเข้าร่วมประชุมเฉลี่ยร้อยละ 85.71 (เกินเกณฑ์ 80%), ติดตามผลการปฏิบัติงาน 5 ด้านเป็นรายไตรมาสและให้ข้อคิดเห็นขับเคลื่อนงาน, ประเมินผลผู้บริหาร (94.60%) ผูกโยงกับระบบแรงจูงใจ และเปิดเผยข้อมูลสารสนเทศครบถ้วนทั้ง 10 ประเด็น
                            </div>
                        </div>

                        <!-- Metric Status Row -->
                        <div class="status-pills-row">
                            <div class="status-metric-card" id="card-metric-complete">
                                <span class="status-metric-label">ความสำเร็จ</span>
                                <span class="status-metric-val" id="metric-complete-val">ครบ 5 ข้อ</span>
                            </div>
                            <div class="status-metric-card" id="card-metric-grade">
                                <span class="status-metric-label">สถานะประเมิน</span>
                                <span class="status-metric-val" id="metric-grade-val">ระดับ 5 (เต็ม)</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 1: ข้อ 1 แผนปฏิบัติการระยะยาว และแผนปี 2570 (30%) ================= -->
            <div class="content-view" id="view-topic-1">
                <div class="card-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <span>📘 1. การจัดให้มีหรือทบทวนแผนระยะยาว (3 - 5 ปี) และแผนปี 2570 (น้ำหนัก 30%)</span>
                        </div>
                        <span class="tab-pct" id="v1-score-pill" style="background: #004b87; color: white; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 700;">น้ำหนัก 30% | ผลงานระดับ 5</span>
                    </div>

                    <!-- 5 Rubric Scales for Sub-topic 1 -->
                    <div class="rubric-strip">
                        <div class="rubric-cell" id="v1-rubric-1">
                            <span class="level-badge">ระดับ 1</span>
                            <span>แผนระยะยาวและแผนประจำปี มีองค์ประกอบไม่ครบถ้วน และไม่สอดคล้องนโยบายรัฐ/ศธ.</span>
                        </div>
                        <div class="rubric-cell" id="v1-rubric-2">
                            <span class="level-badge">ระดับ 2</span>
                            <span>แผนระยะยาวและแผนประจำปี มีองค์ประกอบครบถ้วน แต่ไม่สอดคล้องนโยบายรัฐ/ศธ.</span>
                        </div>
                        <div class="rubric-cell" id="v1-rubric-3">
                            <span class="level-badge">ระดับ 3</span>
                            <span>องค์ประกอบครบถ้วน และสอดคล้องกับนโยบายภาครัฐ/กระทรวงเจ้าสังกัด</span>
                        </div>
                        <div class="rubric-cell" id="v1-rubric-4">
                            <span class="level-badge">ระดับ 4</span>
                            <span>ผ่านเกณฑ์ระดับ 3 มีแผนงาน/โครงการรองรับเป็นรูปธรรม และกำหนดเป้าหมายผลลัพธ์</span>
                        </div>
                        <div class="rubric-cell achieved-gold" id="v1-rubric-5">
                            <span class="level-badge">ระดับ 5 ★</span>
                            <span>ผ่านระดับ 4 และมีการประเมินความเสี่ยงและแนวทางบริหารจัดการความเสี่ยงทุกโครงการ</span>
                        </div>
                    </div>

                    <!-- Process Steps -->
                    <div class="milestone-stepper">
                        <div class="step-item step-complete">
                            <div class="step-title">1. วิเคราะห์บริบท &amp; TOWS</div>
                            <div class="step-sub">McKinsey 7S, PESTEL, TOWS Matrix เชิงยุทธศาสตร์</div>
                        </div>
                        <div class="step-arrow">➔</div>
                        <div class="step-item step-complete">
                            <div class="step-title">2. ยกร่างแผน 3 ปี &amp; ปี 70</div>
                            <div class="step-sub">ประชุมเชิงปฏิบัติการ 15-16 มิ.ย. 69 จ.นนทบุรี</div>
                        </div>
                        <div class="step-arrow">➔</div>
                        <div class="step-item step-complete">
                            <div class="step-title">3. มติ คกก.บริหารฯ</div>
                            <div class="step-sub" id="v1-step3-sub">มติเห็นชอบ คราวประชุม 4/2569 (23 ก.ค. 69)</div>
                        </div>
                        <div class="step-arrow">➔</div>
                        <div class="step-item step-complete">
                            <div class="step-title">4. กรมบัญชีกลางอนุมัติ</div>
                            <div class="step-sub" id="v1-step4-sub">หนังสือ กค 0406.6/36581 (30 ก.ย. 69)</div>
                        </div>
                    </div>

                    <!-- 2 Cards Grid -->
                    <div class="subview-grid-cards">
                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">🎯 1.1 การกำหนดทิศทางยุทธศาสตร์และเป้าประสงค์ (15%)</div>
                                <span style="font-size: 11.5px; background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 10px; font-weight: 600;">ระดับ 5 (0.7500)</span>
                            </div>
                            <div contenteditable="true" id="v1-card-left" class="work-card-body">
                                <div>• <b>การวิเคราะห์บริบท:</b> วิเคราะห์ปัจจัยภายใน (3 ด้าน: บุคลากร, ปฏิบัติการ, บริหารกองทุน) และปัจจัยภายนอก (PEST Analysis 4 มิติ) พร้อมจัดทำ TOWS Matrix กำหนดกลยุทธ์ SO, WO, ST, WT</div>
                                <div>• <b>ความสอดคล้อง:</b> สอดคล้องกับยุทธศาสตร์ชาติ แผนปฏิรูปประเทศ นโยบาย ศธ. และพันธกิจการแก้ไขปัญหาหนี้สินครูอย่างยั่งยืน</div>
                                <div>• <b>มติ คกก.บริหารฯ:</b> ประชุมครั้งที่ 4/2569 เมื่อ 23 ก.ค. 2569 มีมติเห็นชอบทิศทางยุทธศาสตร์และเป้าประสงค์ โดยให้ข้อสังเกตและข้อเสนอแนะในการขับเคลื่อน (เอกสารหมายเลข 1)</div>
                            </div>
                        </div>

                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">📑 1.2 คุณภาพและองค์ประกอบของแผนทั้ง 2 ฉบับ (15%)</div>
                                <span style="font-size: 11.5px; background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 10px; font-weight: 700;">ระดับ 5 (0.7500)</span>
                            </div>
                            <div contenteditable="true" id="v1-card-right" class="work-card-body">
                                <div>• <b>แผนระยะยาว 3 ปี (พ.ศ. 2570–2572):</b> มีองค์ประกอบครบ 7 ด้านสำคัญ ได้แก่ วิสัยทัศน์ พันธกิจ วัตถุประสงค์ ผลผลิต/ผลลัพธ์ ยุทธศาสตร์ เป้าหมายหลัก และการวิเคราะห์ปัจจัย (เอกสารหมายเลข 2)</div>
                                <div>• <b>แผนประจำปีบัญชี 2570:</b> มีองค์ประกอบครบ 7 ส่วน (วัตถุประสงค์, เป้าหมาย, ขั้นตอน, ระยะเวลา, งบประมาณ, ผู้รับผิดชอบ, ตัวชี้วัด) พร้อมระบุการประเมินความเสี่ยงและมาตรการจัดการความเสี่ยงทุกโครงการอย่างชัดเจน (เอกสารหมายเลข 3)</div>
                                <div>• <b>การอนุมัติ:</b> กรมบัญชีกลางมีหนังสืออนุมัติแผนงานประจำปีงบประมาณ 2570 เรียบร้อย เมื่อ 30 ก.ย. 69 (เอกสารหมายเลข 4)</div>
                            </div>
                        </div>
                    </div>

                    <!-- Bottom Score Strip -->
                    <div class="bottom-score-strip">
                        <div class="bottom-score-left">
                            <div class="bottom-score-label">ผลการดำเนินงานข้อ 1 (ข้อ 1.1 + 1.2 น้ำหนักรวม 30%)</div>
                            <div class="bottom-score-value" id="v1-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span></div>
                        </div>
                        <div style="text-align: right; font-size: 12.5px; color: #bae6fd;" id="v1-bottom-callout">
                            บรรลุเกณฑ์ระดับ 5 ทั้ง 2 ประเด็น (คกก.เห็นชอบ 23 ก.ค. 69 และกรมบัญชีกลางอนุมัติ 30 ก.ย. 69) คะแนนถ่วงน้ำหนักรวม 1.5000
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 2: ข้อ 2 การประชุมของคณะกรรมการบริหารฯ (10%) ================= -->
            <div class="content-view" id="view-topic-2">
                <div class="card-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <span>👥 2. การประชุมของคณะกรรมการบริหารทุนหมุนเวียน (น้ำหนัก 10%)</span>
                        </div>
                        <span class="tab-pct" id="v2-score-pill" style="background: #004b87; color: white; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 700;">น้ำหนัก 10% | ผลงานระดับ 5</span>
                    </div>

                    <!-- 5 Rubric Scales for Sub-topic 2 -->
                    <div class="rubric-strip">
                        <div class="rubric-cell" id="v2-rubric-1">
                            <span class="level-badge">ระดับ 1</span>
                            <span>กรรมการไม่สามารถเข้าร่วมประชุมได้เกินกึ่งหนึ่งของการประชุมทั้งหมด</span>
                        </div>
                        <div class="rubric-cell" id="v2-rubric-2">
                            <span class="level-badge">ระดับ 2</span>
                            <span>ร้อยละ 50 ของการประชุม มีกรรมการเข้าประชุมร้อยละ 80 ขึ้นไป</span>
                        </div>
                        <div class="rubric-cell" id="v2-rubric-3">
                            <span class="level-badge">ระดับ 3</span>
                            <span>ร้อยละ 60 ของการประชุม มีกรรมการเข้าประชุมร้อยละ 80 ขึ้นไป</span>
                        </div>
                        <div class="rubric-cell" id="v2-rubric-4">
                            <span class="level-badge">ระดับ 4</span>
                            <span>ร้อยละ 70 ของการประชุม มีกรรมการเข้าประชุมร้อยละ 80 ขึ้นไป</span>
                        </div>
                        <div class="rubric-cell achieved-gold" id="v2-rubric-5">
                            <span class="level-badge">ระดับ 5 ★</span>
                            <span>ร้อยละ 80 ของการประชุม มีกรรมการเข้าประชุมร้อยละ 80 ขึ้นไป</span>
                        </div>
                    </div>

                    <!-- Cards Grid -->
                    <div class="subview-grid-cards">
                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">📅 สถิติการประชุม 7 ครั้งในปีบัญชี 2569</div>
                                <span style="font-size: 11.5px; background: #dcfce7; color: #166534; padding: 2px 8px; border-radius: 10px; font-weight: 700;">เฉลี่ย 85.71%</span>
                            </div>
                            <div contenteditable="true" id="v2-card-left" class="work-card-body">
                                <div>• <b>ครั้งที่ 8/2568 (16 ธ.ค. 68):</b> กรรมการเข้าประชุม 7 จาก 8 ท่าน คิดเป็น <b>ร้อยละ 87.50</b> (✓ ผ่านเกณฑ์)</div>
                                <div>• <b>ครั้งที่ 1/2569 (28 ม.ค. 69):</b> กรรมการเข้าประชุม 7 จาก 8 ท่าน คิดเป็น <b>ร้อยละ 87.50</b> (✓ ผ่านเกณฑ์)</div>
                                <div>• <b>ครั้งที่ 2/2569 (29 เม.ย. 69):</b> กรรมการเข้าประชุม 7 จาก 8 ท่าน คิดเป็น <b>ร้อยละ 87.50</b> (✓ ผ่านเกณฑ์)</div>
                                <div>• <b>ครั้งที่ 3/2569 (26 มิ.ย. 69):</b> กรรมการเข้าประชุม 5 จาก 8 ท่าน คิดเป็น <b>ร้อยละ 62.50</b></div>
                                <div>• <b>ครั้งที่ 4/2569 (23 ก.ค. 69):</b> กรรมการเข้าประชุม 7 จาก 8 ท่าน คิดเป็น <b>ร้อยละ 87.50</b> (✓ ผ่านเกณฑ์)</div>
                                <div>• <b>ครั้งที่ 5/2569 (28 ส.ค. 69):</b> กรรมการเข้าประชุม 7 จาก 8 ท่าน คิดเป็น <b>ร้อยละ 87.50</b> (✓ ผ่านเกณฑ์)</div>
                                <div>• <b>ครั้งที่ 6/2569 (30 ก.ย. 69):</b> กรรมการเข้าประชุม 7 จาก 8 ท่าน คิดเป็น <b>ร้อยละ 87.50</b> (✓ ผ่านเกณฑ์)</div>
                            </div>
                        </div>

                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">🏆 การคำนวณและสรุปผลตามเกณฑ์วัด</div>
                                <span style="font-size: 11.5px; background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 10px; font-weight: 700;">ระดับ 5 (0.5000)</span>
                            </div>
                            <div contenteditable="true" id="v2-card-right" class="work-card-body">
                                <div>• <b>สูตรการคำนวณ:</b> (จำนวนครั้งที่มีกรรมการเข้าประชุม &ge; 80% / จำนวนครั้งการประชุมทั้งหมด) &times; 100</div>
                                <div>• <b>ผลลัพธ์จริง:</b> มีการประชุมที่มีกรรมการเข้าประชุมตั้งแต่ร้อยละ 80 ขึ้นไป จำนวน <b>6 ครั้ง จากทั้งหมด 7 ครั้ง</b> คิดเป็น <b>ร้อยละ 85.71</b> (6 &times; 100 / 7)</div>
                                <div>• <b>การเทียบเคียงเกณฑ์:</b> เกณฑ์ระดับ 5 กำหนดไม่น้อยกว่าร้อยละ 80 ผลงานที่ได้ 85.71% จึงเทียบเท่า <b>ระดับ 5.0000 คะแนน</b> (เต็ม)</div>
                                <div>• <b>เอกสารอ้างอิง:</b> รายงานการประชุมคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ทั้ง 7 ครั้ง (เอกสารหมายเลข 5)</div>
                            </div>
                        </div>
                    </div>

                    <!-- Bottom Score Strip -->
                    <div class="bottom-score-strip">
                        <div class="bottom-score-left">
                            <div class="bottom-score-label">ผลการดำเนินงานข้อ 2 (น้ำหนัก 10%)</div>
                            <div class="bottom-score-value" id="v2-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span></div>
                        </div>
                        <div style="text-align: right; font-size: 12.5px; color: #bae6fd;" id="v2-bottom-callout">
                            การประชุม 6 ใน 7 ครั้ง มีกรรมการเข้าประชุม &ge; 80% คิดเป็นร้อยละ 85.71 บรรลุระดับ 5 เต็ม (คะแนนถ่วงน้ำหนัก 0.5000)
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 3: ข้อ 3 การติดตามผลการปฏิบัติงาน 5 ด้าน (35%) ================= -->
            <div class="content-view" id="view-topic-3">
                <div class="card-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <span>📊 3. การติดตามระบบบริหารจัดการสำคัญและผลการปฏิบัติงาน 5 ด้าน (น้ำหนัก 35%)</span>
                        </div>
                        <span class="tab-pct" id="v3-score-pill" style="background: #004b87; color: white; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 700;">น้ำหนัก 35% | ผลงานระดับ 5</span>
                    </div>

                    <!-- 5 Rubric Scales for Sub-topic 3 -->
                    <div class="rubric-strip">
                        <div class="rubric-cell" id="v3-rubric-1">
                            <span class="level-badge">ระดับ 1</span>
                            <span>ติดตามผลการปฏิบัติงานที่สำคัญเป็นรายไตรมาส จำนวน 4 ด้าน</span>
                        </div>
                        <div class="rubric-cell" id="v3-rubric-2">
                            <span class="level-badge">ระดับ 2</span>
                            <span>ติดตามผลการปฏิบัติงานที่สำคัญเป็นรายไตรมาส จำนวน 5 ด้าน</span>
                        </div>
                        <div class="rubric-cell" id="v3-rubric-3">
                            <span class="level-badge">ระดับ 3</span>
                            <span>ติดตามรายไตรมาส 5 ด้าน + มอบข้อสังเกต/ข้อเสนอแนะในที่ประชุม คกก.บริหารฯ</span>
                        </div>
                        <div class="rubric-cell" id="v3-rubric-4">
                            <span class="level-badge">ระดับ 4</span>
                            <span>ผ่านระดับ 3 + ติดตามการดำเนินงานตามข้อสังเกต/ข้อเสนอแนะและรายงานในที่ประชุม</span>
                        </div>
                        <div class="rubric-cell achieved-gold" id="v3-rubric-5">
                            <span class="level-badge">ระดับ 5 ★</span>
                            <span>ผ่านระดับ 4 + นำผลงานมาใช้วิเคราะห์และกำหนดแผนปฏิบัติการฯ/แผนความเสี่ยง/นโยบาย</span>
                        </div>
                    </div>

                    <!-- Cards Grid -->
                    <div class="subview-grid-cards">
                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">🔍 การติดตามผลงานครบ 5 ด้านเป็นรายไตรมาส</div>
                                <span style="font-size: 11.5px; background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 10px; font-weight: 600;">ครบ 5 ด้านสำคัญ</span>
                            </div>
                            <div contenteditable="true" id="v3-card-left" class="work-card-body">
                                <div>• <b>ด้านที่ติดตามครบ 5 ด้าน:</b> 1) ด้านการเงิน 2) ด้านไม่ใช่การเงินตามภารกิจ 3) ระบบบริหารความเสี่ยง 4) ระบบสารสนเทศ และ 5) ระบบบริหารทรัพยากรบุคคล</div>
                                <div>• <b>ไตรมาสที่ 1 (ประชุม 1/69 วันที่ 28 ม.ค. 69):</b> รายงานผล 5 ด้าน คกก. ให้ข้อเสนอแนะเร่งรัดการเบิกจ่ายตามมาตรการภาครัฐ (เอกสาร 1)</div>
                                <div>• <b>ไตรมาสที่ 2 (ประชุม 2/69 วันที่ 29 เม.ย. 69):</b> รายงานผล 5 ด้าน คกก. มอบหมายให้จำแนกความเสี่ยงคงเหลือ และเร่งรัดการเบิกจ่ายเงินให้กู้ยืม ธ.ก.ส. (เอกสาร 2)</div>
                                <div>• <b>ไตรมาสที่ 3 (ประชุม 4/69 วันที่ 23 ก.ค. 69):</b> รายงานผล 5 ด้าน คกก. ติดตามการเบิกจ่ายสะสมได้ถึง 221.36 ล้านบาท (88.55%) และทบทวนความเสี่ยง 4 ด้าน (เอกสาร 3)</div>
                            </div>
                        </div>

                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">🎯 การนำผลงานไปขับเคลื่อนนโยบาย (เกณฑ์ระดับ 5)</div>
                                <span style="font-size: 11.5px; background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 10px; font-weight: 700;">ระดับ 5 (1.7500)</span>
                            </div>
                            <div contenteditable="true" id="v3-card-right" class="work-card-body">
                                <div>• <b>การมอบข้อสังเกตและติดตามผล:</b> คกก.บริหารฯ มีข้อคิดเห็นเชิงนโยบายทุกครั้ง และฝ่ายเลขาฯ รายงานผลการปฏิบัติตามข้อสังเกตในคราวประชุมถัดไปอย่างต่อเนื่อง</div>
                                <div>• <b>การเชื่อมโยงสู่แผนและนโยบาย:</b> นำผลการเบิกจ่ายเงินกู้ยืมและรายงานลูกหนี้มาใช้ปรับปรุงแผนปฏิบัติการระยะยาว 3 ปี (2570–2572) และแผนบริหารความเสี่ยงปี 2570</div>
                                <div>• <b>ผลสรุป:</b> มีการติดตาม 5 ด้าน มอบข้อคิดเห็น ติดตามความก้าวหน้า และนำผลไปใช้กำหนดนโยบาย ครบถ้วนตามเกณฑ์ <b>ระดับ 5</b></div>
                            </div>
                        </div>
                    </div>

                    <!-- Bottom Score Strip -->
                    <div class="bottom-score-strip">
                        <div class="bottom-score-left">
                            <div class="bottom-score-label">ผลการดำเนินงานข้อ 3 (น้ำหนัก 35%)</div>
                            <div class="bottom-score-value" id="v3-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span></div>
                        </div>
                        <div style="text-align: right; font-size: 12.5px; color: #bae6fd;" id="v3-bottom-callout">
                            ติดตามผลงาน 5 ด้านรายไตรมาส มอบข้อสังเกต ติดตามการแก้ไข และนำผลไปกำหนดนโยบายและแผนงาน (คะแนนถ่วงน้ำหนัก 1.7500)
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 4: ข้อ 4 การจัดให้มีระบบประเมินผลผู้บริหาร (20%) ================= -->
            <div class="content-view" id="view-topic-4">
                <div class="card-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <span>👔 4. การจัดให้มีระบบประเมินผลผู้บริหารทุนหมุนเวียน (น้ำหนัก 20%)</span>
                        </div>
                        <span class="tab-pct" id="v4-score-pill" style="background: #004b87; color: white; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 700;">น้ำหนัก 20% | ผลงานระดับ 5</span>
                    </div>

                    <!-- 5 Rubric Scales for Sub-topic 4 -->
                    <div class="rubric-strip">
                        <div class="rubric-cell" id="v4-rubric-1">
                            <span class="level-badge">ระดับ 1</span>
                            <span>มีระบบประเมินผลผู้บริหาร แต่ไม่มีหลักเกณฑ์ชัดเจน ไม่เชื่อมโยงเป้าหมายองค์กร</span>
                        </div>
                        <div class="rubric-cell" id="v4-rubric-2">
                            <span class="level-badge">ระดับ 2</span>
                            <span>อยู่ระหว่างพัฒนาระบบการประเมินผลผู้บริหารให้เป็นรูปธรรม</span>
                        </div>
                        <div class="rubric-cell" id="v4-rubric-3">
                            <span class="level-badge">ระดับ 3</span>
                            <span>มีการประเมินผลผู้บริหารที่เป็นระบบ โดยมีหลักเกณฑ์ชัดเจน สอดคล้องเป้าหมายองค์กร</span>
                        </div>
                        <div class="rubric-cell" id="v4-rubric-4">
                            <span class="level-badge">ระดับ 4</span>
                            <span>ผ่านระดับ 3 และมีกระบวนการประเมินผลผู้บริหารเสร็จสิ้นตามกรอบเวลา</span>
                        </div>
                        <div class="rubric-cell achieved-gold" id="v4-rubric-5">
                            <span class="level-badge">ระดับ 5 ★</span>
                            <span>นำผลการประเมินผู้บริหารที่เป็นระบบไปใช้ประโยชน์ โดยการผูกโยงกับระบบแรงจูงใจ</span>
                        </div>
                    </div>

                    <!-- Cards Grid -->
                    <div class="subview-grid-cards">
                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">📝 ขั้นตอนการแต่งตั้งและการประเมินผล</div>
                                <span style="font-size: 11.5px; background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 10px; font-weight: 600;">กระบวนการเป็นระบบ</span>
                            </div>
                            <div contenteditable="true" id="v4-card-left" class="work-card-body">
                                <div>• <b>มติเห็นชอบกรอบประเมิน (23 ก.ค. 69):</b> คกก.บริหารฯ (ประชุม 4/69) มีมติเห็นชอบแต่งตั้งคณะอนุกรรมการประเมินผลผู้บริหาร, ร่างบันทึกข้อตกลง และแบบประเมินผล (เอกสาร 1)</div>
                                <div>• <b>ประกาศแต่งตั้งอนุฯ (13 ส.ค. 69):</b> ปลัด ศธ. (ประธานกรรมการบริหารฯ) ลงนามประกาศแต่งตั้งคณะอนุกรรมการประเมินผลผู้บริหาร ประจำปี 2569 (เอกสาร 2)</div>
                                <div>• <b>การประเมินผล (15 ก.ย. 69):</b> คณะอนุกรรมการฯ (ประชุม 1/69) พิจารณาผลงานผู้บริหาร (น.ส.ประทวน มูลหล้า) ได้คะแนน <b>ร้อยละ 94.6000 (ระดับ 4.3300)</b> (เอกสาร 3)</div>
                            </div>
                        </div>

                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">🏆 มติอนุมัติและการผูกโยงแรงจูงใจ (ระดับ 5)</div>
                                <span style="font-size: 11.5px; background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 10px; font-weight: 700;">ระดับ 5 (1.0000)</span>
                            </div>
                            <div contenteditable="true" id="v4-card-right" class="work-card-body">
                                <div>• <b>มติ คกก.บริหารฯ (30 ก.ย. 69):</b> ที่ประชุมครั้งที่ 6/2569 มีมติ <b>อนุมัติผลการประเมินผู้บริหาร 94.60% (ระดับ 4.3300)</b> และให้เสนอสำนักงาน ก.ค.ศ. เพื่อนำไปผูกโยงกับระบบแรงจูงใจ (เอกสาร 4)</div>
                                <div>• <b>การผูกโยงกับระบบแรงจูงใจ:</b> มีหนังสือถึงเลขาธิการ ก.ค.ศ. (ศธ 0206.8/734 ลว. 7 ต.ค. 69) ส่งผลการประเมินเพื่อใช้ประกอบการพิจารณาเลื่อนเงินเดือนของผู้บริหารทุนหมุนเวียน (เอกสาร 5)</div>
                                <div>• <b>สรุปผล:</b> มีกระบวนการประเมินเป็นระบบ มีหลักเกณฑ์ชัดเจน และนำผลไปผูกโยงกับระบบแรงจูงใจอย่างสมบูรณ์ บรรลุเกณฑ์ <b>ระดับ 5</b></div>
                            </div>
                        </div>
                    </div>

                    <!-- Bottom Score Strip -->
                    <div class="bottom-score-strip">
                        <div class="bottom-score-left">
                            <div class="bottom-score-label">ผลการดำเนินงานข้อ 4 (น้ำหนัก 20%)</div>
                            <div class="bottom-score-value" id="v4-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span></div>
                        </div>
                        <div style="text-align: right; font-size: 12.5px; color: #bae6fd;" id="v4-bottom-callout">
                            คกก.บริหารฯ อนุมัติผลประเมินผู้บริหาร 94.60% และส่งสำนักงาน ก.ค.ศ. ผูกโยงระบบแรงจูงใจเลื่อนเงินเดือน (คะแนนถ่วงน้ำหนัก 1.0000)
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 5: ข้อ 5 การเปิดเผยข้อมูลข่าวสาร 10 ด้าน (5%) ================= -->
            <div class="content-view" id="view-topic-5">
                <div class="card-panel">
                    <div class="panel-header">
                        <div class="panel-title">
                            <span>🌐 5. การเปิดเผยข้อมูลสารสนเทศแก่ผู้มีส่วนได้ส่วนเสีย (น้ำหนัก 5%)</span>
                        </div>
                        <span class="tab-pct" id="v5-score-pill" style="background: #004b87; color: white; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 700;">น้ำหนัก 5% | ผลงานระดับ 5</span>
                    </div>

                    <!-- 5 Rubric Scales for Sub-topic 5 -->
                    <div class="rubric-strip">
                        <div class="rubric-cell" id="v5-rubric-1">
                            <span class="level-badge">ระดับ 1</span>
                            <span>มีการเปิดเผยข้อมูลครบถ้วน &lt; 7 ประเด็น</span>
                        </div>
                        <div class="rubric-cell" id="v5-rubric-2">
                            <span class="level-badge">ระดับ 2</span>
                            <span>มีการเปิดเผยข้อมูลครบถ้วน 7 ประเด็น</span>
                        </div>
                        <div class="rubric-cell" id="v5-rubric-3">
                            <span class="level-badge">ระดับ 3</span>
                            <span>มีการเปิดเผยข้อมูลครบถ้วน 8 ประเด็น</span>
                        </div>
                        <div class="rubric-cell" id="v5-rubric-4">
                            <span class="level-badge">ระดับ 4</span>
                            <span>มีการเปิดเผยข้อมูลครบถ้วน 9 ประเด็น</span>
                        </div>
                        <div class="rubric-cell achieved-gold" id="v5-rubric-5">
                            <span class="level-badge">ระดับ 5 ★</span>
                            <span>มีการเปิดเผยข้อมูลครบถ้วน 10 ประเด็นขึ้นไป อย่างถูกต้อง เชื่อถือได้ ทันกาล</span>
                        </div>
                    </div>

                    <!-- Cards Grid -->
                    <div class="subview-grid-cards">
                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">💻 การเปิดเผยข้อมูลผ่านเว็บไซต์ 10 ประเด็นสำคัญ</div>
                                <span style="font-size: 11.5px; background: #e0f2fe; color: #0369a1; padding: 2px 8px; border-radius: 10px; font-weight: 600;">otepc.go.th</span>
                            </div>
                            <div contenteditable="true" id="v5-card-left" class="work-card-body">
                                <div>1. <b>การเงินและงบประมาณ:</b> ข้อมูลรายงานการเงินและรายจ่ายเงินทุนหมุนเวียน</div>
                                <div>2. <b>ภารกิจทุนหมุนเวียน:</b> การจัดสรรเงินกู้และสถิติการแก้ไขปัญหาหนี้สินครู</div>
                                <div>3. <b>โครงสร้างการบริหาร:</b> แผนผังองค์กรและการแบ่งส่วนงานภายใน</div>
                                <div>4. <b>คณะกรรมการและผู้บริหาร:</b> รายนาม บทบาท และหน้าที่ความรับผิดชอบ</div>
                                <div>5. <b>วัตถุประสงค์ พันธกิจ วิสัยทัศน์:</b> กรอบการดำเนินงานตามกฎหมายจัดตั้ง</div>
                                <div>6. <b>แผนระยะยาวและแผนประจำปี:</b> ภาพรวมแผนปฏิบัติการและแผนดิจิทัล</div>
                                <div>7. <b>การกำกับดูแลองค์การที่ดี:</b> นโยบายธรรมาภิบาลและความโปร่งใส</div>
                                <div>8. <b>นโยบายรัฐบาล/กระทรวง:</b> การดำเนินงานตามข้อสั่งการและนโยบาย ศธ.</div>
                                <div>9. <b>กฎหมายและมติ ครม.:</b> พ.ร.บ., ระเบียบ, ข้อบังคับ และหนังสือเวียน</div>
                                <div>10. <b>สถานที่ติดต่อ:</b> ช่องทางติดต่อ ขอรับข้อมูล และรับฟังความคิดเห็น</div>
                            </div>
                        </div>

                        <div class="work-card">
                            <div class="work-card-header">
                                <div class="work-card-title">🔍 ความถูกต้อง ทันกาล และความเชื่อถือได้</div>
                                <span style="font-size: 11.5px; background: #fef3c7; color: #92400e; padding: 2px 8px; border-radius: 10px; font-weight: 700;">ระดับ 5 (0.2500)</span>
                            </div>
                            <div contenteditable="true" id="v5-card-right" class="work-card-body">
                                <div>• <b>ช่องทางเผยแพร่:</b> เว็บไซต์สำนักงาน ก.ค.ศ. (https://otepc.go.th/th/inform-services/mc.html) (เอกสารหมายเลข 12)</div>
                                <div>• <b>ความเป็นปัจจุบัน:</b> มีการทบทวนและปรับปรุงข้อมูลสารสนเทศให้เป็นปัจจุบันตลอดปีบัญชี 2569 ครอบคลุมผู้รับบริการและผู้มีส่วนได้ส่วนเสียทุกกลุ่ม</div>
                                <div>• <b>สรุปผลการประเมิน:</b> เปิดเผยครบถ้วนทั้ง 10 ประเด็นขึ้นไป ตรงตามค่าเกณฑ์วัด <b>ระดับ 5.0000 คะแนน</b> (เต็ม)</div>
                            </div>
                        </div>
                    </div>

                    <!-- Bottom Score Strip -->
                    <div class="bottom-score-strip">
                        <div class="bottom-score-left">
                            <div class="bottom-score-label">ผลการดำเนินงานข้อ 5 (น้ำหนัก 5%)</div>
                            <div class="bottom-score-value" id="v5-bottom-val">ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span></div>
                        </div>
                        <div style="text-align: right; font-size: 12.5px; color: #bae6fd;" id="v5-bottom-callout">
                            เปิดเผยข้อมูลสารสนเทศครบถ้วนทั้ง 10 ประเด็นผ่านเว็บไซต์ ถูกต้อง ทันกาล เชื่อถือได้ (คะแนนถ่วงน้ำหนัก 0.2500)
                        </div>
                    </div>
                </div>
            </div>

            <!-- FOOTER -->
            <div class="dashboard-footer">
                <div>สำนักงานคณะกรรมการข้าราชการครูและบุคลากรทางการศึกษา (ก.ค.ศ.) | สำนักบริหารเงินทุนหมุนเวียนเพื่อแก้ไขปัญหาหนี้สินข้าราชการครู</div>
                <div>คุณภาพการบริหาร เพื่อครู เพื่ออนาคตการศึกษาไทย</div>
            </div>

        </div>
    </div>

    <!-- TOAST NOTIFICATION -->
    <div id="toast-notification" class="toast">บันทึกข้อมูลเรียบร้อยแล้ว</div>

    <script>
        let lastFocusedElement = null;
        let activeQuarter = 4;
        let activeTopic = 0; // 0=Overview, 1..5=Sub-topics
        let currentAppMode = 'preview';

        const topicNames = {
            0: "ภาพรวมสรุป_5_ข้อ",
            1: "ข้อ_1_แผนระยะยาวและแผนปี70",
            2: "ข้อ_2_การประชุมคณะกรรมการ",
            3: "ข้อ_3_ติดตามผลงาน5ด้าน",
            4: "ข้อ_4_ประเมินผลผู้บริหาร",
            5: "ข้อ_5_เปิดเผยข้อมูล10ด้าน"
        };

        const STORAGE_KEY_PREFIX = 'kpi_official_51_v1_Q';

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

        /* Navigation Switcher strictly for 1.1 to 5.1 */
        function navigateToKPI(targetKey) {
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
                '5.1': 'ตัวชี้วัดที่ 5.1.html'
            };
            if (routes[targetKey]) {
                window.location.href = routes[targetKey];
            }
        }

        /* Dual Mode Switcher */
        function setAppMode(mode) {
            currentAppMode = mode;
            const btnPrev = document.getElementById('btn-mode-preview');
            const btnEdit = document.getElementById('btn-mode-edit');
            const fmtBar = document.getElementById('format-toolbar');

            if (mode === 'edit') {
                document.body.classList.remove('app-mode-preview');
                document.body.classList.add('app-mode-edit');
                btnEdit.classList.add('active');
                btnPrev.classList.remove('active');
                if (fmtBar) fmtBar.style.display = 'flex';
                showToast("เข้าสู่โหมดแก้ไขข้อความ (คลิกข้อความบนการ์ดเพื่อแก้ไข)");
            } else {
                document.body.classList.remove('app-mode-edit');
                document.body.classList.add('app-mode-preview');
                btnPrev.classList.add('active');
                btnEdit.classList.remove('active');
                if (fmtBar) fmtBar.style.display = 'none';
                showToast("เข้าสู่โหมดนำเสนอ (Preview)");
            }
        }

        /* Format text commands */
        function formatDoc(cmd, val = null) {
            if (currentAppMode !== 'edit') return;
            document.execCommand(cmd, false, val);
        }

        function changeFontSize(delta) {
            if (currentAppMode !== 'edit') return;
            const sel = window.getSelection();
            if (!sel.rangeCount) return;
            document.execCommand('fontSize', false, delta > 0 ? '4' : '2');
        }

        /* Topic Filter View Switcher */
        function switchTopicView(topicIndex) {
            activeTopic = topicIndex;
            for (let i = 0; i <= 5; i++) {
                const btn = document.getElementById(`tab-btn-${i}`);
                const view = document.getElementById(`view-topic-${i}`);
                if (btn) {
                    if (i === topicIndex) btn.classList.add('active');
                    else btn.classList.remove('active');
                }
                if (view) {
                    if (i === topicIndex) view.classList.add('active');
                    else view.classList.remove('active');
                }
            }
        }

        /* Official Quarter Defaults */
        const quarterDefaults = {
            1: {
                badgeText: 'ไตรมาส 1',
                heroScore: 'ระดับ 0.9500 คะแนน',
                heroStars: '★☆☆☆☆',
                statusBadge: 'ระดับ 0.95 (เบื้องต้น)',
                completeVal: 'เริ่มต้น 2 ข้อ',
                gradeVal: 'ระดับ 0.95 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 1: จัดประชุมคณะกรรมการบริหารเงินทุนหมุนเวียนฯ 1 ครั้ง (ครั้งที่ 8/2568 วันที่ 16 ธ.ค. 68 กรรมการเข้าประชุม 87.5%), เริ่มต้นรวบรวมข้อมูลติดตามผลงาน 5 ด้าน และเปิดเผยข้อมูลสารสนเทศครบ 10 ประเด็นบนเว็บไซต์ ส่วนการจัดทำแผนยุทธศาสตร์และการประเมินผู้บริหารอยู่ระหว่างเตรียมการ',
                table: {
                    s1: 'N/A', ws1: '0.0000',
                    s2: 'N/A', ws2: '0.0000',
                    s3: 'N/A', ws3: '0.0000',
                    s4: '2.0000', ws4: '0.7000',
                    s5: 'N/A', ws5: '0.0000',
                    s6: '5.0000', ws6: '0.2500',
                    totLevel: 'ระดับ 0.95 (เบื้องต้น)', totWScore: '0.9500 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงาน N/A',
                    activeRubric: 1,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 1: อยู่ระหว่างเตรียมการทบทวนบริบทและกรอบหลักเกณฑ์การประเมินผล',
                    step3Sub: 'อยู่ระหว่างเตรียมการ',
                    step4Sub: 'อยู่ระหว่างเตรียมการ'
                },
                v2: {
                    scorePill: 'น้ำหนัก 10% | ผลงาน N/A',
                    activeRubric: 1,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 1: จัดประชุม 1 ครั้ง (16 ธ.ค. 68) เข้าประชุม 87.5% (ยังไม่ครบเกณฑ์วัดสิ้นปี)',
                    cardLeft: '<div>• <b>ครั้งที่ 8/2568 (16 ธ.ค. 68):</b> กรรมการเข้าประชุม 7/8 ท่าน (ร้อยละ 87.50)</div>'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 2',
                    activeRubric: 2,
                    bottomVal: 'ระดับ 2.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 1: รวบรวมรายงานผลการปฏิบัติงาน 5 ด้าน เตรียมเสนอที่ประชุม คกก. ในไตรมาส 2'
                },
                v4: {
                    scorePill: 'น้ำหนัก 20% | ผลงาน N/A',
                    activeRubric: 1,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 1: อยู่ระหว่างเตรียมการจัดทำกรอบการประเมินผลผู้บริหาร'
                },
                v5: {
                    scorePill: 'น้ำหนัก 5% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'ไตรมาสที่ 1: เปิดเผยข้อมูลสารสนเทศครบถ้วน 10 ประเด็นบนเว็บไซต์สำนักงาน (คะแนนถ่วงน้ำหนัก 0.2500)'
                }
            },
            2: {
                badgeText: 'ไตรมาส 2',
                heroScore: 'ระดับ 1.3000 คะแนน',
                heroStars: '★★☆☆☆',
                statusBadge: 'ระดับ 1.30 (เบื้องต้น)',
                completeVal: 'ดำเนินการ 2 ข้อ',
                gradeVal: 'ระดับ 1.30 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 2: คกก.บริหารฯ ติดตามผลการปฏิบัติงานสำคัญครบ 5 ด้านในคราวประชุมครั้งที่ 1/2569 (28 ม.ค. 69) พร้อมให้ข้อคิดเห็นเร่งรัดการเบิกจ่ายงบประมาณ (ระดับ 3 ถ่วงน้ำหนัก 1.0500) และเปิดเผยข้อมูลสารสนเทศครบ 10 ประเด็นบนเว็บไซต์ (ระดับ 5 ถ่วงน้ำหนัก 0.2500)',
                table: {
                    s1: 'N/A', ws1: '0.0000',
                    s2: 'N/A', ws2: '0.0000',
                    s3: 'N/A', ws3: '0.0000',
                    s4: '3.0000', ws4: '1.0500',
                    s5: 'N/A', ws5: '0.0000',
                    s6: '5.0000', ws6: '0.2500',
                    totLevel: 'ระดับ 1.3 (เบื้องต้น)', totWScore: '1.3000 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงาน N/A',
                    activeRubric: 1,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 2: อยู่ในขั้นตอนการทบทวน ศึกษาบริบทที่เกี่ยวข้อง เพื่อกำหนดทิศทางยุทธศาสตร์และแผนงาน',
                    step3Sub: 'อยู่ระหว่างทบทวน',
                    step4Sub: 'อยู่ระหว่างทบทวน'
                },
                v2: {
                    scorePill: 'น้ำหนัก 10% | ผลงาน N/A',
                    activeRubric: 1,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 2: จัดประชุมแล้ว 2 ครั้ง มีกรรมการเข้าประชุมร้อยละ 87.50 ทั้ง 2 ครั้ง (ยังไม่ครบเกณฑ์วัดสิ้นปี)',
                    cardLeft: '<div>• <b>ครั้งที่ 8/2568 (16 ธ.ค. 68):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%)</div><div>• <b>ครั้งที่ 1/2569 (28 ม.ค. 69):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%)</div>'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 3',
                    activeRubric: 3,
                    bottomVal: 'ระดับ 3.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 2: ติดตามผลการปฏิบัติงานครบ 5 ด้าน และมอบข้อสังเกตเร่งรัดการเบิกจ่าย (คะแนนถ่วงน้ำหนัก 1.0500)'
                },
                v4: {
                    scorePill: 'น้ำหนัก 20% | ผลงาน N/A',
                    activeRubric: 1,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 2: อยู่ระหว่างเตรียมการจัดทำร่างบันทึกข้อตกลงและแบบประเมินผู้บริหาร'
                },
                v5: {
                    scorePill: 'น้ำหนัก 5% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'ไตรมาสที่ 2: เปิดเผยข้อมูลสารสนเทศครบถ้วน 10 ประเด็นบนเว็บไซต์สำนักงาน (คะแนนถ่วงน้ำหนัก 0.2500)'
                }
            },
            3: {
                badgeText: 'ไตรมาส 3',
                heroScore: 'ระดับ 1.6500 คะแนน',
                heroStars: '★★★☆☆',
                statusBadge: 'ระดับ 1.65 (เบื้องต้น)',
                completeVal: 'ดำเนินการ 2 ข้อ',
                gradeVal: 'ระดับ 1.65 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 3: คกก.บริหารฯ ติดตามผลงานสำคัญ 5 ด้านอย่างต่อเนื่อง มอบข้อคิดเห็นและติดตามการแก้ไข (ระดับ 4 ถ่วงน้ำหนัก 1.4000) เปิดเผยข้อมูลครบ 10 ประเด็นบนเว็บไซต์ (ระดับ 5 ถ่วงน้ำหนัก 0.2500) และได้จัดประชุมเชิงปฏิบัติการยกร่างแผนระยะยาว 3 ปี และแผนปี 2570 เมื่อ 15-16 มิ.ย. 69 เรียบร้อย',
                table: {
                    s1: 'N/A', ws1: '0.0000',
                    s2: 'N/A', ws2: '0.0000',
                    s3: 'N/A', ws3: '0.0000',
                    s4: '4.0000', ws4: '1.4000',
                    s5: 'N/A', ws5: '0.0000',
                    s6: '5.0000', ws6: '0.2500',
                    totLevel: 'ระดับ 1.65 (เบื้องต้น)', totWScore: '1.6500 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงาน N/A',
                    activeRubric: 2,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 3: จัดประชุมเชิงปฏิบัติการยกร่างแผน 15-16 มิ.ย. 69 เตรียมเสนอ คกก.บริหารฯ ในไตรมาส 4',
                    step3Sub: 'เตรียมเสนอ คกก.บริหารฯ',
                    step4Sub: 'รออนุมัติไตรมาส 4'
                },
                v2: {
                    scorePill: 'น้ำหนัก 10% | ผลงาน N/A',
                    activeRubric: 4,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 3: จัดประชุม 4 ครั้ง มีกรรมการเข้าประชุม &ge; 80% จำนวน 3 ครั้ง คิดเป็น 75% (ยังไม่ครบเกณฑ์วัดสิ้นปี)',
                    cardLeft: '<div>• <b>ครั้งที่ 8/68 (16 ธ.ค. 68):</b> เข้าประชุม 7/8 (87.50%)</div><div>• <b>ครั้งที่ 1/69 (28 ม.ค. 69):</b> เข้าประชุม 7/8 (87.50%)</div><div>• <b>ครั้งที่ 2/69 (29 เม.ย. 69):</b> เข้าประชุม 7/8 (87.50%)</div><div>• <b>ครั้งที่ 3/69 (26 มิ.ย. 69):</b> เข้าประชุม 5/8 (62.50%)</div>'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 4',
                    activeRubric: 4,
                    bottomVal: 'ระดับ 4.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★☆</span>',
                    bottomCallout: 'ไตรมาสที่ 3: ติดตามผลงาน 5 ด้าน มอบข้อคิดเห็น และติดตามการดำเนินงานตามข้อเสนอแนะต่อเนื่อง (คะแนนถ่วงน้ำหนัก 1.4000)'
                },
                v4: {
                    scorePill: 'น้ำหนัก 20% | ผลงาน N/A',
                    activeRubric: 2,
                    bottomVal: 'ระดับ N/A <span style="font-size: 18px; color: #94a3b8;">☆☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาสที่ 3: อยู่ระหว่างเตรียมการเสนอแต่งตั้งคณะอนุกรรมการประเมินผลผู้บริหาร'
                },
                v5: {
                    scorePill: 'น้ำหนัก 5% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'ไตรมาสที่ 3: เปิดเผยข้อมูลสารสนเทศครบถ้วน 10 ประเด็นบนเว็บไซต์สำนักงาน (คะแนนถ่วงน้ำหนัก 0.2500)'
                }
            },
            4: {
                badgeText: 'ไตรมาส 4',
                heroScore: 'ระดับ 5.0000 คะแนน',
                heroStars: '★★★★★',
                statusBadge: 'ระดับ 5.0000 (เต็ม)',
                completeVal: 'ครบ 5 ข้อ',
                gradeVal: 'ระดับ 5 (เต็ม)',
                summaryDesc: 'คณะกรรมการบริหารเงินทุนหมุนเวียนฯ ปฏิบัติหน้าที่กำกับดูแลบรรลุเกณฑ์ระดับ 5 ครบถ้วนทุกข้อ ได้แก่ การกำหนดทิศทางยุทธศาสตร์และแผนปฏิบัติการระยะยาว 3 ปี (2570-2572) และแผนปี 2570 มีคุณภาพครบถ้วน, การเข้าร่วมประชุมเฉลี่ยร้อยละ 85.71 (เกินเกณฑ์ 80%), ติดตามผลการปฏิบัติงาน 5 ด้านเป็นรายไตรมาสและให้ข้อคิดเห็นขับเคลื่อนงาน, ประเมินผลผู้บริหาร (94.60%) ผูกโยงกับระบบแรงจูงใจ และเปิดเผยข้อมูลสารสนเทศครบถ้วนทั้ง 10 ประเด็น',
                table: {
                    s1: '5.0000', ws1: '0.7500',
                    s2: '5.0000', ws2: '0.7500',
                    s3: '5.0000', ws3: '0.5000',
                    s4: '5.0000', ws4: '1.7500',
                    s5: '5.0000', ws5: '1.0000',
                    s6: '5.0000', ws6: '0.2500',
                    totLevel: 'ระดับ 5.0', totWScore: '5.0000 คะแนน'
                },
                v1: {
                    scorePill: 'น้ำหนัก 30% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'บรรลุเกณฑ์ระดับ 5 ทั้ง 2 ประเด็น (คกก.เห็นชอบ 23 ก.ค. 69 และกรมบัญชีกลางอนุมัติ 30 ก.ย. 69) คะแนนถ่วงน้ำหนักรวม 1.5000',
                    step3Sub: 'มติเห็นชอบ คราวประชุม 4/2569 (23 ก.ค. 69)',
                    step4Sub: 'หนังสือ กค 0406.6/36581 (30 ก.ย. 69)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 10% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'การประชุม 6 ใน 7 ครั้ง มีกรรมการเข้าประชุม &ge; 80% คิดเป็นร้อยละ 85.71 บรรลุระดับ 5 เต็ม (คะแนนถ่วงน้ำหนัก 0.5000)',
                    cardLeft: '<div>• <b>ครั้งที่ 8/2568 (16 ธ.ค. 68):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%) ✓</div><div>• <b>ครั้งที่ 1/2569 (28 ม.ค. 69):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%) ✓</div><div>• <b>ครั้งที่ 2/2569 (29 เม.ย. 69):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%) ✓</div><div>• <b>ครั้งที่ 3/2569 (26 มิ.ย. 69):</b> กรรมการเข้าประชุม 5/8 ท่าน (62.50%)</div><div>• <b>ครั้งที่ 4/2569 (23 ก.ค. 69):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%) ✓</div><div>• <b>ครั้งที่ 5/2569 (28 ส.ค. 69):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%) ✓</div><div>• <b>ครั้งที่ 6/2569 (30 ก.ย. 69):</b> กรรมการเข้าประชุม 7/8 ท่าน (87.50%) ✓</div>'
                },
                v3: {
                    scorePill: 'น้ำหนัก 35% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'ติดตามผลงาน 5 ด้านรายไตรมาส มอบข้อสังเกต ติดตามการแก้ไข และนำผลไปกำหนดนโยบายและแผนงาน (คะแนนถ่วงน้ำหนัก 1.7500)'
                },
                v4: {
                    scorePill: 'น้ำหนัก 20% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'คกก.บริหารฯ อนุมัติผลประเมินผู้บริหาร 94.60% และส่งสำนักงาน ก.ค.ศ. ผูกโยงระบบแรงจูงใจเลื่อนเงินเดือน (คะแนนถ่วงน้ำหนัก 1.0000)'
                },
                v5: {
                    scorePill: 'น้ำหนัก 5% | ผลงานระดับ 5',
                    activeRubric: 5,
                    bottomVal: 'ระดับ 5.0000 คะแนน <span style="font-size: 18px; color: #facc15;">★★★★★</span>',
                    bottomCallout: 'เปิดเผยข้อมูลสารสนเทศครบถ้วนทั้ง 10 ประเด็นผ่านเว็บไซต์ ถูกต้อง ทันกาล เชื่อถือได้ (คะแนนถ่วงน้ำหนัก 0.2500)'
                }
            }
        };

        /* Switch Quarter Logic */
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
            document.getElementById('tbl-score-4').innerText = data.table.s4;
            document.getElementById('tbl-wscore-4').innerText = data.table.ws4;
            document.getElementById('tbl-score-5').innerText = data.table.s5;
            document.getElementById('tbl-wscore-5').innerText = data.table.ws5;
            document.getElementById('tbl-score-6').innerText = data.table.s6;
            document.getElementById('tbl-wscore-6').innerText = data.table.ws6;
            document.getElementById('tbl-total-level').innerText = data.table.totLevel;
            document.getElementById('tbl-total-wscore').innerText = data.table.totWScore;

            // 2. View 1 Updates
            document.getElementById('v1-score-pill').innerText = data.v1.scorePill;
            document.getElementById('v1-bottom-val').innerHTML = data.v1.bottomVal;
            document.getElementById('v1-bottom-callout').innerText = data.v1.bottomCallout;
            if (data.v1.step3Sub) document.getElementById('v1-step3-sub').innerText = data.v1.step3Sub;
            if (data.v1.step4Sub) document.getElementById('v1-step4-sub').innerText = data.v1.step4Sub;
            updateRubricHighlight('v1', data.v1.activeRubric);

            // 3. View 2 Updates
            document.getElementById('v2-score-pill').innerText = data.v2.scorePill;
            document.getElementById('v2-bottom-val').innerHTML = data.v2.bottomVal;
            document.getElementById('v2-bottom-callout').innerText = data.v2.bottomCallout;
            if (data.v2.cardLeft) document.getElementById('v2-card-left').innerHTML = data.v2.cardLeft;
            updateRubricHighlight('v2', data.v2.activeRubric);

            // 4. View 3 Updates
            document.getElementById('v3-score-pill').innerText = data.v3.scorePill;
            document.getElementById('v3-bottom-val').innerHTML = data.v3.bottomVal;
            document.getElementById('v3-bottom-callout').innerText = data.v3.bottomCallout;
            updateRubricHighlight('v3', data.v3.activeRubric);

            // 5. View 4 Updates
            document.getElementById('v4-score-pill').innerText = data.v4.scorePill;
            document.getElementById('v4-bottom-val').innerHTML = data.v4.bottomVal;
            document.getElementById('v4-bottom-callout').innerText = data.v4.bottomCallout;
            updateRubricHighlight('v4', data.v4.activeRubric);

            // 6. View 5 Updates
            document.getElementById('v5-score-pill').innerText = data.v5.scorePill;
            document.getElementById('v5-bottom-val').innerHTML = data.v5.bottomVal;
            document.getElementById('v5-bottom-callout').innerText = data.v5.bottomCallout;
            updateRubricHighlight('v5', data.v5.activeRubric);
        }

        function updateRubricHighlight(prefix, activeNum) {
            for (let i = 1; i <= 5; i++) {
                const cell = document.getElementById(`${prefix}-rubric-${i}`);
                if (!cell) continue;
                cell.classList.remove('active', 'achieved-gold');
                if (i === activeNum) {
                    cell.classList.add('achieved-gold');
                }
            }
        }

        /* Save & Load for Edit Mode */
        function saveCurrentQuarter(showFeedback = false) {
            const dataToSave = {
                hdrMain: document.getElementById('hdr-main-title').innerText,
                hdrSub: document.getElementById('hdr-sub-title').innerText,
                summaryDesc: document.getElementById('summary-overview-desc').innerText,
                v1CardLeft: document.getElementById('v1-card-left').innerHTML,
                v1CardRight: document.getElementById('v1-card-right').innerHTML,
                v2CardLeft: document.getElementById('v2-card-left').innerHTML,
                v2CardRight: document.getElementById('v2-card-right').innerHTML,
                v3CardLeft: document.getElementById('v3-card-left').innerHTML,
                v3CardRight: document.getElementById('v3-card-right').innerHTML,
                v4CardLeft: document.getElementById('v4-card-left').innerHTML,
                v4CardRight: document.getElementById('v4-card-right').innerHTML,
                v5CardLeft: document.getElementById('v5-card-left').innerHTML,
                v5CardRight: document.getElementById('v5-card-right').innerHTML
            };

            localStorage.setItem(getStorageKey(activeQuarter), JSON.stringify(dataToSave));
            if (showFeedback) {
                showToast(`บันทึกข้อมูลไตรมาส ${activeQuarter} ลงในเครื่องเรียบร้อยแล้ว`);
            }
        }

        function loadCustomEdits(obj) {
            if (obj.hdrMain) document.getElementById('hdr-main-title').innerText = obj.hdrMain;
            if (obj.hdrSub) document.getElementById('hdr-sub-title').innerText = obj.hdrSub;
            if (obj.summaryDesc) document.getElementById('summary-overview-desc').innerText = obj.summaryDesc;
            if (obj.v1CardLeft) document.getElementById('v1-card-left').innerHTML = obj.v1CardLeft;
            if (obj.v1CardRight) document.getElementById('v1-card-right').innerHTML = obj.v1CardRight;
            if (obj.v2CardLeft) document.getElementById('v2-card-left').innerHTML = obj.v2CardLeft;
            if (obj.v2CardRight) document.getElementById('v2-card-right').innerHTML = obj.v2CardRight;
            if (obj.v3CardLeft) document.getElementById('v3-card-left').innerHTML = obj.v3CardLeft;
            if (obj.v3CardRight) document.getElementById('v3-card-right').innerHTML = obj.v3CardRight;
            if (obj.v4CardLeft) document.getElementById('v4-card-left').innerHTML = obj.v4CardLeft;
            if (obj.v4CardRight) document.getElementById('v4-card-right').innerHTML = obj.v4CardRight;
            if (obj.v5CardLeft) document.getElementById('v5-card-left').innerHTML = obj.v5CardLeft;
            if (obj.v5CardRight) document.getElementById('v5-card-right').innerHTML = obj.v5CardRight;
        }

        /* Year change */
        function changeFiscalYear(yr) {
            showToast(`เลือกดูข้อมูลปีงบประมาณ ${yr}`);
        }

        /* Fullscreen toggle */
        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(err => {
                    alert(`ไม่สามารถเปิดโหมดเต็มจอได้: ${err.message}`);
                });
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                }
            }
        }

        /* Direct Clipboard Copy (PNG) */
        async function copyImageToClipboard() {
            const canvasElem = document.getElementById('report-canvas');
            if (!canvasElem) return;

            showToast("กำลังสร้างรูปภาพและคัดลอกลงคลิปบอร์ด...");

            try {
                const canvas = await html2canvas(canvasElem, {
                    scale: 2,
                    useCORS: true,
                    backgroundColor: '#ffffff'
                });

                canvas.toBlob(async function(blob) {
                    if (!blob) {
                        showToast("เกิดข้อผิดพลาดในการสร้าง Blob ภาพ");
                        return;
                    }
                    try {
                        const item = new ClipboardItem({ "image/png": blob });
                        await navigator.clipboard.write([item]);
                        showToast("คัดลอกรูปภาพลงคลิปบอร์ดแล้ว! วาง (Ctrl+V) ได้ทันที");
                    } catch (err) {
                        console.error("Clipboard API error:", err);
                        const link = document.createElement('a');
                        link.download = `KPI_5.1_Q${activeQuarter}_${topicNames[activeTopic]}.png`;
                        link.href = canvas.toDataURL('image/png');
                        link.click();
                        showToast("เบราว์เซอร์ไม่อนุญาตคลิปบอร์ด จึงดาวน์โหลดเป็นไฟล์ PNG แทน");
                    }
                }, 'image/png');
            } catch (error) {
                console.error("html2canvas error:", error);
                showToast("เกิดข้อผิดพลาดในการคัดลอกภาพ");
            }
        }

        /* Export PNG */
        async function exportToImage() {
            const canvasElem = document.getElementById('report-canvas');
            if (!canvasElem) return;

            showToast("กำลังส่งออกรูปภาพ PNG คุณภาพสูง...");

            try {
                const canvas = await html2canvas(canvasElem, {
                    scale: 2,
                    useCORS: true,
                    backgroundColor: '#ffffff'
                });

                const link = document.createElement('a');
                link.download = `รายงานตัวชี้วัดที่_5.1_ไตรมาส${activeQuarter}_${topicNames[activeTopic]}.png`;
                link.href = canvas.toDataURL('image/png');
                link.click();
                showToast("ดาวน์โหลดรูปภาพ PNG เรียบร้อยแล้ว");
            } catch (error) {
                console.error("Export Image error:", error);
                showToast("เกิดข้อผิดพลาดในการส่งออกภาพ");
            }
        }

        /* Direct PDF Export (Full Bleed) */
        async function exportToPDF() {
            const canvasElem = document.getElementById('report-canvas');
            if (!canvasElem) return;

            showToast("กำลังประมวลผล PDF เต็มแผ่นคุณภาพสูง...");

            try {
                const canvas = await html2canvas(canvasElem, {
                    scale: 2,
                    useCORS: true,
                    backgroundColor: '#ffffff'
                });

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
                pdf.save(`รายงานตัวชี้วัดที่_5.1_ไตรมาส${activeQuarter}_${topicNames[activeTopic]}.pdf`);
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

with open('ตัวชี้วัดที่ 5.1.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS_BUILD_51")
