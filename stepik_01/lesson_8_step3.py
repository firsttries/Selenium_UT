from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")
elements = browser.find_elements_by_css_selector('input')
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_xpath("//*[text()='Отправить']")
button.click()