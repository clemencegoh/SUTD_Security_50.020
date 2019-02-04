#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Clemence Goh (1002075),
# Kenjyi Lim

# Import libraries
import sys
import argparse
import string

def doStuff(filein,fileout, shift, mode):
    # open file handles to both files
    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    fin_b = open(filein, mode='rb')  # binary read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')      # write mode
    fout_b = open(fileout, mode='wb')  # binary write mode

    # PROTIP: pythonic way
    text = fin_b.read()

    # do stuff
    if mode == 'e' or mode == 'E':
        fout_b.write(encrypt(bytearray(text), int(shift)))
    elif mode == 'd' or mode == 'D':
        fout_b.write(decrypt(bytearray(text), int(shift)))
    else:
        print('Wrong mode')
    # file will be closed automatically when interpreter reaches end of the block

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()


def doChecks(_in_args):
    if type(_in_args['filein']) != str:
        print('filename is not a string')
        return False
    if type(_in_args['fileout']) != str:
        print('fileout name is not a string')
        return False
    try:
        key = int(_in_args['key_optional'])
        if not 0 <= key <= 255:
            print('key should be within 0 and 255')
            return False
    except ValueError:
        print('key should be an integer')
        return False

    m = _in_args['mode_optional']

    if m != 'e' and m != 'E' and m != 'd' and m != 'D':
        print('mode should be e or d')
        return False
    return True


def checkLength(_shift_key):
    return 0 > len(_shift_key) > len(string.printable)


def encrypt(_bytearray_msg, _shift):
    # create empty bytearray
    new_bytearray = bytearray()

    _shift = format(int(_shift), "b")

    for b in _bytearray_msg:
        # increase
        b = format(b, "b")
        bin_string = bin(int(b,2) + int(_shift, 2))
        to_hex = int(bin_string, 2)

        if to_hex > 255:
            to_hex = to_hex - 255

        new_bytearray.append(to_hex)

    return bytes(new_bytearray)


def decrypt(_msg, _shift):
    new_bytearray = bytearray()

    _shift = format(int(_shift), "b")

    for b in _msg:
        # decrease
        b = format(b, "b")
        bin_string = bin(int(b,2) - int(_shift, 2))
        to_hex = int(bin_string, 2)

        if to_hex < 0:
            to_hex = 255 + to_hex

        new_bytearray.append(to_hex)

    return bytes(new_bytearray)


# our main function takes in argument
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='key used to shift cipher')
    parser.add_argument('-m', dest='mode', help='mode')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key_optional = args.key
    mode_optional = args.mode

    in_args = {
        'filein': filein,
        'fileout': fileout,
        'mode_optional': mode_optional,
        'key_optional': key_optional,
    }

    # checks
    if not doChecks(in_args):
        print('checks not passed')
        exit(1)

    doStuff(filein,fileout, key_optional, mode_optional)

    # all done

