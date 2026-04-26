# """
# 百度元素定位练习
# """
#
# from selenium import webdriver
# import time
# import pytest
# from selenium.webdriver.common.by import By
#
#
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# class TestDemo1:
#     def test_01(self,driver):
#         driver.get("http://www.baidu.com")
#         # element = driver.find_element(By.ID,'kw') #ID属性
#         # element = driver.find_element(By.NAME, 'wd')  #NAME属性
#         # element = driver.find_element(By.CLASS_NAME, 's_ipt') #CLASS属性
#         elements = driver.find_elements(By.TAG_NAME, 'input')  #TAG标签属性 元素不唯一无法定位
#         elements[0].send_keys("深圳天气")   #控制台$x('input') 定位到输入框元素索引[0]
#         time.sleep(5)
#
#     def test_02(self,driver):
#         driver.get("http://www.baidu.com")
#         # element = driver.find_element(By.LINK_TEXT,'新闻')    #a标签通常是链接所在
#         element = driver.find_element(By.PARTIAL_LINK_TEXT, 'hao')  #模糊文本匹配
#         element.click()
#         time.sleep(5)
#
#     def test_03(self,driver):
#         driver.get("http://www.baidu.com")
#         # driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys("深圳天气")
#         # driver.find_element(By.XPATH,'//input[@type="submit"]').click()
#         driver.find_element(By.XPATH,'//span[text()="担负起新的文化使命"]/..').click()  #/..定位父级目录
#         pass
#         time.sleep(5)
#
