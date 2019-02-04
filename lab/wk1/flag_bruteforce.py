#!/usr/bin/env python3

import os
import imghdr

found_flag = False

for i in range(0, 255):
    command = './binary_shiftcipher.py -i flag -o flag_out -k {} -m d'.format(i)

    print('trying out number:', i)

    os.system(command)

    if imghdr.what('flag_out') == 'png':
        print('png detected at number: {}'.format(i))
        found_flag = True
        break
    print('nope')

if not found_flag:
    print("something is probably wrong with decoder")
