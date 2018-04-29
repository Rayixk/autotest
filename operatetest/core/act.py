from ..auxiliary import VAR
from .runner import HTMLTestRunner
from scripts.test_baidu2 import TestBaiDu

def run():
    # print("start run")
    # print(VAR.driver_dir)
    # print(VAR.report_dir)
    #
    # a = Driver.driver()
    # b = Driver.driver()
    #
    # print(type(a))
    # print(type(b))
    # print(a is b)
    #
    # a.close()
    report = VAR.report_dir + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaiDu('test_search'))


