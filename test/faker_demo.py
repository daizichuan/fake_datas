#-- coding:UTF-8 --
#!/usr/bin/env python
"""

"""

'''
生成不重复数据
'''
from faker import Faker

fk = Faker(locale='zh-cn') # locale参数：默认是英文，'zh-cn'返回中文

# 生成不重复的数据
result_list = [fk.unique.name() for i in range(10)]
print(result_list)