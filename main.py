import time

from public.utils.reports_out import report_out, clear_old_reports, unittest_reports_path

"""
unittest用例执行并生成测试报告
"""

def run_case():
    # 清除旧的测试报告
    clear_old_reports(unittest_reports_path)
    print("======开始执行！！！======")
    name_project = "订阅个人+企业回归测试"
    description = "订阅个人+企业回归测试"
    report_out(name_project, description)
    time.sleep(2)
    print("======执行结束！！！======")

if __name__ == '__main__':
    run_case()

"""
report_out 里配置需要测试的用例
"""