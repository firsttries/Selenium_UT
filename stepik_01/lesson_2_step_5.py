from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = int(browser.find_element_by_css_selector('#input_value').text)
y = calc(x)

answer = browser.find_element_by_css_selector("#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

browser.find_element_by_css_selector('#answer').send_keys(str(y))

browser.find_element_by_css_selector('#robotCheckbox').click()
browser.find_element_by_css_selector('#robotsRule').click()
browser.find_element_by_css_selector('.btn').click()
