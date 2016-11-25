# coding: utf-8
import time

# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = 'E:\\test_object\\report\\'+now+'result.html'
# fp = file(filename, 'wb')

def screenshot(self,dir):
    driver=self.driver
    now_time = time.strftime("%Y%m%d%H%M%S") + '.png'
    path = file.join(dir, now_time)
    print  "save screen to path #{path}"
    driver.save_screenshot(path)
