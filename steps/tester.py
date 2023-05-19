import datetime

a = datetime.time(8,48,45)
b= datetime.time(10,48,45)

td_object =datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
td_object
datetime.timedelta(0)
print(td_object)

d = datetime.datetime.strptime('9:00:00', '%H:%M:%S')
e = datetime.datetime.strptime('10:00:00', '%H:%M:%S')
t =
f = e - d
print(f)