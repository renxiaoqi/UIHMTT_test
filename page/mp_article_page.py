import time

import page
from base.base import Base


# 获取日志器对象
from tools.get_log import GetLog

log = GetLog.get_logger()

class MpArticlePage(Base):

    # 点击 内容管理
    def page_click_content_manage(self):
        time.sleep(2)
        self.base_click(page.mp_content_manage)
        time.sleep(2)
    # 点击 发布文章
    def page_click_publish_article(self):
        self.base_click(page.mp_publish_article)
        time.sleep(1)
    # 输入 文章标题
    def page_input_title(self,title):
        self.base_input(page.mp_article_title,title)
    # 输入 文章内容
    def page_input_content(self,content):
        # 切换iframe
        element = self.base_find(page.mp_iframe)

        self.driver.switch_to.frame(element)
        log.info("已切换到iframe")
        time.sleep(2)
        # 输入文章内容
        self.base_input(page.mp_input_content,content)
        time.sleep(2)
        # 切换会默认目录
        self.driver.switch_to.default_content()

    # 选择 封面
    def page_click_cover(self):
        self.base_click(page.mp_select_cover)
    # 选择 频道
    def page_click_channel(self):

        # 点击选择频道
        self.base_click(page.mp_select)
        time.sleep(2)
        # 选择对应频道
        self.base_click(page.mp_select_database)

    # 点击 发表
    def page_click_commit(self):
        self.base_click(page.mp_commit)

    # 获取 发布提示结果
    def page_get_commit_result(self):
        return self.base_get_text(page.mp_commit_result)
    # 组合业务方法
    def page_publish_article(self,title,content):
        log.info("正在调用文章发布业务方法，文章标题为{}，文章内容为{}".format(time,content))
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_commit()
