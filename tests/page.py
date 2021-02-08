from locator import MainPageLocators
from element import BasePageElement
import time

class SearchBarElement(BasePageElement):
    locator = "search-bar-id"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# define 1 class for 1 page or 3 classes for 3 panels

class MainPage(BasePage):

    search_bar_element = SearchBarElement()

    def is_search_bar_empty(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BAR)
        search_bar_text = element.get_attribute("text")
        return not(search_bar_text)


    def is_submit_empty(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.SUBMIT_MESSAGE).text
        err_message = True if element2 else False
        return err_message

    def is_output(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BAR)
        element.send_keys("chicken")
        element2 = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY).click()
        time.sleep(5)
        element3 = self.driver.find_element(*MainPageLocators.RESULTS).text
        if element3:
            if element3 != 'we could not find anything, sorry.':
                return True
            else:
                return False
        else:
            return False

    # test idea - input = "beef , cheese   " - i.e. VALUES THAT EXIST IN SAMPLE DATA, BUT WITH ABNORMAL SPACING
    # test idea - input = "asdfgh" - i.e. VALUE THAT IS CONFIRMED TO NOT EXIST IN SAMPLE DATA TO CHECK HOW IT'S HANDLED

