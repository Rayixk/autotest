# !/usr/bin/env python
# coding: utf-8

import os
from selenium import webdriver
from operatetest import config

__all__ = ["Driver"]


class Driver:
    @classmethod
    def driver(cls):
        if hasattr(cls, "_instance"):
            return cls._instance

        _type = config.browser_type.lower()
        l = [
            ("chrome", "chromedriver.exe", webdriver.Chrome),
            ("firefox", "geckodriver", webdriver.Firefox),
            ("ie", "IEDriverServer.exe", webdriver.Ie),
            ("phantomjs", "phantomjs.exe", webdriver.PhantomJS),
        ]
        d = {i[0]: i for i in l}
        if _type not in d:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(d.keys()))

        _instance = d[_type][2](executable_path=os.path.join(config.driver_dir, d[_type][1]))
        setattr(cls, "_instance", _instance)
        return _instance


# def get_driver():
#     _type = config.browser_type.lower()
#     l=[
#         ("chrome","chromedriver.exe",webdriver.Chrome),
#         ("firefox","geckodriver",webdriver.Firefox),
#         ("ie","IEDriverServer.exe",webdriver.Ie),
#         ("phantomjs","phantomjs.exe",webdriver.PhantomJS),
#     ]
#     d = {i[0]:i for i in l}
#     if _type not in d:
#         raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(d.keys()))
#
#     return l[_type][2](executable_path=os.path.join(config.driver_dir,l[_type][1]))




class UnSupportBrowserTypeError(Exception):
    pass

    #
    # class Driver11(object):
    #     def __init__(self, browser_type='firefox'):
    #         self._type = browser_type.lower()
    #         if self._type in TYPES:
    #             self.browser = TYPES[self._type]
    #         else:
    #             raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
    #         self.driver = None
    #
    #     def get(self, url, maximize_window=True, implicitly_wait=30):
    #         self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
    #         self.driver.get(url)
    #         if maximize_window:
    #             self.driver.maximize_window()
    #         self.driver.implicitly_wait(implicitly_wait)
    #         return self
    #
    #     def save_screen_shot(self, name='screen_shot'):
    #         day = time.strftime('%Y%m%d', time.localtime(time.time()))
    #         screenshot_path = REPORT_PATH + '\screenshot_%s' % day
    #         if not os.path.exists(screenshot_path):
    #             os.makedirs(screenshot_path)
    #
    #         tm = time.strftime('%H%M%S', time.localtime(time.time()))
    #         screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
    #         return screenshot
    #
    #     def close(self):
    #         self.driver.close()
    #
    #     def quit(self):
    #         self.driver.quit()
    #
    #
    #     def find_element(self,*args,**kwargs):
    #         return self.driver.find_element(*args,**kwargs)
    #
    #     def find_elements(self, *args, **kwargs):
    #         return self.driver.find_elements(*args, **kwargs)
