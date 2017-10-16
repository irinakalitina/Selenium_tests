# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class authorization_future(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_authorization_future(self):
        success = True
        wd = self.wd
        wd.get("https://futurenpf.ru/personal")
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").click()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").clear()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").send_keys("149-___-___ __")
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").click()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").clear()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").send_keys("149-027-332 58")
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").click()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").click()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").clear()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").send_keys("as")
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").click()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").clear()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").send_keys("aojgumfa")
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[4]/input").click()
        wd.find_element_by_xpath("//main[@class='main']/section[2]/div/div[2]/div/div/div[2]/a").click()
        wd.find_element_by_link_text("Калитина Ирина").click()
        wd.find_element_by_css_selector("a.top-bar__arrow.js-lcopen").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
