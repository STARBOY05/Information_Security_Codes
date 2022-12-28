# vignere cipher

def vignere_cipher(text, choice, key):
    if(choice == "encrypt"):
        ct = ""
        for i, j in zip(text, key):
            ascii1 = ord(i)
            ascii2 = ord(j)
            if i == " ":
                ct += " "
            elif i.isupper():
                ct += chr(((ascii1 - 65 + ascii2 - 65) % 26) + 65)
            elif i.islower():
                ascii = ord(i)
                ct += chr(((ascii1 - 97 + ascii2 - 97) % 26) + 97)
            elif i.isnumeric():
                ascii = ord(i)
                ct += chr(((ascii1 - 48 + ascii2 - 48) % 26) + 48)
        return ct
    else:
        pt = ""
        for i, j in zip(text, key):
            ascii1 = ord(i)
            ascii2 = ord(j)
            if i == " ":
                pt += " "
            elif i.isupper():
                pt += chr(((ascii1 - 65 - (ascii2 - 65)) % 26) + 65)
            elif i.islower():
                ascii = ord(i)
                pt += chr(((ascii1 - 97 - (ascii2 - 97)) % 26) + 97)
            elif i.isnumeric():
                ascii = ord(i)
                pt += chr(((ascii1 - 48 - (ascii2 - 48)) % 26) + 48)
        return pt

pt = "ALL IS WELL".replace(' ', '')
key = "CAKE"

cycle = len(pt) // len(key)
cut = len(pt) % len(key)

new_key = key * cycle + key[:cut]
print("Making the len(key) same as len(pt): ", new_key)
ct = vignere_cipher(pt, "encrypt", new_key)
print("Encrypted Text: ", ct)
pt = vignere_cipher(ct, "decrypt", new_key)
print("Decrypted Text: ", pt)
