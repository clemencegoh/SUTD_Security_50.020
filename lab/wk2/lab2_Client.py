#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018
# Andrei + Z.TANG, 2019
# Clemence Goh (1002075)
# kenjyi Lim

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote
from collections import Counter 
import string
import re
import random


def performFrequencyAnalysis(_text):
    res = Counter(_text).most_common()
    
    total = sum([x[1] for x in res])
    
    freq_map = {}

    for p in res:
        freq_map[chr(p[0])] = round(p[1]/total, 3)

    return res, freq_map


def calculateFitness(_text):
    regex = re.compile(b'[^a-zA-Z]')
    only_alpha = regex.sub(b'', _text)
    only_alpha = only_alpha.upper()

    # perform frequency analysis on alpha upper only
    _, freq_map = performFrequencyAnalysis(only_alpha)
    
    analyzed = [x[0] for x in freq_map.items()]

    most_frequent = "ETAOINSHRDLU"
    score = 0

    smaller = len(most_frequent)
    if len(analyzed) < smaller:
        smaller = len(analyzed)

    for letter in range(smaller):
        if most_frequent[letter] == analyzed[letter].upper():
            score += (100/12.0)
    # print('freq_map:', freq_map)
    print('got:', analyzed)
    print('want:', most_frequent)
    print('score:', score)
    return score


def slowReplace(_replace_mapping, _ciphertext):
    # create new string to replace byte by byte
    bytetext = ''

    for i in range(len(_ciphertext)):
        new_char = _replace_mapping[chr(_ciphertext[i])]
        if new_char != '':
            bytetext += new_char
        else:
            bytetext += chr(_ciphertext[i])

    return bytes(bytetext.encode())

        

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
    
    print('DEBUG: Challenge 1')
    
    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()  # challenge is in byte form
    # print(challenge)
    # decrypt the challenge here
    
    # get a counter to analyze frequency of characters
    res, freq_map = performFrequencyAnalysis(challenge)
    
    # print('after initial freq_analysis:', freq_map)
    
    # extract all characters present in challenge
    
    # objective is to fully decode all in here
    all_chars = [chr(x[0]) for x in res]
    # print('extracted data:', all_chars)

    possible_chars = list(string.printable)

    # print('all characters present:', all_chars)

    # build map
    char_map = {}
    for char in string.printable:
        char_map[char] = ''

    cipher_char = ['J', '[', '7', '-', 'C', '2', 
                    '^', ';', 'u', 'F', 'q', 'y', 
                    'n', 'i', 'w', 'm', '\r', ' ', 
                    ']', 'c', '(', 'a', '\t', '8', 
                    '@', 'B', ':', 'e', '9', 'R',
                    '_',]
    decoded_char = [' ', 'e', 't', 'a', 'g', 'l', 
                    'i', 'n', 'm', 'u', 'p', 'o', 
                    'c', 'h', 'r', 'w', 's', 'd', 
                    '.', 'v', 'y', 'k', 'b', 'j', 
                    'f', 'q', '\'', '-', ',', '.',
                    '"',]

    # if len(cipher_char) != len(set(cipher_char)) or len(decoded_char) != len(set(decoded_char)):
    #     print('duplicate elements in list')
    #     exit(1)

    # set this as starting point 
    for i in range(len(cipher_char)):
        char_map[cipher_char[i]] = decoded_char[i]
    
    new_text = slowReplace(char_map, challenge)
    # print(new_text)
    # exit(0)

    # solution = int(0).to_bytes(7408, 'big')
    # conn.send(solution)
    conn.send(bytes(new_text))
    message = conn.recvline()
    message = conn.recvline()
    # print(message)
    if b'Congratulations' in message:
        print(message)
    conn.close()


def sol2(i=0):
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2
    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()

    # some all zero mask. encoded with OTP
    # TODO: find the magic mask!
    to_hack = b'Submitted student ID: 1000000 and grade 0. [<-- this is not the exact plaintext]\n'
    hacked_msg = b'Submitted student ID: 1002075 and grade 4. [<-- this is not the exact plaintext]\n'

    # first XOR
    # msg_prime = XOR(to_hack, hacked_msg)

    # print(msg_prime)

    # msg_length = 140

    # mask = int(0).to_bytes(i, 'big') + msg_prime

    mask = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x07\x05\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    message = XOR(challenge, mask)
    
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    conn.close()
    if b'Submitted' in message:
        print(message)


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '157.230.47.126'
    PORT = 1337

    sol1()
    sol2()