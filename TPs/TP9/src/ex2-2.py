import struct

val = 1.5555555555

with open('fex2-2.txt', 'w') as f:
    f.write(f'{val}')

with open('fex2-2.bin', 'wb') as f:
    f.write(struct.pack('f', val))