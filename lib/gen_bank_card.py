# -- coding:UTF-8 --
# !/usr/bin/env python


import random


class GenBankCard:
    '''
    根据输入的前6位数字，生成银行卡号。前6位数字对应着银行和卡类型
    '''

    def gen_card_num(self, start_with, total_num):
        result = start_with
        # 随机生成前N-1位
        while len(result) < total_num - 1:
            result += str(random.randint(0, 9))
        # 计算前N-1位的校验和
        s = 0
        card_num_length = len(result)
        for _ in range(2, card_num_length + 2):
            t = int(result[card_num_length - _ + 1])
            if _ % 2 == 0:
                t *= 2
                s += t if t < 10 else t % 10 + t // 10
            else:
                s += t
        # 最后一位当做是校验位，用来补齐到能够整除10
        t = 10 - s % 10
        result += str(0 if t == 10 else t)
        return result

    def luhn(self, card_num):
        s = 0
        card_num_length = len(card_num)
        for _ in range(1, card_num_length + 1):
            t = int(card_num[card_num_length - _])
            if _ % 2 == 0:
                t *= 2
                s += t if t < 10 else t % 10 + t // 10
            else:
                s += t
        return s % 10 == 0


if __name__ == '__main__':
    demo = GenBankCard()
    random_card_num = demo.gen_card_num('622609', 16)
    valid_result = demo.luhn(random_card_num)
    print('%s %s' % (random_card_num, valid_result))
