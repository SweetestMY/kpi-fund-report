# -*- coding: utf-8 -*-
with open('ตัวชี้วัดที่ 3.3.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add purgeLegacyKeys right after <script>
old_script_start = '<script>\n        let lastFocusedElement = null;'
new_script_start = '''<script>
        // Purge legacy cached draft keys from earlier version so user browser immediately renders official N/A
        try {
            ['kpi_official_33_Q1', 'kpi_official_33_Q2', 'kpi_official_33_Q3', 'kpi_official_33_Q4'].forEach(k => {
                localStorage.removeItem(k);
            });
        } catch(e) {}

        let lastFocusedElement = null;'''

assert old_script_start in text, "old_script_start not found"
text = text.replace(old_script_start, new_script_start, 1)

# 2. Change resetQuarterDefaults to do location.reload()
old_reset = '''        function resetQuarterDefaults() {
            if (confirm(`ต้องการคืนค่าเริ่มต้นสำหรับ "ไตรมาส ${activeQuarter}" ใช่หรือไม่? ข้อมูลที่แก้ไขจะถูกรีเซ็ต`)) {
                localStorage.removeItem(getStorageKey(activeQuarter));
                applyQuarterDefault(activeQuarter);
                showToast(`🔄 คืนค่าเริ่มต้นไตรมาส ${activeQuarter} แล้ว`);
            }
        }'''

new_reset = '''        function resetQuarterDefaults() {
            if (confirm(`ต้องการคืนค่าเริ่มต้นสำหรับ "ไตรมาส ${activeQuarter}" ใช่หรือไม่? ข้อมูลที่แก้ไขจะถูกรีเซ็ต`)) {
                localStorage.removeItem(getStorageKey(activeQuarter));
                location.reload();
            }
        }'''

assert old_reset in text, "old_reset not found"
text = text.replace(old_reset, new_reset, 1)

# 3. Change STORAGE_KEY_PREFIX
old_prefix = "const STORAGE_KEY_PREFIX = 'kpi_official_33_Q';"
new_prefix = "const STORAGE_KEY_PREFIX = 'kpi_official_33_v2_Q';"

assert old_prefix in text, "old_prefix not found"
text = text.replace(old_prefix, new_prefix, 1)

# 4. Change exportDataBackup check
old_backup = "if (k.startsWith('kpi_official_33_Q')) {"
new_backup = "if (k.startsWith('kpi_official_33_v2_Q')) {"

assert old_backup in text, "old_backup not found"
text = text.replace(old_backup, new_backup, 1)

with open('ตัวชี้วัดที่ 3.3.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated ตัวชี้วัดที่ 3.3.html")
