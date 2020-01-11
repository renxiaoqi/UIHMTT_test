import sys, os

sys.path.append(os.getcwd())

import pytest
from tools.get_log import GetLog


from tools.read_yaml import read_yaml

import page

from page.page_in import PageIn
from tools.get_driver import GetDriver

logger = GetLog.get_logger()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mp)
        # 获取统一入口类的页面对象
        self.pagein = PageIn(self.driver)

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 测试业务方法
    @pytest.mark.parametrize("phone,code,expect", read_yaml("mp_login.yaml"))
    def test01(self, phone, code, expect):
        # 调用登录方法
        self.pagein.get_mp_login_page().mp_login(phone, code)
        # 断言
        try:
            # 断言昵称
            username = self.pagein.get_mp_login_page().mp_login_get_name()
            assert expect == username

        except Exception as e:
            # 日志
            logger.error(e)
            # 截图
            self.pagein.get_mp_login_page().base_get_img()
