import random
import string
import re


valid_str = re.sub(r'[IOQ]', '', (string.digits + string.ascii_uppercase))      # 车架号可用的字符串
str_weight = dict(zip(valid_str, '012345678912345678123457923456789'))      # 各个字符串所对应的值，用于校验计算
index_weight = dict(zip(list(range(16)), [8, 7, 6, 5, 4, 3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]))    # vin各个位数的加权系数


def get_vin():
    """生成随机vin"""
    vin_16 = random.choices(valid_str, k=16)    # 随机生成16位数，第9位是通过加权计算后插入
    ninth = sum(map(lambda x: int(index_weight[x[0]]) * int(str_weight[x[1]]), enumerate(vin_16))) % 11     # 进行加权计算
    if ninth == 10:
        ninth = 'X'
    vin_16.insert(8, str(ninth))
    return ''.join(vin_16)

print(get_vin())
"""
def write_in_csv(num):
    
    批量生成vin号并写入文档中
    :param num: vin数量
    :return:
    
    with open(r'.\random_vin.csv', 'w') as f:
        f.write('vin')
        f.write('\n')
        for i in range(num):
            f.write(get_vin())
            f.write('\n')


if __name__ == '__main__':
    while True:
        a = input()
        vin = get_vin()
        print(vin)
        pyperclip.copy(vin)     # 复制到剪贴板中可以直接复制
"""


