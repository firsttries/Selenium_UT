from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mail.yandex.ru/')


    def test_01(self):
        driver = self.driver
        button_in = driver.find_element_by_xpath('//*[@id="index-page-container"]/div/div[2]/div/div/div[4]/a[2]')
        button_in.click()
        time.sleep(1)
        if driver.find_element_by_name('passwd').size != 0:
            login_field = driver.find_element_by_name('login')
            login_field.send_keys('<YOUR_LOGIN>')
            pass_field = driver.find_element_by_name('passwd')
            pass_field.send_keys('<YOUR_PASS>')
            pass_field.send_keys(Keys.ENTER)
            time.sleep(1)
        time.sleep(3)
        write_post = driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[2]/div[2]/div/div[1]/div/div/a/span')
        write_post.click()
        time.sleep(1)
        field_send = driver.find_element_by_name('to')
        field_send.send_keys('<NAME_SEND>')
        field_subject = driver.find_element_by_xpath('//*[@id="nb-1"]/body/div[2]/div[5]/div/div[3]/div[3]/div[2]/div[5]/div/div[1]/div[2]/div[1]/div/label/div[3]/input')
        field_subject.send_keys('<MESSAGE>')
        time.sleep(2)
        button_final = driver.find_element_by_xpath('//*[@id="nb-13"]/span/span/span')
        button_final.click()
        time.sleep(5)
    def tearDown(self):
        self.driver.close()
