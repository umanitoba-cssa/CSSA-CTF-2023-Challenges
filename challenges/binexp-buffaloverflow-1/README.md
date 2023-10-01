# buffaloverflow-1
- Binary Exploitation
- Easy
- 150 Points

## Description

The AI is using its neural network to generate amazing buffalo facts and hiding them from us! We were able to leak the source code and binary for its security program which protects the buffalo facts, see if you can exploit it to enlighten yourself with fascinating buffalo trivia.

Connect with ncat:

`ncat buffaloverflow-1.ctf.umanitobacssa.ca 14000`

Or with netcat:

`nc buffaloverflow-1.ctf.umanitobacssa.ca 14000`

## Solution
Overflow the buffer with any characters to replace the correct password on the stack. Just input a lot of AAAAAAA.... will work. Inputting too many characters will cause the system function to fail so be careful!

Good introduction to buffer overflow exploits: https://medium.com/techloop/understanding-buffer-overflow-vulnerability-85ac22ec8cd3

## Flag
`cssactf{4n-0v3rFl0W-0F-8uFf41o-kN0wl3dG3-9a0177f1}`