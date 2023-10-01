# Kill Switch 4
- Reverse Engineering
- Medium
- 300 Points

## Description

The AI is getting smarter and our prompt engineers are no longer able to make the AI leak the source code for the key validation. We were however able to find a backdoor into the command server and grab the binary for key validator. This one is using a JAR file, can you decompile it and reverse engineer a valid key?

## Solution
Open the JAR file in a decompiler like jd-gui to see the java source code, then run the operations on the output string in reverse to get the valid input string `HASVTVQAZX`.

## Flag
`cssactf{s0-m4Ny-c0oK13s-1n-7h3-j4R-7ab7cf42}`