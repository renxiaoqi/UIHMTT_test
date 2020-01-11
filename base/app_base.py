from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class AppBase(Base):
    def swipe_method(self,element,channel):
        # 获取元素位置
        sleep(3)
        ele = self.base_find(element)
        location = ele.location
        y = location.get("y")
        # 获取元素宽高
        size = ele.size
        width = size.get("width")
        height = size.get("height")
        # 计算star_x,start_y;end_x,end_y
        star_x = width*0.8
        start_y = height*0.5 + y
        end_x = width*0.2
        end_y = height*0.5 + y
        # 组合包含的元素定位信息
        loc = By.XPATH,"//*[@class='android.widget.HorizontalScrollView']//*[contains(@text,'{}')]".format(channel)
        # 获取当前页面结构
        ele2 = By.XPATH,"//*[@class='android.widget.HorizontalScrollView']//*[@class='android.view.View']"
        page_source = self.base_finds(ele2)

        while True:
            # 首先 查找一次当前页面是否存在要找的元素
            try:
                el = self.base_find(loc,timeout=3)
                print("找到指定频道了！")
                # 找到元素之后点击
                el.click()
                # 跳出循环
                break
            except:
                print("没有找到指定频道。。。")
                # 滑动屏幕
                self.driver.swipe(star_x,start_y,end_x,end_y,2000)
            if page_source == self.base_finds(ele2):
                print("滑不动了")
                raise Exception("异常，已经到最后一屏了")
            else:
                # 更新page_source的值
                page_source = self.base_finds(ele2)

    # 查找指定文章
    def find_article_swipe(self,ele,article):
        sleep(3)
        # 获取元素尺寸
        size = self.base_find(ele).size
        # 获取宽高
        width = size.get("width")
        height = size.get("height")
        # 计算
        star_x = width*0.5
        star_y = height*0.8
        end_x = width*0.5
        end_y = height*0.2
        loc1 = By.XPATH,"//*[@bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(article)
        loc2 = self.driver.page_source
        # 首先 查找当前页面是否存在要查找的文章标题
        while True:
            try:
                print("正在查找名为{}的文章".format(article))
                el = self.base_find(loc1,timeout=5)
                print("查找到名为{}的文章啦".format(article))
                el.click()
                # 跳出循环
                break
            except:
                print("没有查找到名为{}的文章".format(article))
                # 滑动
                self.driver.swipe(star_x,star_y,end_x,end_y,2000)
            if loc2 == self.driver.page_source:
                print("滑不动了，已经是最后一页了！")
                raise Exception("异常！已经是最后一页了")
            else:
                # 更新name_list
                loc2 = self.driver.page_source


















