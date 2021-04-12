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
from locator import TestSampleLocators
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

time1 = 1
time2 = 2
time3 = 3
time5 = 5
time7 = 7
time10 = 10
time20 = 20

time2 = time3 = time5 = time7 = time10 = time20 = 1

def closeLocationPopup():
    time.sleep(time5)
    popup = driver.find_element_by_id("location-modal-close")
    popup.click()

def inputIngredientAndClickSubmit():
    time.sleep(time20)

    search_bar_element = driver.find_element(*MainPageLocators.SEARCH_BAR)
    search_bar_element.send_keys(TestSampleLocators.SAMPLE_INGREDIENT_2)

    time.sleep(time2)

    submitElement = driver.find_element(*FrontendLocators.SUBMIT_BUTTON)
    submitElement.click()  

    time.sleep(time3)

def selectFirstAndLastResult():
    time.sleep(time5)
    resultsElem = driver.find_element(*MainPageLocators.RESULTS)
    time.sleep(time1)
    driver.find_element(By.CSS_SELECTOR, ".result-div:nth-child(1) > button").click()
    time.sleep(time1)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    time.sleep(time1)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    time.sleep(time1)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    resultsElem.send_keys(Keys.PAGE_DOWN)
    time.sleep(time1)
    driver.find_element(By.CSS_SELECTOR, ".result-div:nth-last-child(15) > button").click()
    time.sleep(time1)
    arrow = driver.find_element(*FrontendLocators.MID_ARROW_RIGHT)
    arrow.click()
    time.sleep(time2)


def showResults():
    time.sleep(time5)
    driver.find_element(By.CSS_SELECTOR, "#number-0 > .btn:nth-child(2)").click()
    time.sleep(time7)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(time2)
    for i in range(2):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(time2)
    time.sleep(time2)

    driver.switch_to.window(driver.window_handles[0])    

    driver.find_element(By.CSS_SELECTOR, "#number-1 > .btn:nth-child(20)").click()
    time.sleep(time7)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(time2)
    for i in range(2):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(time2)
    time.sleep(time2)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(time5)

def restOfDemo():
    driver.find_element(By.CSS_SELECTOR, "#number-1 > #clear-button").click()
    time.sleep(time7)
    step3Back = driver.find_element(*FrontendLocators.RIGHT_BACK_BUTTON)
    step3Back.click()
    driver.find_element(By.CSS_SELECTOR, ".result-div:nth-last-child(20) > button").click()
    time.sleep(time7)
    step2Back = driver.find_element(*FrontendLocators.MID_BACK_BUTTON)
    step2Back.click()
    time.sleep(time1)
    search_bar_element = driver.find_element(*MainPageLocators.SEARCH_BAR)
    time.sleep(time1)
    searchText = driver.find_element_by_id("search-bar-id")
    searchText.clear()
    time.sleep(time1)
    search_bar_element.send_keys("Water")
    time.sleep(time1)
    submitElement = driver.find_element(*FrontendLocators.SUBMIT_BUTTON)
    submitElement.click()  
    time.sleep(time1)
    driver.find_element(By.CSS_SELECTOR, ".result-div:nth-child(2) > button").click()
    time.sleep(time1)
    arrow = driver.find_element(*FrontendLocators.MID_ARROW_RIGHT)
    arrow.click()
    time.sleep(time2)
    time.sleep(time1)
    clearBtn = driver.find_element_by_id("clear")
    clearBtn.click()

    time.sleep(time3)



    

closeLocationPopup()
inputIngredientAndClickSubmit()
selectFirstAndLastResult()
restOfDemo()



# showResults()

time.sleep(time10)
driver.close()
driver.quit()