#coding=utf-8

from selenium import webdriver
import unittest,time
from public import login
# from public import common
import xml.dom.minidom
import time
# import os
#打开xml 文档
dom = xml.dom.minidom.parse('C:\\Users\\Administrator\\PycharmProjects\\test_project\\test_data\\login.xml')
#得到文档元素对象
root = dom.documentElement


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('url')
        self.base_url = logins[0].firstChild.data
        self.verificationErrors = []

    # 用户名、密码为空
    def test_null(self):
        u'''用户名、密码为空'''
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('null')
         # 获得null 标签的username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        time.sleep(10)
        # 获取断言信息进行断言
        text = driver.find_element_by_css_selector("p[style='display: block;']").text
        self.assertEqual(text, prompt_info)

    # 输入用户名、密码为空
    def test_pawd_null(self):
        u'''输入用户名、密码为空'''
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('pawd_null')
        # 获得null 标签的username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        time.sleep(10)
        # 获取断言信息进行断言
        text=driver.find_element_by_css_selector("p[style='display: block;']").text
        self.assertEqual(text, prompt_info)

    #用户名为空，只输入密码
    def test_user_null(self):
        u'''用户名为空，只输入密码'''
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('user_null')
        # 获得null 标签的username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        time.sleep(10)
        # 获取断言信息进行断言
        driver.get_screenshot_as_file("D:\\baidu_error.jpg")
        text = driver.find_element_by_css_selector("p[style='display: block;']").text
        self.assertEqual(text, prompt_info)

    # 用户名不存在
    def test_error_user(self):
        u'''用户名不存在'''
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('error_user')
        # 获得null 标签的username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        time.sleep(10)
        # 获取断言信息进行断言
        text = driver.find_element_by_css_selector("p[style='display: block;']").text
        self.assertEqual(text, prompt_info)

    # 密码错误
    def test_error_pawd(self):
        u'''密码错误'''
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('error_pawd')
        # 获得null 标签的username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        time.sleep(10)
        # 获取断言信息进行断言
        text = driver.find_element_by_css_selector("p[style='display: block;']").text
        self.assertEqual(text, prompt_info)

    # 密码长度不够
    def test_error(self):
        u'''密码长度不够'''
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('error')
        # 获得null 标签的username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        # 登录
        login.login(self, username, password)
        time.sleep(10)
        # 获取断言信息进行断言
        text = driver.find_element_by_css_selector("p[style='display: block;']").text
        self.assertEqual(text, prompt_info)

    #用户名、密码正确
    def test_login(self):
        u'''用户名、密码正确'''
        driver = self.driver
        driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        logins = root.getElementsByTagName('user_pawd')
        # 获得null 标签的username、passwrod 属性值
        username = logins[0].getAttribute("username")
        password = logins[0].getAttribute("password")
        prompt_info = logins[0].firstChild.data
        #调用登录函数
        print "登录iCloudUinon"
        login.login(self, username,password)
        time.sleep(2)
        title = driver.title
        print title
        self.assertEqual(title, u"iCloudUnion")
        # 调用退出函数
        print "登出iCloudUinon"
        login.logout(self)

    def tearDown(self):
        # now_time = time.strftime("%Y%m%d%H%M%S")
        # filename = 'C:\\Users\\Administrator\\PycharmProjects\\test_project\\report\\' + now_time + '.png'
        # self.driver.get_screenshot_as_file(filename)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()