# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""

import random

from lib.gen_bank_card import GenBankCard
from lib.sqlite_lib import SqliteContext
from lib.singleton import Singleton

from faker import Faker

fake = Faker(locale='zh_CN')


class GenPerson:
    '''生成姓名和身份证号'''

    def gen_person(self):
        return fake.name(), fake.ssn()


class GenBankcard:
    '''从`银行卡归属银行`中查询一个6位数字，给GenBankCard().gen_card_num()生成银行卡号，同时返回银行卡类型名称'''

    def gen_banCard(self):
        with SqliteContext() as cursor:
            sql_check_table = "select count(*) from `银行卡归属银行`"
            cursor[0].execute(sql_check_table)
            num = cursor[0].fetchall()
            # 执行SQL语句
            ram = random.randint(1, num[0][0] - 1)
            sql_set_data = f"select `卡标识`, `银行`||`卡级别`  AS `卡名称` from `银行卡归属银行` limit {ram},1 "
            cursor[0].execute(sql_set_data)
            res = cursor[0].fetchall()
            # print(GenBankCard().gen_card_num(res[0][0], 16))
            # print(res[0][1])
            return GenBankCard().gen_card_num(res[0][0], 16), res[0][1]


class SetBankcardInfo:
    '''
    往人银行卡库里造人员数据
    '''

    def set_bankCardInfo_to_sqlite(self, data):
        with SqliteContext() as cursor:
            sql_check_table = "create table if not exists `人银行卡库`(`人名`,`身份证号`,`银行卡` primary key,`卡名称`)"
            cursor[0].execute(sql_check_table)
            # 执行SQL语句
            sql_set_data = "insert into `人银行卡库`(`人名`,`身份证号`,`银行卡`,`卡名称`) values(?,?,?,?)"
            cursor[0].executemany(sql_set_data, data)
            cursor[1].commit()
            print("******数据添加成功******")


@Singleton
class GetBankcardPersonInfo:
    '''
    从人银行卡库里随机获取一个人的信息
    '''

    def __init__(self):
        self.data = self.get_bankCard_person_data()

    def get_bankCard_person_data(self):
        with SqliteContext() as cursor:
            # 执行SQL语句
            sql_get_data = f"select * from `人银行卡库`"
            cursor[0].execute(sql_get_data)
            res = cursor[0].fetchall()
            return res

    def get_bankCard_person_Info(self):
        return random.choice(self.data)


def gen(data_num):
    # 生成n个人信息，每个人随机生成1~9个银行卡号
    data_lst = []
    for i in range(data_num):
        t1 = GenPerson().gen_person()

        ram = random.randint(1, 10)
        for j in range(ram):
            t2 = GenBankcard().gen_banCard()
            data_lst.append(t1 + t2)
    # print(data_lst)

    # 在sqlite里生成人银行卡信息
    random.shuffle(data_lst)
    SetBankcardInfo().set_bankCardInfo_to_sqlite(data_lst)


if __name__ == '__main__':
    # 往人银行卡库里造数据
    gen(2000)
    # 从人银行卡库里随机读数据
    # GetBankcardPersonInfo().get_bankCard_person_Info()
