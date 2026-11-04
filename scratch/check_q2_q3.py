with open('scratch/kpi52_investigation.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
q2_sec = text[text.find('Q2:'):text.find('Q3:')] if 'Q3:' in text else text[text.find('Q2:'):]
print("Q2 section length:", len(q2_sec))

q3_sec = text[text.find('Q3:'):text.find('Q2:')]
print("Q3 section length:", len(q3_sec))
