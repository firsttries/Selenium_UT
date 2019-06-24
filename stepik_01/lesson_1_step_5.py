from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element_by_css_selector('#num1').text
b = browser.find_element_by_css_selector('#num2').text
c = int(a) + int(b)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(c)) # ищем элемент с текстом "Python"
browser.find_element_by_css_selector('.btn').click()