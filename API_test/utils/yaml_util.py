# -*- coding:utf-8 -*-
# @FileName  :yaml_util.py
# @Time      :2024/5/13 17:07
# @Author    :Daisy
# @Brief Introduction    :
# -*- coding:utf-8 -*-
# @FileName  :yaml_util.py
# @Time      :2024/5/13 11:31
# @Author    :Daisy
# @Brief Introduction    : yaml读取工具

import yaml




class YamlUtils:
    def __init__(self, yaml_path):
        """
        :param yaml_path: yaml文件路径
        """
        self.yaml_path = yaml_path

    def read_yaml(self):
        """
        读取yaml，对yaml反序列化：把yaml格式转换成dict格式
        :return:
        """
        with open(self.yaml_path, encoding='utf-8') as f:
            value = yaml.safe_load(f)  # 使用 SafeLoader 替代 FullLoader 提高安全性
            return value






if __name__ == '__main__':
    YamlUtils('test_api.yaml').read_yaml()