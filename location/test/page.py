import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from locator import *
from element import BasePageElement


# test page url
base_url = "http://localhost:8000/location/location.html"
# path of Firefox geckodriver
geckodriver_path = os.path.dirname(__file__) + "/geckodriver"

def getDriverGeoOption(argument):
    geoOption = webdriver.FirefoxOptions()
    if argument == "disabled":
        geoOption.set_preference("geo.enabled", False)
    elif argument == "denied":
        geoOption.set_preference("geo.prompt.testing", True)
        geoOption.set_preference("geo.prompt.testing.allow", False)
    elif argument == "allowed":
        geoOption.set_preference('geo.prompt.testing', True)
        geoOption.set_preference('geo.prompt.testing.allow', True)
        # set mock geolocation to Toronto
        geoOption.set_preference('geo.provider.network.url',
            'data:application/json,{"location": {"lat": 43.6532, "lng": -79.3832}, "accuracy": 100.0}')
    return geoOption


class LocationSearchTextElement(BasePageElement):
    def __init__(self):
        self.locator = MainPageLocators.LOCATION_INPUT


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    location_search_text_element = LocationSearchTextElement()

    def get_status(self):
        return self.driver.find_element(*MainPageLocators.STATUS_DIV) \
            .get_attribute("innerHTML")

    def get_location_map_place_name_and_address(self):
        locationIframe = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME)
        self.driver.switch_to.frame(locationIframe)
        placeName = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME_PLACE_NAME) \
            .get_attribute("innerHTML")
        placeAddress = self.driver.find_element(*MainPageLocators.LOCATION_IFRAME_PLACE_ADDRESS) \
            .get_attribute("innerHTML")
        self.driver.switch_to.default_content()
        return (placeName, placeAddress)

    def get_first_dropdown_item_name_and_address(self):
        firstDropdownItem = self.driver.find_element(*MainPageLocators.LOCATION_DROPDOWN) \
            .find_element(*MainPageLocators.LOCATION_DROPDOWN_ITEM)
        placeName = firstDropdownItem \
            .find_element(*MainPageLocators.LOCATION_DROPDOWN_ITEM_PLACE_INFO).text
        placeAddress = firstDropdownItem.text.replace(placeName,"")
        return (placeName, placeAddress)

    def click_first_dropdown_item(self):
        location_input = self.driver.find_element(*MainPageLocators.LOCATION_INPUT)
        location_input.send_keys(Keys.DOWN)
        location_input.send_keys(Keys.RETURN)