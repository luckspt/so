import pickle
import struct

nums = []
with open('ExemploBin', 'rb') as f:
    while bytes := f.read(4):
        nums.append( struct.unpack('i', bytes)[0] )

with open('ExemploBin.txt', 'w') as f:
    f.write(' '.join(str(num) for num in nums))