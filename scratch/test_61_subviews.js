const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const fs = require('fs');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 6.1.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9572;

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

    // Switch to Q2, View 1
    await evaluate(`switchQuarter(2)`);
    await evaluate(`switchTopicView(1)`);
    await new Promise(r => setTimeout(r, 300));
    let v1Q2 = await evaluate(`document.getElementById('v1-bottom-val').innerText`);
    console.log("Q2 View 1:", v1Q2);
    await captureScreenshot('kpi61_q2_v1.png');

    // Switch to Q2, View 2
    await evaluate(`switchTopicView(2)`);
    await new Promise(r => setTimeout(r, 300));
    let v2Q2 = await evaluate(`document.getElementById('v2-bottom-val').innerText`);
    console.log("Q2 View 2:", v2Q2);
    await captureScreenshot('kpi61_q2_v2.png');

    ws.close();
    chrome.kill();

    console.log("Q2 subviews test completed with", errors.length, "errors");
}

main().catch(err => {
    console.error(err);
    process.exit(1);
});
