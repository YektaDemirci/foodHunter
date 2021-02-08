from locator import MainPageLocators
from element import BasePageElement

class SearchFooterElement(BasePageElement):
    locator = "step1"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# define 1 class for 1 page or 3 classes for 3 panels?

class MainPage(BasePage):

    # This was in selenium official tutorial, dont understand 
    # search_footer_element = SearchFooterElement()

    # Should the following 2 helper functions go in another file? 
    def isStepHighlighted(self,step,style):
        element = self.driver.find_element(*step)
        className = element.get_attribute("class")
        return style in className

    def isFooterStylingCorrect(self, array):
        correctStyle = []
        for testCase in array:
            correctStyle.append( self.isStepHighlighted(testCase[0], testCase[1]) )
        return True if False not in correctStyle else False

    def is_footer_step1_highlighted(self):
        return( self.isFooterStylingCorrect(MainPageLocators.STEP_1_HIGHLIGHTED) )

    def is_footer_step2_highlighted(self):
        pass

    def is_footer_step3_highlighted(self):
        pass


    
