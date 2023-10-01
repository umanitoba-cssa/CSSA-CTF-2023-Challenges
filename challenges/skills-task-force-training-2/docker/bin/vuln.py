#!/usr/bin/env python

import sys
import random
import base64
from time import sleep

def print(*args, **kwargs):
    res = __builtins__.print(*args, **kwargs)
    sys.stdout.flush()
    return res

f = open("flag.txt", "r")
flag = f.read()
f.close()
    
def main():
    num1 = random.randint(100000, 999999)
    num2 = random.randint(100000, 999999)
    num3 = random.randint(100000, 999999)
    num4 = random.randint(100000, 999999)


    print("Hello Agent!\n\nGood work getting here. We have 4 skill testing problems for you.\n")
    
    print(f"First off, can you convert {num1} to hexadecimal? Don't worry about endianess or anything fancy like that, just looking for the number.")
    
    while True:
        res = input(f"Answer: ")

        try:
            if int(res, 16) == num1:
                break
        except:
            pass
        
        print("\nNot quite! Give it another shot.")

    print(f"\nGreat work. Next, can you convert {num2} to binary?")

    while True:
        res = input(f"Answer: ")

        try:
            if int(res, 2) == num2:
                break
        except:
            pass
        
        print("\nNot quite! Give it another shot.")

    print(f"\nExcellent work. Now lets try this in reverse. Can you convert {hex(num3)} from hexadecimal to decimal?")

    while True:
        res = input(f"Answer: ")

        try:
            if int(res) == num3:
                break
        except:
            pass
        
        print("\nNot quite! Give it another shot.")

    print(f"\nLast one. Can you convert {bin(num4)} from binary to decimal?")

    while True:
        res = input(f"Answer: ")

        try:
            if int(res) == num4:
                print("\nExcellent work.\n")
                break
        except:
            pass
        
        print("\nNot quite! Give it another shot.")


    sleep(2)
    print("Actually, lets try one more little challenge. Here is your flag, but it's encoded in base64. Can you decode it?\n")

    print(base64.b64encode(flag.encode("ascii")).decode("ascii"))

    print("\nGood luck out there Agent!\n")

    sleep(5)


if __name__ == "__main__":
    main()