with open('scratch/kpi52_investigation.txt', 'r', encoding='utf-8') as f:
    text = f.read()

q2_pos = text.find('=== Q2:')
if q2_pos != -1:
    q2_text = text[q2_pos:]
    print("Q2 text length:", len(q2_text))
    with open('scratch/q2_52_extracted.txt', 'w', encoding='utf-8') as out:
        out.write(q2_text)
    print("Saved Q2 text to scratch/q2_52_extracted.txt")
