# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""
import datetime
from lib.singleton import Singleton


@Singleton
class GenSerialNumber(object):
    '''生成流水号'''
    i = 0

    def gen_serial_number(self):
        code_qz = 'DD'
        code_sj = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.i += 1
        code_ls = str(self.i).zfill(8)
        return code_qz + code_sj + code_ls


if __name__ == '__main__':
    print(GenSerialNumber().gen_serial_number())
    GenSerialNumber().gen_serial_number()
    GenSerialNumber().gen_serial_number()
