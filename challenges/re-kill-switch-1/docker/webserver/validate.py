import sys

def main():
    key = sys.argv[1]

    if (key.count('-') == 4 and key[5] == '-' and key[11] == '-' and key[17] == '-' and key[23] == '-'):
        key = key.replace('-', '')

        if (key[1] == 'P' and
            key[24] == 'P' and
            key[5] == 'R' and
            key[19] == 'H' and
            key[3] == 'R' and
            key[21] == '3' and
            key[23] == 'C' and
            key[0] == '8' and
            key[16] == 'G' and
            key[22] == 'C' and
            key[7] == '6' and
            key[20] == '9' and
            key[6] == 'Z' and
            key[17] == '2' and
            key[8] == 'D' and
            key[4] == 'A' and
            key[12] == '0' and
            key[9] == 'I' and
            key[2] == 'F' and
            key[15] == 'O' and
            key[18] == 'S' and
            key[11] == 'Z' and
            key[14] == 'Y' and
            key[13] == '6' and
            key[10] == 'B'):
            print('true')
    
    print('false')
        


if __name__ == '__main__':
    main()