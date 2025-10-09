
k = int(input())

gen = (n for n in range(k) if n % 3 == 0 and n % 4 == 0)

for value in gen:
    print(value)