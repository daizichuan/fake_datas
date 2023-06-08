# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""

from faker import Faker

'''
频繁加载Faker实例，耗时比较严重，已经换实现方式
'''

class GenDatetime:
    def __init__(self):
        self.fake = Faker(locale='zh-cn')  # locale参数：默认是英文，'zh-cn'返回中文

    def gen_datetime(self):
        return self.fake.date_time_this_decade()


if __name__ == '__main__':
    print(GenDatetime().gen_datetime())