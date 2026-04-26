# -*- coding:utf-8 -*-
# @FileName  :test_request_pay.py
# @Time      :2024/3/30 1:13
# @Author    :Daisy
# @Brief Introduction    :
# -*- coding:utf-8 -*-
# @FileName  :test_app_personal.py
# @Time      :2024/1/27 23:42
# @Author    :Daisy
import os
import allure
import pytest
from page_object.request_pay import *
import warnings
# 忽略urllib3 重连错误
warnings.filterwarnings('ignore', message='.*connection broken by \'NewConnectionError\'')

@allure.feature("APP请款")
class TestPayRequest:
    def setup_class(self):
        chrome_options = Options()
        # 配置为调试模式
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        time.sleep(1)
        self.driver = webdriver.Chrome(options=chrome_options)  # 用调试模式打开driver对象
        self.pay = RequestPayout(self.driver, 'Uat')

    @allure.story("APP请款操作")
    def test_pay_request(self):  # 请款
        self.pay.request_payout()
        allure.attach(self.driver.get_screenshot_as_png(),  "请款截图")

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(
        ['-vs', '--alluredir=../temp/allure/reports', '--clean-alluredir', './test_request_pay.py'])  # 中间生成allure报告路径
    os.system("allure serve ../temp/allure/reports")  # 添加allure服务，生成报告路径
