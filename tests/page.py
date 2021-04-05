import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locator import MainPageLocators, FrontendLocators
from element import BasePageElement

class SearchBarElement(BasePageElement):
    def __init__(self):
        self.locator = MainPageLocators.SEARCH_BAR

class LocationSearchBarElement(BasePageElement):
    def __init__(self):
        self.locator = MainPageLocators.LOCATION_INPUT

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# define 1 class for 1 page or 3 classes for 3 panels

class MainPage(BasePage):
    '''
    Only used for search bars (defined in element.py):
    search_bar_element = "USER_INPUT" <==> search_bar_element.send_keys("USER_INPUT")
    user_input = search_bar_element <==> user_input = search_bar_element.get_attribute("value")
    '''
    search_bar_element = SearchBarElement()
    location_search_bar_element = LocationSearchBarElement()

    # ingredient
    def is_search_bar_empty(self):
        search_text = self.search_bar_element
        return not(search_text)

    def is_submit_empty(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(1)
        element2 = self.driver.find_element(*MainPageLocators.SUBMIT_MESSAGE)
        return (element2.text == 'No input found')

    def is_output(self):
        self.search_bar_element = 'chicken'
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        if element2.text:
            if element2.text != 'Sorry, we could not find anything.':
                return True
            else:
                return False
        else:
            return False

    def is_output_options(self):
        #'bbq sauce/chicken/bacon', 'bbq sauce chicken bacon'
        ingredients = ['chicken', 'rice', 'bacon', 'cheese,chicken', 'rice, chicken','tomato sauce,bacon,ham' ]
        check = True
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        for ingredient in ingredients:
            self.search_bar_element = ingredient
            element.click()
            time.sleep(5)
            if element2.text:
                if element2.text != 'Sorry, we could not find anything.':
                    check &= True
                else:
                    check &= False
            else:
                check &= False
            time.sleep(1)
        return check

    def is_output_valid(self):
<<<<<<< HEAD
        self.search_bar_element = 'tomato sauce,bacon,ham'
        required = ["tomato sauce","bacon","ham"]
=======
        self.search_bar_element = 'tomato sauce,bacon,ham,cheese,brocolli'
        required = ["tomato sauce", "bacon", "ham"]
>>>>>>> origin/link-to-delivery
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        counter = 0
        with open("data_food_sample.json", "r") as file:
            data = json.load(file)
            for entry in data:
                ingredients = entry['ingredients'].split(",")
                ingredients = [x.lower() for x in ingredients]
                for req in required:
                    if req.lower() in ingredients:
                        counter += 1
                if counter == len(required):
                    result_str = entry["product"] + " at " + entry["restaurant"]
                    if element2.text:
                        if element2.text == result_str:
                            return True
                counter = 0
<<<<<<< HEAD
        if element2.text == 'Sorry, we could not find anything.':
=======
        element3 = self.driver.find_elements_by_css_selector('div.result-div')
        if len(element3) > 0:
            return True
        elif len(element3) == 0 and element2.text == "Sorry, we could not find anything.":
>>>>>>> origin/link-to-delivery
            return True
        else:
            return False
    
    def is_output_spacing(self):
        self.search_bar_element = '  beef , cheese   '
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        if element2.text:
            if element2.text != 'Sorry, we could not find anything.':
                return True
            else:
                return False
        else:
            return False

    def is_output_err(self):
        self.search_bar_element = 'asdfgh'
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
<<<<<<< HEAD
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        if element2.text:
            if element2.text == 'Sorry, we could not find anything.':
=======
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        if element2.text:
            if element2.text == 'Sorry, we could not find anything.':
                return True
            else:
                return False
        else:
            return False

    # Step3: delete elements
    def is_div_present(self):
        self.search_bar_element = 'chicken'
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        element3 = self.driver.find_elements_by_css_selector('div.result-div')
        if len(element3) > 0:
            buttons = self.driver.find_elements_by_css_selector('button.selection-button')
            for button in buttons:
                button.click()

            element4 = self.driver.find_elements_by_css_selector('div.selection-div-class')
            count = len(element4)

            if count == len(element3):
>>>>>>> origin/link-to-delivery
                return True
            else:
                return False
        elif len(element3) == 0 and element2.text == 'Sorry, we could not find anything.':
            return True

        else:
            return False

    def is_div_deleted(self):
        self.search_bar_element = 'chicken'
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        element3 = self.driver.find_elements_by_css_selector('div.result-div')
        element4 = self.driver.find_elements_by_css_selector('div.selection-div-class')
        if len(element4) > 0:
            total_divs = len(element4)
            delete_button = self.driver.find_elements_by_css_selector('button.clear-button')
            delete_button[0].click()

            divs_after_1_deletion = len(self.driver.find_elements_by_css_selector('div.selection-div-class'))

            if divs_after_1_deletion + 1 == total_divs:
                return True
            else:
                return False

        else:
            return True

    def is_all_div_deleted(self):
        self.search_bar_element = 'chicken'
        element = self.driver.find_element(*MainPageLocators.SUBMIT_EMPTY)
        element.click()
        time.sleep(5)
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        element3 = self.driver.find_elements_by_css_selector('div.result-div')
        element4 = self.driver.find_elements_by_css_selector('div.selection-div-class')
        if len(element4) > 0:
            total_divs = len(element4)
            clear_all_button = self.driver.find_element(*MainPageLocators.CLEAR_BUTTON)
            clear_all_button.click()

            divs_after_1_deletion = len(self.driver.find_elements_by_css_selector('div.selection-div-class'))

            if divs_after_1_deletion == 0:
                return True
            else:
                return False

        else:
            return True

    # location
    def get_location_status(self):
        return self.driver.find_element(*MainPageLocators.LOCATION_STATUS_DIV) \
            .get_attribute("innerHTML")

    def get_location_map_place_name_and_address(self):
        locationIframe = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME)
        self.driver.switch_to.frame(locationIframe)
        # due to container size, map may not display full place card
        try:
            placeNameElement = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME_PLACE_NAME)
            placeName = placeNameElement.get_attribute("innerHTML")
        except:
            placeName = None
        try:
            placeAddressElement = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME_PLACE_ADDRESS)
            placeAddress = placeAddressElement.get_attribute("innerHTML")
        except:
            placeAddress = None
        self.driver.switch_to.default_content()
        return (placeName, placeAddress)

    def get_location_first_dropdown_item_name_and_address(self):
        firstDropdownItem = self.driver.find_element(*MainPageLocators.LOCATION_DROPDOWN) \
            .find_element(*MainPageLocators.LOCATION_DROPDOWN_ITEM)
        placeName = firstDropdownItem \
            .find_element(*MainPageLocators.LOCATION_DROPDOWN_ITEM_PLACE_INFO).text
        placeAddress = firstDropdownItem.text.replace(placeName,"")
        return (placeName, placeAddress)

    def click_location_first_dropdown_item(self):
        location_input = self.driver.find_element(*MainPageLocators.LOCATION_INPUT)
        location_input.send_keys(Keys.DOWN)
        location_input.send_keys(Keys.RETURN)

