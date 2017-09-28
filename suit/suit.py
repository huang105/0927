#coding:utf-8

import  unittest
import HTMLTestRunner
from unit import  chromemain,mainsunit
import  os
import  sys
reload(sys)
sys.setdefaultencoding("utf8")
#测试套件
suit = unittest.TestSuite()

# #添加单元测试1
# suit.addTest(unittest.makeSuite(chromemain.ChromeMain))
# #路径
# filrname = os.getcwd()+"/jd_login.html"

#添加单元测试2
suit.addTest(unittest.makeSuite(mainsunit.Mainsseaou))
#路径
filrname = os.getcwd()+"/jd_main.html"

files = open(filrname,"wb")
#生成报告
runner = HTMLTestRunner.HTMLTestRunner(stream=files,title=u"京东登录",description=u"京东登录测试用例")
runner.run(suit)




