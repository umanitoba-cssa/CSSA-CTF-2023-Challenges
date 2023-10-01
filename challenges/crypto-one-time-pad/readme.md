# one-time-pad
- Cryptography
- Medium
- 250 Points

## Description

The AI system is learning slowly how to encrypt their messages! We were able to intercept a message over the wire it was sending to its other AI friend who lives across the world, but we were also able to intercept a message saying it was encrypted using one time pad. However the AI got lazy and only used a key that was 8 bytes, but the message is 21 bytes! See if we can use this oversight to our advantage.

## Hints

The key is encrypted in the format cssactf{<message>}
Convert your binary output to ascii via UTF
Repeat the 8 byte key to get the real key

## Solution

One time pad uses XOR with the message and the key to create the cipher text. Here I converted ascii to binary and encrypted using an 8 byte key.

They know what the first 8 bytes of the message are (cssactf{). Thus we can figure out the key by XORing the message and the cipher text. Once we have the key we concatenate it to itself until you have the length of the cipher text. Then preform the trivial decryption algorithm.

message (in binary):
0110001101110011011100110110000101100011011101000110011001111011010010000110010101111001010111110110011001110010011010010110010101101110011001000010110001101000011011110111011101011111011000010111001001100101010111110111100101101111011101010011111101111101

key (8 bytes) = 0110100100100100101001111000010001101000010111001111110100111001

actual key = 0110100100100100101001111000010001101000010111001111110100111001011010010010010010100111100001000110100001011100111111010011100101101001001001001010011110000100011010000101110011111101001110010110100100100100101001111000010001101000010111001111110100111001

cipher text = 0000101001010111110101001110010100001011001010001001101101000010001000010100000111011110110110110000111000101110100101000101110000000111010000001000101111101100000001110010101110100010010110000001101101000001111110001111110100000111001010011100001001000100

## Flag

`cssactf{Hey_friend,how_are_you?}`
