import io, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('d:/ตัวชี้วัด/form/ตัวชี้วัดที่ 6.1.html', 'r', encoding='utf-8') as f:
    html = f.read()

required_ids = [
    'score-hero-val', 'score-hero-stars', 'score-status-badge', 'metric-complete-val', 'metric-grade-val', 'summary-overview-desc',
    'tbl-score-1', 'tbl-wscore-1', 'tbl-score-2', 'tbl-wscore-2', 'tbl-total-level', 'tbl-total-wscore',
    'v1-score-pill', 'v1-bottom-val', 'v1-bottom-callout',
    'v1-rubric-1', 'v1-rubric-2', 'v1-rubric-3', 'v1-rubric-4', 'v1-rubric-5',
    'v2-score-pill', 'v2-bottom-val', 'v2-bottom-callout',
    'v2-rubric-1', 'v2-rubric-2', 'v2-rubric-3', 'v2-rubric-4', 'v2-rubric-5',
    'select-kpi-page', 'quarter-focus', 'select-year',
    'subtopic-0', 'subtopic-1', 'subtopic-2',
    'view-0', 'view-1', 'view-2',
    'format-toolbar', 'btn-mode-preview', 'btn-mode-edit'
]

missing = []
for rid in required_ids:
    if f'id="{rid}"' not in html and f"id='{rid}'" not in html:
        missing.append(rid)

if missing:
    print("MISSING IDs:", missing)
else:
    print("ALL REQUIRED IDs ARE PRESENT!")
