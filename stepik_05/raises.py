import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException



def test_exception():
    browser = webdriver.Chrome()

    browser.get("https://mysite.com")
    with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить"):
        browser.find_element_by_css_selector("button.btn")