import re

with open(r"C:\Users\Abylay\projects\pp2\lab5\a.txt",encoding="utf-8") as f:
    data = f.read()


matches =  re.findall(r'[A-Z][a-z]+',data)

print(matches)
