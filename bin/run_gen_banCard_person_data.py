#-- coding:UTF-8 --
#!/usr/bin/env python

import time

from src.main import GenBanWaterData

if __name__ == '__main__':
    start_time = time.time()  # 记录程序开始运行时间
    demo = GenBanWaterData()
    demo.gen_bankWater_data(10000000, '1000w.csv') #数据条数和文件名
    end_time = time.time()  # 记录程序结束运行时间
    print('cost %f second' % (end_time - start_time))