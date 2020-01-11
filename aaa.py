# 导包
import time

from appium import webdriver

capabilities = {
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "模拟器",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
        "resetKeyboard":True,  # 解决输入中文的问题
    "unicodeKeyboard":True
}

# 创建驱动对象
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                          desired_capabilities=capabilities)
driver.g
# 设置等待
time.sleep(2)
# 退出驱动对象
driver.quit()