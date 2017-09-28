#coding:utf-8
import  unittest
from utlis import  chroemutlis,urlutlis
from mains.control import mainscontrol
class Mainsseaou(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #进行实例化
        self.driver = chroemutlis.startChrome()
        self.URL = urlutlis.URL()
        self.control = mainscontrol.mainsControl(self.driver)
        pass
    def setUp(self):
        #打开浏览器
        self.driver.chromeStart(self.URL.JD_MAIN)

        pass

    def tearDown(self):
        #关闭浏览器
        self.driver.closeChrome()
        pass
    # #输入 物件， 点击一下
    # def test_sou_kuang(self):
    #     self.control.Search(u"袜子")
    #     #断言
    #     #self.control.SesrchAssert(self,u"袜子 - 商品搜索 - 京东")
    #     self.control.CountAssert(self,30)
    #
    #     pass
    #悬浮进行断言
    def test_sou_kuang(self):
        #悬浮上去
        self.driver.ActionMove()
        #断言
        self.control.MainAsser("item",3,self)
        pass

