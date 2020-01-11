from time import sleep

import page
from base.web_base import WebBase


class MisArticlePage(WebBase):
    id_text = None
    # 点击信息管理
    def page_click_manage(self):
        sleep(2)
        self.base_click(page.mis_click_manage)

    # 点击内容审核
    def page_click_content(self):
        sleep(2)
        self.base_click(page.mis_click_article)

    # 输入文章标题
    def page_input_title(self,title):
        self.base_input(page.mis_title,title)

    # 输入频道
    def page_input_channel(self,channel):
        self.base_input(page.mis_channel,channel)

    # 选择状态--待审核
    def page_click_status(self,placeholder_text,click_text):
        self.web_base_click(placeholder_text,click_text)

    # 点击查询按钮
    def page_click_select_btn(self):
        self.base_click(page.mis_search)


    # 点击通过
    def page_click_pass(self):
        self.base_click(page.mis_pass)

    # 确认通过
    def page_click_sure_pass(self):
        sleep(2)
        self.base_click(page.mis_sure_pass)
        sleep(5)

    # 获取id
    def page_get_id(self):
        return self.base_get_text(page.mis_get_id)

    # 组合业务方法
    def mis_article(self,title,channel):
        self.page_click_manage()
        self.page_click_content()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status("请选择状态","待审核")
        self.page_click_select_btn()
        sleep(3)
        # 获取id
        id_text = self.page_get_id()
        print("正在审核的文章id为：", id_text)
        self.page_click_pass()
        self.page_click_sure_pass()

    # 断言
    def ass(self,title,channel):
        sleep(4)
        # 刷新
        self.driver.refresh()
        # 输入标题
        self.page_input_title(title)
        # 输入频道
        self.page_input_channel(channel)
        # 选择状态
        self.page_click_status("请选择状态","审核通过")
        # 点击查询
        self.page_click_select_btn()
        sleep(3)
        # 获取查询id
        return self.get_id(self.page_get_id())