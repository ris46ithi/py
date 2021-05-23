value = 0b01101110
mask = 0b111
mak = mask << 3
res = value ^ mak
print(res,bin(res))
####output 86 ####
#### output 0b1010110
res = value & mak
print(res,bin(res))
###output 0b101000 #### 
