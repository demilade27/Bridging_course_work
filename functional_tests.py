from selenium import webdriver
import unittest

class NewResumeTest(unittest.TestCase):
    def setup(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    

    

if __name__=='__main__':
    unittest.main(warnings='ignore')

