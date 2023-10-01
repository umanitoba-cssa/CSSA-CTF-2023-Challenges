# Kill Switch 2
- Reverse Engineering
- Medium
- 200 Points

## Description

This next command server seems to check the key using a regular expression. Can you reverse engineer a valid key?

## Solution
Reverse engineer the regex to create a valid string. One valid solution: `aaaaaa99999-poe40901-#waaaa#aaaaaw#-tttbdddjj`

*This challenge turned out to be quite difficult and probably should have been marked as Hard and worth 400 points.* One way to make it easier is to use a Regex parser like https://regex101.com/ which labels the exact function of each part of the regex string for you. 

The challenge was designed in such a way that most RegEx string generators (all of the ones I could find on the first page of Google) either do not work at all or do not produce a valid solution.

## Flag
`cssactf{7h4T5-mY-r3gu14R-Ex9r35s10N-a3fde4f5}`