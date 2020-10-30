#1.下载 chrome 驱动 放到 python 安装目录下
#http://chromedriver.storage.googleapis.com/index.html

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Python")
driver.find_element_by_id("kw").send_keys(Keys.RETURN)
driver.find_element_by_id("su").click()
driver.quit()
