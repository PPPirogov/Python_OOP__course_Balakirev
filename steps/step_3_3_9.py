import datetime
import time

class DeltaClock:
    def __init__(self, clock1, clock2):
        self.__clock1 = clock1
        self.__clock2 = clock2

    def __str__(self):
        c1=str(self.__clock1.hours)+': '+str(self.__clock1.minutes)+': '+str(self.__clock1.seconds)
        c2=str(self.__clock2.hours)+': '+str(self.__clock2.minutes)+': '+str(self.__clock2.seconds)
        a = datetime.datetime.strptime(c1,'%H: %M: %S')
        b = datetime.datetime.strptime(c2,'%H: %M: %S')
        c = a -b
        print(c.total_seconds())
        return 'hi'

    def __len__(self):
        c1=str(self.__clock1.hours)+':'+str(self.__clock1.minutes)+':'+str(self.__clock1.seconds)
        c2=str(self.__clock2.hours)+':'+str(self.__clock2.minutes)+':'+str(self.__clock2.seconds)
        a = datetime.datetime.strptime(c1,'%H:%M:%S')
        b = datetime.datetime.strptime(c2,'%H:%M:%S')
        answer = a-b
        return int(answer.total_seconds())

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        return self.__hours
    @property
    def minutes(self):
        return self.__minutes
    @property
    def seconds(self):
        return self.__seconds

    def get_time(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))


print(dt) # 01: 30: 00
len_dt = len(dt)
print(len_dt)