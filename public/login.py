#coding=utf-8
from public import menu
#登录
def login(self,username,password):
    driver = self.driver
    driver.find_element_by_id('start').click()
    driver.implicitly_wait(10)
    driver.find_element_by_id('email').clear()
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('submit').click()
#退出
def logout(self):
    driver = self.driver
    driver.implicitly_wait(10)
    menu.click_username(self)
    driver.implicitly_wait(3)
    driver.find_element_by_link_text(u"登出").click()