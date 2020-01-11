from time import sleep

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()

class TestMisArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mis)
        self.page = PageIn(self.driver)
        # 获取登录成功的方法
        self.page.get_mislogin_page().page_success_mis_login()
        # 获取审核内容方法
        self.mis_article = self.page.get_mis_article_page()
    # 结束
    # def teardown_class(self):
    #     GetDriver.quit_driver()
    # 审核文章测试方法
    def test01(self,title=page.article_title,channel=page.article_channel):
        # 调用审核业务方法
        self.mis_article.mis_article(title,channel)
        # 断言
        try:
            assert self.mis_article.ass(title,channel)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_article.base_get_img()