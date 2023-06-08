#-- coding:UTF-8 --
#!/usr/bin/env python
"""
"""

'''
生成重复数据（一直不重复，无论运行多少次）
'''
from faker import Faker

class repeat_date():
    def __init__(self):
        self.fk = Faker(locale='zh-cn')

    def test_01(self):
        Faker.seed(10)
        print(self.fk.name())

    def test_02(self):
        Faker.seed(10)
        print(self.fk.name())

if __name__ == '__main__':
    tt = repeat_date()
    tt.test_01()
    tt.test_02()