# -*- coding: utf-8 -*-
import os, sys

def generate_kpi61():
    print("Generating KPI 6.1 HTML...")
    
    html_content = '''<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ตัวชี้วัดที่ 6.1 การเบิกจ่ายเงินตามแผนการเบิกจ่ายที่ได้รับอนุมัติ (ร้อยละ 5)</title>
    
    <!-- Google Fonts: Sarabun & Prompt -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800&family=Sarabun:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- External Libraries: html2canvas & jsPDF for Image and PDF Export -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

    <style>
        :root {
            --primary-navy: #002b49;
            --secondary-blue: #004b87;
            --accent-cyan: #0284c7;
            --accent-gold: #d97706;
            --accent-yellow: #f59e0b;
            --bg-canvas: #f8fafc;
            --card-bg: #ffffff;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --border-color: #e2e8f0;
            --success-green: #16a34a;
            --danger-red: #dc2626;
            --shadow-subtle: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            --shadow-card: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.07);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        body {
            background-color: var(--bg-canvas);
            color: var(--text-dark);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 16px;
        }

        /* Top Action Bar / Controls */
        .dashboard-control-bar {
            width: 100%;
            max-width: 1440px;
            background: #ffffff;
            border-radius: 12px;
            padding: 12px 20px;
            margin-bottom: 16px;
            box-shadow: var(--shadow-subtle);
            border: 1px solid var(--border-color);
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }

        .control-group-left, .control-group-right {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .control-label {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .select-input {
            padding: 6px 12px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background-color: #ffffff;
            color: var(--text-dark);
            font-size: 13.5px;
            font-weight: 500;
            cursor: pointer;
            outline: none;
            transition: all 0.2s ease;
        }

        .select-input:hover, .select-input:focus {
            border-color: var(--secondary-blue);
            box-shadow: 0 0 0 3px rgba(0, 75, 135, 0.1);
        }

        .btn-action {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 7px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            border: 1px solid transparent;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            user-select: none;
        }

        .btn-action:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }

        .btn-action:active {
            transform: translateY(0);
        }

        .btn-primary { background: #004b87; color: #ffffff; }
        .btn-primary:hover { background: #003865; }
        .btn-secondary { background: #ffffff; color: var(--text-muted); border-color: var(--border-color); }
        .btn-secondary:hover { background: #f8fafc; color: var(--text-dark); }
        .btn-accent { background: #0284c7; color: #ffffff; }
        .btn-accent:hover { background: #0369a1; }
        .btn-success { background: #16a34a; color: #ffffff; }
        .btn-success:hover { background: #15803d; }
        .btn-warning { background: #d97706; color: #ffffff; }
        .btn-warning:hover { background: #b45309; }

        /* Mode Switcher Pills */
        .mode-toggle-group {
            display: inline-flex;
            background: #f1f5f9;
            padding: 3px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        .btn-mode {
            padding: 5px 12px;
            font-size: 12.5px;
            font-weight: 600;
            border-radius: 6px;
            border: none;
            background: transparent;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn-mode.active {
            background: #004b87;
            color: #ffffff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        /* Format Toolbar (Visible in Edit Mode) */
        .format-toolbar {
            display: none;
            width: 100%;
            max-width: 1440px;
            background: #fffbeb;
            border: 1px dashed #f59e0b;
            border-radius: 8px;
            padding: 8px 16px;
            margin-bottom: 12px;
            align-items: center;
            gap: 12px;
            font-size: 13px;
        }

        .format-toolbar.show {
            display: flex;
        }

        /* Subtopics Navigation Tabs */
        .subtopic-nav-container {
            width: 100%;
            max-width: 1440px;
            background: #ffffff;
            border-radius: 12px;
            padding: 10px 16px;
            margin-bottom: 16px;
            box-shadow: var(--shadow-subtle);
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            gap: 10px;
            overflow-x: auto;
        }

        .subtopic-nav-title {
            font-size: 13px;
            font-weight: 700;
            color: var(--text-dark);
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 6px;
            margin-right: 6px;
        }

        .subtopic-tab {
            padding: 7px 16px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
            background: #f8fafc;
            border: 1px solid var(--border-color);
            cursor: pointer;
            white-space: nowrap;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .subtopic-tab:hover {
            color: var(--secondary-blue);
            background: #eff6ff;
            border-color: #bfdbfe;
        }

        .subtopic-tab.active {
            color: #ffffff;
            background: #004b87;
            border-color: #004b87;
            box-shadow: 0 2px 4px rgba(0, 75, 135, 0.2);
        }

        /* Master Presentation Canvas (16:9 Responsive) */
        .presentation-canvas {
            width: 100%;
            max-width: 1440px;
            background: #ffffff;
            border-radius: 16px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-color);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        /* Header Banner */
        .header-banner {
            background: linear-gradient(135deg, #002b49 0%, #004b87 60%, #0284c7 100%);
            color: #ffffff;
            padding: 20px 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
        }

        .banner-left {
            display: flex;
            align-items: center;
            gap: 18px;
        }

        .banner-icon {
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            font-size: 24px;
        }

        .banner-title-area h1 {
            font-family: 'Prompt', sans-serif;
            font-size: 21px;
            font-weight: 700;
            line-height: 1.3;
            letter-spacing: -0.3px;
        }

        .banner-title-area p {
            font-size: 13.5px;
            color: #e0f2fe;
            margin-top: 4px;
            font-weight: 400;
        }

        .banner-right {
            text-align: right;
            font-size: 12.5px;
            color: #cbd5e1;
            line-height: 1.4;
        }

        .banner-right .motto {
            font-weight: 600;
            color: #ffffff;
            font-size: 13px;
        }

        /* KPI Meta Strip */
        .kpi-meta-strip {
            background: #f8fafc;
            border-bottom: 1px solid var(--border-color);
            padding: 10px 28px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            gap: 12px;
        }

        .meta-badges-left {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            align-items: center;
        }

        .meta-badge {
            background: #ffffff;
            border: 1px solid #cbd5e1;
            padding: 4px 10px;
            border-radius: 6px;
            color: #334155;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .meta-badge strong {
            color: var(--secondary-blue);
        }

        /* 5-Level Rubric Strip */
        .rubric-strip {
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .rubric-pill {
            font-size: 11px;
            padding: 3px 8px;
            border-radius: 4px;
            background: #e2e8f0;
            color: #475569;
            font-weight: 600;
            border: 1px solid #cbd5e1;
            text-align: center;
        }

        .rubric-pill.active {
            background: #d97706;
            color: #ffffff;
            border-color: #b45309;
            box-shadow: 0 1px 3px rgba(217, 119, 6, 0.3);
        }

        /* Content Area */
        .content-container {
            padding: 24px 28px;
            min-height: 520px;
            background: #f8fafc;
        }

        .content-view {
            display: none;
            animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .content-view.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* View 0: Overview Dashboard Grid */
        .overview-grid {
            display: grid;
            grid-template-columns: 1.45fr 1fr;
            gap: 20px;
        }

        .glass-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 20px;
            box-shadow: var(--shadow-subtle);
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .card-header-styled {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 12px;
        }

        .card-header-styled h2 {
            font-family: 'Prompt', sans-serif;
            font-size: 16.5px;
            font-weight: 700;
            color: #004b87;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Master Summary Table */
        .summary-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
            font-size: 13px;
        }

        .summary-table th {
            background: #004b87;
            color: #ffffff;
            padding: 10px 12px;
            font-weight: 600;
            text-align: center;
        }

        .summary-table td {
            padding: 12px 14px;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: middle;
        }

        .summary-table tr:last-child td {
            border-bottom: none;
        }

        .summary-table tr:nth-child(even) td {
            background-color: #f8fafc;
        }

        .summary-table .table-total-row td {
            background-color: #eff6ff;
            font-weight: 700;
            border-top: 2px solid #004b87;
        }

        /* Hero Score Big Card */
        .hero-score-box {
            background: linear-gradient(135deg, #002b49 0%, #004b87 100%);
            color: #ffffff;
            border-radius: 12px;
            padding: 22px;
            text-align: center;
            position: relative;
            box-shadow: var(--shadow-subtle);
        }

        .hero-score-label {
            font-size: 13px;
            color: #93c5fd;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 600;
        }

        .hero-score-val {
            font-family: 'Prompt', sans-serif;
            font-size: 42px;
            font-weight: 800;
            color: #ffcc00;
            margin: 6px 0;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }

        .hero-stars {
            color: #facc15;
            font-size: 22px;
            letter-spacing: 3px;
        }

        /* Metric Mini Cards */
        .metric-cards-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }

        .mini-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px;
            text-align: center;
            transition: all 0.2s ease;
        }

        .mini-card-title {
            font-size: 12px;
            color: var(--text-muted);
            font-weight: 600;
            margin-bottom: 4px;
        }

        .mini-card-val {
            font-family: 'Prompt', sans-serif;
            font-size: 18px;
            font-weight: 700;
            color: #004b87;
        }

        /* Highlight Pills */
        .pill-badge {
            display: inline-flex;
            align-items: center;
            padding: 3px 10px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 600;
        }

        .pill-badge.highlight {
            background: #e0f2fe;
            color: #0369a1;
        }

        .pill-badge.success {
            background: #dcfce7;
            color: #15803d;
        }

        .pill-badge.warning {
            background: #fef3c7;
            color: #b45309;
        }

        /* Callout Boxes */
        .callout-box {
            background: #f8fafc;
            border-left: 4px solid #004b87;
            padding: 12px 16px;
            border-radius: 0 8px 8px 0;
            font-size: 13px;
            line-height: 1.5;
        }

        .callout-box.callout-info {
            background: #f0f9ff;
            border-left-color: #0284c7;
        }

        .callout-box.callout-success {
            background: #f0fdf4;
            border-left-color: #16a34a;
        }

        .callout-box.callout-warning {
            background: #fffbeb;
            border-left-color: #d97706;
        }

        /* Sub-Views (Topics 1 and 2) Layout */
        .subview-container {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .rubric-grid-5 {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 8px;
            margin: 12px 0;
        }

        .rubric-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 10px 8px;
            font-size: 11.5px;
            line-height: 1.4;
            text-align: center;
        }

        .rubric-card-header {
            font-weight: 700;
            color: #004b87;
            margin-bottom: 4px;
            font-size: 12px;
        }

        .rubric-card.active {
            background: #ffffff;
            border: 2px solid #d97706;
            box-shadow: 0 4px 6px -1px rgba(217, 119, 6, 0.15);
        }

        .rubric-card.active .rubric-card-header {
            color: #d97706;
        }

        .timeline-steps {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 14px 0;
        }

        .step-box {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px;
            position: relative;
            box-shadow: var(--shadow-subtle);
        }

        .step-box.primary-step {
            border-top: 3px solid #004b87;
        }

        .step-number {
            font-size: 11px;
            font-weight: 700;
            color: #004b87;
            text-transform: uppercase;
        }

        .step-title {
            font-size: 13.5px;
            font-weight: 700;
            color: var(--text-dark);
            margin: 4px 0;
        }

        .step-desc {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.4;
        }

        /* Footer */
        .dashboard-footer {
            padding: 12px 28px;
            background: #ffffff;
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            color: var(--text-muted);
        }

        /* Toast notification */
        #toast {
            visibility: hidden;
            min-width: 280px;
            background-color: #0f172a;
            color: #fff;
            text-align: center;
            border-radius: 8px;
            padding: 12px 20px;
            position: fixed;
            z-index: 1000;
            right: 30px;
            bottom: 30px;
            font-size: 13.5px;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);
            opacity: 0;
            transition: opacity 0.3s, bottom 0.3s;
        }

        #toast.show {
            visibility: visible;
            opacity: 1;
            bottom: 40px;
        }

        /* Print / PDF Mode */
        @media print {
            body { padding: 0; background: #ffffff; }
            .dashboard-control-bar, .subtopic-nav-container, .format-toolbar { display: none !important; }
            .presentation-canvas { box-shadow: none; border: none; max-width: 100%; width: 100%; }
            .content-view { display: block !important; page-break-after: always; }
        }
    </style>
</head>
<body>

    <!-- Top Action / Control Bar -->
    <div class="dashboard-control-bar">
        <div class="control-group-left">
            <span class="control-label">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                ตัวชี้วัด:
            </span>
            <select id="select-kpi-page" class="select-input" onchange="navigateToKPI(this.value)" style="font-weight: 600; color: #004b87; background: #eff6ff;">
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
                <option value="5.2">5.2 การบริหารทรัพยากรบุคคล</option>
                <option value="6.1" selected>6.1 การเบิกจ่ายเงินตามแผนฯ (ปัจจุบัน)</option>
            </select>

            <span class="control-label" style="margin-left: 8px;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                รายงานถึง:
            </span>
            <select id="quarter-focus" class="select-input" onchange="switchQuarter(this.value)">
                <option value="1">ไตรมาส 1 (ต.ค. - ธ.ค.)</option>
                <option value="2">ไตรมาส 2 (ต.ค. - มี.ค.)</option>
                <option value="3">ไตรมาส 3 (ต.ค. - มิ.ย.)</option>
                <option value="4" selected>ไตรมาส 4 (ครบปี ต.ค. - ก.ย.)</option>
            </select>

            <span class="pill-badge highlight" id="quarter-badge" style="font-size: 12px; margin-left: 4px;">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                ไตรมาส 4
            </span>

            <span class="control-label" style="margin-left: 8px;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                ปี:
            </span>
            <select id="select-year" class="select-input" onchange="changeFiscalYear(this.value)">
                <option value="2568">ปี 2568</option>
                <option value="2569" selected>ปี 2569</option>
                <option value="2570">ปี 2570</option>
            </select>
        </div>

        <div class="control-group-right">
            <!-- Mode Toggle -->
            <div class="mode-toggle-group">
                <button class="btn-mode active" id="btn-mode-preview" onclick="setAppMode('preview')">👁️ โหมดนำเสนอ (Preview)</button>
                <button class="btn-mode" id="btn-mode-edit" onclick="setAppMode('edit')">✏️ โหมดแก้ไขข้อความ (Edit)</button>
            </div>

            <!-- Export Buttons -->
            <button class="btn-action btn-secondary" onclick="saveCustomData()">💾 บันทึก</button>
            <button class="btn-action btn-secondary" onclick="copyDashboardToClipboard()">📋 คัดลอกภาพ</button>
            <button class="btn-action btn-primary" onclick="exportDashboardPNG()">🖼️ ส่งออกภาพ (PNG)</button>
            <button class="btn-action btn-warning" onclick="exportDashboardPDF()">📄 ส่งออก PDF (เต็มแผ่น)</button>
            <button class="btn-action btn-success" onclick="window.print()">🖨️ พิมพ์ (Print)</button>
            <button class="btn-action btn-secondary" onclick="toggleFullscreen()">🔲 เต็มจอ</button>
        </div>
    </div>

    <!-- Format Toolbar for Text Editing -->
    <div class="format-toolbar" id="format-toolbar">
        <span style="font-weight: 700; color: #b45309;">เครื่องมือจัดรูปแบบข้อความ:</span>
        <button class="btn-action btn-secondary" style="padding: 4px 10px;" onclick="document.execCommand('bold', false, null)">หนา</button>
        <button class="btn-action btn-secondary" style="padding: 4px 10px;" onclick="document.execCommand('italic', false, null)">เอียง</button>
        <button class="btn-action btn-secondary" style="padding: 4px 10px;" onclick="document.execCommand('underline', false, null)">ขีดเส้นใต้</button>
        <span style="color: #64748b; font-size: 12px;">| คลิกที่ข้อความในกล่องด้านล่างเพื่อแก้ไขได้ทันที</span>
    </div>

    <!-- Subtopics Navigation Filter (Horizontal Tabs) -->
    <div class="subtopic-nav-container">
        <span class="subtopic-nav-title">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
            ตัวกรองหัวข้อ (Sub-topics):
        </span>
        <button class="subtopic-tab active" id="tab-v0" onclick="switchTopicView(0)">
            📊 ภาพรวม 2 ประเด็น <span class="pill-badge" style="background: rgba(0,0,0,0.15); font-size: 11px;">100%</span>
        </button>
        <button class="subtopic-tab" id="tab-v1" onclick="switchTopicView(1)">
            1. การเบิกจ่ายงบลงทุน <span class="pill-badge" style="background: rgba(0,0,0,0.08); font-size: 11px;">50% (2.5%)</span>
        </button>
        <button class="subtopic-tab" id="tab-v2" onclick="switchTopicView(2)">
            2. การเบิกจ่ายภาพรวม <span class="pill-badge" style="background: rgba(0,0,0,0.08); font-size: 11px;">50% (2.5%)</span>
        </button>
    </div>

    <!-- Master Executive Infographic Presentation (16:9 Aspect Ratio) -->
    <div class="presentation-canvas" id="presentation-canvas">

        <!-- Top Header Banner -->
        <div class="header-banner">
            <div class="banner-left">
                <div class="banner-icon">💰</div>
                <div class="banner-title-area">
                    <h1>ด้านที่ 6 การดำเนินงานตามนโยบายรัฐ/กระทรวงการคลัง | ตัวชี้วัดที่ 6.1 การเบิกจ่ายเงินตามแผนการเบิกจ่ายที่ได้รับอนุมัติ</h1>
                    <p>พิจารณาจากผลการเบิกจ่าย 2 ประเด็นย่อย (งบลงทุน 2.5% และงบประมาณภาพรวม 2.5% รวมน้ำหนักร้อยละ 5)</p>
                </div>
            </div>
            <div class="banner-right">
                <div class="motto">บริหารงบประมาณอย่างคุ้มค่า โปร่งใส และรวดเร็ว</div>
                <div>สอดคล้องกับมาตรการเร่งรัดการเบิกจ่ายงบประมาณและการใช้จ่ายภาครัฐ</div>
            </div>
        </div>

        <!-- KPI Meta & 5-Level Rubric Strip -->
        <div class="kpi-meta-strip">
            <div class="meta-badges-left">
                <span class="meta-badge">📌 <strong>ตัวชี้วัด:</strong> 6.1 การเบิกจ่ายเงินตามแผนฯ</span>
                <span class="meta-badge">🎯 <strong>หน่วยวัด:</strong> ระดับคะแนน (1 - 5)</span>
                <span class="meta-badge">⚖️ <strong>ค่าน้ำหนัก:</strong> ร้อยละ 5 (5%)</span>
                <span class="meta-badge">🏷️ <strong>ค่าเกณฑ์วัด:</strong> เกณฑ์ 5 ระดับ (2 ประเด็นย่อย)</span>
            </div>
            <div class="rubric-strip">
                <span style="font-weight: 700; color: #475569; font-size: 11.5px; margin-right: 4px;">เกณฑ์:</span>
                <div class="rubric-pill">ระดับ 1<br><span style="font-size: 9.5px;">&lt; มติ 12%</span></div>
                <div class="rubric-pill">ระดับ 2<br><span style="font-size: 9.5px;">&lt; มติ 9%</span></div>
                <div class="rubric-pill">ระดับ 3<br><span style="font-size: 9.5px;">&lt; มติ 6%</span></div>
                <div class="rubric-pill active">ระดับ 4<br><span style="font-size: 9.5px;">&lt; มติ 3%</span></div>
                <div class="rubric-pill">ระดับ 5<br><span style="font-size: 9.5px;">ตามมติ ครม.</span></div>
            </div>
        </div>

        <!-- Main Body Container -->
        <div class="content-container">

            <!-- ================= VIEW 0: ภาพรวม 2 ประเด็นย่อย ================= -->
            <div class="content-view active" id="view-topic-0">
                <div class="overview-grid">
                    <!-- Left Column: Master Breakdown Table -->
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>📊 ผลการดำเนินงานรวม 2 ประเด็นย่อย (ตัวชี้วัดที่ 6.1)</h2>
                            <span class="pill-badge highlight" style="font-size: 12px;">น้ำหนักรวม 100% (น้ำหนักในมิติ 5%)</span>
                        </div>

                        <div style="overflow-x: auto;">
                            <table class="summary-table">
                                <thead>
                                    <tr>
                                        <th style="width: 10%;">ข้อ</th>
                                        <th style="text-align: left; width: 44%;">ประเด็นย่อยที่ใช้พิจารณา</th>
                                        <th style="width: 14%;">น้ำหนัก (%)</th>
                                        <th style="width: 16%;">ระดับคะแนน</th>
                                        <th style="width: 16%;">คะแนนถ่วงน้ำหนัก</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td style="text-align: center; font-weight: 700; color: #004b87;">1</td>
                                        <td id="tbl-topic-1-text"><strong>ร้อยละการเบิกจ่ายงบลงทุน</strong> เทียบกับแผนฯ (82,000 / 88,000 บาท)</td>
                                        <td style="text-align: center; font-weight: 600;">50% (2.5%)</td>
                                        <td style="text-align: center; font-weight: 700; color: #d97706;" id="tbl-score-1">4 (93.1818)</td>
                                        <td style="text-align: right; font-weight: 700;" id="tbl-wscore-1">2.0000</td>
                                    </tr>
                                    <tr>
                                        <td style="text-align: center; font-weight: 700; color: #004b87;">2</td>
                                        <td id="tbl-topic-2-text"><strong>ร้อยละการเบิกจ่ายภาพรวม</strong> เทียบกับแผนฯ (272.81 / 279.20 ล้านบาท)</td>
                                        <td style="text-align: center; font-weight: 600;">50% (2.5%)</td>
                                        <td style="text-align: center; font-weight: 700; color: #d97706;" id="tbl-score-2">4 (97.7123)</td>
                                        <td style="text-align: right; font-weight: 700;" id="tbl-wscore-2">2.0000</td>
                                    </tr>
                                    <tr class="table-total-row">
                                        <td colspan="2" style="text-align: center; font-weight: 700;">รวมผลการประเมินถ่วงน้ำหนักทั้งหมด</td>
                                        <td style="text-align: center;">100% (5%)</td>
                                        <td style="text-align: center; color: #d97706;" id="tbl-total-level">ระดับ 4.0</td>
                                        <td style="text-align: right; color: #004b87;" id="tbl-total-wscore">4.0000 คะแนน</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- Summary Connection Callout -->
                        <div class="callout-box callout-info" id="tbl-overview-callout" style="font-size: 12.5px;">
                            💡 <strong>สรุปความเชื่อมโยง:</strong> ผลการเบิกจ่ายงบประมาณของเงินทุนหมุนเวียนฯ ประจำปีบัญชี 2569 บรรลุผลงาน <strong>ระดับ 4.0000 คะแนน</strong> ทั้งสองประเด็น โดยงบลงทุนเบิกจ่ายได้ <strong>ร้อยละ 93.1818</strong> (เบิกจ่าย 82,000 จาก 88,000 บาท สูงกว่าเป้าหมาย ครม. ร้อยละ 75) และการเบิกจ่ายภาพรวมเบิกจ่ายได้ <strong>ร้อยละ 97.7123</strong> (เบิกจ่าย 272,808,720.73 จาก 279,196,000 บาท สูงกว่าเป้าหมาย ครม. ร้อยละ 93) โดยมีเงินให้กู้ยืมแก่ครูและบุคลากรทางการศึกษาเบิกจ่ายจริงถึง 249,788,331.58 บาท (619 ราย)
                        </div>
                    </div>

                    <!-- Right Column: Hero Score Card & Key Highlights -->
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>🏆 สรุปคะแนนผลการประเมินภาพรวม</h2>
                            <span class="pill-badge" id="score-status-badge" style="background: #fef3c7; color: #92400e; font-weight: 700;">ระดับ 4.0000 (ผลงานดีเยี่ยม)</span>
                        </div>

                        <!-- Hero Score Box -->
                        <div class="hero-score-box">
                            <div class="hero-score-label">ผลการดำเนินงานเทียบเท่า</div>
                            <div class="hero-score-val" id="score-hero-val">ระดับ 4.0000 คะแนน</div>
                            <div class="hero-stars" id="score-hero-stars">★★★★☆</div>
                        </div>

                        <!-- Key Achievements Callout -->
                        <div class="callout-box" style="font-size: 13px;">
                            <h4 id="summary-overview-title">🎯 สรุปผลการดำเนินงานสำคัญ:</h4>
                            <p id="summary-overview-desc" style="line-height: 1.55; color: #1e293b;" contenteditable="false">
                                งวดสิ้นปีบัญชี 2569: ดำเนินงานบรรลุเกณฑ์ระดับ 4 ทั้ง 2 ประเด็นย่อย โดยเบิกจ่ายงบลงทุนได้ร้อยละ 93.1818 (เบิกจ่าย 82,000 บาท จาก 88,000 บาท คงเหลือเพียงเครื่องพิมพ์เลเซอร์ที่ราคากลางสูงกว่างบประมาณ) และการเบิกจ่ายภาพรวมทำได้ร้อยละ 97.7123 (เบิกจ่าย 272,808,720.73 บาท จากกรอบ 279,196,000 บาท) ซึ่งสูงกว่าค่าเป้าหมายตามมาตรการเร่งรัดการเบิกจ่ายภาครัฐของ ครม.
                            </p>
                        </div>

                        <!-- Metric Mini Cards -->
                        <div class="metric-cards-grid">
                            <div class="mini-card" style="background: #f0fdf4; border-color: #bbf7d0;">
                                <div class="mini-card-title">ความสำเร็จ</div>
                                <div class="mini-card-val" id="metric-complete-val" style="color: #16a34a;">ครบ 2 ประเด็น</div>
                            </div>
                            <div class="mini-card" style="background: #eff6ff; border-color: #bfdbfe;">
                                <div class="mini-card-title">สถานะประเมิน</div>
                                <div class="mini-card-val" id="metric-grade-val" style="color: #0284c7;">ระดับ 4 (ดีเยี่ยม)</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 1: ประเด็นย่อยที่ 1 งบลงทุน ================= -->
            <div class="content-view" id="view-topic-1">
                <div class="subview-container">
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>🖥️ 1. ร้อยละการเบิกจ่ายงบลงทุนเทียบกับแผนการเบิกจ่ายงบลงทุน ประจำปีบัญชี 2569 (น้ำหนัก 50% หรือ 2.5%)</h2>
                            <span class="pill-badge" id="v1-score-pill" style="background: #d97706; color: #ffffff;">น้ำหนัก 2.5% | ผลงานระดับ 4 (93.1818%)</span>
                        </div>

                        <!-- Rubric Scale Cards -->
                        <div class="rubric-grid-5">
                            <div class="rubric-card" id="v1-rubric-1">
                                <div class="rubric-card-header">ระดับ 1</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 12</div>
                            </div>
                            <div class="rubric-card" id="v1-rubric-2">
                                <div class="rubric-card-header">ระดับ 2</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 9</div>
                            </div>
                            <div class="rubric-card" id="v1-rubric-3">
                                <div class="rubric-card-header">ระดับ 3</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 6</div>
                            </div>
                            <div class="rubric-card active" id="v1-rubric-4">
                                <div class="rubric-card-header">ระดับ 4 ★</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 3 (หรือสูงกว่าเป้าหมาย ครม.)</div>
                            </div>
                            <div class="rubric-card" id="v1-rubric-5">
                                <div class="rubric-card-header">ระดับ 5</div>
                                <div>เบิกจ่ายได้ตามมติ ครม. (ร้อยละ 100)</div>
                            </div>
                        </div>

                        <!-- Timeline & Key Metrics -->
                        <div class="timeline-steps">
                            <div class="step-box primary-step">
                                <div class="step-number">กรอบงบประมาณ</div>
                                <div class="step-title">88,000 บาท (4 รายการ)</div>
                                <div class="step-desc">ได้รับอนุมัติงบลงทุนประจำปีงบประมาณ 2569 จำนวน 88,000 บาท เป็นรายการครุภัณฑ์จำนวน 4 รายการ</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">ผลการเบิกจ่ายจริง</div>
                                <div class="step-title" id="v1-step2-val">82,000 บาท (3 รายการ)</div>
                                <div class="step-desc" id="v1-step2-desc">ดำเนินการจัดซื้อจัดจ้างและเบิกจ่ายเรียบร้อยแล้ว 3 รายการ คิดเป็น <strong>ร้อยละ 93.1818</strong> ของวงเงินที่ได้รับจัดสรร</div>
                            </div>
                            <div class="step-box">
                                <div class="step-number">เป้าหมายตามมติ ครม.</div>
                                <div class="step-title">ไม่น้อยกว่าร้อยละ 75</div>
                                <div class="step-desc" id="v1-step3-desc">มาตรการเร่งรัดการเบิกจ่ายงบลงทุนภาครัฐกำหนดเป้าหมาย ≥ 75% ผลงานจริง 93.1818% สูงกว่าเป้าหมายถึง 18.18%</div>
                            </div>
                            <div class="step-box">
                                <div class="step-number">รายการคงเหลือ</div>
                                <div class="step-title" id="v1-step4-title">คงเหลือ 6,000 บาท (1 รายการ)</div>
                                <div class="step-desc" id="v1-step4-desc">เครื่องพิมพ์ Multifunction เลเซอร์ ราคากลางดีอีเอส 11,000 บาท แต่งบประมาณมี 6,000 บาท ต่ำกว่ามาตรฐานจึงไม่สามารถจัดหาได้</div>
                            </div>
                        </div>

                        <!-- 2 Detail Column Cards -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                            <div class="callout-box callout-info" id="v1-calc-box" style="font-size: 13px;">
                                <h4 style="color: #0369a1;">📐 สูตรการคำนวณและผลลัพธ์</h4>
                                <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                                    (ผลการเบิกจ่ายงบลงทุน / แผนการเบิกจ่ายงบลงทุน) × 100<br>
                                    = (82,000 / 88,000) × 100<br>
                                    = <strong>ร้อยละ 93.1818</strong> ของวงเงินที่ได้รับจัดสรร
                                </div>
                                <p style="margin-top: 8px; color: #334155;">
                                    <strong>เทียบเกณฑ์ประเมิน:</strong> บรรลุเกณฑ์ระดับ 4 ที่คะแนน 93.1818% คิดเป็นคะแนนถ่วงน้ำหนักในตัวชี้วัด <strong>2.0000 คะแนน</strong> (จากน้ำหนัก 50%)
                                </p>
                            </div>
                            <div class="callout-box callout-warning" id="v1-reason-box" style="font-size: 13px;">
                                <h4 style="color: #b45309;">⚠️ เหตุผลความจำเป็นของรายการคงเหลือ 6,000 บาท</h4>
                                <p style="line-height: 1.6; color: #1e293b;">
                                    รายการครุภัณฑ์-เครื่องพิมพ์ Multifunction เลเซอร์ ขาว-ดำ คณะกรรมการฯ ได้ตรวจสอบเกณฑ์ราคากลางและคุณลักษณะพื้นฐานครุภัณฑ์คอมพิวเตอร์ ฉบับเดือนธันวาคม 2568 ของกระทรวงดิจิทัลเพื่อเศรษฐกิจและสังคม พบว่า มีราคามาตรฐานเครื่องละ <strong>11,000 บาท</strong><br>
                                    ขณะที่วงเงินงบประมาณที่ได้รับจัดสรรมีเพียง <strong>6,000 บาท</strong> ซึ่งต่ำกว่าราคามาตรฐาน จึงไม่เพียงพอต่อการจัดหาครุภัณฑ์ที่มีประสิทธิภาพเหมาะสมต่อการใช้งานในราชการ
                                </p>
                            </div>
                        </div>

                        <!-- Bottom Summary Strip -->
                        <div class="hero-score-box" style="padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; text-align: left;">
                            <div>
                                <span style="font-size: 12px; color: #93c5fd; font-weight: 600;">ผลการดำเนินงานข้อ 1 (น้ำหนัก 50% หรือ 2.5%)</span>
                                <div style="font-size: 20px; font-weight: 800; color: #ffcc00;" id="v1-bottom-val">ระดับ 4.0000 คะแนน (93.1818%) <span style="font-size: 16px; color: #facc15;">★★★★☆</span></div>
                            </div>
                            <div style="font-size: 12.5px; color: #e2e8f0; max-width: 65%; text-align: right;" id="v1-bottom-callout">
                                บรรลุเกณฑ์ระดับ 4: เบิกจ่ายงบลงทุนได้ 82,000 บาท คิดเป็นร้อยละ 93.1818 สูงกว่าเป้าหมาย ครม. (ร้อยละ 75) คะแนนถ่วงน้ำหนัก 2.0000 (0.1000)
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ================= VIEW 2: ประเด็นย่อยที่ 2 ภาพรวม ================= -->
            <div class="content-view" id="view-topic-2">
                <div class="subview-container">
                    <div class="glass-card">
                        <div class="card-header-styled">
                            <h2>📊 2. ร้อยละการเบิกจ่ายภาพรวมเทียบกับแผนการเบิกจ่ายภาพรวม ประจำปีบัญชี 2569 (น้ำหนัก 50% หรือ 2.5%)</h2>
                            <span class="pill-badge" id="v2-score-pill" style="background: #d97706; color: #ffffff;">น้ำหนัก 2.5% | ผลงานระดับ 4 (97.7123%)</span>
                        </div>

                        <!-- Rubric Scale Cards -->
                        <div class="rubric-grid-5">
                            <div class="rubric-card" id="v2-rubric-1">
                                <div class="rubric-card-header">ระดับ 1</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 12</div>
                            </div>
                            <div class="rubric-card" id="v2-rubric-2">
                                <div class="rubric-card-header">ระดับ 2</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 9</div>
                            </div>
                            <div class="rubric-card" id="v2-rubric-3">
                                <div class="rubric-card-header">ระดับ 3</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 6</div>
                            </div>
                            <div class="rubric-card active" id="v2-rubric-4">
                                <div class="rubric-card-header">ระดับ 4 ★</div>
                                <div>เบิกจ่ายได้น้อยกว่ามติ ครม. ร้อยละ 3 (หรือสูงกว่าเป้าหมาย ครม.)</div>
                            </div>
                            <div class="rubric-card" id="v2-rubric-5">
                                <div class="rubric-card-header">ระดับ 5</div>
                                <div>เบิกจ่ายได้ตามมติ ครม. (ร้อยละ 100)</div>
                            </div>
                        </div>

                        <!-- Budget Categories Breakdown -->
                        <div class="timeline-steps">
                            <div class="step-box primary-step">
                                <div class="step-number">หมวดที่ 1: งบบุคลากร</div>
                                <div class="step-title" id="v2-cat1-val">3,637,854.27 บาท</div>
                                <div class="step-desc" id="v2-cat1-desc">จากกรอบงบประมาณ 4,155,120.00 บาท สำหรับค่าใช้จ่ายด้านเงินเดือน ค่าจ้าง และบุคลากรของเงินทุนหมุนเวียนฯ</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">หมวดที่ 2: งบดำเนินงาน</div>
                                <div class="step-title" id="v2-cat2-val">19,300,534.88 บาท</div>
                                <div class="step-desc" id="v2-cat2-desc">หมวดค่าตอบแทน ใช้สอยและวัสดุ บริหารจัดการภารกิจ การประชุมสัมมนา และพัฒนาระบบเทคโนโลยีสารสนเทศ</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">หมวดที่ 3: วงเงินให้กู้ยืม</div>
                                <div class="step-title" id="v2-cat3-val">249,788,331.58 บาท</div>
                                <div class="step-desc" id="v2-cat3-desc">ธ.ก.ส. จ่ายเงินให้ผู้กู้ยืมแล้ว 619 ราย จากวงเงินอนุมัติ 250,000,000 บาท (คงเหลือวงเงิน 211,668.42 บาท)</div>
                            </div>
                            <div class="step-box primary-step">
                                <div class="step-number">หมวดที่ 4: งบลงทุน</div>
                                <div class="step-title" id="v2-cat4-val">82,000.00 บาท</div>
                                <div class="step-desc" id="v2-cat4-desc">เบิกจ่ายจัดซื้อครุภัณฑ์ 3 รายการ จากกรอบงบประมาณที่ได้รับอนุมัติ 88,000 บาท</div>
                            </div>
                        </div>

                        <!-- 2 Detail Column Cards -->
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                            <div class="callout-box callout-info" id="v2-calc-box" style="font-size: 13px;">
                                <h4 style="color: #0369a1;">📐 สูตรการคำนวณการเบิกจ่ายภาพรวม</h4>
                                <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                                    (ผลการเบิกจ่ายภาพรวมในปี 2569 / แผนภาพรวม) × 100<br>
                                    = (272,808,720.73 / 279,196,000.00) × 100<br>
                                    = <strong>ร้อยละ 97.7123</strong> ของวงเงินที่ได้รับจัดสรร<br><br>
                                    <span style="font-size: 11.5px; color: #64748b;">(กรณีรวมภาระผูกพันปีก่อน 6.02 ลบ.: 277.59 / 285.22 ลบ. = 97.3256%)</span>
                                </div>
                                <p style="margin-top: 8px; color: #334155;">
                                    <strong>เทียบเกณฑ์ ครม.:</strong> เป้าหมาย ครม. กำหนดไม่น้อยกว่าร้อยละ 93 ผลการเบิกจ่ายจริง 97.7123% สูงกว่าเป้าหมาย ครม. บรรลุ <strong>ระดับ 4 (คะแนน 2.0000)</strong>
                                </p>
                            </div>
                            <div class="callout-box callout-success" id="v2-detail-box" style="font-size: 13px;">
                                <h4 style="color: #15803d;">🏦 รายละเอียดผลการเบิกจ่ายเงินกู้ยืม 3 ครั้ง (ธ.ก.ส.)</h4>
                                <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                                    <li><strong>ครั้งที่ 1 (27 ก.พ. 69):</strong> อนุมัติ 293 ราย เป็นเงิน 118,006,505.74 บาท</li>
                                    <li><strong>ครั้งที่ 2 (27 มี.ค. 69):</strong> อนุมัติ 329 ราย เป็นเงิน 131,879,572.76 บาท</li>
                                    <li><strong>ครั้งที่ 3 (20 ก.ค. 69):</strong> อนุมัติ 68 ราย เป็นเงิน 28,603,087.69 บาท</li>
                                    <li><strong>ผลจ่ายเงินจริง ณ 30 ก.ย. 69:</strong> ธ.ก.ส. จัดทำสัญญาและจ่ายเงินแล้ว <strong>619 ราย เป็นเงิน 249,788,331.58 บาท</strong> (คงเหลือ 211,668.42 บาท)</li>
                                </ul>
                            </div>
                        </div>

                        <!-- Bottom Summary Strip -->
                        <div class="hero-score-box" style="padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; text-align: left;">
                            <div>
                                <span style="font-size: 12px; color: #93c5fd; font-weight: 600;">ผลการดำเนินงานข้อ 2 (น้ำหนัก 50% หรือ 2.5%)</span>
                                <div style="font-size: 20px; font-weight: 800; color: #ffcc00;" id="v2-bottom-val">ระดับ 4.0000 คะแนน (97.7123%) <span style="font-size: 16px; color: #facc15;">★★★★☆</span></div>
                            </div>
                            <div style="font-size: 12.5px; color: #e2e8f0; max-width: 65%; text-align: right;" id="v2-bottom-callout">
                                บรรลุเกณฑ์ระดับ 4: เบิกจ่ายงบภาพรวมได้ 272.81 ล้านบาท คิดเป็นร้อยละ 97.7123 สูงกว่าเป้าหมาย ครม. (ร้อยละ 93) คะแนนถ่วงน้ำหนัก 2.0000 (0.1000)
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
        let currentAppMode = 'preview'; // 'preview' or 'edit'
        let activeQuarter = 4;
        let activeTopic = 0;

        /* KPI Page Navigation Mapping (Only completed KPIs up to 6.1) */
        function navigateToKPI(kpiKey) {
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
            if (routes[kpiKey]) {
                window.location.href = routes[kpiKey];
            } else {
                showToast(`ไม่พบหน้ารายงานสำหรับ ${kpiKey}`);
            }
        }

        /* Subtopic Tab Switching (View 0, View 1, View 2) */
        function switchTopicView(topicIndex) {
            activeTopic = topicIndex;
            for (let i = 0; i <= 2; i++) {
                const tab = document.getElementById(`tab-v${i}`);
                const view = document.getElementById(`view-topic-${i}`);
                if (tab) tab.classList.toggle('active', i === topicIndex);
                if (view) view.classList.toggle('active', i === topicIndex);
            }
        }

        /* Official Data Model for Each Quarter */
        const quarterDefaults = {
            1: {
                heroScore: 'ระดับ 1.0000 คะแนน',
                heroStars: '★☆☆☆☆',
                statusBadge: 'ระดับ 1.00 (เบื้องต้น)',
                completeVal: 'เริ่มต้น 2 ประเด็น',
                gradeVal: 'ระดับ 1.00 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 1: อยู่ระหว่างเตรียมการจัดซื้อจัดจ้างงบลงทุน และเริ่มต้นการเบิกจ่ายงบบุคลากรและงบดำเนินงานตามแผนงาน โดยคณะอนุกรรมการฯ ได้อนุมัติจัดสรรวงเงินให้กู้ยืม 250 ล้านบาท (5 พ.ย. 68) และเปิดรับคำขอกู้ผ่านระบบ WCT',
                table: {
                    t1: '<strong>ร้อยละการเบิกจ่ายงบลงทุน</strong> เทียบกับแผนฯ (กรอบ 88,000 บาท - เตรียมการจัดหา)',
                    t2: '<strong>ร้อยละการเบิกจ่ายภาพรวม</strong> เทียบกับแผนฯ (กรอบ 279.20 ล้านบาท - เริ่มต้นเบิกจ่าย)',
                    s1: '1 (N/A)', ws1: '0.5000',
                    s2: '1 (เบื้องต้น)', ws2: '0.5000',
                    totLevel: 'ระดับ 1.0 (เบื้องต้น)', totWScore: '1.0000 คะแนน',
                    callout: '💡 <strong>สรุปความเชื่อมโยง (ไตรมาส 1):</strong> อยู่ระหว่างการจัดเตรียมคุณลักษณะจัดซื้อครุภัณฑ์งบลงทุน และเริ่มต้นการเบิกจ่ายงบบุคลากรและงบดำเนินงานตามแผนงาน โดยอนุมัติกรอบวงเงินกู้ยืม 250 ล้านบาทแล้ว'
                },
                v1: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 1 (อยู่ระหว่างจัดซื้อจัดจ้าง)',
                    activeRubric: 1,
                    step2Val: 'อยู่ระหว่างจัดหา',
                    step2Desc: 'อยู่ระหว่างเตรียมการกำหนดคุณลักษณะครุภัณฑ์งบลงทุน 4 รายการ วงเงิน 88,000 บาท ยังไม่มีการเบิกจ่ายจริง',
                    step3Desc: 'มาตรการเร่งรัดการเบิกจ่ายงบลงทุนภาครัฐกำหนดเป้าหมาย ≥ 75% อยู่ระหว่างกระบวนการจัดหา',
                    step4Title: 'กรอบวงเงิน 88,000 บาท',
                    step4Desc: 'ครุภัณฑ์ 4 รายการ อยู่ระหว่างเตรียมการจัดซื้อจัดจ้างตามระเบียบพัสดุฯ',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณและผลลัพธ์</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายงบลงทุน / แผนการเบิกจ่ายงบลงทุน) × 100<br>
                        = อยู่ระหว่างเตรียมการจัดซื้อจัดจ้างตามระเบียบพัสดุฯ<br>
                        = ยังไม่มีผลเบิกจ่ายจริง (N/A)
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ประเมิน:</strong> อยู่ระหว่างจัดหา เทียบเท่าระดับ 1 (N/A) คิดเป็นคะแนนถ่วงน้ำหนัก <strong>0.5000 คะแนน</strong>
                    </p>`,
                    reasonHtml: `<h4 style="color: #b45309;">📋 แผนการจัดซื้อจัดจ้างงบลงทุน ไตรมาส 1</h4>
                    <p style="line-height: 1.6; color: #1e293b;">
                        ได้รับอนุมัติกรอบงบลงทุน 88,000 บาท สำหรับจัดหาครุภัณฑ์ 4 รายการ อยู่ระหว่างเจ้าหน้าที่สำนักบริหารเงินทุนหมุนเวียนฯ ดำเนินการกำหนดรายละเอียดคุณลักษณะเฉพาะเพื่อเสนอขอความเห็นชอบและดำเนินการจัดซื้อจัดจ้างตามขั้นตอนของ พ.ร.บ. จัดซื้อจัดจ้างและการบริหารพัสดุภาครัฐ พ.ศ. 2560 ต่อไป
                    </p>`,
                    bottomVal: 'ระดับ 1.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาส 1: อยู่ระหว่างการกำหนดคุณลักษณะและเตรียมการจัดซื้อครุภัณฑ์งบลงทุน (คะแนนถ่วงน้ำหนัก 0.5000)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 1 (เริ่มต้นเบิกจ่าย)',
                    activeRubric: 1,
                    cat1Val: 'เริ่มต้นตามงวด',
                    cat1Desc: 'เบิกจ่ายเงินเดือน ค่าจ้าง และบุคลากรของเงินทุนหมุนเวียนฯ ตามงวดเบิกจ่ายปกติ',
                    cat2Val: 'เริ่มต้นตามแผน',
                    cat2Desc: 'เบิกจ่ายค่าตอบแทน ใช้สอยและวัสดุ บริหารงานทั่วไปตามแผนการปฏิบัติงาน',
                    cat3Val: 'อนุมัติกรอบ 250 ลบ.',
                    cat3Desc: 'คณะอนุกรรมการฯ มีมติอนุมัติกรอบวงเงินให้กู้ยืม 250,000,000 บาท (5 พ.ย. 68)',
                    cat4Val: 'อยู่ระหว่างจัดหา',
                    cat4Desc: 'งบลงทุน 88,000 บาท อยู่ระหว่างเตรียมการจัดหา',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณการเบิกจ่ายภาพรวม</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายภาพรวมในปี 2569 / แผนภาพรวม) × 100<br>
                        = เริ่มต้นการเบิกจ่ายงบบุคลากรและค่าใช้สอยดำเนินงานประจำ<br>
                        = ระดับเริ่มต้น (ระดับ 1)
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ ครม.:</strong> เริ่มต้นเบิกจ่ายในไตรมาสแรก เทียบเท่าระดับ 1 คิดเป็นคะแนนถ่วงน้ำหนัก <strong>0.5000 คะแนน</strong>
                    </p>`,
                    detailHtml: `<h4 style="color: #15803d;">🏦 แผนการจัดสรรวงเงินให้กู้ยืม ไตรมาส 1 (ธ.ก.ส.)</h4>
                    <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                        <li><strong>5 พ.ย. 68 (ประชุมครั้งที่ 9/2568):</strong> คณะอนุกรรมการบริหารเงินทุนหมุนเวียนฯ มีมติอนุมัติจัดสรรวงเงินให้กู้ยืมประจำปี 2569 จำนวน 250,000,000 บาท</li>
                        <li><strong>เปิดรับคำขอกู้:</strong> สำนักบริหารเงินทุนหมุนเวียนฯ เปิดระบบ WCT ให้ข้าราชการครูและบุคลากรทางการศึกษายื่นคำขอกู้ยืม</li>
                        <li><strong>อยู่ระหว่างตรวจสอบคำขอ:</strong> อยู่ระหว่างขั้นตอนตรวจสอบคุณสมบัติและเอกสารของผู้ยื่นกู้ เพื่อเสนอคณะอนุกรรมการฯ อนุมัติต่อไป</li>
                    </ul>`,
                    bottomVal: 'ระดับ 1.0000 คะแนน <span style="font-size: 16px; color: #facc15;">★☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาส 1: เริ่มต้นเบิกจ่ายงบบุคลากรและงบดำเนินงานตามแผนการใช้จ่ายงบประมาณ (คะแนนถ่วงน้ำหนัก 0.5000)'
                }
            },
            2: {
                heroScore: 'ระดับ 1.0000 คะแนน',
                heroStars: '★☆☆☆☆',
                statusBadge: 'ระดับ 1.00 (เบื้องต้น)',
                completeVal: 'ดำเนินงาน 2 ประเด็น',
                gradeVal: 'ระดับ 1.00 (เบื้องต้น)',
                summaryDesc: 'ไตรมาสที่ 2: งบลงทุนอยู่ระหว่างกระบวนการจัดหา (N/A ระดับ 1) และการเบิกจ่ายภาพรวมทำได้ร้อยละ 5.4110 (ระดับ 1) โดยอนุมัติเงินกู้ยืมครั้งที่ 1 (293 ราย 118.01 ลบ.) และครั้งที่ 2 (329 ราย 131.88 ลบ.) รวม 622 ราย 249.89 ลบ. และอยู่ระหว่างการทำสัญญาของ ธ.ก.ส.',
                table: {
                    t1: '<strong>ร้อยละการเบิกจ่ายงบลงทุน</strong> เทียบกับแผนฯ (88,000 บาท - อยู่ระหว่างจัดหา)',
                    t2: '<strong>ร้อยละการเบิกจ่ายภาพรวม</strong> เทียบกับแผนฯ (15.11 / 279.20 ล้านบาท - 5.4110%)',
                    s1: '1 (N/A)', ws1: '0.5000',
                    s2: '1 (5.4110)', ws2: '0.5000',
                    totLevel: 'ระดับ 1.0 (เบื้องต้น)', totWScore: '1.0000 คะแนน',
                    callout: '💡 <strong>สรุปความเชื่อมโยง (ไตรมาส 2):</strong> งบลงทุนอยู่ระหว่างกระบวนการจัดหาตามระเบียบพัสดุฯ ยังไม่มีการเบิกจ่าย (N/A) ขณะที่การเบิกจ่ายภาพรวมทำได้ร้อยละ 5.4110 โดยอนุมัติเงินกู้ยืม 2 ครั้ง รวม 622 ราย (249.89 ลบ.) และ ธ.ก.ส. เบิกจ่ายเงินไปแล้ว 50.88 ล้านบาท'
                },
                v1: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 1 (N/A)',
                    activeRubric: 1,
                    step2Val: 'อยู่ระหว่างจัดหา',
                    step2Desc: 'อยู่ระหว่างกระบวนการจัดหาตามระเบียบพัสดุฯ ครุภัณฑ์ 4 รายการ ยังไม่มีการเบิกจ่ายจริง',
                    step3Desc: 'มาตรการเร่งรัดการเบิกจ่ายงบลงทุนภาครัฐกำหนดเป้าหมาย ≥ 75% ไตรมาส 2 อยู่ระหว่างขั้นตอนจัดซื้อ',
                    step4Title: 'งบลงทุน 88,000 บาท',
                    step4Desc: 'อยู่ระหว่างกระบวนการจัดหาพัสดุตามระเบียบกระทรวงการคลัง',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณและผลลัพธ์</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายงบลงทุน / แผนการเบิกจ่ายงบลงทุน) × 100<br>
                        = อยู่ระหว่างการดำเนินการตามระเบียบพัสดุฯ<br>
                        = ผลงานเทียบเท่าระดับ 1 (N/A)
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ประเมิน:</strong> งบลงทุนอยู่ระหว่างกระบวนการจัดหา ยังไม่ได้เบิกจ่ายจริง เทียบเท่าระดับ 1 (N/A) คะแนนถ่วงน้ำหนัก <strong>0.5000 คะแนน</strong>
                    </p>`,
                    reasonHtml: `<h4 style="color: #b45309;">⚠️ สถานะงบลงทุน ไตรมาส 2</h4>
                    <p style="line-height: 1.6; color: #1e293b;">
                        งบลงทุนจำนวน 88,000 บาท สำหรับจัดหาครุภัณฑ์จำนวน 4 รายการ อยู่ระหว่างการดำเนินการตามระเบียบพัสดุฯ และสืบราคามาตรฐานครุภัณฑ์ โดยเตรียมการจัดหาในไตรมาสที่ 3 ต่อไป
                    </p>`,
                    bottomVal: 'ระดับ 1.0000 คะแนน (N/A) <span style="font-size: 16px; color: #facc15;">★☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาส 2: รายการงบลงทุนอยู่ระหว่างกระบวนการจัดหา ยังไม่ได้เบิกจ่ายจริง (คะแนนถ่วงน้ำหนัก 0.5000)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 1 (5.4110%)',
                    activeRubric: 1,
                    cat1Val: 'เบิกตามงวดงาน',
                    cat1Desc: 'เบิกจ่ายงบบุคลากรตามแผนงานรายเดือน',
                    cat2Val: 'เบิกจ่ายตามเป้าหมาย',
                    cat2Desc: 'หมวดค่าตอบแทน ใช้สอยและวัสดุ ผลการเบิกจ่ายเป็นไปตามเป้าหมาย',
                    cat3Val: '50.88 ล้านบาท (ธ.ก.ส.)',
                    cat3Desc: 'ธ.ก.ส. เบิกเงินไปแล้ว 50.88 ล้านบาท จากการอนุมัติ 2 ครั้ง รวม 622 ราย (249.89 ลบ.)',
                    cat4Val: 'อยู่ระหว่างจัดหา',
                    cat4Desc: 'งบลงทุน 88,000 บาท อยู่ระหว่างจัดหา',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณการเบิกจ่ายภาพรวม</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายภาพรวมในปี 2569 / แผนภาพรวม) × 100<br>
                        = (15,107,313.25 / 279,196,000.00) × 100<br>
                        = <strong>ร้อยละ 5.4110</strong> ของวงเงินที่ได้รับจัดสรร
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ ครม.:</strong> ผลการเบิกจ่ายภาพรวมได้ร้อยละ 5.4110 บรรลุ <strong>ระดับ 1 (คะแนน 0.5000)</strong>
                    </p>`,
                    detailHtml: `<h4 style="color: #15803d;">🏦 รายละเอียดผลการอนุมัติเงินกู้ยืม ไตรมาส 2 (ธ.ก.ส.)</h4>
                    <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                        <li><strong>ครั้งที่ 1 (27 ก.พ. 69 ประชุม 2/2569):</strong> อนุมัติ 293 ราย เป็นเงิน 118,006,505.74 บาท</li>
                        <li><strong>ครั้งที่ 2 (27 มี.ค. 69 ประชุม 3/2569):</strong> อนุมัติ 329 ราย เป็นเงิน 131,879,572.76 บาท</li>
                        <li><strong>รวมอนุมัติ 2 ครั้ง:</strong> 622 ราย เป็นเงิน 249,886,078.50 บาท</li>
                        <li><strong>ผลจ่ายเงินจริง ณ 31 มี.ค. 69:</strong> ธ.ก.ส. เบิกเงินไปแล้ว 50.88 ล้านบาท อยู่ระหว่างเร่งทำสัญญาและจ่ายเงินแก่ผู้กู้</li>
                    </ul>`,
                    bottomVal: 'ระดับ 1.0000 คะแนน (5.4110%) <span style="font-size: 16px; color: #facc15;">★☆☆☆☆</span>',
                    bottomCallout: 'ไตรมาส 2: เบิกจ่ายภาพรวมได้ร้อยละ 5.4110 โดยเบิกจ่ายเงินให้ ธ.ก.ส. 50.88 ล้านบาท (คะแนนถ่วงน้ำหนัก 0.5000)'
                }
            },
            3: {
                heroScore: 'ระดับ 4.0000 คะแนน',
                heroStars: '★★★★☆',
                statusBadge: 'ระดับ 4.00 (ดีเยี่ยม)',
                completeVal: 'ผ่านเกณฑ์ 2 ประเด็น',
                gradeVal: 'ระดับ 4.00 (ดีเยี่ยม)',
                summaryDesc: 'ไตรมาสที่ 3: งบลงทุนเบิกจ่ายแล้ว 3 รายการ เป็นเงิน 82,000 บาท คิดเป็นร้อยละ 93.1818 (ระดับ 4) และการเบิกจ่ายภาพรวมสะสมคิดเป็นร้อยละ 85.3471 (ระดับ 4) โดยยอดเบิกจ่ายเงินให้กู้ยืมสะสม ณ สิ้นสุดไตรมาสที่ 3 เป็นเงิน 221.36 ล้านบาท (88.55%)',
                table: {
                    t1: '<strong>ร้อยละการเบิกจ่ายงบลงทุน</strong> เทียบกับแผนฯ (82,000 / 88,000 บาท)',
                    t2: '<strong>ร้อยละการเบิกจ่ายภาพรวม</strong> เทียบกับแผนฯ (238.29 / 279.20 ล้านบาท - 85.3471%)',
                    s1: '4 (93.1818)', ws1: '2.0000',
                    s2: '4 (85.3471)', ws2: '2.0000',
                    totLevel: 'ระดับ 4.0', totWScore: '4.0000 คะแนน',
                    callout: '💡 <strong>สรุปความเชื่อมโยง (ไตรมาส 3):</strong> ผลการเบิกจ่ายงบลงทุนทำได้ ร้อยละ 93.1818 (เบิกจ่าย 82,000 บาท จาก 88,000 บาท สูงกว่าเป้าหมาย ครม. 75%) และการเบิกจ่ายภาพรวมสะสมทำได้ ร้อยละ 85.3471 บรรลุผลงานระดับ 4.0000 คะแนนทั้งสองประเด็น'
                },
                v1: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 4 (93.1818%)',
                    activeRubric: 4,
                    step2Val: '82,000 บาท (3 รายการ)',
                    step2Desc: 'ดำเนินการจัดซื้อจัดจ้างและเบิกจ่ายเรียบร้อยแล้ว 3 รายการ คิดเป็น <strong>ร้อยละ 93.1818</strong> ของวงเงินที่ได้รับจัดสรร',
                    step3Desc: 'มาตรการเร่งรัดการเบิกจ่ายงบลงทุนภาครัฐกำหนดเป้าหมาย ≥ 75% ผลงานจริง 93.1818% สูงกว่าเป้าหมายถึง 18.18%',
                    step4Title: 'คงเหลือ 6,000 บาท (1 รายการ)',
                    step4Desc: 'เครื่องพิมพ์ Multifunction เลเซอร์ ราคากลางดีอีเอส 11,000 บาท แต่งบประมาณมี 6,000 บาท ต่ำกว่ามาตรฐานจึงไม่สามารถจัดหาได้',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณและผลลัพธ์</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายงบลงทุน / แผนการเบิกจ่ายงบลงทุน) × 100<br>
                        = (82,000 / 88,000) × 100<br>
                        = <strong>ร้อยละ 93.1818</strong> ของวงเงินที่ได้รับจัดสรร
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ประเมิน:</strong> บรรลุเกณฑ์ระดับ 4 ที่คะแนน 93.1818% คิดเป็นคะแนนถ่วงน้ำหนักในตัวชี้วัด <strong>2.0000 คะแนน</strong> (จากน้ำหนัก 50%)
                    </p>`,
                    reasonHtml: `<h4 style="color: #b45309;">⚠️ เหตุผลความจำเป็นของรายการคงเหลือ 6,000 บาท</h4>
                    <p style="line-height: 1.6; color: #1e293b;">
                        รายการครุภัณฑ์-เครื่องพิมพ์ Multifunction เลเซอร์ ขาว-ดำ คณะกรรมการฯ ได้ตรวจสอบเกณฑ์ราคากลางและคุณลักษณะพื้นฐานครุภัณฑ์คอมพิวเตอร์ ฉบับเดือนธันวาคม 2568 ของกระทรวงดิจิทัลเพื่อเศรษฐกิจและสังคม พบว่า มีราคามาตรฐานเครื่องละ <strong>11,000 บาท</strong><br>
                        ขณะที่วงเงินงบประมาณที่ได้รับจัดสรรมีเพียง <strong>6,000 บาท</strong> ซึ่งต่ำกว่าราคามาตรฐาน จึงไม่เพียงพอต่อการจัดหาครุภัณฑ์ที่มีประสิทธิภาพเหมาะสมต่อการใช้งานในราชการ
                    </p>`,
                    bottomVal: 'ระดับ 4.0000 คะแนน (93.1818%) <span style="font-size: 16px; color: #facc15;">★★★★☆</span>',
                    bottomCallout: 'ไตรมาส 3: เบิกจ่ายงบลงทุนได้ 82,000 บาท คิดเป็นร้อยละ 93.1818 สูงกว่าเป้าหมาย ครม. (ร้อยละ 75) คะแนนถ่วงน้ำหนัก 2.0000'
                },
                v2: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 4 (85.3471%)',
                    activeRubric: 4,
                    cat1Val: 'เบิกจ่ายตามงวด',
                    cat1Desc: 'งบบุคลากรเบิกจ่ายตามงวดค่าใช้จ่ายปกติ',
                    cat2Val: 'เบิกจ่ายตามเป้าหมาย',
                    cat2Desc: 'หมวดค่าตอบแทน ใช้สอยและวัสดุ บริหารจัดการภารกิจ การประชุมสัมมนา เป็นไปตามเป้าหมาย',
                    cat3Val: '221.36 ล้านบาท (88.55%)',
                    cat3Desc: 'ธ.ก.ส. เบิกจ่ายเงินให้ผู้กู้ยืมสะสม ณ สิ้นไตรมาสที่ 3 เป็นเงิน 221.36 ล้านบาท คิดเป็น 88.55% ของวงเงิน 250 ลบ.',
                    cat4Val: '82,000.00 บาท',
                    cat4Desc: 'เบิกจ่ายจัดซื้อครุภัณฑ์ 3 รายการ เรียบร้อยแล้ว',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณการเบิกจ่ายภาพรวม</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายภาพรวมสะสมในไตรมาส 3 / แผนภาพรวม) × 100<br>
                        = (238,285,412.18 / 279,196,000.00) × 100<br>
                        = <strong>ร้อยละ 85.3471</strong> ของวงเงินที่ได้รับจัดสรร
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ ครม.:</strong> ผลการเบิกจ่ายภาพรวมสะสมคิดเป็นร้อยละ 85.3471 บรรลุ <strong>ระดับ 4 (คะแนน 2.0000)</strong>
                    </p>`,
                    detailHtml: `<h4 style="color: #15803d;">🏦 รายละเอียดผลการเบิกจ่ายเงินกู้ยืม ณ ไตรมาส 3 (ธ.ก.ส.)</h4>
                    <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                        <li><strong>อนุมัติรอบที่ 1 & 2:</strong> อนุมัติรวม 622 ราย เป็นเงิน 249,886,078.50 บาท</li>
                        <li><strong>การเบิกจ่ายสะสม ณ 30 มิ.ย. 69:</strong> ธ.ก.ส. จัดทำสัญญาและเบิกจ่ายเงินให้ผู้กู้แล้ว <strong>221.36 ล้านบาท</strong> (คิดเป็นร้อยละ 88.55)</li>
                        <li><strong>เตรียมการรอบที่ 3:</strong> เตรียมเสนอคณะอนุกรรมการฯ พิจารณาจัดสรรวงเงินกู้ยืมรอบที่ 3 ในเดือนกรกฎาคม 2569 เพื่อให้ครบถ้วนตามกรอบ 250 ล้านบาท</li>
                    </ul>`,
                    bottomVal: 'ระดับ 4.0000 คะแนน (85.3471%) <span style="font-size: 16px; color: #facc15;">★★★★☆</span>',
                    bottomCallout: 'ไตรมาส 3: เบิกจ่ายงบภาพรวมสะสมได้ร้อยละ 85.3471 คะแนนถ่วงน้ำหนัก 2.0000'
                }
            },
            4: {
                heroScore: 'ระดับ 4.0000 คะแนน',
                heroStars: '★★★★☆',
                statusBadge: 'ระดับ 4.0000 (ผลงานดีเยี่ยม)',
                completeVal: 'ครบ 2 ประเด็น',
                gradeVal: 'ระดับ 4 (ดีเยี่ยม)',
                summaryDesc: 'งวดสิ้นปีบัญชี 2569: ดำเนินงานบรรลุเกณฑ์ระดับ 4 ทั้ง 2 ประเด็นย่อย โดยเบิกจ่ายงบลงทุนได้ร้อยละ 93.1818 (เบิกจ่าย 82,000 บาท จาก 88,000 บาท คงเหลือเพียงเครื่องพิมพ์เลเซอร์ที่ราคากลางสูงกว่างบประมาณ) และการเบิกจ่ายภาพรวมทำได้ร้อยละ 97.7123 (เบิกจ่าย 272,808,720.73 บาท จากกรอบ 279,196,000 บาท) ซึ่งสูงกว่าค่าเป้าหมายตามมาตรการเร่งรัดการเบิกจ่ายภาครัฐของ ครม.',
                table: {
                    t1: '<strong>ร้อยละการเบิกจ่ายงบลงทุน</strong> เทียบกับแผนฯ (82,000 / 88,000 บาท)',
                    t2: '<strong>ร้อยละการเบิกจ่ายภาพรวม</strong> เทียบกับแผนฯ (272.81 / 279.20 ล้านบาท)',
                    s1: '4 (93.1818)', ws1: '2.0000',
                    s2: '4 (97.7123)', ws2: '2.0000',
                    totLevel: 'ระดับ 4.0', totWScore: '4.0000 คะแนน',
                    callout: '💡 <strong>สรุปความเชื่อมโยง:</strong> ผลการเบิกจ่ายงบประมาณของเงินทุนหมุนเวียนฯ ประจำปีบัญชี 2569 บรรลุผลงาน <strong>ระดับ 4.0000 คะแนน</strong> ทั้งสองประเด็น โดยงบลงทุนเบิกจ่ายได้ <strong>ร้อยละ 93.1818</strong> (เบิกจ่าย 82,000 จาก 88,000 บาท สูงกว่าเป้าหมาย ครม. ร้อยละ 75) และการเบิกจ่ายภาพรวมเบิกจ่ายได้ <strong>ร้อยละ 97.7123</strong> (เบิกจ่าย 272,808,720.73 จาก 279,196,000 บาท สูงกว่าเป้าหมาย ครม. ร้อยละ 93) โดยมีเงินให้กู้ยืมแก่ครูและบุคลากรทางการศึกษาเบิกจ่ายจริงถึง 249,788,331.58 บาท (619 ราย)'
                },
                v1: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 4 (93.1818%)',
                    activeRubric: 4,
                    step2Val: '82,000 บาท (3 รายการ)',
                    step2Desc: 'ดำเนินการจัดซื้อจัดจ้างและเบิกจ่ายเรียบร้อยแล้ว 3 รายการ คิดเป็น <strong>ร้อยละ 93.1818</strong> ของวงเงินที่ได้รับจัดสรร',
                    step3Desc: 'มาตรการเร่งรัดการเบิกจ่ายงบลงทุนภาครัฐกำหนดเป้าหมาย ≥ 75% ผลงานจริง 93.1818% สูงกว่าเป้าหมายถึง 18.18%',
                    step4Title: 'คงเหลือ 6,000 บาท (1 รายการ)',
                    step4Desc: 'เครื่องพิมพ์ Multifunction เลเซอร์ ราคากลางดีอีเอส 11,000 บาท แต่งบประมาณมี 6,000 บาท ต่ำกว่ามาตรฐานจึงไม่สามารถจัดหาได้',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณและผลลัพธ์</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายงบลงทุน / แผนการเบิกจ่ายงบลงทุน) × 100<br>
                        = (82,000 / 88,000) × 100<br>
                        = <strong>ร้อยละ 93.1818</strong> ของวงเงินที่ได้รับจัดสรร
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ประเมิน:</strong> บรรลุเกณฑ์ระดับ 4 ที่คะแนน 93.1818% คิดเป็นคะแนนถ่วงน้ำหนักในตัวชี้วัด <strong>2.0000 คะแนน</strong> (จากน้ำหนัก 50%)
                    </p>`,
                    reasonHtml: `<h4 style="color: #b45309;">⚠️ เหตุผลความจำเป็นของรายการคงเหลือ 6,000 บาท</h4>
                    <p style="line-height: 1.6; color: #1e293b;">
                        รายการครุภัณฑ์-เครื่องพิมพ์ Multifunction เลเซอร์ ขาว-ดำ คณะกรรมการฯ ได้ตรวจสอบเกณฑ์ราคากลางและคุณลักษณะพื้นฐานครุภัณฑ์คอมพิวเตอร์ ฉบับเดือนธันวาคม 2568 ของกระทรวงดิจิทัลเพื่อเศรษฐกิจและสังคม พบว่า มีราคามาตรฐานเครื่องละ <strong>11,000 บาท</strong><br>
                        ขณะที่วงเงินงบประมาณที่ได้รับจัดสรรมีเพียง <strong>6,000 บาท</strong> ซึ่งต่ำกว่าราคามาตรฐาน จึงไม่เพียงพอต่อการจัดหาครุภัณฑ์ที่มีประสิทธิภาพเหมาะสมต่อการใช้งานในราชการ
                    </p>`,
                    bottomVal: 'ระดับ 4.0000 คะแนน (93.1818%) <span style="font-size: 18px; color: #facc15;">★★★★☆</span>',
                    bottomCallout: 'บรรลุเกณฑ์ระดับ 4: เบิกจ่ายงบลงทุนได้ 82,000 บาท คิดเป็นร้อยละ 93.1818 สูงกว่าเป้าหมาย ครม. (ร้อยละ 75) คะแนนถ่วงน้ำหนัก 2.0000 (0.1000)'
                },
                v2: {
                    scorePill: 'น้ำหนัก 2.5% | ผลงานระดับ 4 (97.7123%)',
                    activeRubric: 4,
                    cat1Val: '3,637,854.27 บาท',
                    cat1Desc: 'จากกรอบงบประมาณ 4,155,120.00 บาท สำหรับค่าใช้จ่ายด้านเงินเดือน ค่าจ้าง และบุคลากรของเงินทุนหมุนเวียนฯ',
                    cat2Val: '19,300,534.88 บาท',
                    cat2Desc: 'หมวดค่าตอบแทน ใช้สอยและวัสดุ บริหารจัดการภารกิจ การประชุมสัมมนา และพัฒนาระบบเทคโนโลยีสารสนเทศ',
                    cat3Val: '249,788,331.58 บาท',
                    cat3Desc: 'ธ.ก.ส. จ่ายเงินให้ผู้กู้ยืมแล้ว 619 ราย จากวงเงินอนุมัติ 250,000,000 บาท (คงเหลือวงเงิน 211,668.42 บาท)',
                    cat4Val: '82,000.00 บาท',
                    cat4Desc: 'เบิกจ่ายจัดซื้อครุภัณฑ์ 3 รายการ จากกรอบงบประมาณที่ได้รับอนุมัติ 88,000 บาท',
                    calcHtml: `<h4 style="color: #0369a1;">📐 สูตรการคำนวณการเบิกจ่ายภาพรวม</h4>
                    <div style="background: #ffffff; padding: 10px 14px; border-radius: 8px; border: 1px solid #bfdbfe; margin-top: 6px; font-family: monospace; font-size: 13px;">
                        (ผลการเบิกจ่ายภาพรวมในปี 2569 / แผนภาพรวม) × 100<br>
                        = (272,808,720.73 / 279,196,000.00) × 100<br>
                        = <strong>ร้อยละ 97.7123</strong> ของวงเงินที่ได้รับจัดสรร<br><br>
                        <span style="font-size: 11.5px; color: #64748b;">(กรณีรวมภาระผูกพันปีก่อน 6.02 ลบ.: 277.59 / 285.22 ลบ. = 97.3256%)</span>
                    </div>
                    <p style="margin-top: 8px; color: #334155;">
                        <strong>เทียบเกณฑ์ ครม.:</strong> เป้าหมาย ครม. กำหนดไม่น้อยกว่าร้อยละ 93 ผลการเบิกจ่ายจริง 97.7123% สูงกว่าเป้าหมาย ครม. บรรลุ <strong>ระดับ 4 (คะแนน 2.0000)</strong>
                    </p>`,
                    detailHtml: `<h4 style="color: #15803d;">🏦 รายละเอียดผลการเบิกจ่ายเงินกู้ยืม 3 ครั้ง (ธ.ก.ส.)</h4>
                    <ul style="margin-left: 18px; line-height: 1.6; color: #1e293b;">
                        <li><strong>ครั้งที่ 1 (27 ก.พ. 69):</strong> อนุมัติ 293 ราย เป็นเงิน 118,006,505.74 บาท</li>
                        <li><strong>ครั้งที่ 2 (27 มี.ค. 69):</strong> อนุมัติ 329 ราย เป็นเงิน 131,879,572.76 บาท</li>
                        <li><strong>ครั้งที่ 3 (20 ก.ค. 69):</strong> อนุมัติ 68 ราย เป็นเงิน 28,603,087.69 บาท</li>
                        <li><strong>ผลจ่ายเงินจริง ณ 30 ก.ย. 69:</strong> ธ.ก.ส. จัดทำสัญญาและจ่ายเงินแล้ว <strong>619 ราย เป็นเงิน 249,788,331.58 บาท</strong> (คงเหลือ 211,668.42 บาท)</li>
                    </ul>`,
                    bottomVal: 'ระดับ 4.0000 คะแนน (97.7123%) <span style="font-size: 18px; color: #facc15;">★★★★☆</span>',
                    bottomCallout: 'บรรลุเกณฑ์ระดับ 4: เบิกจ่ายงบภาพรวมได้ 272.81 ล้านบาท คิดเป็นร้อยละ 97.7123 สูงกว่าเป้าหมาย ครม. (ร้อยละ 93) คะแนนถ่วงน้ำหนัก 2.0000 (0.1000)'
                }
            }
        };

        /* Fiscal Year Switch */
        function changeFiscalYear(yr) {
            showToast(`เลือกดูข้อมูลปีงบประมาณ ${yr}`);
        }

        /* Quarter Switching */
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
            const t1 = document.getElementById('tbl-topic-1-text');
            if (t1) t1.innerHTML = data.table.t1;
            const t2 = document.getElementById('tbl-topic-2-text');
            if (t2) t2.innerHTML = data.table.t2;

            document.getElementById('tbl-score-1').innerText = data.table.s1;
            document.getElementById('tbl-wscore-1').innerText = data.table.ws1;
            document.getElementById('tbl-score-2').innerText = data.table.s2;
            document.getElementById('tbl-wscore-2').innerText = data.table.ws2;
            document.getElementById('tbl-total-level').innerText = data.table.totLevel;
            document.getElementById('tbl-total-wscore').innerText = data.table.totWScore;

            const tblCallout = document.getElementById('tbl-overview-callout');
            if (tblCallout) tblCallout.innerHTML = data.table.callout;

            // 2. View 1 Updates
            document.getElementById('v1-score-pill').innerText = data.v1.scorePill;
            const v1s2v = document.getElementById('v1-step2-val');
            if (v1s2v) v1s2v.innerText = data.v1.step2Val;
            const v1s2d = document.getElementById('v1-step2-desc');
            if (v1s2d) v1s2d.innerHTML = data.v1.step2Desc;
            const v1s3d = document.getElementById('v1-step3-desc');
            if (v1s3d) v1s3d.innerHTML = data.v1.step3Desc;
            const v1s4t = document.getElementById('v1-step4-title');
            if (v1s4t) v1s4t.innerText = data.v1.step4Title;
            const v1s4d = document.getElementById('v1-step4-desc');
            if (v1s4d) v1s4d.innerHTML = data.v1.step4Desc;

            const v1calc = document.getElementById('v1-calc-box');
            if (v1calc) v1calc.innerHTML = data.v1.calcHtml;
            const v1rsn = document.getElementById('v1-reason-box');
            if (v1rsn) v1rsn.innerHTML = data.v1.reasonHtml;

            document.getElementById('v1-bottom-val').innerHTML = data.v1.bottomVal;
            document.getElementById('v1-bottom-callout').innerText = data.v1.bottomCallout;
            updateRubricHighlight('v1', data.v1.activeRubric);

            // 3. View 2 Updates
            document.getElementById('v2-score-pill').innerText = data.v2.scorePill;
            const v2c1v = document.getElementById('v2-cat1-val');
            if (v2c1v) v2c1v.innerText = data.v2.cat1Val;
            const v2c1d = document.getElementById('v2-cat1-desc');
            if (v2c1d) v2c1d.innerHTML = data.v2.cat1Desc;

            const v2c2v = document.getElementById('v2-cat2-val');
            if (v2c2v) v2c2v.innerText = data.v2.cat2Val;
            const v2c2d = document.getElementById('v2-cat2-desc');
            if (v2c2d) v2c2d.innerHTML = data.v2.cat2Desc;

            const v2c3v = document.getElementById('v2-cat3-val');
            if (v2c3v) v2c3v.innerText = data.v2.cat3Val;
            const v2c3d = document.getElementById('v2-cat3-desc');
            if (v2c3d) v2c3d.innerHTML = data.v2.cat3Desc;

            const v2c4v = document.getElementById('v2-cat4-val');
            if (v2c4v) v2c4v.innerText = data.v2.cat4Val;
            const v2c4d = document.getElementById('v2-cat4-desc');
            if (v2c4d) v2c4d.innerHTML = data.v2.cat4Desc;

            const v2calc = document.getElementById('v2-calc-box');
            if (v2calc) v2calc.innerHTML = data.v2.calcHtml;
            const v2det = document.getElementById('v2-detail-box');
            if (v2det) v2det.innerHTML = data.v2.detailHtml;

            document.getElementById('v2-bottom-val').innerHTML = data.v2.bottomVal;
            document.getElementById('v2-bottom-callout').innerText = data.v2.bottomCallout;
            updateRubricHighlight('v2', data.v2.activeRubric);
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
                if (isEdit) {
                    el.style.outline = '1px dashed #3b82f6';
                    el.style.background = '#fefce8';
                } else {
                    el.style.outline = 'none';
                    el.style.background = '';
                }
            });

            if (isEdit) {
                showToast("เปิดโหมดแก้ไขข้อความแล้ว คลิกที่ข้อความเพื่อแก้ไข");
            } else {
                applyQuarterData(activeQuarter);
                showToast("กลับสู่โหมดนำเสนอ (Preview)");
            }
        }

        /* Local Storage Persistence */
        function getStorageKey(q) {
            return `kpi61_data_q${q}`;
        }

        function saveCustomData() {
            const payload = {
                summaryDesc: document.getElementById('summary-overview-desc').innerText,
                heroScore: document.getElementById('score-hero-val').innerText,
                updatedAt: new Date().toISOString()
            };
            localStorage.setItem(getStorageKey(activeQuarter), JSON.stringify(payload));
            showToast(`บันทึกข้อมูลไตรมาสที่ ${activeQuarter} ในเครื่องเรียบร้อยแล้ว`);
        }

        function loadCustomEdits(parsed) {
            if (parsed.summaryDesc) {
                document.getElementById('summary-overview-desc').innerText = parsed.summaryDesc;
            }
            if (parsed.heroScore) {
                document.getElementById('score-hero-val').innerText = parsed.heroScore;
            }
        }

        /* Export Dashboard PNG */
        function exportDashboardPNG() {
            const canvasEl = document.getElementById('presentation-canvas');
            showToast("กำลังประมวลผลรูปภาพ PNG ความละเอียดสูง...");
            html2canvas(canvasEl, {
                scale: 2,
                useCORS: true,
                backgroundColor: '#ffffff'
            }).then(canvas => {
                const link = document.createElement('a');
                link.download = `ตัวชี้วัดที่_6.1_การเบิกจ่ายงบประมาณ_Q${activeQuarter}.png`;
                link.href = canvas.toDataURL('image/png');
                link.click();
                showToast("ส่งออกรูปภาพ PNG สำเร็จแล้ว!");
            }).catch(err => {
                console.error(err);
                showToast("เกิดข้อผิดพลาดในการส่งออกภาพ");
            });
        }

        /* Copy Canvas to Clipboard */
        function copyDashboardToClipboard() {
            const canvasEl = document.getElementById('presentation-canvas');
            showToast("กำลังคัดลอกภาพไปยังคลิปบอร์ด...");
            html2canvas(canvasEl, { scale: 2, backgroundColor: '#ffffff' }).then(canvas => {
                canvas.toBlob(blob => {
                    if (navigator.clipboard && navigator.clipboard.write) {
                        navigator.clipboard.write([
                            new ClipboardItem({ 'image/png': blob })
                        ]).then(() => {
                            showToast("คัดลอกภาพลงคลิปบอร์ดแล้ว (พร้อมวางใน PowerPoint / Word)");
                        }).catch(() => showToast("เบราว์เซอร์ไม่อนุญาตให้เขียนคลิปบอร์ด"));
                    } else {
                        showToast("คลิปบอร์ดไม่รองรับ API นี้");
                    }
                });
            });
        }

        /* Export Full Page PDF */
        function exportDashboardPDF() {
            const { jsPDF } = window.jspdf;
            const canvasEl = document.getElementById('presentation-canvas');
            showToast("กำลังสร้างไฟล์เอกสาร PDF...");
            html2canvas(canvasEl, { scale: 2, backgroundColor: '#ffffff' }).then(canvas => {
                const imgData = canvas.toDataURL('image/jpeg', 0.95);
                const pdf = new jsPDF({
                    orientation: 'landscape',
                    unit: 'px',
                    format: [canvas.width / 2, canvas.height / 2]
                });
                pdf.addImage(imgData, 'JPEG', 0, 0, canvas.width / 2, canvas.height / 2);
                pdf.save(`ตัวชี้วัดที่_6.1_การเบิกจ่ายงบประมาณ_Q${activeQuarter}.pdf`);
                showToast("ส่งออกไฟล์ PDF สำเร็จแล้ว!");
            });
        }

        /* Fullscreen Toggle */
        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(err => {
                    showToast("ไม่สามารถเปิดโหมดเต็มจอได้: " + err.message);
                });
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                }
            }
        }

        /* Toast Feedback */
        function showToast(message) {
            const t = document.getElementById('toast');
            t.innerText = message;
            t.className = 'show';
            setTimeout(() => { t.className = t.className.replace('show', ''); }, 3200);
        }

        /* Initial Setup */
        window.addEventListener('DOMContentLoaded', () => {
            switchQuarter(4);
            switchTopicView(0);
        });
    </script>
</body>
</html>
'''
    with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 6.1.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("SUCCESS_BUILD_61")

if __name__ == '__main__':
    generate_kpi61()
