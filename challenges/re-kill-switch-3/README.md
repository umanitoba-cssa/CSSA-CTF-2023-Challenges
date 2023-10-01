# Kill Switch 3
- Reverse Engineering
- Medium
- 250 Points

## Description

This next command server uses Java. The bit math here seems tricky. Can you figure out the key? Looks like it should be 10 ASCII characters.

## Solution
Reverse the bit math to get the key `D9WHV8HFKJ`. Mix of operations here, and requires solving a linear system.

A player noticed a bug with the code, the Java code has an integer literal written as `10111000` without the `0b` in front by mistake. This makes Java parse it as a normal base-10 integer. The challenge can still be solved, there are just unintentionally multiple valid letters for some positions due to this.

## Flag
`cssactf{Ju57-4-b1T-0f-m4TH-bf6b47f3}`