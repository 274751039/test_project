#coding=utf-8
from selenium.webdriver.common.keys import Keys
#访问主页
def access_primaryhome(self):
    driver = self.driver
    driver.find_element_by_id("primary-home").click()

#访问工作空间
def access_primaryworkspase(self):
    driver = self.driver
    driver.find_element_by_id("primary-workspaces").click()

#访问数据源
def access_primarydata(self):
    driver=self.driver
    driver.find_element_by_id("primary-data").click()

#访问协作伙伴
def access_primaryuser(self):
    driver=self.driver
    driver.find_element_by_id("primary-users").click()

#访问标签
def access_primarytags(self):
    driver=self.driver
    driver.find_element_by_id("primary-tags").click()

#访问模型示例
def access_primarydemos(self):
    driver=self.driver
    driver.find_element_by_id("primary-demos").click()

#访问导航
def access_primarytour(self):
    driver=self.driver
    driver.find_element_by_id("primary-tour").click()

## 以上7个方法可以用下面的方法代替
def access_primary(self,primaryname):
    driver=self.driver
    driver.find_element_by_id(primaryname).click()

#点击搜索栏
def search(self,searchtext):
    driver=self.driver
    driver.find_element_by_name('search_text').clear()
    driver.find_element_by_name('search_text').send_keys(searchtext)
    driver.find_element_by_name('search_text').sendkeys(Keys.ENTER)

#点击通知栏
def click_notifications(self):
    driver=self.driver
    driver.find_element_by_css_selector('.lozenge ').click()
#点击用户信息
def click_username(self):
    driver=self.driver
    driver.find_element_by_css_selector("span[style='color:white']").click()
#点击中文
def click_chinese(self):
    driver=self.driver
    driver.find_element_by_link_text(u"中文").click()
#点击英文
def click_english(self):
    driver=self.driver
    driver.find_element_by_link_text("English").click()

