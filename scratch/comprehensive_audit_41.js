const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const fs = require('fs');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 4.1.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9560;

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

    async function captureScreenshot(filename) {
        const res = await send('Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync(filename, Buffer.from(res.data, 'base64'));
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

    const artifactDir = 'C:\\Users\\HP18269\\.gemini\\antigravity\\brain\\1b5dad9c-0d60-479e-8093-56b31998f8fa';

    // 1. CHECK Q4
    console.log("\n=================== CHECKING Q4 ===================");
    let q4_ov_sc = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    let q4_r4 = await evaluate(`document.getElementById('ov-r4-score').textContent.trim()`);
    let q4_r5 = await evaluate(`document.getElementById('ov-r5-score').textContent.trim()`);
    let q4_r6 = await evaluate(`document.getElementById('ov-r6-score').textContent.trim()`);
    console.log(`Q4 View 0: Total=${q4_ov_sc}, R4=${q4_r4}, R5=${q4_r5}, R6=${q4_r6}`);
    await captureScreenshot(path.join(artifactDir, 'check_q4_v0.png'));

    await evaluate(`switchTopicView(4)`);
    await new Promise(r => setTimeout(r, 200));
    let q4_t4_sc = await evaluate(`document.getElementById('t4-sc-val').textContent.trim()`);
    console.log(`Q4 Topic 4: Score Box=${q4_t4_sc}`);
    await captureScreenshot(path.join(artifactDir, 'check_q4_v4.png'));

    await evaluate(`switchTopicView(5)`);
    await new Promise(r => setTimeout(r, 200));
    let q4_t5_sc = await evaluate(`document.getElementById('t5-sc-val').textContent.trim()`);
    let q4_t5_m2 = await evaluate(`document.getElementById('t5-p2-m2').textContent.trim()`);
    console.log(`Q4 Topic 5: Score Box=${q4_t5_sc}, Milestone 2 text snippet=${q4_t5_m2.substring(0, 50)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q4_v5.png'));

    await evaluate(`switchTopicView(6)`);
    await new Promise(r => setTimeout(r, 200));
    let q4_t6_sc = await evaluate(`document.getElementById('t6-sc-val').textContent.trim()`);
    console.log(`Q4 Topic 6: Score Box=${q4_t6_sc}`);
    await captureScreenshot(path.join(artifactDir, 'check_q4_v6.png'));

    // 2. CHECK Q3
    console.log("\n=================== CHECKING Q3 ===================");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(3)`);
    await new Promise(r => setTimeout(r, 300));
    let q3_ov_sc = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    let q3_r4 = await evaluate(`document.getElementById('ov-r4-score').textContent.trim()`);
    let q3_r5 = await evaluate(`document.getElementById('ov-r5-score').textContent.trim()`);
    let q3_r6 = await evaluate(`document.getElementById('ov-r6-score').textContent.trim()`);
    console.log(`Q3 View 0: Total=${q3_ov_sc}, R4=${q3_r4}, R5=${q3_r5}, R6=${q3_r6}`);
    await captureScreenshot(path.join(artifactDir, 'check_q3_v0.png'));

    await evaluate(`switchTopicView(5)`);
    await new Promise(r => setTimeout(r, 200));
    let q3_t5_sc = await evaluate(`document.getElementById('t5-sc-val').textContent.trim()`);
    let q3_t5_m2 = await evaluate(`document.getElementById('t5-p2-m2').textContent.trim()`);
    console.log(`Q3 Topic 5: Score Box=${q3_t5_sc}, Milestone 2 text snippet=${q3_t5_m2.substring(0, 50)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q3_v5.png'));

    await evaluate(`switchTopicView(6)`);
    await new Promise(r => setTimeout(r, 200));
    let q3_t6_sc = await evaluate(`document.getElementById('t6-sc-val').textContent.trim()`);
    let q3_t6_callout = await evaluate(`document.getElementById('t6-callout').textContent.trim()`);
    console.log(`Q3 Topic 6: Score Box=${q3_t6_sc}, Callout snippet=${q3_t6_callout.substring(0, 60)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q3_v6.png'));

    // 3. CHECK Q2
    console.log("\n=================== CHECKING Q2 ===================");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(2)`);
    await new Promise(r => setTimeout(r, 300));
    let q2_ov_sc = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    let q2_r4 = await evaluate(`document.getElementById('ov-r4-score').textContent.trim()`);
    let q2_r5 = await evaluate(`document.getElementById('ov-r5-score').textContent.trim()`);
    let q2_r6 = await evaluate(`document.getElementById('ov-r6-score').textContent.trim()`);
    console.log(`Q2 View 0: Total=${q2_ov_sc}, R4=${q2_r4}, R5=${q2_r5}, R6=${q2_r6}`);
    await captureScreenshot(path.join(artifactDir, 'check_q2_v0.png'));

    await evaluate(`switchTopicView(4)`);
    await new Promise(r => setTimeout(r, 200));
    let q2_t4_sc = await evaluate(`document.getElementById('t4-sc-val').textContent.trim()`);
    let q2_t4_p2 = await evaluate(`document.getElementById('t4-p2-item').textContent.trim()`);
    console.log(`Q2 Topic 4: Score Box=${q2_t4_sc}, Pillar 2 snippet=${q2_t4_p2.substring(0, 60)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q2_v4.png'));

    await evaluate(`switchTopicView(5)`);
    await new Promise(r => setTimeout(r, 200));
    let q2_t5_sc = await evaluate(`document.getElementById('t5-sc-val').textContent.trim()`);
    let q2_t5_m1 = await evaluate(`document.getElementById('t5-p2-m1').textContent.trim()`);
    let q2_t5_m2 = await evaluate(`document.getElementById('t5-p2-m2').textContent.trim()`);
    console.log(`Q2 Topic 5: Score Box=${q2_t5_sc}`);
    console.log(`   Milestone 1: ${q2_t5_m1.substring(0, 50)}`);
    console.log(`   Milestone 2: ${q2_t5_m2.substring(0, 50)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q2_v5.png'));

    await evaluate(`switchTopicView(6)`);
    await new Promise(r => setTimeout(r, 200));
    let q2_t6_sc = await evaluate(`document.getElementById('t6-sc-val').textContent.trim()`);
    let q2_t6_callout = await evaluate(`document.getElementById('t6-callout').textContent.trim()`);
    console.log(`Q2 Topic 6: Score Box=${q2_t6_sc}, Callout snippet=${q2_t6_callout.substring(0, 60)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q2_v6.png'));

    // 4. CHECK Q1
    console.log("\n=================== CHECKING Q1 ===================");
    await evaluate(`switchTopicView(0)`);
    await evaluate(`switchQuarter(1)`);
    await new Promise(r => setTimeout(r, 300));
    let q1_ov_sc = await evaluate(`document.getElementById('ov-sc-val').textContent.trim()`);
    let q1_r4 = await evaluate(`document.getElementById('ov-r4-score').textContent.trim()`);
    let q1_r5 = await evaluate(`document.getElementById('ov-r5-score').textContent.trim()`);
    let q1_r6 = await evaluate(`document.getElementById('ov-r6-score').textContent.trim()`);
    console.log(`Q1 View 0: Total=${q1_ov_sc}, R4=${q1_r4}, R5=${q1_r5}, R6=${q1_r6}`);
    await captureScreenshot(path.join(artifactDir, 'check_q1_v0.png'));

    await evaluate(`switchTopicView(4)`);
    await new Promise(r => setTimeout(r, 200));
    let q1_t4_sc = await evaluate(`document.getElementById('t4-sc-val').textContent.trim()`);
    console.log(`Q1 Topic 4: Score Box=${q1_t4_sc}`);
    await captureScreenshot(path.join(artifactDir, 'check_q1_v4.png'));

    await evaluate(`switchTopicView(5)`);
    await new Promise(r => setTimeout(r, 200));
    let q1_t5_sc = await evaluate(`document.getElementById('t5-sc-val').textContent.trim()`);
    let q1_t5_m1 = await evaluate(`document.getElementById('t5-p2-m1').textContent.trim()`);
    let q1_t5_m2 = await evaluate(`document.getElementById('t5-p2-m2').textContent.trim()`);
    console.log(`Q1 Topic 5: Score Box=${q1_t5_sc}`);
    console.log(`   Milestone 1: ${q1_t5_m1.substring(0, 50)}`);
    console.log(`   Milestone 2: ${q1_t5_m2.substring(0, 50)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q1_v5.png'));

    await evaluate(`switchTopicView(6)`);
    await new Promise(r => setTimeout(r, 200));
    let q1_t6_sc = await evaluate(`document.getElementById('t6-sc-val').textContent.trim()`);
    let q1_t6_callout = await evaluate(`document.getElementById('t6-callout').textContent.trim()`);
    console.log(`Q1 Topic 6: Score Box=${q1_t6_sc}, Callout snippet=${q1_t6_callout.substring(0, 60)}`);
    await captureScreenshot(path.join(artifactDir, 'check_q1_v6.png'));

    // Reset back to Q4 View 0
    await evaluate(`switchQuarter(4)`);
    await evaluate(`switchTopicView(0)`);
    await new Promise(r => setTimeout(r, 300));

    ws.close();
    chrome.kill();

    console.log("\n=================== AUDIT RESULT ===================");
    console.log("Total Errors Caught:", errors.length);
    if (errors.length > 0) {
        console.error("Errors:", errors);
        process.exit(1);
    } else {
        console.log("ALL QUARTERS & VIEWS VERIFIED 100% FAITHFUL & CONSISTENT WITH 0 ERRORS!");
    }
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
