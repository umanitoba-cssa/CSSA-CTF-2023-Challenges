#!/usr/bin/env python

import sys
import select
import random
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

    print("Hello Agent! I hope you're connecting using code, because otherwise there's no way you can solve this challenge fast enough!\n")

    sleep(3)

    print("Ready?\n")

    sleep(2)

    print(f"{num1} + {num2}")
    print("= ", end="")

    i, o, e = select.select([sys.stdin], [], [], 0.5)

    if (i):
        answer = sys.stdin.readline().strip()
        if (answer == str(num1 + num2)):
            print("\nGood job! Here's your flag:")
            print(flag)
        else:
            print("\nWrong answer!")
    else:
        print("\nToo slow!")



if __name__ == "__main__":
    main()