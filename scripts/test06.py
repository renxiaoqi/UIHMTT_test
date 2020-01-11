from time import sleep

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()

class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_app_driver()
        # 获取统一入口类
        self.page = PageIn(self.driver)
        # 获取登录成功方法
        self.page.get_app_login_page().get_app_login_success_page()
        # 获取apparticlepage方法
        self.app_article = self.page.get_app_article_page()


    # 结束
    def teardown_class(self):
        GetDriver.quit_app_driver()
    # 查找文章测试业务方法
    def test01(self,channel="java",article="Java"):
        # 调用查找文章的方法
        self.app_article.app_article(channel,article)
        # 断言


