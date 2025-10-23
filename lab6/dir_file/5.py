lst = ["some", "text", "inlst"]
f = open("a.txt", "w")
for i in lst:
    f.write(i + "\n")
f.close()