from aw import *
from operatetest import *


class TestBaiDu(TestCase):
    def setUp(self):
        # self.driver = Driver.driver()
        pass

    def test_search(self):
        common.get(self.driver, 'http://www.web.com')
        common.send_keys(self.driver, "id", "kw", keys="selenium 灰蓝")
        common.touch_by_id(self.driver, 'su')
        common.sleep(3)

        links = common.find_elements(self.driver, "xpath", '//div[contains(@class, "result")]/h3/a')
        for link in links:
            self.log.info(link.text)
        common.sleep(2)

    def tearDown(self):
        # self.driver.quit()
        # self.driver.close()
        pass

