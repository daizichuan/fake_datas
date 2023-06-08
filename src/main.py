# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""
import calendar
import csv
import datetime
import random
import time

from lib.gen_JieDai_flag import GenJieDaiFlag
from lib.gen_bankCard_person import GetBankcardPersonInfo
from lib.gen_datetime import GenDatetime
from lib.gen_serial_number import GenSerialNumber
from lib.sqlite_lib import SqliteContext
from lib.singleton import Singleton


class GenBankWater:
    '''往sqlite里插入银行流水数据，现在是把这个生成csv数据'''

    def set_bankWater_to_sqlite(self, data):
        with SqliteContext() as cursor:
            sql_check_table = "create table if not exists `银行卡流水`(`交易流水号`,`客户证件号码`,`客户名称`,`查询卡号`,`银行`," \
                              "`交易对方证件号码`,`交易对方名称`,`交易对方卡号`,`交易对方账号开户行`,`交易金额`,`交易时间`,`借贷标志`,`交易余额`)"
            cursor[0].execute(sql_check_table)
            # 执行SQL语句
            sql_set_data = "insert into `银行卡流水`(`交易流水号`,`客户证件号码`,`客户名称`,`查询卡号`,`银行`,`交易对方证件号码`,\
            `交易对方名称`,`交易对方卡号`,`交易对方账号开户行`,`交易金额`,`交易时间`,`借贷标志`,`交易余额`) values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
            cursor[0].executemany(sql_set_data, data)
            cursor[1].commit()


@Singleton
class GenTradeDatetime:
    '''初始设置为self.ts_front时间戳转成的时间日期2014-7-21 9:0:0，然后随机往取1秒到86400往后延的时间'''
    d = dict()

    def __init__(self):
        self.ts_front = 1405904400
        self.ts_end = calendar.timegm(datetime.datetime.now().timetuple())  # 当前时间的时间戳

    def gen_datetime(self, datetime_old):
        datetime_old = calendar.timegm(
            datetime.datetime.strptime(datetime_old, "%Y-%m-%d %H:%M:%S").timetuple())  # 日期转时间戳
        d = random.randint(1, 86400) + datetime_old
        return d if d < self.ts_end else self.ts_end  # 防止时间超过当前时间而报错

    def get_datetime(self, bank_card):
        if bank_card not in self.d.keys():
            self.d[bank_card] = datetime.datetime.utcfromtimestamp(self.ts_front).strftime(
                "%Y-%m-%d %H:%M:%S")  # 时间戳转日期
        else:
            self.d[bank_card] = datetime.datetime.utcfromtimestamp(
                self.gen_datetime(self.d[bank_card])).strftime("%Y-%m-%d %H:%M:%S")
        return self.d[bank_card]


@Singleton
class GenMoneyRemain:
    d = dict()

    def get_money(self, remain):
        return round(random.uniform(0, remain / random.randint(1, 8)), 2)  # 下一次数据取这次的1/1或1/8

    def get_remain(self, bank_card, flag):
        global money
        if bank_card not in self.d.keys() or self.d[bank_card] < 1:  # 把余数放进d字典里，当余额小于1时，重新生成余额
            money = remain = round(random.uniform(10000, 100000), 2)
            self.d[bank_card] = remain
        elif flag == '进':
            money = self.get_money(self.d[bank_card])
            self.d[bank_card] += money
        elif flag == '出':
            money = self.get_money(self.d[bank_card])
            self.d[bank_card] -= money
        self.d[bank_card] = round(self.d[bank_card], 2)
        return money, self.d[bank_card]


class GenBanWaterData:
    def gen_bankWater_data(self, loop, file_name='bank_water.csv'):
        data = []
        for i in range(loop):
            s_no = GenSerialNumber().gen_serial_number()  # 生成流水号
            my_info = GetBankcardPersonInfo().get_bankCard_person_Info()  # 生成本方姓名，身份证，银行卡，卡名称
            while True:
                other_info = GetBankcardPersonInfo().get_bankCard_person_Info()
                if other_info[2] != my_info[2]:  # 本方和对方不能相同，不能自己往自己卡里转钱
                    break
            # datetime = GenDatetime().gen_datetime()
            datetime = GenTradeDatetime().get_datetime(my_info[2])  # 生成交易时间
            flag = GenJieDaiFlag().gen_jieDai_flag()  # 生成借贷标志
            money, remain = GenMoneyRemain().get_remain(my_info[2], flag)  # 生成交易金额和余额
            # print(s_no, my_info, other_info, money, datetime, flag, remain)

            tmp = []
            tmp.append(s_no)
            tmp.extend(list(my_info))
            tmp.extend(list(other_info))
            tmp.append(money)
            tmp.append(datetime)
            tmp.append(flag)
            tmp.append(remain)

            data.append(tuple(tmp))
        # print(data)

        # 往sqlite里写
        # GenBankWater().set_bankWater_to_sqlite(data)
        # 往csv里写
        headers = ['交易流水号', '客户证件号码', '客户名称', '查询卡号', '银行', '交易对方证件号码', '交易对方名称', '交易对方卡号', '交易对方账号开户行', '交易金额', '交易时间',
                   '借贷标志', '交易余额']
        with open(f'..//data//{file_name}', 'a', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(data)


if __name__ == '__main__':
    start_time = time.time()  # 记录程序开始运行时间
    demo = GenBanWaterData()
    demo.gen_bankWater_data(100)
    # print(GenTradeDatetime.d)
    # print(GenMoneyRemain.d)
    end_time = time.time()  # 记录程序结束运行时间
    print('cost %f second' % (end_time - start_time))
