# -*- coding:utf-8 -*-
# @FileName  :test_order_approval.py
# @Time      :2024/3/30 1:14
# @Author    :Daisy
# @Brief Introduction    :
# -*- coding:utf-8 -*-
# @FileName  :test_app_personal.py
# @Time      :2024/1/27 23:42
# @Author    :Daisy
import os

import allure
import pytest
from page_object.approve_order import *
import warnings
# 忽略urllib3 重连错误
warnings.filterwarnings('ignore')

@allure.feature("PC信审")
class TestAppApproval:
    def setup_class(self):
        self.driver = webdriver.Chrome(options=chrome_options)  # 用调试模式打开driver对象
        self.app = ApprovalProcess(self.driver, 'Pre')

    @allure.story("信审操作")
    def test_order_approval(self):  # 信审
        self.app.approve_process('6799674996')
        # allure.attach(self.driver.get_screenshot_as_png(),  "信审截图")

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(
        ['-vs', '--alluredir=../temp/allure/reports', '--clean-alluredir', './test_order_approval.py'])
    # 中间生成allure报告路径
    os.system("allure serve ../temp/allure/reports")  # 添加allure服务，生成报告路径
