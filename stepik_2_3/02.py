
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

browser.find_element_by_css_selector('.btn').click()

new_window = browser.window_handles[1]
old_window = browser.window_handles[0]
browser.switch_to.window(new_window)

x = int(browser.find_element_by_css_selector('#input_value').text)
y = str(calc(x))

browser.find_element_by_css_selector('#answer').send_keys(y)
browser.find_element_by_css_selector('.btn').click()
