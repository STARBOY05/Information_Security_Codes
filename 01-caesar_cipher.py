
def caesar_cipher(text, choice, key):
    if(choice == "encrypt"):
        ct = ""
        for i in text:
            if i == " ":
                ct += " "
            elif i.isupper():
                ascii = ord(i)
                ct += chr(((ascii - 65 + key) % 26) + 65)
            elif i.islower():
                ascii = ord(i)
                ct += chr(((ascii - 97 + key) % 26) + 97)
            elif i.isnumeric():
                ascii = ord(i)
                ct += chr(((ascii - 48 + key) % 26) + 48)
        return ct
    else:
        pt = ""
        for i in text:
            if i == " ":
                pt += " "
            elif i.isupper():
                ascii = ord(i)
                pt += chr(((ascii - 65 - key) % 26) + 65)
            elif i.islower():
                ascii = ord(i)
                pt += chr(((ascii - 97 - key) % 26) + 97)
            elif i.isnumeric():
                ascii = ord(i)
                pt += chr(((ascii - 48 - key) % 26) + 48)
        return pt

pt = str(input("Enter Plain Text: "))
key = int(input("Enter key: "))
ct = caesar_cipher(pt, "encrypt", key)
print("Encrypted Text is: ", ct)
pt = caesar_cipher(ct, "decrypt", key)
print("Encrypted Text is: ", pt)