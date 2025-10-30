import string
for letter in string.ascii_uppercase:
    f = open(letter + ".txt", "w")
    f.close()