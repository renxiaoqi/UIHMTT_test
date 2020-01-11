"""封装公共方法http://ttmp.research.itcast.cn/#/index"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 获取日志器对象
from tools.get_log import GetLog

logger = GetLog.get_logger()


class Base:
    pass

    # 初始化driver
    def __init__(self, driver):

        logger.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    # 查找元素方法
    def base_find(self, loc, timeout=5, poll=1):
        logger.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 查找一组元素方法
    def base_finds(self, loc, timeout=5, poll=1):
        logger.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))


    # 输入方法
    def base_input(self, loc, text):

        in1 = self.base_find(loc)
        logger.info("正在给{}执行清空操作".format(loc))
        in1.clear()
        logger.info("正在给{}输入信息为：{}".format(loc, text))
        in1.send_keys(text)

    # 点击方法
    def base_click(self, loc):
        logger.info("正在点击：{}".format(loc))
        self.base_find(loc).click()

    # 获取文本方法
    def base_get_text(self, loc):
        logger.info("正在获取{}元素文本值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text
    # 截图
    def base_get_img(self):
        logger.info("出现异常！正在截图")
        # 截图
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用将图片写入报告
        self.__base_write_img()
    # 将图片写入allure报告
    def __base_write_img(self):
        logger.info("有异常！正在截图写入报告")
        with open("./image/err.png","rb",encoding="utf-8") as f:
            allure.attach("错误原因：",f.read(),allure.attach_type.PNG)