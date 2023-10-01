import sys
import re

def main():
    key = sys.argv[1]

    if key.isascii() and re.search("(?<=\w{4}[a-e]{2}\d{5}-poe4[90])(?<!9)\d{3}-\W\w.{5}\\b.{5}\w\W-[t-v]{3}(?!.*[acefgik])[a-c]{1}[d-f]{3}[h-k]{2}", key):
        print('true')
        return
    
    print('false')
        


if __name__ == '__main__':
    main()