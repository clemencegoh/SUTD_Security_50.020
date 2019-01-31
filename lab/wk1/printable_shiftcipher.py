#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

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
    c    = fin.read()         # read in file into c as a str
    # and write to fileout

    # PROTIP: pythonic way
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        text = fin.read()
        # do stuff
        if mode == 'e' or mode == 'E':
            fout.write(encrypt(text, int(shift)))
        elif mode == 'd' or mode == 'D':
            fout.write(decrypt(text, int(shift)))
        else:
            print('Wrong mode')
        # file will be closed automatically when interpreter reaches end of the block

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()


def checkType(_in_args):
    for i in _in_args:
        if type(i) != str and type(i) != int:
            print("Please input correct type")
            return False
    return True


def checkLength(_shift_key):
    return 0 > len(_shift_key) > len(string.printable)


def encrypt(_msg, _shift):
    alphabet = string.printable
    shifted_alphabet = alphabet[_shift:] + alphabet[:_shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return _msg.translate(table)


def decrypt(_msg, _shift):
    _shift = len(string.printable) - int(_shift)
    alphabet = string.printable
    shifted_alphabet = alphabet[_shift:] + alphabet[:_shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return _msg.translate(table)


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

    in_args = [filein, fileout, key_optional, mode_optional]

    # checks
    try:
        key_optional = int(key_optional)
    except ValueError:
        print("Key must be an int")
        exit(1)

    if not checkType(in_args):
        exit(1)

    doStuff(filein,fileout, key_optional, mode_optional)

    # all done

