import time
from selenium.webdriver.common.by import By

def sleep(n):
    time.sleep(n)

def touch_by_id(driver, id):
    """click by id"""
    driver.find_element(By.ID, id).click()


def get(driver, url, maximize_window=True, implicitly_wait=30):
    driver.get(url)
    if maximize_window:
        driver.maximize_window()
    driver.implicitly_wait(implicitly_wait)

def send_keys(driver,*con,keys):
    """
    输入字符
    :param driver: webdriver对象
    :param con: 元素搜索条件,如 "id","kw" 
    :param keys: 需要输入字符
    :example:common.send_keys(driver,"id","kw",keys="baidu") 
    """
    driver.find_element(*con).send_keys(keys)

def find_elements(driver,*con):
    """
    查找元素
    :param driver: webdriver对象
    :param con: 元素搜索条件,如 "id","kw" 
    :return: elements
    :example:common.find_elements(driver,"xpath", '//div[contains(@class, "result")]/h3/a') 
    """
    return driver.find_elements(*con)






