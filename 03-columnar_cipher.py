import math
# # SINGLE COLUMNAR
pt = "COLUMNAR TRANSPOSITION"
key = "HEAVEN"

pt = pt.replace(" ", "")

rows = math.ceil(len(pt) / len(key))
cols = len(key)

matrix = [[''] * cols for _ in range(rows)]
k = 0
for i in range(rows):
    for j in range(cols):
        if(k < len(pt)):
            matrix[i][j] = pt[k]
            k+=1
        else:
            matrix[i][j] = "!"

# return to heaven
new_k = sorted(key)
d1 = dict()
for idx, k in enumerate(new_k):
    d1[idx+1] = k
print(d1)
final_lst = []
for (idx, k) in enumerate(key):
    for i, j in d1.items():
        if k == j:
            final_lst.append([idx, i, k])
            d1.pop(i)
            break # VERY IMPORTANT BECAUSE DICT SIZE CHANGES
print(final_lst)

for i in range(cols):
  print(key[i], end=" ")
print('\n')
for i in final_lst:
  print(i[1], end=" ")
print('\n')
for i in range(rows):
  for j in range(cols):
    print(matrix[i][j] ,end=" ")
  print('\n')

ct = ""
ct_lst = []
final_lst.sort(key=lambda x: x[1])    
for i in final_lst:
    ct_lst.extend([matrix[j][i[0]] for j in range(rows)])
ct = ''.join(ct_lst)
print("Cipher Text: ", ct)


# DECRYPTION
key = "HEAVEN"
rows = math.ceil(len(ct) / len(key))
cols = len(key)
print()
dematrix = [[''] * cols for _ in range(rows)]
k = 0
for l in final_lst:
    for i in range(cols):
        if(l[0] == i):
            for j in range(rows):
                dematrix[j][i] = ct[k]
                k+=1

final_lst.sort(key=lambda x: x[0])    
for i in range(cols):
  print(key[i], end=" ")
print('\n')
for i in final_lst:
  print(i[1], end=" ")
print('\n')
for i in range(rows):
  for j in range(cols):
    print(dematrix[i][j] ,end=" ")
  print('\n')

pt = ""
pt_lst = []
for i in range(rows):
    for j in range(cols):
        pt += dematrix[i][j]

print(pt)

pt = "COLUMNAR TRANSPOSITION"
key1 = "CRYPTO"
key2 = "APPLE"

pt = pt.replace(" ", "")

for i in range(2):
    if i == 0:
        rows = math.ceil(len(pt) / len(key1))
        cols = len(key1)

        matrix1 = [[''] * cols for _ in range(rows)]
        k = 0
        for i in range(rows):
            for j in range(cols):
                if(k < len(pt)):
                    matrix1[i][j] = pt[k]
                    k+=1
                else:
                    matrix1[i][j] = "!"

        # return to heaven
        new_k = sorted(key1)
        d1 = dict()
        for idx, k in enumerate(new_k):
            d1[idx+1] = k
        
        final_lst1 = []
        for (idx, k) in enumerate(key1):
            for i, j in d1.items():
                if k == j:
                    final_lst1.append([idx, i, k])
                    d1.pop(i)
                    break # VERY IMPORTANT BECAUSE DICT SIZE CHANGES

        for i in range(cols):
            print(key1[i], end=" ")
        print('\n')
        for i in final_lst1:
            print(i[1], end=" ")
        print('\n')
        for i in range(rows):
            for j in range(cols):
                print(matrix1[i][j] ,end=" ")
            print('\n')

        ct = ""
        ct_lst = []
        final_lst1.sort(key=lambda x: x[1])    
        for i in final_lst1:
            ct_lst.extend([matrix1[j][i[0]] for j in range(rows)])
        ct = ''.join(ct_lst)
        pt = ct
    else:
        rows = math.ceil(len(pt) / len(key2))
        cols = len(key2)

        matrix1 = [[''] * cols for _ in range(rows)]
        k = 0
        for i in range(rows):
            for j in range(cols):
                if(k < len(pt)):
                    matrix1[i][j] = pt[k]
                    k+=1
                else:
                    matrix1[i][j] = "!"

        # return to heaven
        new_k = sorted(key2)
        d1 = dict()
        for idx, k in enumerate(new_k):
            d1[idx+1] = k
        
        final_lst2 = []
        for (idx, k) in enumerate(key2):
            for i, j in d1.items():
                if k == j:
                    final_lst2.append([idx, i, k])
                    d1.pop(i)
                    break # VERY IMPORTANT BECAUSE DICT SIZE CHANGES

        for i in range(cols):
            print(key2[i], end=" ")
        print('\n')
        for i in final_lst2:
            print(i[1], end=" ")
        print('\n')
        for i in range(rows):
            for j in range(cols):
                print(matrix1[i][j] ,end=" ")
            print('\n')

        ct = ""
        ct_lst = []
        final_lst2.sort(key=lambda x: x[1])    
        for i in final_lst2:
            ct_lst.extend([matrix1[j][i[0]] for j in range(rows)])
        ct = ''.join(ct_lst)
        print("CIPHER TEXT: ", ct)

# DECRYPTION
key1 = "CRYPTO"
key2 = "APPLE"

for i in range(2):
    if i == 0:
        rows = math.ceil(len(ct) / len(key2))
        cols = len(key2)
        print()
        dematrix = [[''] * cols for _ in range(rows)]
        k = 0
        for l in final_lst2:
            for i in range(cols):
                if(l[0] == i):
                    for j in range(rows):
                        dematrix[j][i] = ct[k]
                        k+=1

        final_lst2.sort(key=lambda x: x[0])    
        for i in range(cols):
            print(key2[i], end=" ")
        print('\n')
        for i in final_lst2:
            print(i[1], end=" ")
        print('\n')
        for i in range(rows):
            for j in range(cols):
                print(dematrix[i][j] ,end=" ")
            print('\n')

        pt = ""
        pt_lst = []
        for i in range(rows):
            for j in range(cols):
                pt += dematrix[i][j]
        ct = pt
        print("HERE: ", ct)
    else:
        rows = math.ceil(len(ct) / len(key1))
        cols = len(key1)
        print()
        dematrix = [[''] * cols for _ in range(rows)]
        k = 0
        for l in final_lst1:
            for i in range(cols):
                if(l[0] == i):
                    for j in range(rows):
                        try:
                            dematrix[j][i] = ct[k]
                            k+=1
                        except:
                            continue

        final_lst1.sort(key=lambda x: x[0])
        for i in range(cols):
            print(key1[i], end="\t")
        print('\n')
        for i in final_lst1:
            print(i[1], end="\t")
        print('\n')
        for i in range(rows):
            for j in range(cols):
                print(dematrix[i][j] ,end="\t")
            print('\n')

        pt = ""
        pt_lst = []
        for i in range(rows):
            for j in range(cols):
                pt += dematrix[i][j]
        print("PLAIN TEXT: ", pt)
































