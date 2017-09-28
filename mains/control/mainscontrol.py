#coding:utf-8
from utlis import chroemutlis

class mainsControl(object):

    def __init__(self,driver):
        #self.driver = chroemutlis.startChrome()
        self.driver =driver
        pass
    #输入框点击一下
    def Search(self,messg):
        self.driver.FindId("key").send_keys(messg)
        self.driver.click_class("button")
        pass
    #断言标题
    def SesrchAssert(self,self1,massg):
        tilet = self.driver.getTilet()
        self1.assertEqual(tilet, massg)
        pass
    # 断言标题
    def CountAssert(self, self1, count):
        gl_item = self.driver.FindClassnames("gl-item")

        self1.assertEqual(len(gl_item), count)
        pass
    #断言悬浮
    def MainAsser(self,cls,itmes,self1):
        #获取列表跑内容
        address = self.driver.FindXPATHs("//div[@class = 'item']/a")
        #指定的内容
        messag = address[itmes].text
        #加入休眠
        self.driver.TimeSleep(4)
        # 通过class 查询
        gl_itmes =  self.driver.FindClassnames(cls)
        #点击
        gl_itmes[itmes].click()
        # 获断取当前显示的位置进行断言
        ui_areamini_text = self.driver.FindClassname("ui-areamini-text")
        #获取内容
        msg = ui_areamini_text.text
        self1.assertEqual(msg,messag)




        pass


