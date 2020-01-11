import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

# 获取日志器对象
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mp)
        # 获取统一入口类
        self.page = PageIn(self.driver)
        # 调用登录成功业务方法
        self.page.get_mp_login_page().mp_login_success()
        # 获取MpArticlePAge对象
        self.article = self.page.get_mp_article_page()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()

    # 测试发布文章业务方法
    @pytest.mark.parametrize("title,content,expect",read_yaml("mp_article.yml"))
    def test_article(self,title,content,expect):
        # 调用发布文章的方法
        self.article.page_publish_article(title,content)
        # 断言
        try:
            assert expect == self.article.page_get_commit_result()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()

