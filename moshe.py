#decode the flag
import struct
import binascii

pre = 0x10265D12
#kkk = ['0x61657247', '0x00003a74', '0x09ad55d6', '0x857ed90d', '0x0b2562f1', '0x12083432', '0x7d7a16e6', '0xe20856a0', '0x9aeaeb11', '0x7bd2faee', '0x622bb2ab', '0xb84488ed', '0x4a714a11', '0x0000008a', '0x00000000', '0x00000000', '0xf7e70800', '0x00007fff', '0x8de8eff5', '0x143022d8', '0x3bd0b944', '0x568c2bbe', '0x5aaa1ba2', '0x96b42c51', '0x1f830f5d', '0xa6c5dc26', '0x9f1c9c44', '0xe3325c5b', '0x02e03d74']
#ppp = ['0x09ad55d6', '0x857ed90d', '0x0b2562f1', '0x12083432', '0x7d7a16e6', '0xe20856a0', '0x9aeaeb11', '0x7bd2faee', '0x622bb2ab', '0xb84488ed', '0x4a714a11', '0x0000008a']

rdi = ['0x04061026', '0x00005d12', '0x00030003', '0x00030003', '0x00030003', '0x00040004', '0x00040004', '0x00040004', '0x00040004', '0x00000000', '0x01010100', '0x01000101', '0x01010101', '0x01000101', '0x01000101', '0x01010101']
rdis = ['0x04061026', '0x00005d12', '0x00030003', '0x00030003', '0x00030003', '0x00040004', '0x00040004', '0x00040004', '0x00040004', '0x00000000', '0x01010100', '0x01000101', '0x01010101', '0x01000101', '0x01000101', '0x01010101']
iii = '''Great: \365\357\350\215\330\"0\024D\271\320;\276+\214V\242\033\252ZQ,\264\226]\017\203\037&\334ŦD\234\034\237[\\2\343t=\340\002\202'''

ttt = []
xorByN = 68

toXor = '3a'
i = int(str(xorByN), 16)
j = int(str(toXor), 16)
print chr(j ^ i)











def Edian(i):
    listy = []
    for j in range(4):
        listy.append(i[0:2])
        i = i[2:]
    listy.reverse()
    return ''.join(listy)

#for i in kkk:
 #   i = i.replace('0x','')
  #  ttt.append(Edian(i))

#for i in ttt:
 #   print i.decode('hex')









flagHex = '0x61657247 0xf5203a74 0xd88de8ef 0x44143022 0xbe3bd0b9 0xa2568c2b 0x515aaa1b 0x5d96b42c 0x261f830f 0x44a6c5dc 0x5b9f1c9c 0x74e3325c 0x8202e03d 0xff6c800a 0xff6070b0 0xffd8fcfc'
flagHexList = ['0x61657247', '0xf5203a74', '0xd88de8ef', '0x44143022', '0xbe3bd0b9', '0xa2568c2b', '0x515aaa1b', '0x5d96b42c', '0x261f830f', '0x44a6c5dc', '0x5b9f1c9c', '0x74e3325c', '0x8202e03d', '0xff6c800a', '0xff6070b0', '0xffd8fcfc']

'''
void decode(byte *pre,byte *local140)

{
  *local140 = *pre ^ 0x61;
  local140[1] = pre[1] ^ 0x62;
  local140[2] = pre[2] ^ 99;
  local140[3] = pre[3] ^ 0x65;
  local140[4] = pre[4] ^ 0x66;
  local140[5] = pre[5] ^ 0x67;
  return;
}
'''

a = '10265D12'

print chr(12^62)


