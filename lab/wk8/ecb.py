#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014

"""
Done by:
Clemence Goh (1002075)
Kenjyi Lim
"""


from present import present, present_inv
import argparse

nokeybits=80
blocksize=64


def ecb(infile, outfile, key, mode):
    if mode == 'e':
        print("encrypting..")
        transform = present
    elif mode == 'd':
        print("decrypting..")
        transform = present_inv
    else:
        raise TypeError('mode should be "d" or "e"')
    s = 0 
    byte_number = 0
    done = False
    with open(infile, 'rb') as f_in:
        with open(outfile, 'wb') as f_out:
            while not done:
                byte = f_in.read(1)
                if byte:
                    s += byte[0] << (8 * (int(blocksize/8) - 1 - byte_number))
                    byte_number += 1 
                else:
                    s = s << (int(blocksize/8)-byte_number)*8
                    byte_number == 8    
                    done = True

                if byte_number % (blocksize/8) == 0:
                    assert s < 2**64
                    transformed_data = transform(s, key)
                    
                    out = [] 
                    for i in range(0, 8):
                        out.append(transformed_data>>(i*8)&0xff)
                    out.reverse()

                    f_out.write(bytes(out))
                    s = 0
                    byte_number=0
    

def setDefault(infile, outfile, keyfile, mode):
    """
    Sets default params for easier testing/input in command line
    :param infile: file to read
    :param outfile: file to output
    :param keyfile: file to read key from
    :param mode: mode, either encrypt or decrypt only
    :return: all 4 fields initialized with their default values
    """

    plainfile = "Tux.ppm"
    encrypted_file = "Tux_encrypted.ppm"
    decrypted_file = "Tux_decrypted.ppm"

    if keyfile:
        key = open(keyfile, 'r').read()
    else:
        key = 0xFFFFFFFFFFFFFFFFFFFF

    if mode is None:
        print("mode must be 'e' or 'd'")
        exit(1)
    
    if mode != 'e' and mode != 'd':
        print("mode must be 'e' or 'd'")
        exit(1)
    
    if mode == 'e':    
        if infile is None:
            infile = plainfile
        
        if outfile is None:
            outfile = encrypted_file
    if mode == 'd':
        if infile is None:
            infile = encrypted_file
        if outfile is None:
            outfile = decrypted_file
    
    return infile, outfile, key, mode


if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode = args.mode

    # default params
    infile, outfile, key, mode = setDefault(infile, outfile, keyfile, mode)

    print('carrying out task with params:', infile, outfile, hex(key), mode)
    ecb(infile, outfile, key, mode)
            



