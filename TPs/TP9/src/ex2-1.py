import struct

val = 1.5

with open('fex2-1.txt', 'w') as f:
    f.write(f'{val}')

with open('fex2-1.bin', 'wb') as f:
    f.write(struct.pack('f', val))