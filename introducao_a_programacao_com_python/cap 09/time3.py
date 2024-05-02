import datetime

print(datetime.date.today())
print(datetime.date(2018, 11, 1))
print(datetime.datetime.now())
print(datetime.datetime(2018, 11, 1, 13, 45, 11, 877875))
print(datetime.datetime.now().time())
print(datetime.time(13, 45, 26, 437575))

data = datetime.datetime.today()
print(data.day)
print(data.month)
print(data.year)

momento = datetime.datetime.now()
print(momento.date())
print(datetime.date(2018, 11, 1))
print(momento.time())
print(datetime.time(13, 46, 17, 94101))
print(momento.hour)
print(momento.minute)
print(momento.second)
print(momento.microsecond)
print(momento.weekday())
print(momento.isoweekday())

print(momento.isoformat())

data = datetime.date(year=2019, month=9, day=7)
print(data)
print(datetime.date(2019, 9, 7))

daqui_90_dias = momento + datetime.timedelta(days=90)
print(daqui_90_dias)
print(datetime.datetime(2019, 1, 30, 13, 46, 17, 94101))
print(momento - datetime.timedelta(minutes=30))
print(datetime.datetime(2018, 11, 1, 13, 16, 17, 94101))
