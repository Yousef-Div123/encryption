#getting input
key = input("key: ").upper()

#checking if it is a key
if len(key) != 26:
    print("This is not a valid key!!")
    input("press enter to exit...........")
    quit()

plaintext = input("Plaintext: ")
plaintext_copy2 = plaintext.upper()
plaintext_copy = ""

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c in plaintext_copy2:
    if c == " ":
        plaintext_copy += " "
    for i in abc:
        if c == i:
            if plaintext[plaintext_copy2.index(c)].islower():
                plaintext_copy += key[abc.index(i)].lower()
            else:
                plaintext_copy += key[abc.index(i)]
            
     

print(plaintext_copy)
input("press enter to exit.......")