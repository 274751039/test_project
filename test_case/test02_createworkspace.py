#coding=utf-8

from selenium import webdriver
import unittest,time
from public import login
from public import menu
from public import workspace

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://192.168.1.55:8080"
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        login.login(self,"zhongshunci@unionbigdata.com","123456")
        time.sleep(2)

    def test_createworkspace(self):
        u'''创建工作空间'''
        driver = self.driver
        #调用访问工作空间函数
        menu.access_primaryworkspase(self)
        driver.implicitly_wait(30)
        #调用创建工作空间函数
        workspace.create_workspace(self,"Test CreateWorkspace1")
        driver.implicitly_wait(30)
        text = driver.find_element_by_id("sub_header_pagetitle").text
        self.assertEqual(text,u"Test CreateWorkspace1")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()