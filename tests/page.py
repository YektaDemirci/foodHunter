from locator import MainPageLocators
from element import BasePageElement

import time

class SearchFooterElement(BasePageElement):
    locator = "step1"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# define 1 class for 1 page or 3 classes for 3 panels?

class MainPage(BasePage):

    def is_footer_step1_highlighted(self):
        return ( self.isStylingCorrect(MainPageLocators.STEP_1_HIGHLIGHTED) )
    
    def is_footer_step2_highlighted(self):
        self.inputIngredientAndClickSubmit()
        return ( self.isStylingCorrect(MainPageLocators.STEP_2_HIGHLIGHTED) )

    def is_footer_step3_highlighted(self):
        self.inputIngredientAndClickSubmit()
        nextButtonElement = self.driver.find_element(*MainPageLocators.MID_NEXT_BUTTON)
        nextButtonElement.click()
        return ( self.isStylingCorrect(MainPageLocators.STEP_3_HIGHLIGHTED) )
    
    #The test to check if the boxes have right styles in step 1
    def is_box_step1_highlighted(self):
        return ( self.isStylingCorrect(MainPageLocators.STEP_1_BOX) )
    
    #Test to check if the boxes have right styles: step1->step2
    def is_box_step2_highlighted(self):
        self.inputIngredientAndClickSubmit()
        return ( self.isStylingCorrect(MainPageLocators.STEP_2_BOX) )

    #Test to check if the boxes have right styles: step1->step2->step3
    def is_box_step3_highlighted(self):
        self.inputIngredientAndClickSubmit()
        self.driver.find_element(*MainPageLocators.MID_NEXT_BUTTON).click()
        return ( self.isStylingCorrect(MainPageLocators.STEP_3_BOX) )

    #Test to check if the boxes have right styles: step1->step2->step3->step2
    def is_box_step2_rehighlighted(self):
        self.inputIngredientAndClickSubmit()
        self.driver.find_element(*MainPageLocators.MID_NEXT_BUTTON).click()
        self.driver.find_element(*MainPageLocators.RIGHT_BACK_BUTTON).click()
        return ( self.isStylingCorrect(MainPageLocators.STEP_2_BOX) )

    #Test to check if the boxes have right styles: step1->step2->step3->step2->step1
    def is_box_step1_rehighlighted(self):
        self.inputIngredientAndClickSubmit()
        self.driver.find_element(*MainPageLocators.MID_NEXT_BUTTON).click()
        self.driver.find_element(*MainPageLocators.RIGHT_BACK_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*MainPageLocators.MID_BACK_BUTTON).click()
        return ( self.isStylingCorrect(MainPageLocators.STEP_1_BOX) )

    # This was in selenium official tutorial, dont understand purpose of following function:
    # search_footer_element = SearchFooterElement()

#########################
####### HELPER FUNCTIONS
#########################
    def isStepHighlighted(self,step,style):
        element = self.driver.find_element(*step)
        className = element.get_attribute("class")
        return style in className

    def isStylingCorrect(self, array):
        correctStyle = []
        for testCase in array:
            correctStyle.append( self.isStepHighlighted(testCase[0], testCase[1]) )
        return True if False not in correctStyle else False

    def inputIngredientAndClickSubmit(self):
        searchElement = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        searchElement.send_keys(MainPageLocators.SAMPLE_INGREDIENT)

        submitElement = self.driver.find_element(*MainPageLocators.SUBMIT_BUTTON)
        submitElement.click()

    


    
