from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000')
    )

browser.find_element_by_css_selector('#book').click()

x = int(browser.find_element_by_css_selector('#input_value').text)
y = str(calc(x))

browser.find_element_by_css_selector('#answer').send_keys(y)
browser.find_element_by_css_selector('#solve').click()
