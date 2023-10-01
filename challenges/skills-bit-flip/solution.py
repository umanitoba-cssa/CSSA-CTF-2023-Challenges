# usr/bin/env python
from PIL import Image
import os
import io

def flipbit(byte, bit):
    return (byte ^ (1 << bit)).to_bytes(1, 'big')

source = open('code.png', 'rb').read()

try:
    os.mkdir("out")
except:
    pass


# Loop through every bit in the source file
for i in range(len(source)):
    # Loop through every bit in the byte
    for j in range(8):
        # Flip the bit
        flipped = flipbit(source[i], j)
        new = source[:i] + flipped + source[i+1:]
        with open('out/bit-flip-%d-%d.png' % (i, j), 'wb') as f:
            f.write(new)