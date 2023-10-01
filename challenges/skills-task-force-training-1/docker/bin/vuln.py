#!/usr/bin/env python

import sys
import random

def print(*args, **kwargs):
    res = __builtins__.print(*args, **kwargs)
    sys.stdout.flush()
    return res

f = open("flag.txt", "r")
flag = f.read()
f.close()
    
def main():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print("Hello Agent!\n\nGood work getting here. Just to make sure you aren't a robot though, can you answer this simple math problem? Turns out most AI can't even add numbers properly.\n")

    res = input(f"What's {num1} + {num2}? ")

    try:
        if int(res) == num1 + num2:
            print("\nGreat, you're not a robot. Here's the flag:")
            print(flag)
            print("\nGood luck out there Agent!\n")
            return
    except:
        pass
    
    print("\nAH! That's not right. You're a robot, aren't you!? Get out of here!\n")

if __name__ == "__main__":
    main()