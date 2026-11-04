const { spawn } = require('child_process');
const http = require('http');
const path = require('path');
const fs = require('fs');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 3.3.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9333;

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
    if (!pageTarget) {
        console.error('No page target found');
        chrome.kill();
        return;
    }

    const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
    let id = 1;
    const pending = new Map();
    const errors = [];

    ws.onmessage = msg => {
        const data = JSON.parse(msg.data);
        if (data.id && pending.has(data.id)) {
            pending.get(data.id)(data.result);
            pending.delete(data.id);
        }
        if (data.method === 'Runtime.exceptionThrown') {
            errors.push(data.params.exceptionDetails);
        }
        if (data.method === 'Runtime.consoleAPICalled' && data.params.type === 'error') {
            errors.push(data.params.args);
        }
    };

    const send = (method, params = {}) => new Promise(res => {
        const curId = id++;
        pending.set(curId, res);
        ws.send(JSON.stringify({ id: curId, method, params }));
    });

    await new Promise(r => ws.onopen = r);
    await send('Runtime.enable');
    await send('Page.enable');

    console.log('Testing interactive functions...');
    // Test edit mode
    await send('Runtime.evaluate', { expression: "setAppMode('edit')" });
    await new Promise(r => setTimeout(r, 300));
    const editSnap = await send('Page.captureScreenshot');
    fs.writeFileSync('C:\\Users\\HP18269\\.gemini\\antigravity\\brain\\1b5dad9c-0d60-479e-8093-56b31998f8fa\\verify_edit_mode_33.png', Buffer.from(editSnap.data, 'base64'));

    // Test preview mode
    await send('Runtime.evaluate', { expression: "setAppMode('preview')" });
    await new Promise(r => setTimeout(r, 300));
    const previewSnap = await send('Page.captureScreenshot');
    fs.writeFileSync('C:\\Users\\HP18269\\.gemini\\antigravity\\brain\\1b5dad9c-0d60-479e-8093-56b31998f8fa\\verify_preview_33.png', Buffer.from(previewSnap.data, 'base64'));

    // Test quarter switching
    await send('Runtime.evaluate', { expression: "switchQuarter(3)" });
    await new Promise(r => setTimeout(r, 200));
    await send('Runtime.evaluate', { expression: "switchQuarter(4)" });
    await new Promise(r => setTimeout(r, 200));

    console.log('Errors caught:', errors.length);
    if (errors.length > 0) {
        console.error('JS Errors:', JSON.stringify(errors, null, 2));
    } else {
        console.log('SUCCESS: 0 JS ERRORS!');
    }

    ws.close();
    chrome.kill();
}

main().catch(console.error);
