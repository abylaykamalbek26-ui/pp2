import datetime 

time_delta = datetime.timedelta(days=5)

current_datetime = datetime.datetime.now()

new_date = current_datetime - time_delta

print(new_date)