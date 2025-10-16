import datetime 

time_delta = datetime.timedelta(days=1)

current_datetime = datetime.datetime.now()

yesterday = current_datetime - time_delta

tomorrow = current_datetime + time_delta

print(yesterday)
print(current_datetime)
print(tomorrow)