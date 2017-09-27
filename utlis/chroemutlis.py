#coding:utf-8

#封装思想
#1：高内聚  低耦合
#2：测试用例与逻辑代码的分离
#3：以面向对象的思想写脚本
#4：mvc 模型搭建框架  m model层 也就是数据层
#   v view 视图展示层,对应的是咱们这里的单元测试层
#   c control 控制层, 对应的是逻辑控制层

# 高内聚的具体体现 : 把竟可能关联的代码放在一个类里面,封装成各种方法,


#导包

from selenium import webdriver
#休眠包
import time

#枚举包
from  enum import Enum

#导入三个结合使用的显示休眠
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#定义一个类 继承 object ：
class startChrome(object):

    #类实例化的时候执行一个方法
    def __init__(self):
        # 将枚举实例化
        # 在 Java中实例化需要使用的关键字叫 new , 在python 中不需要使用关键字,直接类型()
        pass
    def chrome(self,url):
        #打开浏览器
        self.driver = webdriver.Chrome()
        #最大化
        self.driver.maximize_window()
        #打开网页
        self.driver.get(url)
        #设置等待时间
        self.TimeSleep(ENUM.FIVE_TIME)
        pass
    #关闭浏览器的方法
    def closeChrome(self):
        self.driver.quit()
        pass
    # 休眠方法 三种 1: 静止休眠 2 : 隐士休眠  3: 显示休眠
    def TimeSleep(self,timesleep):
        time.sleep(timesleep)
        pass
    def ImplaySeleep(self,timesleep):
        self.driver.implicitly_wait(timesleep)
        pass

    # 显示休眠
    def WebWait(self, message):
        # 查找内容
        text = (By.LINK_TEXT, message)
        # 设置休眠时间
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(text))

        pass
    #定义八种控件查找方式1
    def FindId(self,ID):

        try:
            #查找内容
            ids = (By.ID,ID)
            #设置休眠时间
            WebDriverWait(self.driver,ENUM.TWENTY_TIME,ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
            return self.driver.find_element_by_id(ID)
        except  Exception:

         pass
    # 定义八种控件查找方式2
    def FindName(self, NAME):
        try:
            # 查找内容
            ids = (By.NAME, NAME)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
            return self.driver.find_element_by_name(NAME)
        except  Exception:

            pass
    # 定义八种控件查找方式3
    def FindClassname(self, CLASSNAME):
        try:
            # 查找内容
            ids = (By.CLASSNAME, CLASSNAME)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
            return self.driver.find_element_by_class_name(CLASSNAME)
        except  :
            return self.driver.find_element_by_class_name(CLASSNAME)
            pass
    # 定义八种控件查找方式4
    def FindLIKE_TEST(self, LIKE_TEST):
        try:
            # 查找内容
            ids = (By.LINK_TEXT, LIKE_TEST)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式5
    def FindPARTIAL_LINK_TEXT(self, PARTIAL_LINK_TEXT):
        try:
            # 查找内容
            ids = (By.PARTIAL_LINK_TEXT, PARTIAL_LINK_TEXT)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式6
    def FindXPATH(self, XPATH):
        try:
            # 查找内容
            ids = (By.XPATH, XPATH)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
     # 定义八种控件查找方式7
    def FindCSS_SELECTOR(self, CSS_SELECTOR):
        try:
            # 查找内容
            ids = (By.CSS_SELECTOR, CSS_SELECTOR)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
     # 定义八种控件查找方式8
    def FindTAG_NAME(self, TAG_NAME):
        try:
            # 查找内容
            ids = (By.TAG_NAME, TAG_NAME)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass

    # 以下是加S
    #   定义八种控件查找方式1
    def FindIds(self, ID):
        try:
            # 查找内容
            ids = (By.ID, ID)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式2
    def FindNames(self, NAME):
        try:
            # 查找内容
            ids = (By.NAME, NAME)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式3
    def FindClassnames(self, CLASSNAME):
        try:
            # 查找内容
            ids = (By.CLASSNAME, CLASSNAME)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式4
    def FindLIKE_TESTs(self, LIKE_TEST):
        try:
            # 查找内容
            ids = (By.LINK_TEXT, LIKE_TEST)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式5
    def FindPARTIAL_LINK_TEXTs(self, PARTIAL_LINK_TEXT):
        try:
            # 查找内容
            ids = (By.PARTIAL_LINK_TEXT, PARTIAL_LINK_TEXT)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式6
    def FindXPATHs(self, XPATH):
        try:
            # 查找内容
            ids = (By.XPATH, XPATH)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式7
    def FindCSS_SELECTORs(self, CSS_SELECTOR):
        try:
            # 查找内容
            ids = (By.CSS_SELECTOR, CSS_SELECTOR)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    # 定义八种控件查找方式8
    def FindTAG_NAMEs(self, TAG_NAME):
        try:
            # 查找内容
            ids = (By.TAG_NAME, TAG_NAME)
            # 设置休眠时间
            WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ZONE_TIME).until(EC.presence_of_element_located(ids))
        except  Exception:

            pass
    #点击class方法
    def click_class(self,cls):
        self.FindClassname(cls).click()
        self.TimeSleep(ENUM.TWO_TIME)
        pass

    # 点击class方法
    def click_id(self, cls):
        self.FindId(cls).click()
        self.TimeSleep(ENUM.TWO_TIME)
        pass
    #获取title的方法
    def getTilet(self):
        self.TimeSleep(ENUM.TWO_TIME)
        return self.driver.title
        pass





#定义一个枚举
class ENUM(Enum):
    # 一秒
    OND_TIME = 1
    # 二秒
    TWO_TIME = 3
    # 五秒
    FIVE_TIME = 5
    # 十秒
    TEN_TIME = 10
    # 二十秒
    TWENTY_TIME = 20
    # 0.5 秒
    ZONE_TIME = 0.5












