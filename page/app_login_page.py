from time import sleep

import page
from base.app_base import AppBase


class AppLoginPage(AppBase):
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.app_username,username)
    # 输入密码
    def page_input_password(self,app_password):
        self.base_input(page.app_password,app_password)
    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)
    # 判断我是否存在
    def page_get_nickname(self):
        try:
            el = self.base_find(page.app_my,timeout=3)
            print("找到我的菜单了，他的位置位于{}".format(el.location))
            return True
        except:
            print("没有找到我的菜单")
            return False

    # 组合登录方法
    def page_app_login(self,username,pwd):
        sleep(2)
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()

    def get_app_login_success_page(self,username=page.app_get_app_login_data[0],
                                   pwd=page.app_get_app_login_data[1]):
        sleep(2)
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()
