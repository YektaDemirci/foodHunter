import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locator import MainPageLocators, FrontendLocators
from element import BasePageElement

'''
    SearchBarElement: 
    only used for search bars (defined in element.py)
    search_bar_element = "USER_INPUT" <==> search_bar_element.send_keys("USER_INPUT")
    user_input = search_bar_element <==> user_input = search_bar_element.get_attribute("value")
'''
class SearchBarElement(BasePageElement):
    def __init__(self):
        self.locator = MainPageLocators.SEARCH_BAR

class LocationSearchBarElement(BasePageElement):
    def __init__(self):
        self.locator = MainPageLocators.LOCATION_INPUT

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(2)
    
    def close_location_modal(self):
        element = self.driver.find_element(*MainPageLocators.LOCATION_MODAL_CLOSE)
        element.click()
    
    def wait_for_geolocation(self):
        time.sleep(3)


class MainPage(BasePage):
    search_bar_element = SearchBarElement()

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_geolocation()
        self.close_location_modal()
        
    '''
        Helper functions
    '''
    def submit(self):
        element = self.driver.find_element(*MainPageLocators.SUBMIT)
        element.click()

    def wait_for_results(self):
        time.sleep(5)

    def has_output_for_input(self, search_input):
        self.search_bar_element = search_input
        self.submit()
        self.wait_for_results()
        element = self.driver.find_element(*MainPageLocators.RESULTS)
        if element.text:
            if element.text != 'Sorry, we could not find anything.':
                return True
            else:
                return False
        else:
            return False

    '''
        Ingredient
    '''
    def is_input_empty(self):
        self.submit()
        element = self.driver.find_element(*MainPageLocators.SUBMIT_MESSAGE)
        return (element.text == 'No input found')

    def has_output_for_one_ingredient(self):
        return self.has_output_for_input('chicken')

    def has_output_for_multiple_ingredients(self):
        return self.has_output_for_input('tomato sauce,bacon,ham')

    def has_output_for_different_inputs(self):
        different_inputs = ['ing1', 'ing2', 'ing3']
        for one_input in different_inputs:
            # return False if current input has no output
            if not self.has_output_for_input(one_input):
                return False
        return True

    def has_output_for_input_with_spacing(self):
        return self.has_output_for_input('  beef , cheese   ')

    def has_no_output_for_bad_input(self):
        self.search_bar_element = 'asdfgh'
        self.submit()
        self.wait_for_results()
        element = self.driver.find_element(*MainPageLocators.RESULTS)
        if element.text:
            if element.text == 'Sorry, we could not find anything.':
                return True
            else:
                return False
        else:
            return False

    '''
        Step 2
    '''
    def is_output_with_matching_ingredients(self):
        required = ['tomato sauce', 'bacon', 'ham']
        self.search_bar_element = 'tomato sauce,bacon,ham'
        self.submit()
        self.wait_for_results()
        elements = self.driver.find_elements(*MainPageLocators.RESULT_DIV)
        # get product, restaurant, and address of the result
        result_split = elements[0].text.split('\n')
        result_product = result_split[0]
        result_restaurant = result_split[1].replace('Location: ','')
        result_address = result_split[2].replace('Address: ','')
        check = True
        with open("data_food_sample.json", "r") as file:
            data = json.load(file)
            for entry in data:
                counter = 0
                ingredients = entry['ingredients'].split(",")
                ingredients = [x.lower() for x in ingredients]
                # check how many required ingredients does current item have
                for req in required:
                    if req.lower() in ingredients:
                        counter += 1
                # matched item: should have all the ingredients
                if (entry['product'] == result_product) and (entry['restaurant'] == result_restaurant) \
                    and (entry['address'] == result_address):
                    check &= (counter == len(required))
                    break
        return check
    
    def is_output_sorted_by_distance(self):
        self.search_bar_element = 'cheese, tomato'
        self.submit()
        self.wait_for_results()
        elements = self.driver.find_elements(*MainPageLocators.RESULT_DIV)
        previous_distance = None
        for element in elements:
            # get distance of the result
            result_split = element.text.split('\n')
            result_distance_split = result_split[3].split()
            result_distance = float(result_distance_split[1])
            if previous_distance != None:
                # current distance is expected to be larger
                if result_distance < previous_distance:
                    return False
            previous_distance = result_distance
        return True

    '''
        Step 3: delete elements
    '''
    def is_div_present(self):
        self.search_bar_element = 'chicken'
        self.submit()
        self.wait_for_results()
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        element3 = self.driver.find_elements_by_css_selector('div.result-div')
        if len(element3) > 0:
            buttons = self.driver.find_elements_by_css_selector('button.selection-button')
            for button in buttons:
                button.click()

            element4 = self.driver.find_elements_by_css_selector('div.selection-div-class')
            count = len(element4)

            if count == len(element3):
                return True
            else:
                return False
        elif len(element3) == 0 and element2.text == 'Sorry, we could not find anything.':
            return True

        else:
            return False

    def is_div_deleted(self):
        self.search_bar_element = 'chicken'
        self.submit()
        self.wait_for_results()
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
        self.submit()
        self.wait_for_results()
        element2 = self.driver.find_element(*MainPageLocators.RESULTS)
        element3 = self.driver.find_elements_by_css_selector('div.result-div')
        element4 = self.driver.find_elements_by_css_selector('div.selection-div-class')
        if len(element4) > 0:
            total_divs = len(element4)
            clear_all_button = self.driver.find_element(*FrontendLocators.CLEAR_BUTTON)
            clear_all_button.click()

            divs_after_1_deletion = len(self.driver.find_elements_by_css_selector('div.selection-div-class'))

            if divs_after_1_deletion == 0:
                return True
            else:
                return False

        else:
            return True
            

