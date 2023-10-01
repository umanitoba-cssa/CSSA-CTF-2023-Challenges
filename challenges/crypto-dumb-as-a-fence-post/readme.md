# Dumb as a Fence Post
- Cryptography
- Medium
- 200 Points

## Description

Humans are a dumb as a fence post! So I think that this cipher will be right up your alley!

## Solution

A rail fence cipher is a type of encryption that uses a pattern like the following

W . . . E . . . C . . . R . . . U . . . O . . .
. E . R . D . S . O . E . E . R . N . T . N . E
. . A . . . I . . . V . . . D . . . A . . . C .

where you read along the diagonals. The number of key is the number of "rails"
are; in the example above there are 3 rails. To solve it you can just generate
all 20 rails and see if any of them work. You can just brute force it using an online
tool like https://www.boxentriq.com/code-breaking/rail-fence-cipher and just click
through all of the rails. You could also probably be clever and make a program that does
it for you, or use the placement of cssactf{} in the cipher to find it.

## Hints

https://en.wikipedia.org/wiki/Rail_fence_cipher

## Flag

`cssactf{Thequickbrownfoxjumpsoverthelazydog}`
