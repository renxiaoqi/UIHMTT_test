from time import sleep

import page
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()

class MisLoginPage(Base):
    # 输入用户名
    def page_send_username(self,username):
        self.base_input(page.mis_username,username)

    # 输入密码
    def page_send_password(self,password):
        self.base_input(page.mis_password,password)

    # 点击登录
    def page_click_btn(self):
        # 改变按钮为可点击状态
        js = "document.getElementById('inp1').disabled=false"
        # 调用执行js语句的方法
        self.driver.execute_script(js)
        self.base_click(page.mis_commit_btn)
    # 获取昵称
    def get_nickname(self):
        return self.base_get_text(page.mis_get_nickname)

    # 组合业务方法
    def page_mis_login(self,username,password):
        log.info("正在调用后台登录的组合业务方法")
        self.page_send_username(username)
        self.page_send_password(password)
        self.page_click_btn()

    # 组合业务成功方法
    def page_success_mis_login(self, username="testid", password="testpwd123"):
        log.info("正在调用后台登录的组合业务方法")
        self.page_send_username(username)
        self.page_send_password(password)
        self.page_click_btn()
