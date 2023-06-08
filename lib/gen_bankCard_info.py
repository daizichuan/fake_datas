# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""

from lib.mysql_lib import MysqlContext
from lib.mysql_lib import get_mysql_params
from lib.sqlite_lib import SqliteContext

'''
mysql上有银行卡前归属地银行，把数据导入sqlite，方便造数据时查询
'''


class GetBankcardInfo:
    def get_bankCardInfo_from_mysql(self):
        with MysqlContext() as cursor:
            sql = f"SELECT `卡标识`,  `银行`, `卡级别` FROM `{get_mysql_params.get_table()}`"
            # 执行SQL语句
            cursor.execute(sql)
            res = list(cursor.fetchall())
            # print(res)
            return res


class SetBankcardInfo:
    def set_bankCardInfo_to_sqlite(self, data):
        with SqliteContext() as cursor:
            sql_check_table = "create table if not exists `银行卡归属银行`(`卡标识` primary key,`银行`,`卡级别`)"
            cursor[0].execute(sql_check_table)
            # 执行SQL语句
            sql_set_data = "insert into `银行卡归属银行`(`卡标识`,`银行`,`卡级别`) values(?,?,?)"
            cursor[0].executemany(sql_set_data, data)
            cursor[1].commit()
            print("******数据添加成功******")


if __name__ == '__main__':
    SetBankcardInfo().set_bankCardInfo_to_sqlite(GetBankcardInfo().get_bankCardInfo_from_mysql())
