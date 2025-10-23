f = open("a.txt", "r")
lines = f.readlines()
f.close()
print(len(lines))