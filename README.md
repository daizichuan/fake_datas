# fake_datas
当时用来造银行卡流水数据

#### 1、lib.gen_bankCard_info.py mysql上有银行卡前归属地银行，把数据导入sqlite，方便造数据是查询
#### 2、lib.gen_bankCard_person 生成人银行卡数据入sqlite
#### 3、src.main.py GenBanWaterData 调取各种创建数据的类/方法，放入列表里，然后写入csv或sqlite里
#### 4、bin.run_gen_banCard_person_data.py 设置需要的数据条数和csv名称，此为主入口