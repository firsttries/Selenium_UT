
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)


browser.find_element_by_css_selector('.btn').click()

browser.switch_to.alert.accept()

x = int(browser.find_element_by_css_selector('#input_value').text)
y = str(calc(x))

browser.find_element_by_css_selector('#answer').send_keys(y)
browser.find_element_by_css_selector('.btn').click()