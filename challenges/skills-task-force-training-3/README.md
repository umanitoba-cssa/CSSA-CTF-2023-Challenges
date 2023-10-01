# task-force-training-2
- General Skills
- Easy
- 100 Points

## Description

Excellent job! You seem to have the real makings of an Agent ready to kick some robot butt!

However, lets acknowledge that our enemy has the upper hand in some areas: computers are faster, and more precise than humans for many technical tasks.

So lets augment our abilities. It's extremely helpful to be able to interface with websites or servers using code!

Feel free to use your favorite language if you already have one. You'll need to be able to connect to this server either by running ncat/netcat using your language, or by connecting directly to the TCP socket.

If you don't know what any of that means, don't worry! I've given you a Python file to get you started.

So here's the challenge: use pwntools, a library for Python, to connect to our training server and solve a challenge. You can try to connect to the server yourself if you wish:

`ncat task-force-training-3.ctf.umanitobacssa.ca 10002` or `netcat task-force-training-3.ctf.umanitobacssa.ca 10002`

The server will ask you to add 2 numbers together. Sounds easy enough. The catch? You only have 500 milliseconds to do it, far too fast for a human to add together and type!

So instead, try to write some code to handle it for you.

You can install Python from here if you don't already have it: https://www.python.org/downloads/

Then install the pwntools library. Pwntools lets you easily connect and interface with a server using Python code, as well as perform common binary exploitation tasks.

`pip install pwntools`

If that doesn't work you can try pip3 instead:

`pip3 install pwntools`

If that still doesn't work, you may need to reboot your computer after installing Python, then try again.

Now, download the `connect.py` script and see if you can automate adding the numbers together to get the flag!

Good luck Agent!

## Solution

Modify the template to add numbers together and send the result. See solution.py

## Flag
`cssactf{L1g7tN1nG-f4$T-m47H3M4t1c5-47b97eb9}`