# define 1 class for 1 page or 3 classes for 3 panels?


class FrontendPage(BasePage):

    search_bar_element = SearchBarElement()

    def is_footer_step1_highlighted(self):
        return ( self.isStylingCorrect(FrontendLocators.STEP_1_HIGHLIGHTED) )
    
    def is_footer_step2_highlighted(self):
        self.inputIngredientAndClickSubmit()
        return ( self.isStylingCorrect(FrontendLocators.STEP_2_HIGHLIGHTED) )

    def is_footer_step3_highlighted(self):
        self.inputIngredientAndClickSubmit()
        nextButtonElement = self.driver.find_element(*FrontendLocators.MID_NEXT_BUTTON)
        nextButtonElement.click()
        return ( self.isStylingCorrect(FrontendLocators.STEP_3_HIGHLIGHTED) )
    
    #The test to check if the boxes have right styles in step 1
    def is_box_step1_highlighted(self):
        return ( self.isStylingCorrect(FrontendLocators.STEP_1_BOX) )
    
    #Test to check if the boxes have right styles: step1->step2
    def is_box_step2_highlighted(self):
        self.inputIngredientAndClickSubmit()
        return ( self.isStylingCorrect(FrontendLocators.STEP_2_BOX) )

    #Test to check if the boxes have right styles: step1->step2->step3
    def is_box_step3_highlighted(self):
        self.inputIngredientAndClickSubmit()
        self.driver.find_element(*FrontendLocators.MID_NEXT_BUTTON).click()
        return ( self.isStylingCorrect(FrontendLocators.STEP_3_BOX) )

    #Test to check if the boxes have right styles: step1->step2->step3->step2
    def is_box_step2_rehighlighted(self):
        self.inputIngredientAndClickSubmit()
        self.driver.find_element(*FrontendLocators.MID_NEXT_BUTTON).click()
        self.driver.find_element(*FrontendLocators.RIGHT_BACK_BUTTON).click()
        return ( self.isStylingCorrect(FrontendLocators.STEP_2_BOX) )

    #Test to check if the boxes have right styles: step1->step2->step3->step2->step1
    def is_box_step1_rehighlighted(self):
        self.inputIngredientAndClickSubmit()
        self.driver.find_element(*FrontendLocators.MID_NEXT_BUTTON).click()
        self.driver.find_element(*FrontendLocators.RIGHT_BACK_BUTTON).click()
        time.sleep(0.5)
        self.driver.find_element(*FrontendLocators.MID_BACK_BUTTON).click()
        return ( self.isStylingCorrect(FrontendLocators.STEP_1_BOX) )

    def is_gifsPresent(self):
        step2Gif = ( self.driver.find_element(*FrontendLocators.BOX_STEP2).value_of_css_property("background-image") != "none" )
        step3Gif = ( self.driver.find_element(*FrontendLocators.BOX_STEP3).value_of_css_property("background-image") != "none" )
        return ( step2Gif and step3Gif )

    def is_gifsDisappear(self):
        self.inputIngredientAndClickSubmit()
        step2Gif = ( self.driver.find_element(*FrontendLocators.BOX_STEP2).value_of_css_property("background-image") == "none" )
        step3Gif = ( self.driver.find_element(*FrontendLocators.BOX_STEP3).value_of_css_property("background-image") == "none" )
        return ( step2Gif and step3Gif )

    def is_arrow_pulsing(self):
        self.inputIngredientAndClickSubmit()
        return ( self.driver.find_element(*FrontendLocators.MID_ARROW_RIGHT).value_of_css_property("animation-delay") != "0s" )

    def is_step3_options_invisible(self):
        reviewButton = ( self.driver.find_element(*FrontendLocators.REVIEW_BUTTON).value_of_css_property("display") == "none" )
        clearButton = ( self.driver.find_element(*FrontendLocators.CLEAR_BUTTON).value_of_css_property("display") == "none" )
        return ( reviewButton and clearButton)

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
        self.search_bar_element = FrontendLocators.SAMPLE_INGREDIENT

        submitElement = self.driver.find_element(*FrontendLocators.SUBMIT_BUTTON)
        submitElement.click()
