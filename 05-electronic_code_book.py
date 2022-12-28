plain_text = "abcdefg hijklm nopqrs tuvw"
print("Plain Text: ", plain_text)
# key 
key = 129
bin_key = bin(key)[2:]
print("Key in binary: ",bin_key)

# Convert plain text into blocks of each 16 chars
blocks = []
for i in range(0, len(plain_text), 16):
  part = list(plain_text[i: i+16])
  if(len(part) % 16 != 0):
    for _ in range(16 - len(part)):
      part += 'x'
  blocks.append(part)
print("Blocks:",blocks)

txt = ""
cipher_text = ""
for block in blocks:
  for j in block:
    # ascii to binary
    x = bin(ord(j))[2:].zfill(8)
    # cir_shift_left
    txt = x[1:] + x[0]
    # XOR with key
    xor = int(txt, 2) ^ int(bin_key, 2)
    cipher_text += chr(xor)
print("cipher_text: ", cipher_text)

# key 
key = 129
bin_key = bin(key)[2:]
print("Key in binary: ",bin_key)

txt = ""
decry_text = ""
lst = []
for i in cipher_text:
  # ascii to binary
  x = bin(ord(i))[2:].zfill(8)
  # xor
  xor = bin(int(x, 2) ^ int(bin_key, 2))[2:]
  # circular shift right
  txt = xor[-1] + xor[:-1]
  decry_text += chr(int(txt, 2))
print(decry_text[:len(plain_text)])






























# pt = "GOOD MORNING ALISTAIR" # Take any input
# key = 129 # Take a key of 128bits

# # Make sure that the len of pt is divisible by 16 for block16
# if len(pt) % 16 != 0:
#     while(len(pt) % 16 != 0):
#         pt += 'X'

# # Divide the plaintext into blocks of 16 chars
# blocks_16 = []
# for i in range(0, len(pt), 16):
#     blocks_16.append(pt[i:i+16])
# # print(blocks_16)

# ascii_blocks = []
# for block in blocks_16:
#     temp = []
#     for i in block:
#         temp.append(ord(i))
#     ascii_blocks.append(temp)
# # print(ascii_blocks)
# binary_blocks = []
# for block in ascii_blocks:
#     temp = []
#     for i in block:
#         temp.append(bin(i)[2:].zfill(8))
#     binary_blocks.append(temp)
# # print(binary_blocks)

# binary_key = bin(key)[2:]
# # print(binary_key)

# # XOR
# ct = []
# for block in binary_blocks:
#     txt = ""
#     for i, j in zip(block, binary_key):
#         txt += str(int(i) ^ int(j))
#     ct.append(txt)
# print(ct)