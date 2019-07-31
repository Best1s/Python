#coding:utf-8
#https://seleniumhq.github.io/selenium/docs/api/py/index.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
'''
find_element_by_id()
find_element_by_name()
find_element_by_class_name()
find_element_by_tag_name()
find_element_by_link_text()
find_element_by_partial_link_text
find_element_by_xpath()
find_element_by_css_selector()
备注：元素定位必须确保该定位方式定位出的元素具有唯一性，若定位出多组元素，需对元素进行筛选，或者调整定位方式。
还有两个通用方法 find_element和find_elements
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH,'//button[text()]="Some text"]')

1:页面交互与填充表单
2:元素拖拽
3:窗口和页面frame的切换
4:弹窗处理
5:历史记录
6:Cookie处理
7:设置phantomJS请求头中User-Agent
8:等待，不确定网页元素什么时候被完全加载，选取元素困难;Selenium 有两种等待方式
显示等待和隐式等待。
'''

#binary = FirefoxBinary(r'/usr/bin/firefox')
#driver = webdriver.Firefox(firefox_binary=binary)

driver = webdriver.Firefox()

driver.get("www.baidu.com")
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u'网络爬虫')
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u'网络爬虫.' not in driver.page_source
driver.close()
