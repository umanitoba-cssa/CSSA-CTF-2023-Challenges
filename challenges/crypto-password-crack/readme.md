# Password Crack
- Cryptography
- Medium
- 300 Points
- **Flash Challenge**

## Description

You're decryption skills are so weak that I encrypted this 7zip file with only 1 word. With all
the words out there, by the time you try them I will have already taken everything over!

use this word list https://github.com/kkrypt0nn/wordlists/blob/main/passwords/password.txt
checkout hash cat

## Solution

This is an encrypted 7zip file. The password for the encryption is center. So you can use hashcat using the words only to brute force it. I didnt test how long this would take but we could use numbers inqstead if we need. Message.txt is the flag.

I have included a word dictionary to the directory.

https://github.com/philsmd/7z2hashcat this is also useful to get the hash file

## Flag

`cssactf{you_brute_forced_it!!!}`
