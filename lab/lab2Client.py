#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018
# Andrei + Z.TANG, 2019
# Lim Ken Jyi (1002208)

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote
import string

# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r


def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # print(challenge)
    # decrypt the challenge here

    #construct a dictionary for all ascii char
    ascii_dict = dict()
    ascii_in_number = range(0,256)
    for i in ascii_in_number:
        ascii_dict[chr(i)] = 0

    #use dictionary to track occurrence freq
    for i in challenge:
        ascii_dict[chr(i)] += 1

    sorted_descending_list = []
    for key, value in sorted(ascii_dict.items(), key=lambda kv: (-kv[1], kv[0])):
        sorted_descending_list.append(key)
    # print(sorted_descending_list)

    # Start decoding from general char frequency for english
    base_char_freq = [32, 101, 116, 97, 111, 105, 110, 115, 114, 104, 108, 100, 99, 117, 109, 102, 103, 112, 121, 119, 10, 98, 44, 46, 118, 107, 45, 34, 95, 39, 120, 41, 40, 59, 48, 106, 49, 113, 61, 50, 58, 122, 47, 42, 33, 63, 36, 51, 53, 62, 123, 125, 52, 57, 91, 93, 56, 54, 55, 92, 43, 124, 38, 60, 37, 64, 35, 94, 39, 126]
    temp = [32, 101, 116, 97, 111, 104, 114, 110, 100, 105, 115, 108, 119, 46, 103, 10, 117, 99, 109, 121, 102, 112, 44, 98, 107, 34, 118, 45, 106, 39, 63, 113, 40, 59, 48, 95, 49, 41, 61, 50, 58, 122, 47, 42, 33, 120, 36, 51, 53, 62, 123, 125, 52, 57, 91, 93, 56, 54, 55, 92, 43, 124, 38, 60, 37, 64, 35, 94, 39, 126]

    order = ''
    for i in temp:
        order += chr(i)
    print(order)

    solution = ""
    for i in challenge:
        pos =  sorted_descending_list.index(chr(i))
        if pos < len(char_freq_ascii) :
            solution += chr(temp[pos])

    print(solution)

    # solution = int(0).to_bytes(7408, 'big') 
    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    conn.close()


def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # some all zero mask.
    # TODO: find the magic mask!
    mask = int(0).to_bytes(len(message), 'big')
    message = XOR(challenge, mask)
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'exact' in message:
        print(message)
    conn.close()


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '157.230.47.126'
    PORT = 1337

    sol1()
    #sol2()
