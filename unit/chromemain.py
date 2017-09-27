#coding:utf-8
import unittest
from utlis import urlutlis,chroemutlis
from loginse.control import chromecontrol

class ChromeMain(unittest.TestCase):

    #所有测试用例之前的方法
    @classmethod
    def setUpClass(self):
        self.utls = chroemutlis.startChrome()
        self.url = urlutlis.URL
        self.control = chromecontrol.loginCon(self.utls)
        pass
    #每一条测试用例执行之前执行的方法
    def setUp(self):
        #打开浏览器
        self.utls.chrome(self.url.JD_LOGIN)
        pass

    # 关闭浏览器
    def tearDown(self):
        self.utls.closeChrome()


        pass
    #  # 测试用例
    # def test_us_pw(self):
    #     """登录用例 --用户名，密码为空"""
    #     self.control.Sendkeys("","",'login-tab-r')
    #     #断言
    #     self.control.LoginAssert(self,u"请输入账户名和密码","msg-error")
    #     pass
    #
    # # 测试用例
    # def test_us_ps(self):
    #     """登录用例 --用户名，密码正确"""
    #     self.control.Sendkeys("15139945447", "15139945447hh.", 'login-tab-r')
    #     # 断言
    #     self.control.LoginTitle(self, u"京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！")
    #     pass
    #断言切换是不是正常
    def test_us_clicl(self):
        """测试断言的切换1"""
        # 点击用户登陆
        self.control.ClickAccout("login-tab-r")
        # 断言元素是不是存在
        self.control.Loginsexist(self, "login-box")
        pass
        # 扫码登陆

    def test_code_click(self):
        """测试断言的切换2"""
        # 点击用户登陆
        self.control.ClickAccout("login-tab-l")

        # 断言元素是不是存在login-box
        self.control.Loginsexist(self, "qrcode-login")

        pass
    # 所有测试用例执行完的时候执行的方法
    @classmethod
    def tearDownClass(self):
        # 销毁对象
        self.firfox = None

        pass




