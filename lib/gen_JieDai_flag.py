# -- coding:UTF-8 --
# !/usr/bin/env python
"""

"""

import random
from lib.singleton import Singleton


@Singleton
class GenJieDaiFlag:
    '''随机生成借贷标志'''

    def gen_jieDai_flag(self):
        return '进' if random.randint(0, 100) % 2 else '出'


if __name__ == '__main__':
    print(GenJieDaiFlag().gen_jieDai_flag())
