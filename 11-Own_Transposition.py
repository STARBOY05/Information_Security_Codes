import math
pt = "No good deed will go unpunished"
key = 8

rows = math.ceil(len(pt) / key)
cols = key

matrix = [[''] * cols for _ in range(rows)]
k=0
for i in range(rows):
    for j in range(cols):
        if(k < len(pt)):
            matrix[i][j] = pt[k]
            k+=1
        else:
            matrix[i][j] = "!"
for i in range(cols):
    print(i, end=" ")
print()
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print("\n")

cipher_text = ""
col = 0
for col in range(cols):
    for row in range(rows):
        cipher_text += matrix[row][col]

print(cipher_text)

k=0
dematrix = [[''] * cols for _ in range(rows)]
for col in range(cols):
    for row in range(rows):
        dematrix[row][col] = cipher_text[k]
        k+=1

for i in range(cols):
    print(i, end=" ")
print()
for i in range(rows):
    for j in range(cols):
        print(dematrix[i][j], end=" ")
    print("\n")

ct_lst = []
for i in dematrix:
    ct_lst.extend(i)

print(''.join(ct_lst))