class LocationModalPage(BasePage):
    location_search_bar_element = LocationSearchBarElement()

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_geolocation()
    
    '''
        Helper functions
    '''
    def get_location_status(self):
        return self.driver.find_element(*MainPageLocators.LOCATION_STATUS_DIV) \
            .get_attribute('innerHTML')

    def get_location_map_place_name_and_address(self):
        locationIframe = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME)
        self.driver.switch_to.frame(locationIframe)
        # due to container size, map may not display full place card
        try:
            placeNameElement = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME_PLACE_NAME)
            placeName = placeNameElement.get_attribute('innerHTML')
        except:
            placeName = None
        try:
            placeAddressElement = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME_PLACE_ADDRESS)
            placeAddress = placeAddressElement.get_attribute('innerHTML')
        except:
            placeAddress = None
        self.driver.switch_to.default_content()
        return (placeName, placeAddress)

    def get_location_first_dropdown_item_name_and_address(self):
        firstDropdownItem = self.driver.find_element(*MainPageLocators.LOCATION_DROPDOWN) \
            .find_element(*MainPageLocators.LOCATION_DROPDOWN_ITEM)
        placeName = firstDropdownItem \
            .find_element(*MainPageLocators.LOCATION_DROPDOWN_ITEM_PLACE_INFO).text
        placeAddress = firstDropdownItem.text.replace(placeName,'')
        return (placeName, placeAddress)

    def click_location_first_dropdown_item(self):
        location_input = self.driver.find_element(*MainPageLocators.LOCATION_INPUT)
        location_input.send_keys(Keys.DOWN)
        location_input.send_keys(Keys.RETURN)

    '''
        Location
    '''
    def is_geolocation_access_disabled(self):
        return (self.get_location_status() == "Error: Your browser doesn't support geolocation.")

    def is_geolocation_access_denied(self):
        return (self.get_location_status() == "Error: The Geolocation service failed.")
    
    def is_geolocation_access_allowed(self):
        if self.get_location_status() != "":
            return False
        time.sleep(2)
        placeName, _ = self.get_location_map_place_name_and_address()
        return (placeName == '''43°28'23.9"N 80°32'27.6"W''')

    def is_location_output_valid(self, input_option):
        if input_option == "postal_code":
            searchInput = 'N2L 3E9'
            expectedFirstItemName = 'N2L 3E9'
            expectedFirstItemAddress = 'Waterloo, ON, Canada'
            expectedPlaceName = 'Waterloo, ON N2L 3E9'
            expectedPlaceAddress = None
        elif input_option == "address":
            searchInput = '200 University Ave W, Waterloo, ON'
            expectedFirstItemName = '200 University Ave W'
            expectedFirstItemAddress = 'Waterloo, Ontario, Canada'
            expectedPlaceName = 'Engineering 5'
            expectedPlaceAddress = None
        else:
            return False
        self.location_search_bar_element = searchInput
        time.sleep(3)
        firstItemName, firstItemAddress = self.get_location_first_dropdown_item_name_and_address()
        if (firstItemName != expectedFirstItemName) or (firstItemAddress != expectedFirstItemAddress):
            return False
        self.click_location_first_dropdown_item()
        time.sleep(5)
        placeName, placeAddress = self.get_location_map_place_name_and_address()
        if (expectedPlaceName != None) and (placeName != expectedPlaceName):
            return False
        if (expectedPlaceAddress != None) and (placeAddress != expectedPlaceAddress):
            return False
        return True


class FrontendPage(BasePage):
    search_bar_element = SearchBarElement()

    def __init__(self, driver):
        super().__init__(driver)
        self.close_location_modal()

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
