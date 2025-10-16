import re

with open(r"C:\Users\Abylay\projects\pp2\lab5\a.txt",encoding="utf-8") as f:
    data = f.read()


matches =  re.sub(r"(?=[A-Z])", " ", data).strip()

print(matches)