import time

import page
from base.base import Base
from tools.get_log import GetLog

logger = GetLog.get_logger()

class MpLoginPage(Base):
    # 输入手机号
    def mp_login_input_phone(self,phone):
        self.base_input(page.mp_phone,phone)
    # 输入验证码
    def mp_login_input_verify_code(self,password):
        self.base_input(page.mp_code,password)
    # 点击登录
    def mp_login_click(self):
        self.base_click(page.mp_login_but)
    # 获取昵称
    def mp_login_get_name(self):
        return self.base_get_text(page.mp_nickname)
    # 组合业务方法（测试脚本业务层调用）
    def mp_login(self,phone,code):
        logger.info("正在调用自媒体登录业务方法，用户名：{} 密码：{}".format(phone,code))
        self.mp_login_input_phone(phone)
        self.mp_login_input_verify_code(code)
        self.mp_login_click()

    def mp_login_success(self,phone="13812345678",code="246810"):
        logger.info("正在调用自媒体登录业务方法，用户名：{} 密码：{}".format(phone,code))
        self.mp_login_input_phone(phone)
        self.mp_login_input_verify_code(code)
        time.sleep(1)
        self.mp_login_click()
