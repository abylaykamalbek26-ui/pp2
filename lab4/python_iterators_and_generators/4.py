def a_to_b_generator(a,b):
    for i in range(a,b+1):
        i = i **2
        yield i

a= int(input())
b= int(input())
print(list(a_to_b_generator(a,b)))        