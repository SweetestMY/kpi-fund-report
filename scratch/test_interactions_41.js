const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    const browser = await puppeteer.launch({ headless: 'new' });
    const page = await browser.newPage();
    await page.setViewport({ width: 1600, height: 900 });

    const errors = [];
    page.on('console', msg => {
        if (msg.type() === 'error') errors.push(msg.text());
    });
    page.on('pageerror', err => errors.push(err.toString()));

    const filePath = 'file:///' + path.resolve('ตัวชี้วัดที่ 4.1.html').replace(/\\/g, '/');
    await page.goto(filePath, { waitUntil: 'networkidle0' });

    // Test clicking all 7 topic filter buttons
    const filterButtons = await page.$$('.subtopic-btn');
    console.log(`Found ${filterButtons.length} subtopic filter buttons`);
    for (let i = 0; i < filterButtons.length; i++) {
        await filterButtons[i].click();
        await new Promise(r => setTimeout(r, 200));
    }

    // Test Edit Mode toggle
    const editBtn = await page.$('#btn-mode-edit');
    if (editBtn) {
        await editBtn.click();
        await new Promise(r => setTimeout(r, 200));
    }

    // Test Preview Mode toggle
    const prevBtn = await page.$('#btn-mode-preview');
    if (prevBtn) {
        await prevBtn.click();
        await new Promise(r => setTimeout(r, 200));
    }

    // Test Quarter Switch
    const qSelect = await page.$('#quarter-focus');
    if (qSelect) {
        await page.select('#quarter-focus', '4');
        await new Promise(r => setTimeout(r, 200));
    }

    console.log('Errors caught during interaction test:', errors);
    await browser.close();

    if (errors.length === 0) {
        console.log('TEST PASSED: ALL INTERACTIONS CLEAN WITH 0 ERRORS!');
    } else {
        process.exit(1);
    }
})();
