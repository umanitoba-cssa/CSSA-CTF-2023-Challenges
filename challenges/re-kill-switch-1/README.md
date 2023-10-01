# Kill Switch 1
- Reverse Engineering
- Easy
- 100 Points

## Description

The AI learned to create malware and managed to build several botnets for nefarious purposes. We were able to find the command servers but the malware kill switch requires a key. Our prompt engineers were able to trick the AI into giving us the source code for one of the key validation algorithms, can you reverse engineer a valid deactivation key?

## Solution
Reverse the key from the provided validation.py file: `8PFRA-RZ6DI-BZ06Y-OG2SH-93CCP`

## Flag
`cssactf{c0mM4nD-4nd-C0nqu3R-1fea5e27}`