# -*- coding:utf-8 -*-
# @FileName  :elements.py
# @Time      :2024/1/27 18:13
# @Author    :Daisy
"""
存放页面元素
"""


class Element():
    #登陆输入框
    ele_userInput = '//*[@id="app"]/div[1]/div[2]/div/div[2]/form/div[1]/div/div/div/input'
    ele_userPwd = '//*[@id="app"]/div[1]/div[2]/div/div[2]/form/div[2]/div/div/div/input'
    #首页查询中心
    home_Query_Center = '//span[text()="查询中心"]'
    #查询中心下
    query_Preaudit = '//span[text()=" 预审结果查询 "]'
    order_List = '//span[text()=" 订单列表 "]'
    query_Sign = '//span[text()=" 签约结果查询 "]'
    #销售中心下
    query_OrderInfo = '//span[text()=" 订单信息查询 "]'
    query_ContractInfo = '//span[text()=" 对公合同信息查询 "]'
    query_Commission = '//span[text()=" 佣金查询 "]'