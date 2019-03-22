# from math import ceil, log


sbox = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
        0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]

def subtitute(_hex_text, hex_length):
    item = 0x0
    for i in range(hex_length):
        h = sbox[_hex_text%16]
        item += h*(16**i)
        _hex_text = _hex_text/16
    return hex(item)

def subLeftmost(_hex_num):
    new_hex = ''
    to_change = hex(_hex_num)[2]

    new_hex += hex(sbox[int(to_change, 16)])
    new_hex += hex(_hex_num)[3:]

    return (new_hex)

def set_bit(v, index, x):
  """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
  mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
  v ^= ~mask          # Clear the bit indicated by the mask (if x is False)
  if x:
    v ^= mask         # If x was True, set the bit indicated by the mask.
  return v  

def step3(_hex_num, round):
    # get rightmost bit of round counter 
    rightmost = round & 1
    
    # build mask
    if rightmost == 1:
        mask = 31 << 16
        mask = mask | _hex_num
    else:
        mask = 31 << 16
        mask = ~mask & _hex_num    
    
    return(mask)


# print(subtitute(0xfbac, 1))
# print(subLeftmost(0x0))
# print(step3(0xbb23bcafffff, 2))
print(0b11111000000000001100)