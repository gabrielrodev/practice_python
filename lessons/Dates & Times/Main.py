
import datetime

date = datetime.date(2025, 7, 29)
today = datetime.date.today()

time = datetime.time(6,51,0)
now = datetime.datetime.now() #returns date and time also

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030,4,24,10,30,0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print(f"{target_datetime} has passed")
else:
    print(f"{target_datetime} has not passed")
print("")
print(date)
print(today)
print(time)
print(now)