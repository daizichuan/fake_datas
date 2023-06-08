# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""
import calendar
import datetime
import random
import time


# print(calendar.timegm(datetime.datetime.strptime('2022-12-2 09:56:27', "%Y-%m-%d %H:%M:%S").timetuple()))

class GenTradeDatetime:
    d = dict()

    def __init__(self, bank_card):
        self.ts_front = 1405904400
        self.ts_end = calendar.timegm(datetime.datetime.now().timetuple())
        self.bank_card = bank_card

    def gen_datetime(self, datetime_old):
        datetime_old = calendar.timegm(datetime.datetime.strptime(datetime_old, "%Y-%m-%d %H:%M:%S").timetuple())
        d = random.randint(1, 86400) + datetime_old
        return d if d < self.ts_end else self.ts_end

    def get_datetime(self):
        if self.bank_card not in self.d.keys():
            self.d[self.bank_card] = datetime.datetime.utcfromtimestamp(self.ts_front).strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.d[self.bank_card] = datetime.datetime.utcfromtimestamp(
                self.gen_datetime(self.d[self.bank_card])).strftime("%Y-%m-%d %H:%M:%S")
        return self.d[self.bank_card]


if __name__ == '__main__':
    for _ in range(100):
        print(GenTradeDatetime('111').get_datetime())
    # d = '2022-12-2 09:56:27'
    # # print(calendar.timegm(datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").timetuple()))
    # t = calendar.timegm(datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").timetuple())
    # print(datetime.datetime.strptime(d, "%Y-%m-%d %H:%M:%S").timetuple())
    # print(datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"))
    # print(datetime.datetime.utcfromtimestamp(t))