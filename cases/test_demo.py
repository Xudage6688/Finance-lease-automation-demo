# """
# fixture夹具练习
# """
# # from selenium import webdriver
# #
# import pytest
# import time
# #
# # user = [['张三','123456'],['李四','654321']]    #定义参数
# #
# # #影响域 class module session
# #
# # @pytest.fixture(scope='module',params=user)    #params 传参    #影响域 class module session
# # def driver(request):     #定义一个driver函数 放共性部分功能，引用该函数实现通用功能  #request 必不可少
# #     driver =webdriver.Chrome()
# #     driver.maximize_window()
# #     print("当前登陆用户是："+request.param[0])
# #     print("当前登陆密码是："+request.param[1])
# #     # return driver
# #     yield driver    #添加影响域时需要用yield
# #     driver.quit()
#
#
# class Testdemo01:
#     def test_01(self,driver):  # 引用driver函数，每次运行前会先运行该函数
#         browser = driver
#         browser.get("http://www.baidu.com")
#         time.sleep(3)
#
#     def test_02(self,driver): #引用driver函数，每次运行前会先运行该函数
#         browser = driver
#         browser.get("http://image.baidu.com")
#         time.sleep(3)
#
#     def test_03(self): #不引用driver函数 单独运行test03功能
#         print("test03")
#
# class Testdemo02:
#     def test_04(self,driver): #引用driver函数，每次运行前会先运行该函数
#         browser = driver
#         browser.get("http://www.baidu.com")
#         time.sleep(3)
#
#     def test_05(self,driver): #引用driver函数，每次运行前会先运行该函数
#         browser = driver
#         browser.get("http://image.baidu.com")
#         time.sleep(3)
#
#     def test_06(self): #不引用driver函数 单独运行test06功能
#         print("test06")
#
# if __name__ == '__main__':
#     pytest.main('-vs','./test_demo.py')