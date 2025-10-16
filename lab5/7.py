import re

with open(r"C:\Users\Abylay\projects\pp2\lab5\a.txt",encoding="utf-8") as f:
    data = f.read()


matches =  re.sub(r'_([a-z])',lambda m : m.group(1).upper(),data)

print(matches)