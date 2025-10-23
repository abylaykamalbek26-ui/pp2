def count(s):
    lower = 0
    upper = 0
    for i in s:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return upper,lower

s = input()

print(count(s))