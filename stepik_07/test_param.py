import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, link):
        browser.implicitly_wait(10)
        link = "https://stepik.org/lesson/{}/step/1".format(link)
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.find_element_by_css_selector('#ember1550').send_keys(str(answer))
        browser.find_element_by_css_selector('.submit-submission').click()
        time.sleep(1)
        assert 'Correct!' == browser.find_element_by_css_selector('.smart-hints__hint').text, 'upal'
