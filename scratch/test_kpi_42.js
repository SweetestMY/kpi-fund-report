const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const fs = require('fs');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 4.2.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9561;

    const chrome = spawn(chromePath, [
        '--headless=new',
        `--remote-debugging-port=${port}`,
        '--disable-gpu',
        '--window-size=1920,1080',
        fileUrl
    ]);

    await new Promise(r => setTimeout(r, 1500));

    const targets = await new Promise((resolve, reject) => {
        http.get(`http://127.0.0.1:${port}/json`, res => {
            let data = '';
            res.on('data', c => data += c);
            res.on('end', () => resolve(JSON.parse(data)));
        }).on('error', reject);
    });

    const pageTarget = targets.find(t => t.type === 'page');
    const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);

    let id = 1;
    const callbacks = new Map();
    const errors = [];

    ws.onmessage = (event) => {
        const msg = JSON.parse(event.data);
        if (msg.method === 'Runtime.consoleAPICalled' && msg.params.type === 'error') {
            errors.push('Console Error: ' + JSON.stringify(msg.params.args));
        }
        if (msg.method === 'Runtime.exceptionThrown') {
            errors.push('Exception: ' + JSON.stringify(msg.params.exceptionDetails));
        }
        if (msg.id && callbacks.has(msg.id)) {
            callbacks.get(msg.id)(msg.result);
            callbacks.delete(msg.id);
        }
    };

    function send(method, params = {}) {
        return new Promise((resolve) => {
            const currentId = id++;
            callbacks.set(currentId, resolve);
            ws.send(JSON.stringify({ id: currentId, method, params }));
        });
    }

    await new Promise(r => ws.onopen = r);
    await send('Runtime.enable');
    await send('Page.enable');
    await send('DOM.enable');

    async function evaluate(expression) {
        const res = await send('Runtime.evaluate', { expression, returnByValue: true });
        return res.result ? res.result.value : null;
    }

    const artifactDir = 'C:\\Users\\HP18269\\.gemini\\antigravity\\brain\\1b5dad9c-0d60-479e-8093-56b31998f8fa';
    async function captureScreenshot(filename) {
        const fullPath = path.join(artifactDir, filename);
        const res = await send('Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync(fullPath, Buffer.from(res.data, 'base64'));
        console.log(`Saved screenshot: ${filename}`);
    }

    // Wait until document ready
    let ready = false;
    for (let i = 0; i < 20; i++) {
        let state = await evaluate(`document.readyState`);
        let hasOv = await evaluate(`!!document.getElementById('ov-sc-val')`);
        if (state === 'complete' && hasOv) {
            ready = true;
            break;
        }
        await new Promise(r => setTimeout(r, 200));
    }
    console.log("Page ready state:", ready);

    // 1. Check Q4 (Overview & Sub-views)
    console.log("\n=== 1. VERIFYING Q4 (DEFAULT STATE) ===");
    let q4_score = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    let q4_r1 = await evaluate(`document.getElementById('ov-r1-score').textContent.trim()`);
    let q4_r2 = await evaluate(`document.getElementById('ov-r2-score').textContent.trim()`);
    let q4_r3 = await evaluate(`document.getElementById('ov-r3-score').textContent.trim()`);
    console.log(`Q4 View 0: Total Score=${q4_score}, Sub1=${q4_r1}, Sub2=${q4_r2}, Sub3=${q4_r3}`);
    await captureScreenshot('kpi42_q4_v0.png');

    await evaluate(`switchTopicView(1)`);
    await new Promise(r => setTimeout(r, 200));
    let q4_v1_sc = await evaluate(`document.getElementById('t1-sc-val').textContent.trim()`);
    console.log(`Q4 View 1 Score: ${q4_v1_sc}`);
    await captureScreenshot('kpi42_q4_v1.png');

    await evaluate(`switchTopicView(2)`);
    await new Promise(r => setTimeout(r, 200));
    let q4_v2_sc = await evaluate(`document.getElementById('t2-sc-val').textContent.trim()`);
    console.log(`Q4 View 2 Score: ${q4_v2_sc}`);
    await captureScreenshot('kpi42_q4_v2.png');

    await evaluate(`switchTopicView(3)`);
    await new Promise(r => setTimeout(r, 200));
    let q4_v3_sc = await evaluate(`document.getElementById('t3-sc-val').textContent.trim()`);
    console.log(`Q4 View 3 Score: ${q4_v3_sc}`);
    await captureScreenshot('kpi42_q4_v3.png');

    // 2. Check Q3
    console.log("\n=== 2. VERIFYING Q3 ===");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(3)`);
    await new Promise(r => setTimeout(r, 300));
    let q3_score = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    let q3_r1 = await evaluate(`document.getElementById('ov-r1-score').textContent.trim()`);
    console.log(`Q3 View 0: Total Score=${q3_score}, Sub1=${q3_r1}`);
    await captureScreenshot('kpi42_q3_v0.png');

    // 3. Check Q2
    console.log("\n=== 3. VERIFYING Q2 ===");
    await evaluate(`switchQuarter(2)`);
    await new Promise(r => setTimeout(r, 300));
    let q2_score = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    let q2_summary = await evaluate(`document.getElementById('ov-summary-desc').textContent.trim()`);
    console.log(`Q2 View 0: Total Score=${q2_score}`);
    console.log(`Q2 Summary snippet: ${q2_summary.substring(0, 80)}`);
    await captureScreenshot('kpi42_q2_v0.png');

    await evaluate(`switchTopicView(1)`);
    await new Promise(r => setTimeout(r, 200));
    let q2_v1_sc = await evaluate(`document.getElementById('t1-sc-val').textContent.trim()`);
    console.log(`Q2 View 1 Score: ${q2_v1_sc}`);
    await captureScreenshot('kpi42_q2_v1.png');

    // 4. Check Q1
    console.log("\n=== 4. VERIFYING Q1 ===");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(1)`);
    await new Promise(r => setTimeout(r, 300));
    let q1_score = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    console.log(`Q1 View 0: Total Score=${q1_score}`);
    await captureScreenshot('kpi42_q1_v0.png');

    // 5. Check Edit Mode Toggle
    console.log("\n=== 5. VERIFYING EDIT MODE ===");
    await evaluate(`setMode('edit')`);
    await new Promise(r => setTimeout(r, 200));
    let formatBarDisplay = await evaluate(`document.getElementById('formatBar').style.display`);
    console.log(`Edit Mode Format Bar Display: ${formatBarDisplay}`);
    await captureScreenshot('kpi42_edit_mode.png');

    // Switch back to Preview and Q4 View 0
    await evaluate(`setMode('preview')`);
    await evaluate(`switchQuarter(4)`);
    await evaluate(`switchTopicView(0)`);
    await new Promise(r => setTimeout(r, 300));

    ws.close();
    chrome.kill();

    console.log("\n=================== TEST RESULTS ===================");
    console.log("Total Errors Caught:", errors.length);
    if (errors.length > 0) {
        console.error("Errors:", errors);
        process.exit(1);
    } else {
        console.log("SUCCESS: All KPI 4.2 tests passed with 0 errors!");
    }
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
