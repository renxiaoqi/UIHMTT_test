from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base import Base


class WebBase(Base):

    # 选择状态ul->li
    def web_base_click(self,placeholder_text,click_text):
        # 组合placeholder文本元素定位信息
        loc = By.XPATH,'//*[@placeholder="{}"]'.format(placeholder_text)
        # 查找元素并点击
        self.base_click(loc)
        sleep(2)
        # 定位ul->li  ->列表
        loc = By.CSS_SELECTOR,'ul>li'
        my_list = self.base_finds(loc)
        # 遍历text内容=click_text 条件成立，点击
        for el in my_list:
            if el.text == click_text:
                el.click()
                break
    # 判断元素是否存在
    def get_id(self,id):
        loc = By.XPATH,"//*[contains(text(),'{}')]".format(id)
        try:
            self.base_find(loc,timeout=3)
            print("找到元素啦!")
            return True
        except:
            print("没有找到元素 。。")
            return False
