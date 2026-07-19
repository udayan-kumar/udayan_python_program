import datetime

date = datetime.date(2026 , 7 , 19)
today = datetime.date.today()

time = datetime.time(12,30,0)
now = datetime.datetime.now()
now = now.strftime("%H : %M : %S  %d-%m-%y")

print(date)
print(today)
print(time)
print(now)

target_datetime = datetime.datetime(2030 , 2 , 2 , 12 , 30 , 40)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("target date has been passed")
else:
    print("target date has not passed")