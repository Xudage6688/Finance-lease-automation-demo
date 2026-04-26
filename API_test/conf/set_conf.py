# -*- coding:utf-8 -*-
# @FileName  :set_conf.py
# @Time      :2024/5/7 16:00
# @Author    :Daisy
# @Brief Introduction    : 获取配置文件中相关信息
import configparser
import pathlib

# 定义conf.ini路径
file = pathlib.Path(__file__).parents[0].resolve() / "conf.ini"

# 读取conf配置信息
def read(section, option):
    conf = configparser.ConfigParser()
    conf.read(file)
    values = conf.get(section, option)
    return values