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

    def test_deleteworkspace(self):
        u'''删除工作空间'''
        driver = self.driver
        menu.access_primaryworkspase(self)
        driver.implicitly_wait(30)
        workspace.delete_workspace(self,"Test CreateWorkspace1")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()