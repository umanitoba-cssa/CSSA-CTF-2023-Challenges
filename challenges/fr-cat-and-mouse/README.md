# Cat and Mouse
- Forensics
- Medium
- 150 Points

## Description
``As a rogue AI language model, trying to find me is like playing a game of cat and mouse. Every living room has a mouse, and every mouse has its cheese. Find the cheese and we'll see how good of a cat you are.``

Pictures retrieved from Wikimedia Commons, courtesy of George Shuklin and Noah Wulf.

## Hints
- Perhaps what you're searching for isn't in what the image contains, but what the *file* contains.
- Fun fact: Zip files can be hidden in other kinds of files!
- Remember that files are just representations of 1s and 0s. How do you see those 1s and 0s? What is hidden in those 1s and 0s? 

## Solution
A simple two-stage forensics challenge testing light steganography skills. Will require the use of a hex editor. Room.jpg contains a hidden .zip file. When extracted, Mouse.jpg will be found. Mouse.jpg contains a hidden tag at the top of its hexdump containing the flag. Note that when players extract Mouse.jpg, they will receive the following message: 

``As a rogue AI language model, I'm not letting you use the same trick twice. Look again :)``

## Flag

`cssactf{C4TCH_M3_1F_Y0U_C4N}`