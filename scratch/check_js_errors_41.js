const { spawn } = require('child_process');
const http = require('http');
const path = require('path');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 4.1.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9558;

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

    for (let i = 0; i <= 6; i++) {
        await send('Runtime.evaluate', { expression: `switchTopicView(${i})` });
        await new Promise(r => setTimeout(r, 100));
    }

    await send('Runtime.evaluate', { expression: "setAppMode('edit')" });
    await new Promise(r => setTimeout(r, 100));
    await send('Runtime.evaluate', { expression: "setAppMode('preview')" });
    await new Promise(r => setTimeout(r, 100));

    console.log('Total JS Errors caught in 4.1:', errors.length);
    if (errors.length > 0) {
        console.error('Errors:', JSON.stringify(errors, null, 2));
    } else {
        console.log('PERFECT: 0 JS ERRORS IN KPI 4.1!');
    }

    ws.close();
    chrome.kill();
}

main().catch(console.error);
