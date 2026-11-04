const { spawn } = require('child_process');
const http = require('http');
const path = require('path');

async function main() {
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    const htmlPath = path.resolve('ตัวชี้วัดที่ 4.1.html');
    const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
    const port = 9557;

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

    ws.onmessage = msg => {
        const data = JSON.parse(msg.data);
        if (data.id && pending.has(data.id)) {
            pending.get(data.id)(data.result);
            pending.delete(data.id);
        }
    };

    const send = (method, params = {}) => new Promise(res => {
        const curId = id++;
        pending.set(curId, res);
        ws.send(JSON.stringify({ id: curId, method, params }));
    });

    await new Promise(r => ws.onopen = r);
    await send('Runtime.enable');

    const res = await send('Runtime.evaluate', { expression: `
        (() => {
            const th = document.getElementById('ov-th-1');
            const scoreBox = document.querySelector('#view-topic-0 .big-score-box');
            return {
                thBg: th ? window.getComputedStyle(th).backgroundImage : null,
                thBgColor: th ? window.getComputedStyle(th).backgroundColor : null,
                thColor: th ? window.getComputedStyle(th).color : null,
                scoreBoxBg: scoreBox ? window.getComputedStyle(scoreBox).backgroundImage : null,
                scoreBoxBgColor: scoreBox ? window.getComputedStyle(scoreBox).backgroundColor : null,
                scoreBoxColor: scoreBox ? window.getComputedStyle(scoreBox).color : null,
            };
        })()
    `, returnByValue: true });

    console.log('Styles:', JSON.stringify(res.result.value, null, 2));

    ws.close();
    chrome.kill();
}

main().catch(console.error);
