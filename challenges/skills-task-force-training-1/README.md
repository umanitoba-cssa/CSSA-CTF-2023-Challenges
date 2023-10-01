# task-force-training-1
- General Skills
- Easy
- 50 Points

## Description

Hello Agent! Glad to have you, we are going to need everyone we can to take down this rogue AI!

We want to offer some training for you to get you prepared for the challenges that lie ahead. We hope the skills you learn with us will enable you to tackle whatever barriers that artificially intelligent monster may throw in your way.

Let's start simple. The AI often likes to communicate over TCP sockets, so let's make sure you are equipped for that. You'll need a tool like netcat or ncat. 

If you are on Windows or Mac, you should grab ncat which is included with nmap. If you don't already have it, you can download and install it from [the nmap website](https://nmap.org/ncat/).

If you are on Linux, it should be enough to install netcat with your favorite package manager. On Ubuntu or Debian, you'd run `sudo apt install netcat`, but every distro is different.

Once you have ncat or netcat install, open a command prompt, powershell window, or terminal, and run one of the following commands:

For ncat:

`ncat task-force-training-1.ctf.umanitobacssa.ca 10000`

or for netcat:

`nc task-force-training-1.ctf.umanitobacssa.ca 10000`

Good luck Agent!

## Solution

Connect to the server, answer the simple math problem, profit.

## Flag
`cssactf{aG3n7-1n-7ra1n1nG-f732262c}`