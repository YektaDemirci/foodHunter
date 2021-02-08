from locator import MainPageLocators
from element import BasePageElement

class SearchFooterElement(BasePageElement):
    locator = "step1"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# define 1 class for 1 page or 3 classes for 3 panels?

class MainPage(BasePage):

    search_footer_element = SearchFooterElement()

    def is_footer_step1_highlighted(self):
        elementActive = self.driver.find_element(*MainPageLocators.FOOTER_STEP1)
        classNameActive = elementActive.get_attribute("class")

        elementPassive1 = self.driver.find_element(*MainPageLocators.FOOTER_STEP2)
        classNamePassive1 = elementPassive1.get_attribute("class")

        elementPassive2 = self.driver.find_element(*MainPageLocators.FOOTER_STEP3)
        classNamePassive2 = elementPassive2.get_attribute("class")

        return (("current-step" in classNameActive) and ("undone-step" in classNamePassive1 and "undone-step" in classNamePassive2))
