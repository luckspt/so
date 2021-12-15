import pickle
import struct

nums = []
with open('ExemploBin', 'rb') as f:
    while bytes := f.read(4):
        nums.append( struct.unpack('i', bytes)[0] )

print(nums)