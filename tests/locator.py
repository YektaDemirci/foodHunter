from selenium.webdriver.common.by import By

class MainPageLocators(object):
    # footer prefixes because step# by className returned panel divs instead of footer
    FOOTER_STEP1 = (By.ID, "footer-step1")
    FOOTER_STEP2 = (By.ID, "footer-step2")
    FOOTER_STEP3 = (By.ID, "footer-step3")

    