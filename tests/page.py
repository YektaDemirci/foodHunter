from locator import MainPageLocators
from element import BasePageElement
import time
import json

class SearchBarElement(BasePageElement):
    locator = "search-bar-id"

class SearchFooterElement(BasePageElement):
    locator = "step1"

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

    def is_output_options(self):
        #'bbq sauce/chicken/bacon', 'bbq sauce chicken bacon'
        ingredients = ['chicken', 'rice', 'bacon', 'cheese,chicken', 'rice, chicken','tomato sauce,bacon,ham' ]
        check = False
        for ingredient in ingredients:
            element = self.driver.find_element(*MainPageLocators.SEARCH_BAR)
            elem = self.driver.find_element(*MainPageLocators.SEARCH_BAR).clear()
            element.send_keys(ingredient)
            element2 = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY).click()
            time.sleep(5)
            element3 = self.driver.find_element(*MainPageLocators.RESULTS).text
            if element3:
                if element3 != 'we could not find anything, sorry.':
                    check = True
                else:
                    check = False
            else:
                check = False
            time.sleep(5)
        return check

    def is_output_valid(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BAR)
        element.send_keys("tomato sauce,bacon,ham")
        required = ["tomato sauce","bacon","ham"]
        element2 = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY).click()
        time.sleep(5)
        element3 = self.driver.find_element(*MainPageLocators.RESULTS).text
        counter = 0
        with open("../data_food_sample.json", "r") as file:
            data = json.load(file)
            for entry in data:
                ingredients = entry['ingredients'].split(",")
                ingredients = [x.lower() for x in ingredients]
                for req in required:
                    if req.lower() in ingredients:
                        counter += 1
                if counter == len(required):
                    result_str = entry["product"] + " at " + entry["restaurant"]
                    if element3:
                        if element3 == result_str:
                            return True
                counter = 0

        if element3 == 'we could not find anything, sorry.':
            return True
        else:
            return False
    
    def is_output_spacing(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BAR)
        element.send_keys("  beef , cheese   ")
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

    def is_output_err(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BAR)
        element.send_keys("asdfgh")
        element2 = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY).click()
        time.sleep(5)
        element3 = self.driver.find_element(*MainPageLocators.RESULTS).text
        if element3:
            if element3 == 'we could not find anything, sorry.':
                return True
            else:
                return False
        else:
            return False

# define 1 class for 1 page or 3 classes for 3 panels?

#class MainPage(BasePage):

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

    


    
