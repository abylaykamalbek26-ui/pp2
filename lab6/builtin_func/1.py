def multiply(lst):
    res = 1
    for i in lst:
        res = i* res
    return res

lst = [3,5,7,6,4]

print(multiply(lst))