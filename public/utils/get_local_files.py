# -*- coding:utf-8 -*-
# @FileName  :get_local_files.py
# @Time      :2024/3/29 23:35
# @Author    :Daisy
# @Brief Introduction    :
from csv import DictReader
import openpyxl


def read_excel(filename, sheetname='Sheet1'):
    '''
    打开Excel，从sheet1 第二行开始读取数据 注：excel纯数字需要定义为文本格式
    :param sheetname: sheet name
    :return: key:value
    '''
    wb = openpyxl.load_workbook(filename)
    ws = wb[sheetname]
    for wd in ws.iter_rows(min_row=2, values_only=True):
        yield wd


def read_csv(filename):
    """
    打开cxv文件
    :param filename:
    :return: key:value
    """
    with open(filename, 'r', encoding='utf-8') as f:
        reader = DictReader(f)
        for rd in reader:
            yield rd