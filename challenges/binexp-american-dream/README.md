# american-dream
- Binary Exploitation
- Medium
- 300 Points
- **Flash Challenge**

## Description

It seems the AI is trying to learn about our culture by creating an "american dream simulator". The gameplay is a bit... dull. I guess the goal is to buy a house, maybe give the game a shot and try to find a way to afford one?

Connect with netcat:

`nc american-dream.ctf.umanitobacssa.ca 11000`

Or with ncat:

`ncat american-dream.ctf.umanitobacssa.ca 11000`

## Solution
Game outputs save data as bytes encoded in base64 format. Three possible solutions:
1. Edit inventory to own a house
2. Edit money value (first 8 bytes) to >$2.1M and buy a house
3. Edit pay rate (bytes 9-12) to earn a lot of money and buy a house

Once player owns a house, check inventory and flag is printed.

## Flag
`cssactf{Im4g1N3-8Uy1nG-4-H0u53-1n-Th15-3c0NomY-0876d38a}`