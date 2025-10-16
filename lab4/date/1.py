# import datetime 

# time_delta = datetime.timedelta(days=5)

# current_datetime = datetime.datetime.now()

# new_date = current_datetime - time_delta

# print(new_date)

def gen(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    yield sum

n = int(input())
print(list(gen(n)))