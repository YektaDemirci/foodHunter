import unittest
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import page


def getDriver():
    path_parent = os.path.dirname(__file__)
    path_parent = os.path.join(path_parent, os.pardir)
    os.chdir(path_parent)

    PATH = "file://"+os.getcwd()+"/main.html"

    options = Options()
    options.headless = True

    driver = webdriver.Firefox( \
        options=options, \
        executable_path='tests/geckodriver', \
        service_log_path='/dev/null')
    driver.get(PATH)
    return driver


class FooterUI(unittest.TestCase):
    @classmethod
    def setUp(self):
        # Geckodriver in tests folder doesnt work for me (I think its computer architecture specific)
        '''
        Might be due to different executable_path for geckodriver. 
        Should be solved now because test/geckodriver is on gitlab.
        '''
        # self.driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver", service_log_path = '/dev/null')
        self.driver = getDriver()

    def test_footerStep1(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_footer_step1_highlighted(), "\nInitial styling of footer is incorrect"

    def test_footerStep2(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_footer_step2_highlighted(), "\nStyling for second step is incorrect"

    def test_footerStep3(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_footer_step3_highlighted(), "\nStyling for final step is incorrect"

    def test_boxStep1(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step1_highlighted(), "\nStyling for box 1st step is incorrect"

    def test_boxStep2(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step2_highlighted(), "\nStyling for box 2nd step is incorrect"
    
    def test_boxStep3(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step3_highlighted(), "\nStyling for box 3th step is incorrect"
    
    def test_boxStep2re(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step2_rehighlighted(), "\nStyling for box 2nd re-step is incorrect"
    
    def test_boxStep1re(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_box_step1_rehighlighted(), "\nStyling for box 1st re-step is incorrect"

    def test_gifsPresent(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_gifsPresent(), "\nGifs are not present when page is loaded"

    def test_gifsDisappear(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_gifsDisappear(), "\nGifs do not disappear when ingredients are input"

    def test_arrowAnimation(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_arrow_pulsing(), "\nArrow is not pulsing to indicate next steps"


    
    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)