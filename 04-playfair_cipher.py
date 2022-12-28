def create_matrix(key):
    letters_added = []
    for i in key:
        if i not in letters_added:
            letters_added.append(i)
    
    for i in range(65, 91):
        if i == 74:
            continue
        else:
            if (chr(i) not in letters_added):
                letters_added.append(chr(i))

    matrix = [['' for i in range(5)] for j in range(5)]
    k = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[k]
            k+=1
    return matrix

def seperate_letters(pt):
    for i in range(len(pt)-1):
        if pt[i] == pt[i+1]:
            pt = pt[:i+1] + 'X' + pt[i+1:]
    if(len(pt) % 2 != 0):
        pt += 'X'
    return pt

def indexOf(letter, matrix):
    for i in range(5):
        try:
            j = matrix[i].index(letter)
            return (i, j)
        except:
            continue

def playfair(pt, key, encrypt=True):
    inc = 1
    if(encrypt == False):
        inc = -1

    matrix = create_matrix(key)
    pt = seperate_letters(pt)
    ct = ""
    for (l1, l2) in zip(pt[0::2], pt[1::2]):
        row1, col1 = indexOf(l1, matrix)
        row2, col2 = indexOf(l2, matrix)

        if(row1 == row2):
            ct += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        elif(col1 == col2):
            ct += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else:
            ct += matrix[row1][col2] + matrix[row2][col1]
    return ct

pt = "INSTRUMENTS"
key = "MONARCHY"

print(playfair(pt, key, True))
ct = playfair(pt, key, True)
print(playfair(ct, key, False))