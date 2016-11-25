#coding=utf-8
#创建工作空间
def create_workspace(self,workspacename):
    driver = self.driver
    driver.find_element_by_css_selector(".create_workspace").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("workspaceNameField").clear()
    driver.find_element_by_id("workspaceNameField").send_keys(workspacename)
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector("[type = submit]").click()

#删除工作空间
def delete_workspace(self, workspacename):
    driver = self.driver
    for element in driver.find_elements_by_css_selector(".item_wrapper"):
        if element.find_element_by_css_selector(".name").text == workspacename:
            element.find_element_by_css_selector("input[type='checkbox']").click()
            driver.implicitly_wait(30)
    driver.find_element_by_css_selector(".delete_workspace").click()
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector("[type='submit']").click()