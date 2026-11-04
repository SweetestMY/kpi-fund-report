const http = require('http');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

async function testPage() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 3.3.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');

    const port = 9222;
    const chromeProc = spawn(chromePath, [
        '--headless=new',
        `--remote-debugging-port=${port}`,
        '--disable-gpu',
        '--window-size=1920,1080',
        fileUrl
    ]);

    await new Promise(r => setTimeout(r, 1500));

    // Get websocket URL
    const getJson = () => new Promise((resolve, reject) => {
        http.get(`http://127.0.0.1:${port}/json`, res => {
            let data = '';
            res.on('data', c => data += c);
            res.on('end', () => resolve(JSON.parse(data)));
        }).on('error', reject);
    });

    const targets = await getJson();
    const wsUrl = targets[0].webSocketDebuggerUrl;

    const WebSocket = require('child_process'); // we can use simple cdp or fetch
    console.log('Connected to target:', targets[0].title);

    chromeProc.kill();
}
