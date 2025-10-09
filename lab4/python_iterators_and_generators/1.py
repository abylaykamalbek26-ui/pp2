# m = int(input())
# square_generator = (n*n for n in range(m))

# print(square_generator)

def square_generator(start = 0):
    current1 = start

    while True:
        current1 += 1
        current = current1**2
        yield current

gen = square_generator()
m = int (input())
for i in range(m):
    print(next(gen))