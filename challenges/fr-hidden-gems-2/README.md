# fr-hidden-gems-2
- Forensics
- Medium
- 250 Points

## Description
This goes deeper than we thought. It looks like the AI has already gotten access to the CSSA's website somehow. We don't know exactly what it changed, but whatever it did to the website could hold a clue to stopping it.

## Solution
Mia's headshot on the CSSA website has been replaced, the new version contains two hidden images. Players can be directed to the right picture by looking at the website's commit history on GitHub. Comparing the two images' binary contents in a diff tool will reveal the flag.

## Flag
`cssactf{3XEC_M0L3_1111}`