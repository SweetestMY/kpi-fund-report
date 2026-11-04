# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ตัวชี้วัดที่ 4.1.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find CSS rules for .panel-box, .topic-view, #report-canvas
css_matches = re.findall(r'(\.(?:panel-box|topic-view|grid-split|rubric-5step-grid|overview-kpi-table|big-score-box)[^{]*\{[^}]*\})', text)
for m in css_matches:
    print(m)
    print('-'*40)
