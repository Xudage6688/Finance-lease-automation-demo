"""
fixture夹具 session级别配置文件
"""

from selenium import webdriver

import pytest
import time

user = [['张三','123456'],['李四','654321']]    #定义参数

#影响域session

# @pytest.fixture(scope='session',params=user)    #params 传参    #影响域 class module session
# def driver(request):     #定义一个driver函数 放共性部分功能，引用该函数实现通用功能  #request 必不可少
#     driver =webdriver.Chrome()
#     driver.maximize_window()
#     print("当前登陆用户是："+request.param[0])
#     print("当前登陆密码是："+request.param[1])
#     # return driver
#     yield driver    #添加影响域时需要用yield
#     driver.quit()
