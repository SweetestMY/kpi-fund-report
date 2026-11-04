# -*- coding: utf-8 -*-
with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("STORAGE_KEY_PREFIX present:", "STORAGE_KEY_PREFIX = 'kpi_official_33_v2_Q'" in text)
print("Purge logic present:", "kpi_official_33_Q1" in text and "localStorage.removeItem" in text)
print("Backup v2 check present:", "kpi_official_33_v2_Q" in text)
