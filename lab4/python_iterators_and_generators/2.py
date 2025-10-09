# def even_generator(start = 0):
#     current = start
#     while True:
#         current += 1
#         if current % 2 == 0:
#             yield current

# gen = even_generator()
# n = int(input())
# for i in range(n):
#     k = next(gen)
#     if k < n:
    

def even_generator(n):
    for i in range(0,n+1,2):
        yield i

n = int(input())

print(", ".join(map(str,even_generator(n))))
