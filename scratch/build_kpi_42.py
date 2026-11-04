import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
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
            width: 100%;
            max-width: 1560px;
            min-width: 980px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        /* Toolbar Top Controls (Screen Only) */
        .toolbar-container {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .toolbar {
            background: #ffffff;
            padding: 10px 18px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 45, 90, 0.08);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            border: 1px solid #c8dced;
        }

        .toolbar-left, .toolbar-right {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .control-group {
            display: flex;
            align-items: center;
            gap: 6px;
            background: #f0f6fa;
            padding: 4px 10px;
            border-radius: 8px;
            border: 1px solid #d0e2f0;
            font-size: 13px;
            font-weight: 600;
            color: #003366;
        }

        .select-input {
            border: 1px solid #a8c8e4;
            border-radius: 6px;
            padding: 5px 10px;
            font-size: 13px;
            font-weight: 600;
            color: #003366;
            background: #ffffff;
            cursor: pointer;
            outline: none;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            border: none;
            transition: all 0.2s ease;
            text-decoration: none;
        }

        .btn-primary { background: #005691; color: #ffffff; }
        .btn-primary:hover { background: #003d66; }
        .btn-success { background: #0e8a43; color: #ffffff; }
        .btn-success:hover { background: #096330; }
        .btn-warning { background: #d97706; color: #ffffff; }
        .btn-warning:hover { background: #b45309; }
        .btn-outline {
            background: #ffffff;
            color: #004b87;
            border: 1.5px solid #004b87;
        }
        .btn-outline:hover { background: #e6f0fa; }

        .mode-toggle {
            display: inline-flex;
            background: #e2ecf5;
            border-radius: 20px;
            padding: 3px;
            border: 1px solid #b8d4ec;
        }

        .mode-btn {
            padding: 5px 14px;
            border-radius: 16px;
            font-size: 12.5px;
            font-weight: 700;
            border: none;
            cursor: pointer;
            background: transparent;
            color: #406080;
            transition: all 0.2s;
        }

        .mode-btn.active {
            background: #004b87;
            color: #ffffff;
            box-shadow: 0 2px 6px rgba(0, 75, 135, 0.3);
        }

        /* Sub-topics Filter Tabs Bar */
        .filter-tabs-bar {
            background: #ffffff;
            border: 1.5px solid #b8d4ee;
            border-radius: 12px;
            padding: 9px 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            box-shadow: 0 4px 16px rgba(0, 45, 90, 0.08);
        }

        .filter-tab-title {
            font-size: 14px;
            font-weight: 800;
            color: #003366;
            margin-right: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .tab-btn {
            background: #f1f7fc;
            color: #0f2742;
            border: 1.5px solid #bcd8f0;
            border-radius: 8px;
            padding: 7px 14px;
            font-size: 13.5px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .tab-btn:hover {
            background: #e0effa;
            border-color: #005691;
            color: #003366;
        }

        .tab-btn.active {
            background: linear-gradient(135deg, #003a66 0%, #001a33 100%);
            color: #ffffff;
            border-color: #001529;
            box-shadow: 0 3px 10px rgba(0, 45, 90, 0.3);
        }

        .tab-btn .tab-pct {
            font-size: 11.5px;
            padding: 2px 7px;
            border-radius: 10px;
            background: rgba(0, 86, 145, 0.15);
            color: #004575;
            font-weight: 800;
        }

        .tab-btn.active .tab-pct {
            background: #f59e0b;
            color: #ffffff;
        }

        /* Format Control Bar (Edit Mode Only) */
        .format-bar {
            background: #ffffff;
            border: 1px solid #c8dced;
            border-radius: 10px;
            padding: 6px 14px;
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
            box-shadow: 0 2px 8px rgba(0, 45, 90, 0.04);
            font-size: 12.5px;
        }

        .format-title {
            font-weight: 700;
            color: #005691;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .format-sep {
            width: 1px;
            height: 18px;
            background: #d4e4f2;
            margin: 0 2px;
        }

        .active-target-pill {
            font-size: 12px;
            color: #1e3a56;
            background: #f0f6fa;
            padding: 3px 10px;
            border-radius: 6px;
            border: 1px solid #c8dced;
            max-width: 280px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* Dashboard Slide Canvas */
        .slide-canvas {
            background: #ffffff;
            border-radius: 16px;
            border: 1.5px solid #a8cce8;
            box-shadow: 0 8px 30px rgba(0, 40, 80, 0.12);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        /* Header Banner */
        .header-banner {
            background: linear-gradient(135deg, #001933 0%, #00386b 40%, #005999 100%);
            padding: 18px 24px;
            color: #ffffff;
            position: relative;
            border-bottom: 4px solid #f0b429;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .header-icon {
            width: 48px;
            height: 48px;
            background: rgba(255, 255, 255, 0.12);
            border: 1.5px solid rgba(255, 255, 255, 0.3);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: #ffffff;
        }

        .header-title-box h1 {
            font-size: 20px;
            font-weight: 800;
            letter-spacing: -0.2px;
            color: #ffffff;
            margin-bottom: 3px;
        }

        .header-title-box p {
            font-size: 13px;
            color: #cde4f7;
            font-weight: 500;
        }

        .header-right-tag {
            text-align: right;
            font-size: 12.5px;
            color: #a8d4f5;
            font-weight: 600;
            line-height: 1.4;
            font-style: italic;
        }

        /* Sub-Header Metadata Bar */
        .sub-header-bar {
            background: #f7fafc;
            border-bottom: 1px solid #d4e4f2;
            padding: 10px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        .meta-pills-row {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .meta-pill {
            background: #ffffff;
            border: 1px solid #c0daf0;
            border-radius: 6px;
            padding: 4px 12px;
            font-size: 13px;
            font-weight: 600;
            color: #0f2d4a;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .meta-pill span.val {
            font-weight: 800;
            color: #004b87;
        }

        .rubric-mini-box {
            display: flex;
            align-items: center;
            gap: 6px;
            background: #ffffff;
            border: 1px solid #c0daf0;
            border-radius: 6px;
            padding: 3px 8px;
            font-size: 11.5px;
            font-weight: 700;
        }

        .rubric-pill {
            padding: 2px 7px;
            border-radius: 4px;
            font-weight: 800;
            font-size: 11.5px;
        }

        .rubric-1 { background: #e0f2fe; color: #0284c7; }
        .rubric-2 { background: #dbeafe; color: #2563eb; }
        .rubric-3 { background: #e0e7ff; color: #4338ca; }
        .rubric-4 { background: #ccfbf1; color: #0d9488; }
        .rubric-5 { background: #dcfce7; color: #15803d; }

        /* Content Area */
        .slide-body {
            padding: 20px 24px;
            background: #f4f8fc;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        /* Views management */
        .topic-view {
            display: none;
            flex-direction: column;
            gap: 16px;
            animation: fadeIn 0.25s ease-out;
        }

        .topic-view.active {
            display: flex;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Split Layout (2 Columns) */
        .split-layout {
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 16px;
        }

        /* Modern Executive Card */
        .content-card {
            background: #ffffff;
            border-radius: 12px;
            border: 1.5px solid #c4dcee;
            box-shadow: 0 4px 14px rgba(0, 35, 70, 0.05);
            padding: 16px 20px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .card-header-line {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e2ecf5;
            padding-bottom: 8px;
        }

        .card-title {
            font-size: 15.5px;
            font-weight: 800;
            color: #003366;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .card-badge {
            background: #e1effa;
            color: #004b87;
            font-size: 12px;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 20px;
            border: 1px solid #b3d5ee;
        }

        /* Overview Table */
        .overview-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 10px;
            overflow: hidden;
            border: 1.5px solid #003d73;
            font-size: 14px;
        }

        .overview-table th {
            background: #003366;
            color: #ffffff;
            padding: 10px 12px;
            font-weight: 700;
            text-align: center;
            font-size: 13.5px;
            border-right: 1px solid #1a4d80;
        }

        .overview-table th:last-child {
            border-right: none;
        }

        .overview-table td {
            padding: 12px 14px;
            border-bottom: 1px solid #d0e2f0;
            border-right: 1px solid #d0e2f0;
            color: #0f2742;
            vertical-align: middle;
            font-size: 14px;
        }

        .overview-table td:last-child {
            border-right: none;
        }

        .overview-table tr:hover {
            background: #f0f7fd;
            cursor: pointer;
        }

        .overview-table tr.total-row {
            background: #e6f1fb;
            font-weight: 800;
            border-top: 2px solid #003d73;
        }

        .overview-table tr.total-row td {
            color: #003366;
            font-size: 14.5px;
            border-bottom: none;
        }

        /* Big Score Box */
        .big-score-box {
            background: linear-gradient(135deg, #001f3f 0%, #003b6f 100%);
            border-radius: 12px;
            padding: 16px 20px;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            gap: 6px;
            box-shadow: 0 4px 16px rgba(0, 31, 63, 0.25);
            border: 1px solid #004d99;
        }

        .big-score-subtitle {
            font-size: 13px;
            font-weight: 600;
            color: #a3c9ea;
            letter-spacing: 0.3px;
        }

        .big-score-val {
            font-size: 32px;
            font-weight: 800;
            color: #ffcc00;
            letter-spacing: -0.5px;
            line-height: 1.1;
        }

        .stars-row {
            color: #ffcc00;
            font-size: 18px;
            letter-spacing: 2px;
            display: flex;
            gap: 4px;
        }

        /* Summary Text Box */
        .summary-box {
            background: #ffffff;
            border-radius: 10px;
            border: 1px solid #c0daf0;
            padding: 14px 16px;
            font-size: 13.5px;
            color: #1a334d;
            line-height: 1.55;
            box-shadow: 0 2px 8px rgba(0, 45, 90, 0.03);
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .summary-box-title {
            font-weight: 800;
            color: #004b87;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Status Badge Container */
        .status-container-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .status-card {
            background: #f7fafc;
            border: 1px solid #ccdff0;
            border-radius: 10px;
            padding: 12px 14px;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .status-label {
            font-size: 12px;
            font-weight: 700;
            color: #4a6a8a;
        }

        .status-val {
            font-size: 18px;
            font-weight: 800;
            color: #006633;
        }

        /* Rubric Criteria 5 Cards (for Sub-views) */
        .rubric-grid-5 {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
        }

        .rubric-card {
            background: #f8fbfe;
            border: 1.5px solid #d2e4f3;
            border-radius: 10px;
            padding: 12px 10px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            transition: all 0.2s;
        }

        .rubric-card.active {
            border: 2px solid #ea580c;
            background: #fffdfa;
            box-shadow: 0 4px 14px rgba(234, 88, 12, 0.15);
        }

        .rubric-header-tag {
            display: inline-block;
            font-size: 12.5px;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 5px;
            align-self: flex-start;
        }

        .rubric-card.active .rubric-header-tag {
            background: #ea580c;
            color: #ffffff;
        }

        .rubric-desc {
            font-size: 12px;
            line-height: 1.45;
            color: #2c445c;
        }

        /* Process Flow 3 Columns (for Sub-views) */
        .process-flow-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            position: relative;
        }

        .flow-step-card {
            background: #ffffff;
            border: 1.5px solid #b8d6ee;
            border-radius: 10px;
            padding: 14px 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            box-shadow: 0 3px 10px rgba(0, 45, 90, 0.04);
            position: relative;
        }

        .flow-step-card.completed {
            background: #f4fbf7;
            border-color: #8fd0a8;
        }

        .step-pill-top {
            font-size: 11.5px;
            font-weight: 800;
            color: #005691;
            background: #e2f0fa;
            padding: 3px 10px;
            border-radius: 12px;
            align-self: flex-start;
        }

        .flow-step-card.completed .step-pill-top {
            color: #0b6b36;
            background: #dcf2e3;
        }

        .step-title {
            font-size: 14.5px;
            font-weight: 800;
            color: #0f2742;
        }

        .step-desc {
            font-size: 13px;
            color: #2d4560;
            line-height: 1.5;
        }

        /* Callout Box */
        .callout-box {
            background: #f1f8fc;
            border-left: 4px solid #005691;
            padding: 12px 16px;
            border-radius: 0 8px 8px 0;
            font-size: 13.5px;
            line-height: 1.5;
            color: #123456;
        }

        /* Evidence Box */
        .evidence-box {
            background: #ffffff;
            border: 1px solid #bcd8f0;
            border-radius: 8px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            font-size: 13px;
        }

        .evidence-title {
            font-weight: 800;
            color: #004b87;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .evidence-list {
            list-style: none;
            padding-left: 0;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .evidence-list li {
            position: relative;
            padding-left: 18px;
            color: #223e59;
            line-height: 1.45;
        }

        .evidence-list li::before {
            content: "📄";
            position: absolute;
            left: 0;
            font-size: 12px;
        }

        /* Bottom Footer Bar */
        .slide-footer {
            background: #ffffff;
            border-top: 1px solid #d4e4f2;
            padding: 10px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            color: #55728f;
            font-weight: 600;
        }

        /* Toast Notification */
        .toast {
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #002244;
            color: #ffffff;
            padding: 12px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
            font-size: 14px;
            font-weight: 700;
            display: none;
            z-index: 9999;
            border-left: 4px solid #f59e0b;
        }

        /* Print Media Style (Full-Page 100% Fit) */
        @media print {
            body {
                background: #ffffff;
                padding: 0 !important;
                margin: 0 !important;
            }
            .toolbar-container, .format-bar, .toast {
                display: none !important;
            }
            .page-wrapper {
                width: 100% !important;
                max-width: 100% !important;
                min-width: 0 !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .slide-canvas {
                border: none !important;
                box-shadow: none !important;
                border-radius: 0 !important;
            }
            @page {
                size: A4 landscape;
                margin: 8mm;
            }
        }
    </style>
</head>
<body>

<div class="page-wrapper">
    <!-- Top Toolbar Controls -->
    <div class="toolbar-container">
        <div class="toolbar">
            <div class="toolbar-left">
                <!-- KPI Switcher -->
                <div class="control-group">
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
                </div>

                <!-- Quarter Switcher -->
                <div class="control-group">
                    <label for="quarterSelect">📊 รายงานถึง:</label>
                    <select id="quarterSelect" class="select-input" onchange="switchQuarter(this.value)">
                        <option value="1">ไตรมาส 1 (ต.ค. - ธ.ค.)</option>
                        <option value="2">ไตรมาส 2 (ต.ค. - มี.ค.)</option>
                        <option value="3">ไตรมาส 3 (ต.ค. - มิ.ย.)</option>
                        <option value="4" selected>ไตรมาส 4 (ครบปี ต.ค. - ก.ย.)</option>
                    </select>
                </div>

                <div class="control-group">
                    <span id="activeQuarterBadge">📁 ข้อมูลเฉพาะ: ไตรมาส 4</span>
                </div>

                <div class="control-group">
                    <label>📅 ปี:</label>
                    <select class="select-input" style="padding: 3px 6px;">
                        <option selected>ปี 2569</option>
                    </select>
                </div>
            </div>

            <div class="toolbar-right">
                <!-- Dual Mode Toggle -->
                <div class="mode-toggle">
                    <button class="mode-btn active" id="btnModePreview" onclick="setMode('preview')">👁️ โหมดนำเสนอ (Preview)</button>
                    <button class="mode-btn" id="btnModeEdit" onclick="setMode('edit')">✏️ โหมดแก้ไขข้อความ (Edit)</button>
                </div>

                <button class="btn btn-outline" onclick="saveToStorage()">💾 บันทึก</button>
                <button class="btn btn-outline" onclick="copySlideImage()">📋 คัดลอกภาพ</button>
                <button class="btn btn-primary" onclick="exportSlidePNG()">🖼️ ส่งออกภาพ (PNG)</button>
                <button class="btn btn-warning" onclick="exportSlidePDF()">📄 ส่งออก PDF (เต็มแผ่น)</button>
                <button class="btn btn-success" onclick="window.print()">🖨️ พิมพ์ (Print)</button>
                <button class="btn btn-outline" onclick="toggleFullScreen()">⛶ เต็มจอ</button>
            </div>
        </div>

        <!-- Format Bar for Edit Mode -->
        <div class="format-bar" id="formatBar" style="display: none;">
            <div class="format-title">🛠️ จัดรูปแบบข้อความ:</div>
            <button class="btn btn-outline" style="padding: 3px 10px;" onclick="formatDoc('bold')"><b>B</b></button>
            <button class="btn btn-outline" style="padding: 3px 10px;" onclick="formatDoc('italic')"><i>I</i></button>
            <button class="btn btn-outline" style="padding: 3px 10px;" onclick="formatDoc('underline')"><u>U</u></button>
            <div class="format-sep"></div>
            <label>สี:</label>
            <input type="color" onchange="formatDoc('foreColor', this.value)" style="border:none; width:26px; height:26px; cursor:pointer; background:none;">
            <div class="format-sep"></div>
            <button class="btn btn-outline" style="padding: 3px 8px;" onclick="changeFontSize(1)">A+</button>
            <button class="btn btn-outline" style="padding: 3px 8px;" onclick="changeFontSize(-1)">A-</button>
            <div class="format-sep"></div>
            <span class="active-target-pill" id="activeTargetLabel">📌 คลิกข้อความที่ต้องการพิมพ์แก้ไข</span>
        </div>

        <!-- Sub-topics Filter Tabs -->
        <div class="filter-tabs-bar">
            <span class="filter-tab-title">📑 ตัวกรองหัวข้อ (Sub-topics):</span>
            <button class="tab-btn active" id="tab0" onclick="switchTopicView(0)">
                <span>📊 ภาพรวมสรุป 3 ข้อ</span>
                <span class="tab-pct">100%</span>
            </button>
            <button class="tab-btn" id="tab1" onclick="switchTopicView(1)">
                <span>1. การปฏิบัติงานตรวจสอบภายใน</span>
                <span class="tab-pct">45%</span>
            </button>
            <button class="tab-btn" id="tab2" onclick="switchTopicView(2)">
                <span>2. การประชุมปิดการตรวจสอบ</span>
                <span class="tab-pct">15%</span>
            </button>
            <button class="tab-btn" id="tab3" onclick="switchTopicView(3)">
                <span>3. การปฏิบัติงานตามข้อเสนอแนะ</span>
                <span class="tab-pct">40%</span>
            </button>
        </div>
    </div>

    <!-- Main Slide Canvas -->
    <div class="slide-canvas" id="slideCaptureArea">
        <!-- Header Banner -->
        <div class="header-banner">
            <div class="header-left">
                <div class="header-icon">🛡️</div>
                <div class="header-title-box">
                    <h1 id="banner-main-title" contenteditable="false">ด้านที่ 4 การบริหารจัดการทุนหมุนเวียน | ตัวชี้วัดที่ 4.2 การตรวจสอบภายใน</h1>
                    <p id="banner-sub-title" contenteditable="false">กรณีที่ 3 ทุนหมุนเวียนที่ใช้หน่วยงานตรวจสอบภายในจากหน่วยงานต้นสังกัด พิจารณาผลการดำเนินงาน 3 ประเด็นย่อย</p>
                </div>
            </div>
            <div class="header-right-tag">
                บริหารอย่างมีประสิทธิภาพ<br>โปร่งใส เพื่อการพัฒนาที่ยั่งยืน
            </div>
        </div>

        <!-- Sub-Header Metadata Bar -->
        <div class="sub-header-bar">
            <div class="meta-pills-row">
                <div class="meta-pill">📋 ตัวชี้วัด: <span class="val">4.2 การตรวจสอบภายใน</span></div>
                <div class="meta-pill">🎯 หน่วยวัด: <span class="val">ระดับคะแนน (1 - 5)</span></div>
                <div class="meta-pill">⚖️ ค่าน้ำหนัก: <span class="val">ร้อยละ 4</span></div>
                <div class="meta-pill">📐 ค่าเกณฑ์วัด: <span class="val">เกณฑ์ 5 ระดับ (กรณีที่ 3)</span></div>
            </div>
            <div class="rubric-mini-box">
                <span>เกณฑ์:</span>
                <span class="rubric-pill rubric-1">ระดับ 1: 1.00</span>
                <span class="rubric-pill rubric-2">ระดับ 2: 2.00</span>
                <span class="rubric-pill rubric-3">ระดับ 3: 3.00</span>
                <span class="rubric-pill rubric-4">ระดับ 4: 4.00</span>
                <span class="rubric-pill rubric-5">ระดับ 5: 5.00</span>
            </div>
        </div>

        <!-- Body Area -->
        <div class="slide-body">
            <!-- VIEW 0: OVERVIEW (3 SUB-ISSUES) -->
            <div class="topic-view active" id="view0">
                <div class="split-layout">
                    <!-- Left: Table -->
                    <div class="content-card">
                        <div class="card-header-line">
                            <div class="card-title">📊 ผลการดำเนินงานรวม 3 ประเด็นย่อย (ตัวชี้วัดที่ 4.2)</div>
                            <div class="card-badge">น้ำหนักรวม 100% (น้ำหนักในมิติ 4%)</div>
                        </div>
                        <table class="overview-table">
                            <thead>
                                <tr>
                                    <th style="width: 10%;">ข้อ</th>
                                    <th style="width: 48%; text-align: left; padding-left: 14px;">ประเด็นย่อยที่ใช้พิจารณา</th>
                                    <th style="width: 14%;">น้ำหนัก (%)</th>
                                    <th style="width: 14%;">ระดับคะแนน</th>
                                    <th style="width: 14%;">คะแนนถ่วงน้ำหนัก</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr onclick="switchTopicView(1)">
                                    <td style="text-align: center; font-weight: 700;">1</td>
                                    <td><b>การปฏิบัติงานตรวจสอบภายใน</b></td>
                                    <td style="text-align: center; font-weight: 700;">45%</td>
                                    <td style="text-align: center; font-weight: 800; color: #059669;" id="ov-r1-score" contenteditable="false">5.0000</td>
                                    <td style="text-align: center; font-weight: 800; color: #004b87;" id="ov-r1-weighted" contenteditable="false">2.2500</td>
                                </tr>
                                <tr onclick="switchTopicView(2)">
                                    <td style="text-align: center; font-weight: 700;">2</td>
                                    <td><b>การประชุมปิดการตรวจสอบ</b></td>
                                    <td style="text-align: center; font-weight: 700;">15%</td>
                                    <td style="text-align: center; font-weight: 800; color: #059669;" id="ov-r2-score" contenteditable="false">5.0000</td>
                                    <td style="text-align: center; font-weight: 800; color: #004b87;" id="ov-r2-weighted" contenteditable="false">0.7500</td>
                                </tr>
                                <tr onclick="switchTopicView(3)">
                                    <td style="text-align: center; font-weight: 700;">3</td>
                                    <td><b>การปฏิบัติงานตามข้อเสนอแนะ</b></td>
                                    <td style="text-align: center; font-weight: 700;">40%</td>
                                    <td style="text-align: center; font-weight: 800; color: #059669;" id="ov-r3-score" contenteditable="false">5.0000</td>
                                    <td style="text-align: center; font-weight: 800; color: #004b87;" id="ov-r3-weighted" contenteditable="false">2.0000</td>
                                </tr>
                                <tr class="total-row">
                                    <td colspan="2" style="text-align: center; font-size: 15px;">รวมผลการประเมินถ่วงน้ำหนักทั้งหมด</td>
                                    <td style="text-align: center; font-size: 15px;">100%</td>
                                    <td style="text-align: center; color: #005691; font-size: 15px;" id="ov-total-level" contenteditable="false">ระดับ 5</td>
                                    <td style="text-align: center; color: #059669; font-size: 15.5px;" id="ov-total-weighted" contenteditable="false">5.0000 คะแนน</td>
                                </tr>
                            </tbody>
                        </table>

                        <!-- Official Case Note -->
                        <div class="callout-box" style="margin-top: 2px;">
                            💡 <b>กรณีที่ 3 ทุนหมุนเวียนที่ใช้หน่วยงานตรวจสอบภายในจากหน่วยงานต้นสังกัด:</b> ได้รับการแต่งตั้งผู้ตรวจสอบภายในของสำนักงาน ก.ค.ศ. เป็นผู้ตรวจสอบภายในของเงินทุนหมุนเวียนฯ (มติ คกก.บริหารฯ 28 ธ.ค. 65) และมีกฎบัตรการตรวจสอบภายใน (มติ 30 เม.ย. 67) สำหรับเป็นกรอบการปฏิบัติงาน
                        </div>
                    </div>

                    <!-- Right: Score & Highlights -->
                    <div class="content-card" style="justify-content: space-between;">
                        <div class="card-header-line">
                            <div class="card-title">🏆 สรุปคะแนนผลการประเมินภาพรวม</div>
                            <div class="card-badge" id="ov-badge" style="background: #eef7ed; color: #15803d; border-color: #bbf7d0;">ระดับคะแนนสูงสุด</div>
                        </div>

                        <!-- Big Score Box -->
                        <div class="big-score-box">
                            <div class="big-score-subtitle">ผลการดำเนินงานเทียบเท่า</div>
                            <div class="big-score-val" id="ov-sc-val" contenteditable="false">ระดับ 5.0000 คะแนน</div>
                            <div class="stars-row" id="ov-stars">★★★★★</div>
                        </div>

                        <!-- Narrative Summary Box -->
                        <div class="summary-box">
                            <div class="summary-box-title">🎯 สรุปผลการดำเนินงานสำคัญ:</div>
                            <div id="ov-summary-desc" contenteditable="false">
                                ได้รับการตรวจสอบจากผู้ตรวจสอบภายในต้นสังกัดครบถ้วนตามแผน 2 ครั้ง มีการประชุมปิดการตรวจสอบร่วมกันระหว่างผู้บริหารและผู้ตรวจสอบภายใน ปฏิบัติตามข้อสังเกตและข้อเสนอแนะครบถ้วนทุกข้อ โดย คกก.บริหารเงินทุนหมุนเวียนฯ ได้มอบนโยบายการปฏิบัติงานที่สอดคล้องกับรายงานผลการตรวจสอบ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี
                            </div>
                        </div>

                        <!-- Status Cards -->
                        <div class="status-container-row">
                            <div class="status-card">
                                <div class="status-label">ความสำเร็จ</div>
                                <div class="status-val" id="ov-prog-label" contenteditable="false">ครบ 3 ประเด็น</div>
                            </div>
                            <div class="status-card">
                                <div class="status-label">สถานะประเมิน</div>
                                <div class="status-val" id="ov-eval-label" contenteditable="false">ระดับ 5 (เต็ม)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- VIEW 1: SUB-TOPIC 1: การปฏิบัติงานตรวจสอบภายใน (45%) -->
            <div class="topic-view" id="view1">
                <div class="content-card">
                    <div class="card-header-line">
                        <div class="card-title">🔍 1. การปฏิบัติงานตรวจสอบภายใน (น้ำหนัก 45%) - การตรวจสอบและรายงานผลต่อคณะกรรมการ</div>
                        <div class="card-badge" id="t1-badge">น้ำหนัก 45% | ผลงานระดับ 5</div>
                    </div>

                    <!-- Rubric 5 Levels -->
                    <div class="rubric-grid-5">
                        <div class="rubric-card" id="t1-r1">
                            <span class="rubric-header-tag rubric-1">ระดับ 1</span>
                            <div class="rubric-desc">ทุนหมุนเวียนประสานงานกับหน่วยตรวจสอบภายในต้นสังกัด แต่ไม่ได้รับการตรวจสอบจากผู้ตรวจสอบภายใน</div>
                        </div>
                        <div class="rubric-card" id="t1-r2" style="opacity: 0.5;">
                            <span class="rubric-header-tag rubric-2">ระดับ 2</span>
                            <div class="rubric-desc" style="text-align: center; padding-top: 10px;">-</div>
                        </div>
                        <div class="rubric-card" id="t1-r3">
                            <span class="rubric-header-tag rubric-3">ระดับ 3</span>
                            <div class="rubric-desc">ได้รับการตรวจสอบและได้รับรายงานผล นำเสนอรายงานผลการตรวจสอบต่อคณะกรรมการบริหารทุนหมุนเวียนรับทราบ</div>
                        </div>
                        <div class="rubric-card" id="t1-r4" style="opacity: 0.5;">
                            <span class="rubric-header-tag rubric-4">ระดับ 4</span>
                            <div class="rubric-desc" style="text-align: center; padding-top: 10px;">-</div>
                        </div>
                        <div class="rubric-card active" id="t1-r5">
                            <span class="rubric-header-tag rubric-5">ระดับ 5 ★</span>
                            <div class="rubric-desc">ได้รับการตรวจสอบ นำเสนอรายงานต่อคณะกรรมการบริหารทุนหมุนเวียน และ<b>คณะกรรมการฯ ได้มอบนโยบายการปฏิบัติงานที่สอดคล้องกับรายงานผลการตรวจสอบ</b></div>
                        </div>
                    </div>

                    <!-- Process Flow 3 Steps -->
                    <div class="process-flow-3">
                        <div class="flow-step-card completed" id="t1-s1">
                            <span class="step-pill-top">ขั้นตอนที่ 1 (กรอบ & กฎบัตร)</span>
                            <div class="step-title">แต่งตั้งผู้ตรวจ & จัดทำกฎบัตร</div>
                            <div class="step-desc" id="t1-s1-d" contenteditable="false">
                                • มติ คกก.บริหารฯ ครั้งที่ 8/2565 (28 ธ.ค. 65) แต่งตั้งผู้ตรวจสอบภายในของสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>
                                • มติ คกก.บริหารฯ ครั้งที่ 3/2567 (30 เม.ย. 67) เห็นชอบกฎบัตรการตรวจสอบภายใน และทบทวนสอบทานทุกปี
                            </div>
                        </div>
                        <div class="flow-step-card completed" id="t1-s2">
                            <span class="step-pill-top">ขั้นตอนที่ 2 (ปฏิบัติการตรวจ)</span>
                            <div class="step-title">แผนตรวจสอบ 2 ครั้ง ประจำปี 69</div>
                            <div class="step-desc" id="t1-s2-d" contenteditable="false">
                                • <b>ครั้งที่ 1 (รายงานการเงิน):</b> ดำเนินการ เม.ย. - ก.ค. 69 ประชุมปิดตรวจ 10 ก.ย. 69 และเสนอรายงานสำเร็จ<br>
                                • <b>ครั้งที่ 2 (เงินนอกงบประมาณ):</b> ดำเนินการ ก.ย. 69 สรุปผลการตรวจสอบเรียบร้อยตามแผน
                            </div>
                        </div>
                        <div class="flow-step-card completed" id="t1-s3">
                            <span class="step-pill-top">ขั้นตอนที่ 3 (นโยบาย คกก.)</span>
                            <div class="step-title">เสนอ คกก. & มอบนโยบาย</div>
                            <div class="step-desc" id="t1-s3-d" contenteditable="false">
                                เสนอรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 เมื่อ <b>30 กันยายน 2569</b> โดยคณะกรรมการฯ ได้มอบนโยบายและข้อสังเกตในการปฏิบัติงานสอดคล้องกับรายงานผล
                            </div>
                        </div>
                    </div>

                    <!-- Callout & Score Footer -->
                    <div style="display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 14px; align-items: stretch;">
                        <div class="evidence-box">
                            <div class="evidence-title">📄 เอกสารและหลักฐานอ้างอิงสำคัญ:</div>
                            <ul class="evidence-list" id="t1-evidence">
                                <li><b>เอกสารหมายเลข 1:</b> แผนการตรวจสอบประจำปีงบประมาณ พ.ศ. 2569 ของผู้ตรวจสอบภายใน สำนักงาน ก.ค.ศ.</li>
                                <li><b>เอกสารหมายเลข 2:</b> รายงานการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ (10 กันยายน 2569)</li>
                                <li><b>เอกสารหมายเลข 3:</b> รายงานผลการตรวจสอบการจัดทำรายงานการเงินของเงินทุนหมุนเวียนฯ โดยผู้ตรวจสอบภายใน</li>
                                <li><b>เอกสารหมายเลข 4:</b> รายงานการประชุมคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 (30 กันยายน 2569)</li>
                            </ul>
                            <div class="callout-box" id="t1-callout" style="margin-top: 6px;" contenteditable="false">
                                <b>สรุปผลการประเมิน:</b> ทุนหมุนเวียนได้รับการตรวจสอบภายใน รายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ และคณะกรรมการฯ ได้มอบนโยบายการปฏิบัติงาน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="justify-content: center;">
                            <div class="big-score-subtitle">ผลการดำเนินงานข้อที่ 1 (น้ำหนัก 45%)</div>
                            <div class="big-score-val" id="t1-sc-val" contenteditable="false">ระดับ 5.0000 คะแนน</div>
                            <div class="stars-row" id="t1-stars">★★★★★</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- VIEW 2: SUB-TOPIC 2: การประชุมปิดการตรวจสอบ (15%) -->
            <div class="topic-view" id="view2">
                <div class="content-card">
                    <div class="card-header-line">
                        <div class="card-title">🤝 2. การประชุมปิดการตรวจสอบ (น้ำหนัก 15%) - การมีส่วนร่วมของผู้บริหารและกำหนดแนวทางแก้ไข</div>
                        <div class="card-badge" id="t2-badge">น้ำหนัก 15% | ผลงานระดับ 5</div>
                    </div>

                    <!-- Rubric 5 Levels -->
                    <div class="rubric-grid-5">
                        <div class="rubric-card" id="t2-r1">
                            <span class="rubric-header-tag rubric-1">ระดับ 1</span>
                            <div class="rubric-desc">ประสานงานกับหน่วยตรวจ แต่ไม่ได้รับการตรวจสอบจากผู้ตรวจสอบภายในต้นสังกัด</div>
                        </div>
                        <div class="rubric-card" id="t2-r2">
                            <span class="rubric-header-tag rubric-2">ระดับ 2</span>
                            <div class="rubric-desc">มีการประชุมปิดการตรวจสอบ แต่ไม่ครบทุกเรื่อง/ครั้งที่ได้รับการตรวจสอบ</div>
                        </div>
                        <div class="rubric-card" id="t2-r3">
                            <span class="rubric-header-tag rubric-3">ระดับ 3</span>
                            <div class="rubric-desc">ผู้บริหารทุนหมุนเวียนเข้าร่วมประชุมปิดการตรวจสอบ ครบทุกเรื่อง/ครั้งที่ได้รับการตรวจสอบ</div>
                        </div>
                        <div class="rubric-card" id="t2-r4">
                            <span class="rubric-header-tag rubric-4">ระดับ 4</span>
                            <div class="rubric-desc">ผู้บริหารเข้าร่วมประชุมปิดตรวจครบทุกครั้ง และกำหนดแนวทางแก้ไขได้อย่างชัดเจน แต่ไม่ครบทุกข้อเสนอแนะ</div>
                        </div>
                        <div class="rubric-card active" id="t2-r5">
                            <span class="rubric-header-tag rubric-5">ระดับ 5 ★</span>
                            <div class="rubric-desc">ผู้บริหารเข้าร่วมประชุมปิดตรวจครบทุกครั้ง และ<b>กำหนดแนวทางแก้ไขการปฏิบัติงานตามข้อเสนอแนะได้อย่างชัดเจน และครบถ้วนทุกข้อเสนอแนะ</b></div>
                        </div>
                    </div>

                    <!-- Process Flow 3 Steps -->
                    <div class="process-flow-3">
                        <div class="flow-step-card completed" id="t2-s1">
                            <span class="step-pill-top">ประเด็นที่ 1 (การเข้าร่วมประชุม)</span>
                            <div class="step-title">ผู้บริหารเข้าร่วมครบทุกครั้ง</div>
                            <div class="step-desc" id="t2-s1-d" contenteditable="false">
                                ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียน พร้อมด้วยหัวหน้ากลุ่ม และเจ้าหน้าที่ผู้เกี่ยวข้อง ได้เข้าร่วมการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 เมื่อวันที่ <b>10 กันยายน 2569</b> ครบถ้วนทุกครั้ง
                            </div>
                        </div>
                        <div class="flow-step-card completed" id="t2-s2">
                            <span class="step-pill-top">ประเด็นที่ 2 (การกำหนดแนวทาง)</span>
                            <div class="step-title">กำหนดแนวทางแก้ไขชัดเจน</div>
                            <div class="step-desc" id="t2-s2-d" contenteditable="false">
                                ผู้ตรวจสอบภายในรายงานข้อตรวจพบ ข้อสังเกต และข้อเสนอแนะ โดยเงินทุนหมุนเวียนฯ ได้กำหนดแนวทางและดำเนินการปรับปรุงการปฏิบัติงานตามข้อเสนอแนะแล้วเสร็จอย่างชัดเจน ครบถ้วนทุกข้อเสนอแนะ
                            </div>
                        </div>
                        <div class="flow-step-card completed" id="t2-s3">
                            <span class="step-pill-top">ประเด็นที่ 3 (การรายงานผล)</span>
                            <div class="step-title">รายงานผลต่อผู้บริหาร & คกก.</div>
                            <div class="step-desc" id="t2-s3-d" contenteditable="false">
                                จัดทำรายงานผลการตรวจสอบรายงานการเงินเสนอต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ในคราวประชุมครั้งที่ 6/2569 เมื่อวันที่ 30 กันยายน 2569 ครบถ้วนสมบูรณ์
                            </div>
                        </div>
                    </div>

                    <!-- Evidence & Score Box -->
                    <div style="display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 14px; align-items: stretch;">
                        <div class="evidence-box">
                            <div class="evidence-title">📄 เอกสารและหลักฐานอ้างอิง:</div>
                            <ul class="evidence-list" id="t2-evidence">
                                <li><b>เอกสารหมายเลข 2:</b> รายงานการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 เมื่อวันที่ 10 กันยายน 2569</li>
                                <li><b>เอกสารหมายเลข 3:</b> รายงานผลการตรวจสอบการจัดทำรายงานการเงินของเงินทุนหมุนเวียนฯ โดยผู้ตรวจสอบภายใน</li>
                            </ul>
                            <div class="callout-box" id="t2-callout" style="margin-top: 6px;" contenteditable="false">
                                <b>สรุปผลการประเมิน:</b> ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียนเข้าร่วมประชุมปิดการตรวจสอบครบทุกครั้ง และกำหนดแนวทางแก้ไขตามข้อเสนอแนะได้ชัดเจนและครบถ้วนทุกข้อเสนอแนะ ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="justify-content: center;">
                            <div class="big-score-subtitle">ผลการดำเนินงานข้อที่ 2 (น้ำหนัก 15%)</div>
                            <div class="big-score-val" id="t2-sc-val" contenteditable="false">ระดับ 5.0000 คะแนน</div>
                            <div class="stars-row" id="t2-stars">★★★★★</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- VIEW 3: SUB-TOPIC 3: การปฏิบัติงานตามข้อเสนอแนะ (40%) -->
            <div class="topic-view" id="view3">
                <div class="content-card">
                    <div class="card-header-line">
                        <div class="card-title">⚡ 3. การปฏิบัติงานตามข้อเสนอแนะ (น้ำหนัก 40%) - การแก้ไขปรับปรุงและการไม่เกิดข้อตรวจพบผิดซ้ำ</div>
                        <div class="card-badge" id="t3-badge">น้ำหนัก 40% | ผลงานระดับ 5</div>
                    </div>

                    <!-- Rubric 5 Levels -->
                    <div class="rubric-grid-5">
                        <div class="rubric-card" id="t3-r1">
                            <span class="rubric-header-tag rubric-1">ระดับ 1</span>
                            <div class="rubric-desc">ปฏิบัติงานตามข้อเสนอแนะ แต่แก้ไขแล้วเสร็จช้ากว่าระยะเวลาที่กำหนด</div>
                        </div>
                        <div class="rubric-card" id="t3-r2">
                            <span class="rubric-header-tag rubric-2">ระดับ 2</span>
                            <div class="rubric-desc">ปฏิบัติตามข้อเสนอแนะตามระยะเวลาที่กำหนด แต่ไม่ครบถ้วนทุกข้อเสนอแนะ</div>
                        </div>
                        <div class="rubric-card" id="t3-r3">
                            <span class="rubric-header-tag rubric-3">ระดับ 3</span>
                            <div class="rubric-desc">ปฏิบัติตามข้อเสนอแนะตามเวลาที่กำหนด และรายงานผลการแก้ไขต่อที่ประชุมคณะกรรมการบริหารทุนหมุนเวียนเพื่อพิจารณา</div>
                        </div>
                        <div class="rubric-card" id="t3-r4">
                            <span class="rubric-header-tag rubric-4">ระดับ 4</span>
                            <div class="rubric-desc">ผลการตรวจสอบของทุนหมุนเวียนในรอบ 2 ปี ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</div>
                        </div>
                        <div class="rubric-card active" id="t3-r5">
                            <span class="rubric-header-tag rubric-5">ระดับ 5 ★</span>
                            <div class="rubric-desc"><b>ผลการตรวจสอบของทุนหมุนเวียนในรอบ 3 ปี ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</b></div>
                        </div>
                    </div>

                    <!-- Process Flow 3 Steps -->
                    <div class="process-flow-3">
                        <div class="flow-step-card completed" id="t3-s1">
                            <span class="step-pill-top">ด้านที่ 1 (การแก้ไขข้อตรวจพบ)</span>
                            <div class="step-title">แก้ไขตามเวลาที่กำหนด</div>
                            <div class="step-desc" id="t3-s1-d" contenteditable="false">
                                การตรวจสอบครั้งที่ 1 พบข้อสังเกตให้ตรวจปรับปรุงรายการบัญชี เงินทุนหมุนเวียนฯ ได้ตรวจปรับปรุงรายการบัญชีโดยเร็ว ณ วันที่ตรวจพบ พร้อมทั้งจัดทำรายละเอียดประกอบการปรับปรุงรายการบัญชีเรียบร้อยทันเวลา
                            </div>
                        </div>
                        <div class="flow-step-card completed" id="t3-s2">
                            <span class="step-pill-top">ด้านที่ 2 (การรายงานผลต่อ คกก.)</span>
                            <div class="step-title">รายงานการแก้ไขเรียบร้อย</div>
                            <div class="step-desc" id="t3-s2-d" contenteditable="false">
                                ผู้ตรวจสอบภายในได้บันทึกการดำเนินการแก้ไขไว้ในรายงานผล และรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 (30 ก.ย. 69) รับทราบเรียบร้อย
                            </div>
                        </div>
                        <div class="flow-step-card completed" id="t3-s3">
                            <span class="step-pill-top">ด้านที่ 3 (สถิติไม่ผิดซ้ำ 3 ปี)</span>
                            <div class="step-title">ไม่มีข้อตรวจพบผิดซ้ำในรอบ 3 ปี</div>
                            <div class="step-desc" id="t3-s3-d" contenteditable="false">
                                ผลการตรวจสอบภายในของเงินทุนหมุนเวียนฯ ในรอบ 3 ปีบัญชีที่ผ่านมา <b>ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</b> แสดงถึงประสิทธิภาพและความต่อเนื่องในการควบคุมและปรับปรุงการปฏิบัติงาน
                            </div>
                        </div>
                    </div>

                    <!-- Evidence & Score Box -->
                    <div style="display: grid; grid-template-columns: 1.3fr 0.7fr; gap: 14px; align-items: stretch;">
                        <div class="evidence-box">
                            <div class="evidence-title">📄 เอกสารและหลักฐานอ้างอิง:</div>
                            <ul class="evidence-list" id="t3-evidence">
                                <li><b>เอกสารหมายเลข 2:</b> รายงานการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 (10 กันยายน 2569)</li>
                                <li><b>เอกสารหมายเลข 3:</b> รายงานผลการตรวจสอบการจัดทำรายงานการเงินของเงินทุนหมุนเวียนฯ โดยผู้ตรวจสอบภายใน</li>
                                <li><b>เอกสารหมายเลข 4:</b> รายงานการประชุมคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 เมื่อวันที่ 30 กันยายน 2569</li>
                            </ul>
                            <div class="callout-box" id="t3-callout" style="margin-top: 6px;" contenteditable="false">
                                <b>สรุปผลการประเมิน:</b> มีการปฏิบัติตามข้อเสนอแนะของผู้ตรวจสอบภายในแล้วเสร็จตามกำหนด รายงานต่อคณะกรรมการบริหารฯ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน
                            </div>
                        </div>
                        <div class="big-score-box" style="justify-content: center;">
                            <div class="big-score-subtitle">ผลการดำเนินงานข้อที่ 3 (น้ำหนัก 40%)</div>
                            <div class="big-score-val" id="t3-sc-val" contenteditable="false">ระดับ 5.0000 คะแนน</div>
                            <div class="stars-row" id="t3-stars">★★★★★</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide Footer -->
        <div class="slide-footer">
            <div>สำนักงานคณะกรรมการข้าราชการครูและบุคลากรทางการศึกษา (ก.ค.ศ.) | สำนักบริหารเงินทุนหมุนเวียนเพื่อแก้ไขปัญหาหนี้สินข้าราชการครู</div>
            <div>คุณภาพการบริหาร เพื่อครู เพื่ออนาคตการศึกษาไทย</div>
        </div>
    </div>
</div>

<div class="toast" id="toastMessage">บันทึกข้อมูลเรียบร้อยแล้ว</div>

<script>
    // Quarter Defaults Data for KPI 4.2
    const quarterDefaults42 = {
        1: {
            ovBadge: 'อยู่ระหว่างดำเนินการ',
            ovBadgeStyle: 'background: #fff7ed; color: #c2410c; border-color: #ffedd5;',
            ovScoreVal: 'N/A (รอผลการตรวจสอบ)',
            ovStars: '⏳',
            ovSummaryDesc: 'ไตรมาสที่ 1 (ต.ค. - ธ.ค. 2568): เงินทุนหมุนเวียนฯ อยู่ระหว่างประสานงานกับหน่วยตรวจสอบภายในของสำนักงาน ก.ค.ศ. (หน่วยงานต้นสังกัด) เพื่อจัดเตรียมข้อมูลและรายงานการเงินตามกรอบแผนการตรวจสอบประจำปีบัญชี 2569',
            ovProgLabel: 'เตรียมการ',
            ovEvalLabel: 'N/A (รอผล)',
            r1Score: 'N/A', r1Weighted: '-',
            r2Score: 'N/A', r2Weighted: '-',
            r3Score: 'N/A', r3Weighted: '-',
            totalLevel: 'N/A', totalWeighted: 'N/A (รอผลตรวจสอบ)',

            // View 1
            t1ActiveRubric: 1,
            t1Badge: 'น้ำหนัก 45% | อยู่ระหว่างเตรียมการ (N/A)',
            t1S1Desc: '• มติ คกก.บริหารฯ ครั้งที่ 8/2565 แต่งตั้งผู้ตรวจสอบภายในสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>• มีกฎบัตรการตรวจสอบภายในเป็นกรอบการปฏิบัติงาน',
            t1S2Desc: '• อยู่ระหว่างจัดเตรียมรายงานการเงินและเอกสารประกอบ เพื่อเตรียมจัดส่งให้หน่วยตรวจสอบภายในตามแผนงาน',
            t1S3Desc: '• ยังไม่ถึงรอบการประชุมรายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ (กำหนดช่วงท้ายปีงบประมาณ)',
            t1Callout: '<b>สรุปผลการประเมิน (ไตรมาส 1):</b> อยู่ระหว่างเตรียมการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน ผลการดำเนินงานยังไม่ถึงรอบการประเมิน (N/A)',
            t1ScoreVal: 'N/A',
            t1Stars: '⏳',

            // View 2
            t2ActiveRubric: 1,
            t2Badge: 'น้ำหนัก 15% | อยู่ระหว่างรอการตรวจสอบ (N/A)',
            t2S1Desc: '• ผู้บริหารและเจ้าหน้าที่อยู่ระหว่างประสานงานกำหนดการตรวจสอบกับหน่วยตรวจสอบภายในต้นสังกัด',
            t2S2Desc: '• ยังไม่ถึงรอบการประชุมปิดการตรวจสอบรายงานการเงิน',
            t2S3Desc: '• ยังไม่มีการจัดทำรายงานผลการประชุมปิดตรวจเสนอคณะกรรมการบริหารฯ',
            t2Callout: '<b>สรุปผลการประเมิน (ไตรมาส 1):</b> อยู่ระหว่างรอบัญชีและการเข้าตรวจสอบของผู้ตรวจสอบภายใน (N/A)',
            t2ScoreVal: 'N/A',
            t2Stars: '⏳',

            // View 3
            t3ActiveRubric: 1,
            t3Badge: 'น้ำหนัก 40% | อยู่ระหว่างรอผลการตรวจสอบ (N/A)',
            t3S1Desc: '• อยู่ระหว่างรอรับข้อสังเกตและข้อเสนอแนะจากผู้ตรวจสอบภายในประจำปี 2569',
            t3S2Desc: '• เตรียมความพร้อมระบบบัญชีและการจัดทำรายละเอียดประกอบเพื่อรองรับการตรวจสอบ',
            t3S3Desc: '• สถิติย้อนหลังในรอบ 3 ปีที่ผ่านมาไม่มีประเด็นข้อตรวจพบผิดซ้ำ (รอการตรวจสอบรอบปี 2569)',
            t3Callout: '<b>สรุปผลการประเมิน (ไตรมาส 1):</b> อยู่ระหว่างรอรับรายงานผลการตรวจสอบและข้อเสนอแนะ (N/A)',
            t3ScoreVal: 'N/A',
            t3Stars: '⏳'
        },
        2: {
            ovBadge: 'อยู่ระหว่างดำเนินการ',
            ovBadgeStyle: 'background: #fff7ed; color: #c2410c; border-color: #ffedd5;',
            ovScoreVal: 'N/A (รอผลการตรวจสอบ)',
            ovStars: '⏳',
            ovSummaryDesc: 'ไตรมาสที่ 2 (ต.ค. 2568 - มี.ค. 2569): ทุนหมุนเวียนอยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายในของสำนักงาน ก.ค.ศ. ตามแผนการตรวจสอบประจำปีบัญชี 2569',
            ovProgLabel: 'จัดส่งรายงานการเงิน',
            ovEvalLabel: 'N/A (รอผล)',
            r1Score: 'N/A', r1Weighted: '-',
            r2Score: 'N/A', r2Weighted: '-',
            r3Score: 'N/A', r3Weighted: '-',
            totalLevel: 'N/A', totalWeighted: 'N/A (รอผลตรวจสอบ)',

            // View 1
            t1ActiveRubric: 1,
            t1Badge: 'น้ำหนัก 45% | อยู่ระหว่างส่งรายงานการเงิน (N/A)',
            t1S1Desc: '• มติ คกก.บริหารฯ ครั้งที่ 8/2565 แต่งตั้งผู้ตรวจสอบภายในสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>• มีกฎบัตรการตรวจสอบภายในเป็นกรอบการปฏิบัติงาน',
            t1S2Desc: '• เงินทุนหมุนเวียนฯ อยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายในเพื่อเข้าปฏิบัติงานตรวจสอบ',
            t1S3Desc: '• ยังไม่ถึงรอบการประชุมรายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ',
            t1Callout: '<b>สรุปผลการประเมิน (ไตรมาส 2):</b> ตามเอกสารทางการ ทุนหมุนเวียนอยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน (N/A)',
            t1ScoreVal: 'N/A',
            t1Stars: '⏳',

            // View 2
            t2ActiveRubric: 1,
            t2Badge: 'น้ำหนัก 15% | อยู่ระหว่างส่งรายงานการเงิน (N/A)',
            t2S1Desc: '• ประสานงานกับผู้ตรวจสอบภายในอย่างต่อเนื่องในการจัดส่งข้อมูลรายงานการเงิน',
            t2S2Desc: '• อยู่ระหว่างดำเนินการตรวจสอบรายงานการเงิน ยังไม่ถึงรอบการประชุมปิดการตรวจสอบ',
            t2S3Desc: '• ยังไม่มีรายงานผลเสนอคณะกรรมการบริหารฯ ในไตรมาสที่ 2',
            t2Callout: '<b>สรุปผลการประเมิน (ไตรมาส 2):</b> อยู่ระหว่างดำเนินการจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน ยังไม่มีการประชุมปิดการตรวจสอบ (N/A)',
            t2ScoreVal: 'N/A',
            t2Stars: '⏳',

            // View 3
            t3ActiveRubric: 1,
            t3Badge: 'น้ำหนัก 40% | อยู่ระหว่างส่งรายงานการเงิน (N/A)',
            t3S1Desc: '• อยู่ระหว่างส่งรายงานการเงิน ยังไม่มีข้อเสนอแนะจากการตรวจสอบรอบปีบัญชี 2569',
            t3S2Desc: '• กำกับติดตามการบันทึกบัญชีให้เป็นไปตามระเบียบอย่างเคร่งครัด',
            t3S3Desc: '• สถิติย้อนหลังในรอบ 3 ปีที่ผ่านมาไม่มีประเด็นข้อตรวจพบผิดซ้ำ',
            t3Callout: '<b>สรุปผลการประเมิน (ไตรมาส 2):</b> เงินทุนหมุนเวียนฯ อยู่ระหว่างจัดส่งรายงานการเงินให้หน่วยตรวจสอบภายใน (N/A)',
            t3ScoreVal: 'N/A',
            t3Stars: '⏳'
        },
        3: {
            ovBadge: 'อยู่ระหว่างการตรวจสอบ',
            ovBadgeStyle: 'background: #eff6ff; color: #1d4ed8; border-color: #dbeafe;',
            ovScoreVal: 'N/A (รอผลการตรวจสอบ)',
            ovStars: '⏳',
            ovSummaryDesc: 'ไตรมาสที่ 3 (ต.ค. 2568 - มิ.ย. 2569): หน่วยตรวจสอบภายในของสำนักงาน ก.ค.ศ. อยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ตามแผนงานประจำปีบัญชี 2569',
            ovProgLabel: 'อยู่ระหว่างตรวจสอบ',
            ovEvalLabel: 'N/A (รอผล)',
            r1Score: 'N/A', r1Weighted: '-',
            r2Score: 'N/A', r2Weighted: '-',
            r3Score: 'N/A', r3Weighted: '-',
            totalLevel: 'N/A', totalWeighted: 'N/A (รอผลตรวจสอบ)',

            // View 1
            t1ActiveRubric: 1,
            t1Badge: 'น้ำหนัก 45% | ผู้ตรวจอยู่ระหว่างตรวจสอบ (N/A)',
            t1S1Desc: '• มีคำสั่งแต่งตั้งและกฎบัตรการตรวจสอบภายในครบถ้วน',
            t1S2Desc: '• <b>ผู้ตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงิน</b>ของเงินทุนหมุนเวียนฯ (เม.ย. - ก.ค. 69)',
            t1S3Desc: '• รอการสรุปผลและรายงานต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ในช่วงไตรมาสที่ 4',
            t1Callout: '<b>สรุปผลการประเมิน (ไตรมาส 3):</b> ตามเอกสารทางการ หน่วยตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ (N/A)',
            t1ScoreVal: 'N/A',
            t1Stars: '⏳',

            // View 2
            t2ActiveRubric: 1,
            t2Badge: 'น้ำหนัก 15% | อยู่ระหว่างตรวจสอบรายงานการเงิน (N/A)',
            t2S1Desc: '• หน่วยตรวจสอบภายในอยู่ระหว่างตรวจสอบเอกสารและรายการทางการเงิน',
            t2S2Desc: '• มีกำหนดการจัดประชุมปิดการตรวจสอบในช่วงไตรมาสที่ 4 หลังการตรวจสอบรายงานการเงินแล้วเสร็จ',
            t2S3Desc: '• อยู่ระหว่างเตรียมข้อมูลสรุปสำหรับนำเสนอผู้บริหาร',
            t2Callout: '<b>สรุปผลการประเมิน (ไตรมาส 3):</b> หน่วยตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ยังไม่ถึงรอบการประชุมปิดตรวจ (N/A)',
            t2ScoreVal: 'N/A',
            t2Stars: '⏳',

            // View 3
            t3ActiveRubric: 1,
            t3Badge: 'น้ำหนัก 40% | อยู่ระหว่างตรวจสอบรายงานการเงิน (N/A)',
            t3S1Desc: '• เจ้าหน้าที่ให้ข้อมูลและร่วมประสานงานกับผู้ตรวจสอบภายในอย่างใกล้ชิดระหว่างการตรวจสอบ',
            t3S2Desc: '• เตรียมพร้อมแนวทางการปรับปรุงรายการบัญชีทันทีหากได้รับข้อสังเกตเบื้องต้น',
            t3S3Desc: '• สถิติย้อนหลังในรอบ 3 ปีที่ผ่านมาไม่มีประเด็นข้อตรวจพบผิดซ้ำ',
            t3Callout: '<b>สรุปผลการประเมิน (ไตรมาส 3):</b> หน่วยตรวจสอบภายในอยู่ระหว่างดำเนินการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ (N/A)',
            t3ScoreVal: 'N/A',
            t3Stars: '⏳'
        },
        4: {
            ovBadge: 'ระดับคะแนนสูงสุด',
            ovBadgeStyle: 'background: #eef7ed; color: #15803d; border-color: #bbf7d0;',
            ovScoreVal: 'ระดับ 5.0000 คะแนน',
            ovStars: '★★★★★',
            ovSummaryDesc: 'ได้รับการตรวจสอบจากผู้ตรวจสอบภายในต้นสังกัดครบถ้วนตามแผน 2 ครั้ง มีการประชุมปิดการตรวจสอบร่วมกันระหว่างผู้บริหารและผู้ตรวจสอบภายใน ปฏิบัติตามข้อสังเกตและข้อเสนอแนะครบถ้วนทุกข้อ โดย คกก.บริหารเงินทุนหมุนเวียนฯ ได้มอบนโยบายการปฏิบัติงานที่สอดคล้องกับรายงานผลการตรวจสอบ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี',
            ovProgLabel: 'ครบ 3 ประเด็น',
            ovEvalLabel: 'ระดับ 5 (เต็ม)',
            r1Score: '5.0000', r1Weighted: '2.2500',
            r2Score: '5.0000', r2Weighted: '0.7500',
            r3Score: '5.0000', r3Weighted: '2.0000',
            totalLevel: 'ระดับ 5', totalWeighted: '5.0000 คะแนน',

            // View 1
            t1ActiveRubric: 5,
            t1Badge: 'น้ำหนัก 45% | ผลงานระดับ 5',
            t1S1Desc: '• มติ คกก.บริหารฯ ครั้งที่ 8/2565 (28 ธ.ค. 65) แต่งตั้งผู้ตรวจสอบภายในของสำนักงาน ก.ค.ศ. เป็นผู้ตรวจของเงินทุนหมุนเวียนฯ<br>• มติ คกก.บริหารฯ ครั้งที่ 3/2567 (30 เม.ย. 67) เห็นชอบกฎบัตรการตรวจสอบภายใน และทบทวนสอบทานทุกปี',
            t1S2Desc: '• <b>ครั้งที่ 1 (รายงานการเงิน):</b> ดำเนินการ เม.ย. - ก.ค. 69 ประชุมปิดตรวจ 10 ก.ย. 69 และเสนอรายงานสำเร็จ<br>• <b>ครั้งที่ 2 (เงินนอกงบประมาณ):</b> ดำเนินการ ก.ย. 69 สรุปผลการตรวจสอบเรียบร้อยตามแผน',
            t1S3Desc: 'เสนอรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 เมื่อ <b>30 กันยายน 2569</b> โดยคณะกรรมการฯ ได้มอบนโยบายและข้อสังเกตในการปฏิบัติงานสอดคล้องกับรายงานผล',
            t1Callout: '<b>สรุปผลการประเมิน:</b> ทุนหมุนเวียนได้รับการตรวจสอบภายใน รายงานผลต่อคณะกรรมการบริหารเงินทุนหมุนเวียนฯ และคณะกรรมการฯ ได้มอบนโยบายการปฏิบัติงาน ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน',
            t1ScoreVal: 'ระดับ 5.0000 คะแนน',
            t1Stars: '★★★★★',

            // View 2
            t2ActiveRubric: 5,
            t2Badge: 'น้ำหนัก 15% | ผลงานระดับ 5',
            t2S1Desc: 'ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียน พร้อมด้วยหัวหน้ากลุ่ม และเจ้าหน้าที่ผู้เกี่ยวข้อง ได้เข้าร่วมการประชุมปิดการตรวจสอบรายงานการเงินของเงินทุนหมุนเวียนฯ ประจำปีงบประมาณ พ.ศ. 2569 เมื่อวันที่ <b>10 กันยายน 2569</b> ครบถ้วนทุกครั้ง',
            t2S2Desc: 'ผู้ตรวจสอบภายในรายงานข้อตรวจพบ ข้อสังเกต และข้อเสนอแนะ โดยเงินทุนหมุนเวียนฯ ได้กำหนดแนวทางและดำเนินการปรับปรุงการปฏิบัติงานตามข้อเสนอแนะแล้วเสร็จอย่างชัดเจน ครบถ้วนทุกข้อเสนอแนะ',
            t2S3Desc: 'จัดทำรายงานผลการตรวจสอบรายงานการเงินเสนอต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ในคราวประชุมครั้งที่ 6/2569 เมื่อวันที่ 30 กันยายน 2569 ครบถ้วนสมบูรณ์',
            t2Callout: '<b>สรุปผลการประเมิน:</b> ผู้อำนวยการสำนักบริหารเงินทุนหมุนเวียนเข้าร่วมประชุมปิดการตรวจสอบครบทุกครั้ง และกำหนดแนวทางแก้ไขตามข้อเสนอแนะได้ชัดเจนและครบถ้วนทุกข้อเสนอแนะ ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน',
            t2ScoreVal: 'ระดับ 5.0000 คะแนน',
            t2Stars: '★★★★★',

            // View 3
            t3ActiveRubric: 5,
            t3Badge: 'น้ำหนัก 40% | ผลงานระดับ 5',
            t3S1Desc: 'การตรวจสอบครั้งที่ 1 พบข้อสังเกตให้ตรวจปรับปรุงรายการบัญชี เงินทุนหมุนเวียนฯ ได้ตรวจปรับปรุงรายการบัญชีโดยเร็ว ณ วันที่ตรวจพบ พร้อมทั้งจัดทำรายละเอียดประกอบการปรับปรุงรายการบัญชีเรียบร้อยทันเวลา',
            t3S2Desc: 'ผู้ตรวจสอบภายในได้บันทึกการดำเนินการแก้ไขไว้ในรายงานผล และรายงานต่อเลขาธิการ ก.ค.ศ., ปลัดกระทรวงศึกษาธิการ และคณะกรรมการบริหารเงินทุนหมุนเวียนฯ ครั้งที่ 6/2569 (30 ก.ย. 69) รับทราบเรียบร้อย',
            t3S3Desc: 'ผลการตรวจสอบภายในของเงินทุนหมุนเวียนฯ ในรอบ 3 ปีบัญชีที่ผ่านมา <b>ไม่มีประเด็นข้อตรวจพบที่เป็นประเด็นผิดซ้ำ</b> แสดงถึงประสิทธิภาพและความต่อเนื่องในการควบคุมและปรับปรุงการปฏิบัติงาน',
            t3Callout: '<b>สรุปผลการประเมิน:</b> มีการปฏิบัติตามข้อเสนอแนะของผู้ตรวจสอบภายในแล้วเสร็จตามกำหนด รายงานต่อคณะกรรมการบริหารฯ และไม่มีประเด็นข้อตรวจพบผิดซ้ำในรอบ 3 ปี ผลการดำเนินงานเทียบเท่าระดับ 5.0000 คะแนน',
            t3ScoreVal: 'ระดับ 5.0000 คะแนน',
            t3Stars: '★★★★★'
        }
    };

    const STORAGE_KEY_PREFIX = 'kpi_official_42_v1_Q';
    let currentQuarter = 4;
    let currentTopicView = 0;
    let currentAppMode = 'preview';
    let currentEditingEl = null;

    function initPage() {
        applyQuarterDefault(currentQuarter);
        switchTopicView(0);
        setupEditableListeners();
    }

    function switchKPI(url) {
        if (url && url !== 'ตัวชี้วัดที่ 4.2.html') {
            window.location.href = url;
        }
    }

    function switchQuarter(quarterNum) {
        quarterNum = parseInt(quarterNum, 10);
        if (quarterNum < 1 || quarterNum > 4) quarterNum = 4;
        
        currentQuarter = quarterNum;
        document.getElementById('quarterSelect').value = currentQuarter;
        document.getElementById('activeQuarterBadge').textContent = `📁 ข้อมูลเฉพาะ: ไตรมาส ${currentQuarter}`;

        // In edit mode, check localStorage first. In preview mode, always apply authentic defaults.
        const storageKey = STORAGE_KEY_PREFIX + currentQuarter;
        const saved = localStorage.getItem(storageKey);
        if (currentAppMode === 'edit' && saved) {
            try {
                applyCapturedState(JSON.parse(saved));
            } catch(e) {
                applyQuarterDefault(currentQuarter);
            }
        } else {
            applyQuarterDefault(currentQuarter);
        }

        showToast(`สลับมาที่ "ไตรมาส ${currentQuarter}" เรียบร้อยแล้ว`);
    }

    function applyQuarterDefault(q) {
        const d = quarterDefaults42[q];
        if (!d) return;

        // View 0
        const ovBadge = document.getElementById('ov-badge');
        if (ovBadge) {
            ovBadge.textContent = d.ovBadge;
            ovBadge.setAttribute('style', d.ovBadgeStyle);
        }
        setElText('ov-sc-val', d.ovScoreVal);
        setElText('ov-stars', d.ovStars);
        setElText('ov-summary-desc', d.ovSummaryDesc);
        setElText('ov-prog-label', d.ovProgLabel);
        setElText('ov-eval-label', d.ovEvalLabel);
        setElText('ov-r1-score', d.r1Score);
        setElText('ov-r1-weighted', d.r1Weighted);
        setElText('ov-r2-score', d.r2Score);
        setElText('ov-r2-weighted', d.r2Weighted);
        setElText('ov-r3-score', d.r3Score);
        setElText('ov-r3-weighted', d.r3Weighted);
        setElText('ov-total-level', d.totalLevel);
        setElText('ov-total-weighted', d.totalWeighted);

        // View 1
        setElText('t1-badge', d.t1Badge);
        setElHtml('t1-s1-d', d.t1S1Desc);
        setElHtml('t1-s2-d', d.t1S2Desc);
        setElHtml('t1-s3-d', d.t1S3Desc);
        setElHtml('t1-callout', d.t1Callout);
        setElText('t1-sc-val', d.t1ScoreVal);
        setElText('t1-stars', d.t1Stars);
        highlightRubric(1, d.t1ActiveRubric);

        // View 2
        setElText('t2-badge', d.t2Badge);
        setElHtml('t2-s1-d', d.t2S1Desc);
        setElHtml('t2-s2-d', d.t2S2Desc);
        setElHtml('t2-s3-d', d.t2S3Desc);
        setElHtml('t2-callout', d.t2Callout);
        setElText('t2-sc-val', d.t2ScoreVal);
        setElText('t2-stars', d.t2Stars);
        highlightRubric(2, d.t2ActiveRubric);

        // View 3
        setElText('t3-badge', d.t3Badge);
        setElHtml('t3-s1-d', d.t3S1Desc);
        setElHtml('t3-s2-d', d.t3S2Desc);
        setElHtml('t3-s3-d', d.t3S3Desc);
        setElHtml('t3-callout', d.t3Callout);
        setElText('t3-sc-val', d.t3ScoreVal);
        setElText('t3-stars', d.t3Stars);
        highlightRubric(3, d.t3ActiveRubric);
    }

    function highlightRubric(topicNum, level) {
        for (let l = 1; l <= 5; l++) {
            const card = document.getElementById(`t${topicNum}-r${l}`);
            if (card) {
                if (l === level) {
                    card.classList.add('active');
                } else {
                    card.classList.remove('active');
                }
            }
        }
    }

    function setElText(id, text) {
        const el = document.getElementById(id);
        if (el) el.textContent = text;
    }

    function setElHtml(id, html) {
        const el = document.getElementById(id);
        if (el) el.innerHTML = html;
    }

    function switchTopicView(viewIdx) {
        viewIdx = parseInt(viewIdx, 10);
        if (viewIdx < 0 || viewIdx > 3) viewIdx = 0;
        currentTopicView = viewIdx;

        // Update tabs
        for (let i = 0; i <= 3; i++) {
            const tab = document.getElementById(`tab${i}`);
            if (tab) {
                if (i === viewIdx) tab.classList.add('active');
                else tab.classList.remove('active');
            }
            const view = document.getElementById(`view${i}`);
            if (view) {
                if (i === viewIdx) view.classList.add('active');
                else view.classList.remove('active');
            }
        }

        // Subtitle dynamic banner
        const subTitle = document.getElementById('banner-sub-title');
        if (subTitle) {
            if (viewIdx === 0) {
                subTitle.textContent = "กรณีที่ 3 ทุนหมุนเวียนที่ใช้หน่วยงานตรวจสอบภายในจากหน่วยงานต้นสังกัด พิจารณาผลการดำเนินงาน 3 ประเด็นย่อย";
            } else if (viewIdx === 1) {
                subTitle.textContent = "ข้อ 1. การปฏิบัติงานตรวจสอบภายใน (น้ำหนัก 45%) - การตรวจสอบและรายงานผลต่อคณะกรรมการบริหารฯ";
            } else if (viewIdx === 2) {
                subTitle.textContent = "ข้อ 2. การประชุมปิดการตรวจสอบ (น้ำหนัก 15%) - การมีส่วนร่วมของผู้บริหารและกำหนดแนวทางแก้ไข";
            } else if (viewIdx === 3) {
                subTitle.textContent = "ข้อ 3. การปฏิบัติงานตามข้อเสนอแนะ (น้ำหนัก 40%) - การแก้ไขปรับปรุงและการไม่เกิดข้อตรวจพบผิดซ้ำในรอบ 3 ปี";
            }
        }
    }

    function setMode(mode) {
        currentAppMode = mode;
        const btnPrev = document.getElementById('btnModePreview');
        const btnEdit = document.getElementById('btnModeEdit');
        const formatBar = document.getElementById('formatBar');

        if (mode === 'edit') {
            btnEdit.classList.add('active');
            btnPrev.classList.remove('active');
            formatBar.style.display = 'flex';
            setEditableAll(true);
            showToast("เข้าสู่ 'โหมดแก้ไขข้อความ' สามารถคลิกเพื่อพิมพ์แก้ไขได้");
        } else {
            btnPrev.classList.add('active');
            btnEdit.classList.remove('active');
            formatBar.style.display = 'none';
            setEditableAll(false);
            showToast("เข้าสู่ 'โหมดนำเสนอ'");
        }
    }

    function setEditableAll(isEditable) {
        const editables = document.querySelectorAll('[contenteditable]');
        editables.forEach(el => {
            el.setAttribute('contenteditable', isEditable ? 'true' : 'false');
            if (isEditable) {
                el.style.outline = '1px dashed #60a5fa';
            } else {
                el.style.outline = 'none';
            }
        });
    }

    function setupEditableListeners() {
        document.addEventListener('focusin', function(e) {
            if (currentAppMode === 'edit' && e.target.getAttribute('contenteditable') === 'true') {
                currentEditingEl = e.target;
                const label = document.getElementById('activeTargetLabel');
                if (label) {
                    label.textContent = `📌 กำลังแก้ไข: ${e.target.id || e.target.tagName}`;
                }
            }
        });
    }

    function formatDoc(command, value = null) {
        if (currentAppMode !== 'edit') {
            showToast("กรุณาเปิด 'โหมดแก้ไขข้อความ' ก่อนจัดรูปแบบ");
            return;
        }
        document.execCommand(command, false, value);
    }

    function changeFontSize(diff) {
        if (!currentEditingEl) return;
        const style = window.getComputedStyle(currentEditingEl);
        let curr = parseFloat(style.fontSize);
        curr += diff;
        if (curr < 10) curr = 10;
        if (curr > 48) curr = 48;
        currentEditingEl.style.fontSize = curr + 'px';
    }

    function saveToStorage() {
        if (currentAppMode !== 'edit') {
            showToast("บันทึกสำเร็จ (ระบบพร้อมนำเสนอ)");
            return;
        }
        const state = captureCurrentState();
        const storageKey = STORAGE_KEY_PREFIX + currentQuarter;
        localStorage.setItem(storageKey, JSON.stringify(state));
        showToast(`บันทึกข้อมูลไตรมาส ${currentQuarter} ลงเบราว์เซอร์เรียบร้อยแล้ว`);
    }

    function captureCurrentState() {
        const state = {};
        const editables = document.querySelectorAll('[contenteditable]');
        editables.forEach(el => {
            if (el.id) {
                state[el.id] = el.innerHTML;
            }
        });
        return state;
    }

    function applyCapturedState(state) {
        if (!state) return;
        Object.keys(state).forEach(id => {
            const el = document.getElementById(id);
            if (el) el.innerHTML = state[id];
        });
    }

    async function copySlideImage() {
        showToast("กำลังประมวลผลคัดลอกภาพ...");
        const target = document.getElementById('slideCaptureArea');
        try {
            const canvas = await html2canvas(target, { scale: 2, useCORS: true });
            canvas.toBlob(async blob => {
                try {
                    await navigator.clipboard.write([
                        new ClipboardItem({ 'image/png': blob })
                    ]);
                    showToast("คัดลอกภาพสไลด์ลง Clipboard เรียบร้อยแล้ว!");
                } catch(err) {
                    exportSlidePNG();
                }
            });
        } catch(e) {
            alert("ไม่สามารถคัดลอกภาพได้ กรุณาใช้ปุ่ม ส่งออกภาพ (PNG)");
        }
    }

    async function exportSlidePNG() {
        showToast("กำลังสร้างไฟล์ PNG...");
        const target = document.getElementById('slideCaptureArea');
        try {
            const canvas = await html2canvas(target, { scale: 2, useCORS: true });
            const link = document.createElement('a');
            link.download = `KPI_4.2_Internal_Audit_Q${currentQuarter}.png`;
            link.href = canvas.toDataURL('image/png');
            link.click();
            showToast("ดาวน์โหลดภาพ PNG เรียบร้อยแล้ว!");
        } catch(e) {
            alert("เกิดข้อผิดพลาดในการส่งออกภาพ PNG");
        }
    }

    function exportSlidePDF() {
        window.print();
    }

    function toggleFullScreen() {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(err => {
                alert(`Error attempting to enable full-screen mode: ${err.message}`);
            });
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }
    }

    function showToast(msg) {
        const t = document.getElementById('toastMessage');
        if (!t) return;
        t.textContent = msg;
        t.style.display = 'block';
        clearTimeout(t.timer);
        t.timer = setTimeout(() => {
            t.style.display = 'none';
        }, 2500);
    }

    window.onload = initPage;
</script>
</body>
</html>
"""

output_path = "ตัวชี้วัดที่ 4.2.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"SUCCESS: Created {output_path} ({len(html_content)} bytes)")
