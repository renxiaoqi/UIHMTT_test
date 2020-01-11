from page.app_login_page import AppLoginPage
from page.mis_article_check import MisArticlePage
from page.mis_login_page import MisLoginPage
from page.mp_article_page import MpArticlePage
from page.mp_login_page import MpLoginPage
from page.app_article_page import AppArticlePage


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取MpLoginPage对象
    def get_mp_login_page(self):
        return MpLoginPage(self.driver)

    # 获取MpArticlePage对象
    def get_mp_article_page(self):
        return MpArticlePage(self.driver)

    # 获取MisLoginPage对象
    def get_mislogin_page(self):
        return MisLoginPage(self.driver)

    # 获取MisArticlePage对象
    def get_mis_article_page(self):
        return MisArticlePage(self.driver)

    # 获取AppLoginPage对象
    def get_app_login_page(self):
        return AppLoginPage(self.driver)

    # 获取AppArticlePage对象
    def get_app_article_page(self):
        return AppArticlePage(self.driver)
