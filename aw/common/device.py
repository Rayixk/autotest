import time


def sleep(n):
    time.sleep(n)


def touchByText(ad, text):
    """
    根据文本点击
    :param ad: 
    :param text: 
    :return: 
    """
    ad(text=text).click()

def touchByDesc(ad,desc):
    """
    根据描述点击
    :param ad: 
    :param desc: 
    :return: 
    """
    ad(description=desc).click()

def launchApp(ad,pkgname):
    """
    启动app
    :param ad: 
    :param pkgname: 
    :return: 
    """
    ad.app_start(pkgname)

def stopApp(ad,pkgname):
    """
    停止app
    :param ad: 
    :param pkgname: 
    :return: 
    """
    ad.app_stop(pkgname)

def touchById(ad, id):
    """
    根据id点击
    :param ad: 
    :param id: 
    :return: 
    """
    ad(text='私人FM').click()

