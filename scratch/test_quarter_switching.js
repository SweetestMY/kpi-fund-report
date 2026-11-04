const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const fs = require('fs');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 4.1.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9559;

    const chrome = spawn(chromePath, [
        '--headless=new',
        `--remote-debugging-port=${port}`,
        '--disable-gpu',
        '--window-size=1920,1080',
        fileUrl
    ]);

    await new Promise(r => setTimeout(r, 1200));

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

    async function captureScreenshot(filename) {
        const res = await send('Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync(filename, Buffer.from(res.data, 'base64'));
        console.log(`Saved screenshot: ${filename}`);
    }

    // 1. Initial State (Q4)
    console.log("=== CHECKING Q4 ===");
    let score = await evaluate(`document.getElementById('ov-sc-val').innerText`);
    let q4_v4_score = await evaluate(`document.getElementById('ov-r4-score').innerText`);
    let q4_v5_score = await evaluate(`document.getElementById('ov-r5-score').innerText`);
    console.log(`Q4 Total Score: ${score}, V4 Score: ${q4_v4_score}, V5 Score: ${q4_v5_score}`);
    await captureScreenshot('scratch/snap_q4_v0.png');

    // 2. Switch to Q3
    console.log("\n=== SWITCHING TO Q3 ===");
    await evaluate(`switchQuarter(3)`);
    await new Promise(r => setTimeout(r, 400));
    let q3_total = await evaluate(`document.getElementById('ov-sc-val').innerText`);
    let q3_v4 = await evaluate(`document.getElementById('ov-r4-score').innerText`);
    let q3_v5 = await evaluate(`document.getElementById('ov-r5-score').innerText`);
    let q3_v6 = await evaluate(`document.getElementById('ov-r6-score').innerText`);
    console.log(`Q3 Total: ${q3_total}, V4: ${q3_v4}, V5: ${q3_v5}, V6: ${q3_v6}`);
    await captureScreenshot('scratch/snap_q3_v0.png');

    // Switch to Topic 5 in Q3
    await evaluate(`switchTopicView(5)`);
    await new Promise(r => setTimeout(r, 300));
    let q3_t5_score = await evaluate(`document.getElementById('t5-sc-val').innerText`);
    console.log(`Q3 Topic 5 Score Box: ${q3_t5_score}`);
    await captureScreenshot('scratch/snap_q3_v5.png');

    // 3. Switch to Q2
    console.log("\n=== SWITCHING TO Q2 ===");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(2)`);
    await new Promise(r => setTimeout(r, 400));
    let q2_total = await evaluate(`document.getElementById('ov-sc-val').innerText`);
    let q2_v4 = await evaluate(`document.getElementById('ov-r4-score').innerText`);
    let q2_v5 = await evaluate(`document.getElementById('ov-r5-score').innerText`);
    let q2_v6 = await evaluate(`document.getElementById('ov-r6-score').innerText`);
    console.log(`Q2 Total: ${q2_total}, V4: ${q2_v4}, V5: ${q2_v5}, V6: ${q2_v6}`);
    await captureScreenshot('scratch/snap_q2_v0.png');

    // Switch to Topic 4 in Q2
    await evaluate(`switchTopicView(4)`);
    await new Promise(r => setTimeout(r, 300));
    let q2_t4_score = await evaluate(`document.getElementById('t4-sc-val').innerText`);
    console.log(`Q2 Topic 4 Score Box: ${q2_t4_score}`);
    await captureScreenshot('scratch/snap_q2_v4.png');

    // Switch to Topic 5 in Q2
    await evaluate(`switchTopicView(5)`);
    await new Promise(r => setTimeout(r, 300));
    let q2_t5_score = await evaluate(`document.getElementById('t5-sc-val').innerText`);
    console.log(`Q2 Topic 5 Score Box: ${q2_t5_score}`);
    await captureScreenshot('scratch/snap_q2_v5.png');

    // 4. Switch to Q1
    console.log("\n=== SWITCHING TO Q1 ===");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(1)`);
    await new Promise(r => setTimeout(r, 400));
    let q1_total = await evaluate(`document.getElementById('ov-sc-val').innerText`);
    let q1_v4 = await evaluate(`document.getElementById('ov-r4-score').innerText`);
    let q1_v5 = await evaluate(`document.getElementById('ov-r5-score').innerText`);
    console.log(`Q1 Total: ${q1_total}, V4: ${q1_v4}, V5: ${q1_v5}`);
    await captureScreenshot('scratch/snap_q1_v0.png');

    // Back to Q4
    await evaluate(`switchQuarter(4)`);
    await new Promise(r => setTimeout(r, 400));

    ws.close();
    chrome.kill();

    console.log("\nTotal Errors Caught:", errors.length);
    if (errors.length > 0) {
        console.error("Errors:", errors);
        process.exit(1);
    } else {
        console.log("ALL QUARTER TESTS PASSED WITH 0 ERRORS!");
    }
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
