from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOCATION_INPUT = (By.ID, "location-input")
    LOCATION_IFRAME = (By.ID, "location-map")
    STATUS_DIV = (By.ID, "status")
    LOCATION_DROPDOWN = (By.CLASS_NAME, "pac-container")
    LOCATION_DROPDOWN_ITEM = (By.CLASS_NAME, "pac-item")