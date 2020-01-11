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
        # 获取登录方法
        self.app_login = PageIn(self.driver).get_app_login_page()

    # 结束
    def teardown_class(self):
        GetDriver.quit_app_driver()
    # app登录业务方法
    def test01(self,username=page.app_get_app_login_data[0],pwd=page.app_get_app_login_data[1]):
        # 调用app登录的方法
        self.app_login.page_app_login(username,pwd)
        # 断言
        try:
            self.app_login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.app_login.base_get_img()

