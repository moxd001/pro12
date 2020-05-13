from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_actionchains(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        sleep(2)
        #xpath定位
        # element_click = self.driver.find_element('xpath','//*[@value="click me"]')
        # element_doubleclick = self.driver.find_element('xpath','//*[@value="dbl click me"]')
        # element_rightclick = self.driver.find_element('xpath','//*[@value="right click me"]')
        # css selector
        element_click = self.driver.find_element('css selector','[value="click me"]')
        element_doubleclick = self.driver.find_element('css selector','[value="dbl click me"]')
        element_rightclick = self.driver.find_element('css selector','[value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        action.perform()
        sleep(2)
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        sleep(2)
        ele = self.driver.find_element('css selector','#s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
    @pytest.mark.dragdrop
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        self.driver.maximize_window()
        drap_ele = self.driver.find_element('id','dragger')
        drop_ele = self.driver.find_element('xpath','/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drap_ele,drop_ele).perform()
        action.click_and_hold(drap_ele).release(drop_ele).perform()
        sleep(2)
    @pytest.mark.keys
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element('xpath','/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("hello").pause(1)
        action.send_keys(Keys.BACKSPACE).perform()
        sleep(3)



if __name__ == '__main__':
    pytest.main()