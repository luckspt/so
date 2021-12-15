import struct

val = 1/3

with open('fex2-3.txt', 'w') as f:
    f.write(f'{val}')

with open('fex2-3.bin', 'wb') as f:
    f.write(struct.pack('f', val))