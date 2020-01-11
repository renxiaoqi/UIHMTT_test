import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mis)
        # 获取统一入口类
        self.page = PageIn(self.driver)
        # 获取登录业务方法
        self.mis_login = self.page.get_mislogin_page()
    # 结束
    def teardown_class(self):
        # 退出driver
        GetDriver.quit_driver()
    # 登录测试方法
    @pytest.mark.parametrize("username,password,expect",read_yaml("mis_login.yaml"))
    def test01(self,username,password,expect):
        # 调用后台管理员登录的方法
        self.mis_login.page_mis_login(username,password)
        # 断言
        try:
            assert expect == self.mis_login.get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_img()

