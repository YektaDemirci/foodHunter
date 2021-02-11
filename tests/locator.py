from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BAR = (By.ID, "search-bar-id")
    SUBMIT_EMPTY = (By.ID, "submit_one")
    SUBMIT_MESSAGE = (By.ID, "message_submit")
    RESULTS = (By.ID, "results")
