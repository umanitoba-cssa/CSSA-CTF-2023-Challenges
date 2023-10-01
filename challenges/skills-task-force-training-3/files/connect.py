#!/usr/bin/env python

# First we import functions from the pwntools library
from pwn import *

# The remote function allows us to connect to a remote server
connection = remote("task-force-training-3.ctf.umanitobacssa.ca", 10002)

# We want to keep getting lines from the server until we get a line
# with a '+' symbol, this line contains our math problem to solve!
# To get lines from the server, we use the recvline() function
#
#    This function returns a bytes object, which is a sequence of bytes
#    We need to convert this to a string so we can parse it
#    We can do this by calling the decode() function on the bytes object
#
# To check if a line contains a '+' symbol, we use the in operator

# We'll run this in an infinite loop until we get a line with a '+' symbol
# Then once we have a line with a '+' symbol, we'll break out of the loop

nextLine = ""

while True:
    nextLine = connection.recvline().decode()
    print(nextLine, end="")
    if "+" in nextLine:
        break

# Now we have the line with the math problem, we need to parse it.
# Can you figure out how to parse the line to get the two numbers?
# Hint: You can use the split() function to split a string into a list
# Then you can use the int() function to convert a string to an integer

# Add to or modify the code below to parse the line and get the two numbers

###############################################
number1Text = "0"
number2Text = "0"

number1 = int(number1Text)
number2 = int(number2Text)

result = number1 + number2
###############################################

# Now we have the result, we need to send it to the server.
# To send data to the server, we use the sendline() function

connection.sendline(str(result).encode())

# Now we need to get the response from the server.
# To get the response, we use the recvall() function.
# This function will continue to receive data from the server until the
# connection is closed. Then we can decode the bytes object to get a string.

response = connection.recvall().decode()

# If our code worked, our response should be the flag!

print(response)

# Now we can run our code and see if it works!
# Run this file with the following command:
# python connect.py
# If it works, you should see the flag printed out!