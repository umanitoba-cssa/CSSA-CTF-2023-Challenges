# Kill Switch 5
- Reverse Engineering
- Hard
- 350 Points

## Description

Another validator binary. A DLL file, probably compiled from C#? You should be able to decompile this, see if you can figure out the key.

## Solution
Open the DLL file in a .NET decompiler like ilSpy or DotPeek, then run the operations on the output string in reverse to get the valid input string `syu3Gx8ywQ0bs1XPLOj3EzdeoMueHRxt`.

The easiest way to do this is to install C# and use a binary writer to write the bytes in reverse. See solution.cs

**This was the only challenge in the competition to remain unsolved.**

## Flag
`cssactf{Ju57-4-qu1C5-p33K-f75bf4a5}`