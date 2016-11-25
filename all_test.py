#coding=utf-8
import unittest
import os,time,sys
import HTMLTestRunner
reload(sys)
sys.setdefaultencoding("utf-8")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from test_case import test01_login

mailto_list = ["hourufen@unionbigdata.com"]
mail_host = "mail.unionbigdata.com"  # 设置服务器
mail_user = "icloudunion"  # 用户名
mail_pass = "icu@@235"  # 口令
mail_postfix = "unionbigdata.com"  # 发件箱的后缀

#=============定义发送邮件==========
def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    me = "icloudunion" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    f = open(content, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
    print 'email has send out !'

#======查找测试报告目录，找到最新生成的测试报告文件====
def send_report(testreport):
    result_dir = testreport
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    #print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    send_mail(mailto_list,u'自动化测试报告',file_new)

def creatsuite():
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    test_dir='C:\\Users\\Administrator\\PycharmProjects\\test_project\\test_case'
    #定义discover 方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,pattern ='test*.py',top_level_dir=None)
    # suite = unittest.TestSuite()
    # suite.addTest(test01_login.MyTest("test_login"))
    # return suite
   #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print testunit
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = 'C:\\Users\\Administrator\\PycharmProjects\\test_project\\report\\'+now+'result.html'
testreport = '\\Users\\Administrator\\PycharmProjects\\test_project\\report\\'
filename = testreport+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'iCloudUnion测试报告',
    description=u'用例执行情况：')

if __name__ == '__main__':
    # runner =unittest.TextTestRunner()
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
    send_report(testreport)
