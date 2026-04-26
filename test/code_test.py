
import unittest
from time import strftime
from data.path_config import  unittest_reports_path
from public.utils.HTMLTestRunnerNew import HTMLTestRunner


class TestUnittestReport(unittest.TestCase):
    def setUp(self):
        print('这是用例的前置条件')

    def test_01(self):
        print('这是第一条用例')
        assert True

    def test_02(self):
        print('这是第二条用例')
        assert False
    @unittest.skip('跳过这条报错用例')
    def test_03(self):
        print('这是第三条用例')
        raise Exception

    def test_04(self):
        print('这是第四条用例')



    def tearDown(self):
        print('这是用例的后置条件')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    cases = [TestUnittestReport('test_01'), TestUnittestReport('test_02')]
    suite.addTests(cases)
    # 生成测试报告的路径
    now = strftime('%Y-%m-%d-%H-%M-%S')
    filename = unittest_reports_path + now + '_report.html'
    try:
        with open(filename, 'wb') as f:
            runner = HTMLTestRunner(stream=f, title='测试报告', description='用例运行情况如下', tester='Daisy')
            runner.run(suite)
            print("报告生成结束")
    except Exception as e:
        print(f"Error occurred while generating the report: {e}")



