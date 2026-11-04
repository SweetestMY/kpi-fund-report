const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const chromePath = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"';
const htmlPath = path.resolve('ตัวชี้วัดที่ 3.3.html');
const outPng = 'C:\\Users\\HP18269\\.gemini\\antigravity\\brain\\1b5dad9c-0d60-479e-8093-56b31998f8fa\\verify_preview_33_fixed.png';

const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');

console.log('Rendering:', fileUrl);
const cmd = `${chromePath} --headless=new --disable-gpu --window-size=1920,1080 --screenshot="${outPng}" "${fileUrl}"`;
try {
    execSync(cmd, { stdio: 'inherit', timeout: 15000 });
    console.log('Screenshot saved to:', outPng);
    if (fs.existsSync(outPng)) {
        console.log('File size:', fs.statSync(outPng).size);
    }
} catch (e) {
    console.error('Render error:', e);
}
