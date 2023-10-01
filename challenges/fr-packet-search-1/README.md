# fr-packet-search-1
- Forensics
- Easy
- 100 Points

## Description

We've intercepted some network traffic that we believe is the AI sending messages to its botnets. Can you find anything useful hidden in the messages?

## Solution

Open the .pcap in Wireshark and look through the traffic. Flag is plaintext in a UDP message from 1.1.1.1 to 42.42.42.42, preceded by three "INCOMING MESSAGE ..." messages.

## Flag
`cssactf{53cr3t_R0b0t_M3554g3}`