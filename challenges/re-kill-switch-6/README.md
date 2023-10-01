# Kill Switch 6
- Reverse Engineering
- Hard
- 400 Points

## Description

This is the last command server we could find. It seems to be using a native Linux binary to check the key. Probably needs to be decompiled, can you take a look?

## Solution
Open the binary in a decompiler like Ghidra, reverse the operations on the output string to get the valid input string `DXOQKUCZGJPWLRMHTEASVIFNBY`.

## Flag
`cssactf{C-7Hr0uGh-b1N4Ry-7e3002c9}`