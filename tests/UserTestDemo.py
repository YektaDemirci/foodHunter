import os
import time
import json
import unittest
import page
import warnings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locator import MainPageLocators
from locator import FrontendLocators
from element import BasePageElement

path_parent = os.path.dirname(__file__)
path_parent = os.path.join(path_parent, os.pardir)
os.chdir(path_parent)
# print(os.getcwd())

PATH = "file://"+os.getcwd()+"/main.html"

def getDriverOption(argument):
    option = Options()
    if argument == "disabled":
        option.set_preference("geo.enabled", False)
    elif argument == "denied":
        option.set_preference("geo.prompt.testing", True)
        option.set_preference("geo.prompt.testing.allow", False)
    elif argument == "allowed":
        option.set_preference('geo.prompt.testing', True)
        option.set_preference('geo.prompt.testing.allow', True)
        # set mock geolocation to University of Waterloo Station
        option.set_preference('geo.provider.network.url',
            'data:application/json,{"location": {"lat": 43.4733, "lng": -80.5410}, "accuracy": 100.0}')
    return option

driver = webdriver.Firefox( \
        options=getDriverOption("allowed"), \
        # executable_path='tests/geckodriver', \
        service_log_path='/dev/null')
driver.get(PATH)
driver.implicitly_wait(3)
warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


def inputIngredientAndClickSubmit():
    search_bar_element = driver.find_element(*MainPageLocators.SEARCH_BAR)
    search_bar_element.send_keys(FrontendLocators.SAMPLE_INGREDIENT)

    time.sleep(1)

    submitElement = driver.find_element(*FrontendLocators.SUBMIT_BUTTON)
    submitElement.click()  

    time.sleep(2)

def selectFirstAndLastResult():
    resultsElem = driver.find_element(*MainPageLocators.RESULTS)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".result-div:nth-child(1) > button").click()
    time.sleep(1)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".result-div:nth-last-child(1) > button").click()
    time.sleep(1)
    arrow = driver.find_element(*FrontendLocators.MID_ARROW_RIGHT)
    arrow.click()
    time.sleep(2)


def showResults():
    reviewButton = driver.find_element(*FrontendLocators.REVIEW_BUTTON)
    reviewButton.click()
    time.sleep(3)
    closeReview = driver.find_element(*MainPageLocators.REVIEW_SUMMARY_CLOSE)
    closeReview.click()


inputIngredientAndClickSubmit()
selectFirstAndLastResult()
showResults()

time.sleep(2)
driver.close()
driver.quit()