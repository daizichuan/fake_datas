# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""

import configparser


class IniLib:
    '''读取Ini配置信息'''

    def __init__(self, ini_name):
        # 实例化configParser对象
        self.config = configparser.ConfigParser()
        # read读取ini文件,设定编解码方式
        self.config.read(f'{ini_name}', encoding='UTF8')

    def get_keys(self, section):
        # 获取指定段的所有key
        return self.config.options(f'{section}')

    def get_kv(self, section):
        # 获取指定段的所有kv,元祖转换测字典
        return dict(self.config.items(f'{section}'))

    def get_value(self, section, key):
        # 获取对应段的k的v
        return self.config.get(f'{section}', f'{key}')


if __name__ == '__main__':
    demo = IniLib('..//conf//mysql.ini')
    print(demo.get_keys('银行卡归属银行'))
    print(demo.get_kv('银行卡归属银行'))
    print(demo.get_value('银行卡归属银行', 'ip'))
