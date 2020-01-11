# 自媒体
from tools.read_yaml import read_yaml

url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"


"""以下为自媒体配置数据"""
from selenium.webdriver.common.by import By


# 手机号
mp_phone = By.CSS_SELECTOR,"[placeholder='请输入手机号']"
# 验证码
mp_code = By.CSS_SELECTOR,'[placeholder="验证码"]'
# 登录按钮
mp_login_but = By.CSS_SELECTOR,'.el-button--primary'
# 获取昵称
mp_nickname = By.CSS_SELECTOR,".user-name"


"""

"""
# 点击 内容管理
mp_content_manage = By.XPATH,'//*[@class="el-submenu__title"]//*[text()="内容管理"]'
# 点击 发布文章
mp_publish_article = By.XPATH,'//*[contains(text(),"发布文章")]'
# 输入 文章标题
mp_article_title = By.CSS_SELECTOR,'[placeholder="文章名称"]'
# 输入内容之前要切换iframe标签
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 输入 文章内容
mp_input_content = By.CSS_SELECTOR, "#tinymce"
# 选择 封面
mp_select_cover = By.XPATH,"//*[text()='自动']"
# 选择点击请选
mp_select = By.CSS_SELECTOR, "[placeholder='请选择']"
# 点击具体频道
mp_select_database = By.XPATH, "//*[text()='数据库']"
# 点击发表
mp_commit = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取发表结果
mp_commit_result = By.XPATH, "//*[contains(text(),'成功')]"


"""以下为后台管理页面的配置数据"""
# 输入用户名
mis_username = By.CSS_SELECTOR,'[placeholder="用户名"]'
# 输入密码
mis_password = By.CSS_SELECTOR,'[placeholder="密码"]'
# 点击登录按钮
mis_commit_btn = By.ID,"inp1"
# 获取登录用户名
mis_get_nickname = By.CSS_SELECTOR,'[class="user_info"]>span'



# 点击信息管理
mis_click_manage = By.XPATH,'//*[@class="menu"]//*[text()="信息管理"]'
# 点击信息审核
mis_click_article = By.XPATH,'//*[@class="current3"]//*[text()="内容审核"]'
# 标题
mis_title =By.CSS_SELECTOR,'[placeholder="请输入: 文章名称"]'
# 频道
mis_channel =By.CSS_SELECTOR,'[placeholder="请输入: 频道"]'
# 查询
mis_search = By.CSS_SELECTOR,'.find'
# 通过
mis_pass = By.XPATH,'//*[text()="通过"]/..'
# 确认通过
mis_sure_pass = By.CSS_SELECTOR,'.el-button--primary'
# 获取ID
mis_get_id = By.CSS_SELECTOR,'.cell>span'
"""以下为文章配置数据"""
article_title = read_yaml("mp_article.yml")[0][0]
article_channel = "数据库"


"""app端"""
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"
# 用户名
app_username = By.XPATH,"//*[@index='1' and @class='android.widget.EditText']"
# 密码
app_password = By.XPATH,"//*[@index='2' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn =By.CLASS_NAME,"android.widget.Button"
# 判断登录成功
app_my = By.XPATH,"//*[contains(@text,'我的') and @class='android.widget.ImageView']"
# 获取用户名
app_get_app_login_data = read_yaml("mp_login.yaml")[0]




ele = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
ele2 = By.XPATH,"//*[@bounds='[0,260][720,1144]']"