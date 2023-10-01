# fr-scavenger-hunt-1
- Forensics
- Easy
- 150 Points

## Description
We're detecting some strange patterns in the AI's outgoing messages. See if you can trace these abnormal files to their source.

## Solution
Run the image through [this LSB decoder](https://stylesuxx.github.io/steganography/) to find a URL. Download the image in the URL and run that through the LSB encoder to find the flag.

## Flag
`cssactf{W3LC0M3_b@ck_2_U0FM}`