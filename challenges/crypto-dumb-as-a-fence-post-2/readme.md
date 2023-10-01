# Dumb as a Fence Post 2

## Description

Hmmm, maybe you're smarter than I thought. Well try to crack this then!

**Note the prefix cssactf{ and postfix } does not exist in the ciphertext**

## Solution

A rail fence cipher is a type of encryption that uses a pattern like the following

W . . . E . . . C . . . R . . . U . . . O . . .
. E . R . D . S . O . E . E . R . N . T . N . E
. . A . . . I . . . V . . . D . . . A . . . C .

where you read along the diagonals. Here I filled the spaces with random letters that
are thrown away once decoded. The number that is like a key is the number of "rails"
are; in the example above there are 3 rails. To solve it you can just generate
all 20 rails and see if any of them work. You probably need to write a program
that goes through all of the rails and then outputs a string. The program would
have to throw away the non needed characters. You can also do this by hand 
by seeing how it is dividable by. Brute force is likely
needed, only 20 different operations need to be checked so the output can be
checked manually.

```
s       b       r       m
 p     f l     a t     e y
  h   o   a   u   z   g   v  
   i x     c q     j d     o
    n       k       u       w
```

**s**tjimlre**b**ufrshyx**r**opcnhwz**m**idze

q**p**unreg**f**a**l**evedj**a**h**t**jdseg**e**r**y**bnv

cv**h**two**o**vdo**a**keq**u**lho**z**jrx**g**rwo**v**wo

pyo**i**o**x**vowzq**c**d**q**iqpbd**j**l**d**svcyn**o**s

lksa**n**hbiwfgw**k**vzjkptg**u**fltkfim**w**

7, 7, 7, 4
1, 5, 1, 5, 1, 5, 1, 3
2, 3, 3, 3, 3, 3, 3, 2
3, 1, 5, 1, 5, 1, 5, 1
4, 7, 7, 7

## Hints

https://en.wikipedia.org/wiki/Rail_fence_cipher
What about the space between the letters in the cipher?

## Flag

`cssactf{sphinxofblackquartzjudgemyvow}`
