const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const fs = require('fs');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 6.1.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9571;

    console.log("Starting Chrome with URL:", fileUrl);
    const chrome = spawn(chromePath, [
        '--headless=new',
        `--remote-debugging-port=${port}`,
        '--disable-gpu',
        '--window-size=1920,1080',
        fileUrl
    ]);

    await new Promise(r => setTimeout(r, 2000));

    const targets = await new Promise((resolve, reject) => {
        http.get(`http://127.0.0.1:${port}/json`, res => {
            let data = '';
            res.on('data', c => data += c);
            res.on('end', () => resolve(JSON.parse(data)));
        }).on('error', reject);
    });

    const pageTarget = targets.find(t => t.type === 'page');
    console.log("Connecting WebSocket to:", pageTarget.webSocketDebuggerUrl);
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
        let hasScore = await evaluate(`!!document.getElementById('score-hero-val')`);
        if (state === 'complete' && hasScore) {
            ready = true;
            break;
        }
        await new Promise(r => setTimeout(r, 200));
    }
    console.log("Page ready state:", ready);

    // 1. Verify Q4 (Default)
    console.log("\n=== 1. VERIFYING Q4 (DEFAULT) ===");
    let score = await evaluate(`document.getElementById('score-hero-val').innerText`);
    let s1 = await evaluate(`document.getElementById('tbl-score-1').innerText`);
    let s2 = await evaluate(`document.getElementById('tbl-score-2').innerText`);
    let tot = await evaluate(`document.getElementById('tbl-total-wscore').innerText`);
    console.log(`Q4 View 0: Score=${score}, S1=${s1}, S2=${s2}, Total=${tot}`);
    await captureScreenshot('kpi61_q4_v0.png');

    // Switch and test View 1
    await evaluate(`switchTopicView(1)`);
    await new Promise(r => setTimeout(r, 200));
    let v1Score = await evaluate(`document.getElementById('v1-score-pill').innerText`);
    console.log(`View 1 pill: ${v1Score}`);
    await captureScreenshot('kpi61_q4_v1.png');

    // Switch and test View 2
    await evaluate(`switchTopicView(2)`);
    await new Promise(r => setTimeout(r, 200));
    let v2Score = await evaluate(`document.getElementById('v2-score-pill').innerText`);
    console.log(`View 2 pill: ${v2Score}`);
    await captureScreenshot('kpi61_q4_v2.png');

    // 2. Test Quarter 3 Switch
    console.log("\n=== 2. VERIFYING Q3 ===");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(3)`);
    await new Promise(r => setTimeout(r, 300));
    let q3Score = await evaluate(`document.getElementById('score-hero-val').innerText`);
    let q3S1 = await evaluate(`document.getElementById('tbl-score-1').innerText`);
    let q3S2 = await evaluate(`document.getElementById('tbl-score-2').innerText`);
    console.log(`Q3 View 0: Score=${q3Score}, S1=${q3S1}, S2=${q3S2}`);
    await captureScreenshot('kpi61_q3_v0.png');

    // 3. Test Quarter 2 Switch
    console.log("\n=== 3. VERIFYING Q2 ===");
    await evaluate(`switchQuarter(2)`);
    await new Promise(r => setTimeout(r, 300));
    let q2Score = await evaluate(`document.getElementById('score-hero-val').innerText`);
    let q2S1 = await evaluate(`document.getElementById('tbl-score-1').innerText`);
    let q2S2 = await evaluate(`document.getElementById('tbl-score-2').innerText`);
    console.log(`Q2 View 0: Score=${q2Score}, S1=${q2S1}, S2=${q2S2}`);
    await captureScreenshot('kpi61_q2_v0.png');

    // 4. Test Quarter 1 Switch
    console.log("\n=== 4. VERIFYING Q1 ===");
    await evaluate(`switchQuarter(1)`);
    await new Promise(r => setTimeout(r, 300));
    let q1Score = await evaluate(`document.getElementById('score-hero-val').innerText`);
    console.log(`Q1 View 0: Score=${q1Score}`);
    await captureScreenshot('kpi61_q1_v0.png');

    // 5. Test Edit Mode
    console.log("\n=== 5. VERIFYING EDIT MODE ===");
    await evaluate(`setAppMode('edit')`);
    await new Promise(r => setTimeout(r, 200));
    await captureScreenshot('kpi61_edit_mode.png');
    await evaluate(`setAppMode('preview')`);

    // Reset to Q4 View 0
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
        console.log("SUCCESS: All KPI 6.1 tests passed with 0 errors!");
    }
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
