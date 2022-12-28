"""
Algorithm: 
1. Take a 64-bit input 
2. Divide it into 2 parts LPT and RPT of 32 bits each 
3. Prepare a function with the following rounds 
a) Take RPT as input and expand it into 48 bits using an expansion permutation 
table 
b) XOR result of step 3.1 and a 48-bit key 
c) Convert the result of step 3.2 into a 32-bit value using an s box substitution. 
4. Move out of the function block and XOR with 32-bit LPT 
5. Swap LPT and RPT 
6. Repeat the Process one more time with a new 48-bit key and expansion permutation 
tables. 
7. finally swap after 2 rounds and concatenate LPT and RPT to obtain the 64-bit 
Ciphertext. 
"""
import numpy as np

def expansion_permutation(rpt):
    # 32bits divided into blocks of 4bits each
    blocks_4bits = []
    for i in range(0, len(rpt), 4):
        blocks_4bits.append(rpt[i:i+4])
    print("blocks_4bits: ", blocks_4bits)
    n = len(blocks_4bits)
    # 32bits to 48bits rpt
    blocks_6bits = []
    for idx, txt in enumerate(blocks_4bits):
        if idx == 0:
            temp = blocks_4bits[-1][-1] + txt + blocks_4bits[1][0]
        elif idx == n-1:
            temp = blocks_4bits[-2][-1] + txt + blocks_4bits[0][0]
        else:
            temp = blocks_4bits[idx-1][-1] + txt + blocks_4bits[idx+1][0]
        blocks_6bits.append(temp)
    print("blocks_6bits: ", blocks_6bits)
    return ''.join(blocks_6bits)

def xored(txt, key):
    xored_out = ""
    for i, j in zip(txt, key):
        xored_out += str(int(i) ^ int(j))
    print("xored_out with key1:", xored_out)
    return xored_out

# 48bit rpt to 32bit
def sbox_substitution(rpt, num):
    blocks_6bits = []
    for i in range(0, len(rpt), 6):
        blocks_6bits.append(rpt[i:i+6])
    s_boxes = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
    15, 12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
    3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5, 
    0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 
    13, 8, 10, 1, 3, 15, 4, 2, 1, 6, 7, 12, 0, 5, 14, 9]
    ]
    blocks_4bits = []
    if num == 0:        
        for six_bit in blocks_6bits:
            row = int(six_bit[0] + six_bit[-1], 2)
            col = int(six_bit[1:5], 2)
            s_box = np.reshape(s_boxes[0], (4, 16))
            four_bit = bin(s_box[row][col])[2:].zfill(4)
            blocks_4bits.append(four_bit)
        return ''.join(blocks_4bits)
    else:
        for six_bit in blocks_6bits:
            row = int(six_bit[0] + six_bit[-1], 2)
            col = int(six_bit[1:5], 2)
            s_box = np.reshape(s_boxes[1], (4, 16))
            four_bit = bin(s_box[row][col])[2:].zfill(4)
            blocks_4bits.append(four_bit)
        return ''.join(blocks_4bits)

    # for six_bit, s_box in zip(blocks_6bits, s_boxes):
    #     row = int(six_bit[0] + six_bit[-1], 2)
    #     col = int(six_bit[1:5], 2)
    #     s_box = np.reshape(s_box, (4, 16))
    #     four_bit = bin(s_box[row][col])[2:].zfill(4)
    #     blocks_4bits.append(four_bit)
    # return ''.join(blocks_4bits)

def encryption(pt, key1, key2):
    n = len(pt) // 2
    # Divide the pt into lpt rpt of 32bits each
    lpt, rpt = pt[:n], pt[n:]
    # rounds ka function
    for i in range(2):
        print("LPT: ", lpt)
        print("RPT: ", rpt)

        if i==0:
            # 32bit to 48bit
            exp_rpt = expansion_permutation(rpt)
            # 48bit rpt xored with 48bit key
            xored_out = xored(exp_rpt, key1)
            # 48bit rpt to 32bit rpt
            sboxed = sbox_substitution(xored_out, 0)
        else:
            # 32bit to 48bit
            exp_rpt = expansion_permutation(rpt)
            # 48bit rpt xored with 48bit key
            xored_out = xored(exp_rpt, key2)
            # 48bit rpt to 32bit rpt
            sboxed = sbox_substitution(xored_out, 1)
        xor_with_lpt = ""
        for i, j in zip(lpt, sboxed):
            xor_with_lpt += str(int(i) ^ int(j))
        lpt = xor_with_lpt
        lpt, rpt = rpt, lpt
    return lpt + rpt


pt = '0100110010100001101101111110111000000110010111110100010001010010' #64bit
key1 = '001111111010110111000011111100010110110011110100' #48bit
key2 = '110000000101001000111100000011101001001100001011' #48bit

print(encryption(pt, key1, key2))