from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from details import details
from random import choice, sample

class AppDynamicsJob(unittest.TestCase):
    options = Options()
    options.add_argument('--start-maximized')
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome(options=self.options)
        # self.driver.implicitly_wait(30)
        
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://healingstreams.tv/3days/online_reg.php?r=2TCG3")
        counter = 0
        for detail in details:
            fullName = detail['fullName']
            first_name = fullName.split(' ')[0].title()
            last_name = fullName.split(' ')[1].title() if len(fullName.split(' ')) > 1 else fullName.split(' ')[0]
            services =  ['yahoo.com', 'outlook.com']
            email = first_name + last_name + ''.join(sample(first_name, 1)) + '@' + choice(services)
            email = email.lower()
            driver.find_element_by_id("button").click()
            driver.find_element_by_xpath("//div[10]/form/inpur/div/div/input").click()
            driver.find_element_by_xpath("//div[10]/form/inpur/div/div/input").clear()
            driver.find_element_by_xpath("//div[10]/form/inpur/div/div/input").send_keys(first_name)
            driver.find_element_by_xpath("//div[10]/form/inpur/div/div[2]/input").clear()
            driver.find_element_by_xpath("//div[10]/form/inpur/div/div[2]/input").send_keys(last_name)
            driver.find_element_by_id("email").click()
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("email").send_keys(email)
            driver.find_element_by_id("country1").click()
            Select(driver.find_element_by_id("country1")).select_by_visible_text("Nigeria")
            driver.find_element_by_id("state1").click()
            Select(driver.find_element_by_id("state1")).select_by_visible_text("Edo")
            driver.find_element_by_xpath("//div[10]/form/inpur/div[6]/div/input").click()
            driver.find_element_by_xpath("//div[10]/form/inpur/div[6]/div/input").clear()
            driver.find_element_by_xpath("//div[10]/form/inpur/div[6]/div/input").send_keys("Benin")
            driver.find_element_by_xpath("//div[10]/form/inpur/div[7]/input[2]").click()
            driver.find_element_by_xpath("//div[10]/form/inpur/input").click()

            driver.get('https://healingstreams.tv/3days/online_reg.php?r=2TCG3')
            counter += 1
            print(counter)

            

    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e: return False
    #     return True
    
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True
    
    # def tearDown(self):
    #     # To know more about the difference between verify and assert,
    #     # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
