# coding:utf-8

class loginCon(object):
    def __init__(self,driver):
        self.driver = driver
        pass
    #点击账号登录
    def  ClickAccout(self,cls):

        self.driver.click_class(cls)

        pass
    #输入用户名密码
    def Sendkeys(self,username,password,cls):
        #self.driver.FindClassname('login-tab-r').click()
        self.ClickAccout(cls)

        self.driver.FindId('loginname').send_keys(username)
        self.driver.FindId('nloginpwd').send_keys(password)
        self.driver.click_id('loginsubmit')
       # self.driver.FindId('loginsubmit').click()
        pass
    # 断言
    def LoginAssert(self, self1, expects, cls):
        # 查找控件进行断言
        message = self.driver.FindClassname(cls).text
        self1.assertEqual(message, expects)

        pass
    # 断言tilte
    def LoginTitle(self, self1, expects):
        # 查找控件进行断言
        message = self.driver.getTilet()
        self1.assertEqual(message, expects)
        pass
    # 断言元素是不是存在
    def Loginsexist(self,self1,cls):
        self1.assertTrue(self.driver.FindClassname(cls).is_displayed())

        pass

