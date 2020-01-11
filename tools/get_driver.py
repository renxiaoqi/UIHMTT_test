"""
# 自媒体
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"

"""

from selenium import webdriver
from appium import webdriver as app

import page


class GetDriver:
    # web 页面 driver
    __driver = None
    # app 页面 driver
    __app_driver = None
    # 获取web 页面 driver
    @classmethod
    def get_driver(cls,url):
        if cls.__driver is None:
            # 获取driver对象
            cls.__driver = webdriver.Chrome()
            # 窗口最大化
            cls.__driver.maximize_window()
            # 打开url
            cls.__driver.get(url)
        # 返回driver
        return cls.__driver
    # 关闭web 页面 driver
    @classmethod
    def quit_driver(cls):
        # 如果driver不为空，关闭driver
        if cls.__driver is not None:
            cls.__driver.quit()
            # 置空
            cls.__driver = None
    # 获取app 页面 driver
    @classmethod
    def get_app_driver(cls):
        cap = {}
        if cls.__app_driver is None:
            # server 启动参数
            # 设备信息
            cap['platformName'] = 'Android'
            cap['platformVersion'] = '5.1'
            cap['deviceName'] = 'CSX0217728000025'
            # app的信息
            cap['appPackage'] = page.appPackage
            cap['appActivity'] = page.appActivity
            # 中文
            cap['unicodeKeyboard'] = True
            cap['resetKeyboard'] = True
            # 不重置应用
            # cap['noReset'] = False
        return app.Remote("http://127.0.0.1:4723/wd/hub",cap)
    # 关闭app 页面 driver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver :
            cls.__app_driver.quit()
            cls.__app_driver = None

