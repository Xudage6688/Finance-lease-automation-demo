# -*- coding:utf-8 -*-
# @FileName  :reports_out.py
# @Time      :2024/5/10 11:17
# @Author    :Daisy
# @Brief Introduction    : 封装测试报告
import shutil
import time
import unittest
from public.utils.HTMLTestRunnerNew import HTMLTestRunner  # 引入导入的报告模板
from data.path_config import *


from BeautifulReport import BeautifulReport as bf


def report_out(name_project, description):
    """
    :name_project : 项目名称=>用于报告命名及描述
    :description : 描述
    """

    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(cases_path, pattern='*subscription.py')
    # HTMLTestRunner版本

    # report_name = unittest_reports_path + now + '-' + name_project + '_report.html'  # 报告名称
    # with open(report_name, 'wb') as f:  # 运行用例生成测试报告
    #     runner = HTMLTestRunner(stream=f,
    #                             title=name_project,
    #                             description=description,
    #                             tester='Daisy',
    #                             verbosity=2)
    #     runner.run(discover)

    """
    stream:要操作的文件；
    title：测试报告标题；
    description：报告描述；
    verbosity：报告级别。
    """

    # BeautifulReport版本
    run = bf(discover)
    report_name = now + '-' + name_project + '_report.html'  # 报告名称
    run.report(filename=report_name, report_dir=unittest_reports_path, description=description)

    """
    stream:要操作的文件；
    title：测试报告标题；
    description：报告描述；
    verbosity：报告级别。
    """


# 清空历史报告
def clear_old_reports(directory):
    if os.path.exists(directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):  # 如果是目录，则递归删除
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")


# 清除unittest_reports目录下的旧报告
unittest_reports_path = 'C:\\Users\\Xu\\PycharmProjects\\pythonProject2\\temp\\unittest_reports'
# clear_old_reports(unittest_reports_path)
