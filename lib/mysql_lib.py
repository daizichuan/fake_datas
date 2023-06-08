# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""
import pymysql

from lib.parse_ini import IniLib

'''从conf.mysql.ini里获取mysql配置，生成mysql操作的上下文'''


class GetMysqlParams:
    def __init__(self):
        self.mysql_params = IniLib('..//conf//mysql.ini').get_kv('银行卡归属银行')
        self.host = self.mysql_params['host']
        self.user = self.mysql_params['user']
        self.password = self.mysql_params['password']
        self.database = self.mysql_params['database']
        self.table = self.mysql_params['table']
        self.port = int(self.mysql_params['port'])

    def get_host(self):
        return self.host

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_database(self):
        return self.database

    def get_table(self):
        return self.table

    def get_port(self):
        return self.port


get_mysql_params = GetMysqlParams()


class MysqlContext:
    def __init__(self):
        self.conn = pymysql.connect(host=get_mysql_params.get_host(),
                                    port=get_mysql_params.get_port(),
                                    user=get_mysql_params.get_user(),
                                    password=get_mysql_params.get_password(),
                                    database=get_mysql_params.get_database())
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()
