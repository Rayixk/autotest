
from aw import *
from operatetest import *

class TestBaiDu(TestCase):
    URL = 'http://www.web.com'
    # excel = DATA_PATH + '/web.xlsx'
    #
    # locator_kw = (By.ID, 'kw')
    # locator_su = (By.ID, 'su')
    # locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        # self.driver = driver.Driver("chrome")
        # self.driver.get(self.URL)
        self.driver = Driver.driver()

    def test_search(self):
        common.get(self.driver,self.URL)
        common.send_keys(self.driver,"id","kw",keys="selenium 灰蓝")
        common.touch_by_id(self.driver,'su')
        common.sleep(3)

        links = common.find_elements(self.driver,"xpath", '//div[contains(@class, "result")]/h3/a')
        for link in links:
            logger.info(link.text)
        common.sleep(2)

        # for d in datas:
        #     with self.subTest(data=d):
        #         self.sub_setUp()
        #         self.driver.find_element(*self.locator_kw).send_keys(d['search'])
        #         self.driver.find_element(*self.locator_su).click()
        #         time.sleep(2)
        #         links = self.driver.find_elements(*self.locator_result)
        #         for link in links:
        #             logger.info(link.text)
        #         self.sub_tearDown()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    pass
    # report = REPORT_PATH + '\\report.html'
    # with open(report, 'wb') as f:
    #     runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
    #     runner.run(TestBaiDu('test_search'))