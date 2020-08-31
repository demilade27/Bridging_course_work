from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class NewResumeTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_log_in_to_admin(self):
        # demilade wants to start up his cv so he goes to a website he bought 
        self.browser.get("http://127.0.0.1:8000")
        # he notices the websites title is Demi's blog
        self.assertIn("Demi's blog",self.browser.title)
        # he goes to the resume page to add his resume 
        self.browser.get("http://127.0.0.1:8000/cv/resume")
        # he sees no post and a message telling him to create a user /admin to login 
        # he goes to the admin page 
        self.browser.get("http://127.0.0.1:8000/admin")
        # he attempts to sign in 

        # he writes his  user name 
        inputbox= self.browser.find_element_by_id("id_username")
        inputbox.send_keys("demi")
        inputbox.send_keys(Keys.ENTER) 
        time.sleep(1) 

        # he writes his  password
        inputbox= self.browser.find_element_by_id("id_password")
        inputbox.send_keys("Password")
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1) 
        # 
        






    

    

if __name__=='__main__':
    unittest.main(warnings='ignore')

