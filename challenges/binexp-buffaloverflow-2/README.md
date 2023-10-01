# buffaloverflow-2
- Binary Exploitation
- Medium
- 250 Points

## Description

The AI has upgraded it's security and the buffalo facts are even harder to get now! See if you can crack this binary too.

Connect with ncat:

`ncat buffaloverflow-2.ctf.umanitobacssa.ca 14001`

Or with netcat:

`nc buffaloverflow-2.ctf.umanitobacssa.ca 14001`

## Solution
Need to overwrite the return address on the stack to jump to fact() function. See solution.py.

Good introduction to buffer overflow exploits: https://medium.com/techloop/understanding-buffer-overflow-vulnerability-85ac22ec8cd3

## Flag
`cssactf{R37uRn-t0-8uFF4L0-Fac7$-2c14afb3}`