import page
from base.app_base import AppBase


class AppArticlePage(AppBase):

    # 查找频道
    def page_find_channel(self,channel):
        self.swipe_method(page.ele,channel)
    # 查找文章
    def page_find_article(self,article):
        self.find_article_swipe(page.ele2,article)

    # 组合业务方法
    def app_article(self,channel,article):
        self.page_find_channel(channel)
        self.page_find_article(article)