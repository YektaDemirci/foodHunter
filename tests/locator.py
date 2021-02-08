from selenium.webdriver.common.by import By

class MainPageLocators(object):
    # footer prefixes because step# by className returned panel divs instead of footer
    FOOTER_STEP1 = (By.ID, "footer-step1")
    FOOTER_STEP2 = (By.ID, "footer-step2")
    FOOTER_STEP3 = (By.ID, "footer-step3")

    # Should constants be in the 'locators.py' file or another file?
    FOOTER_ACTIVE_STYLE = "current-step"
    FOOTER_DONE_STYLE = "done-step"
    FOOTER_UNDONE_STYLE = "undone-step"

    # Should these kind of const's be in another file?
    STEP_1_HIGHLIGHTED = [ 
        [FOOTER_STEP1, FOOTER_ACTIVE_STYLE],
        [FOOTER_STEP2, FOOTER_UNDONE_STYLE],
        [FOOTER_STEP3, FOOTER_UNDONE_STYLE] ]

    STEP_2_HIGHLIGHTED = [ 
        [FOOTER_STEP1, FOOTER_DONE_STYLE],
        [FOOTER_STEP2, FOOTER_ACTIVE_STYLE],
        [FOOTER_STEP3, FOOTER_UNDONE_STYLE] ]

    STEP_3_HIGHLIGHTED = [ 
        [FOOTER_STEP1, FOOTER_UNDONE_STYLE],
        [FOOTER_STEP2, FOOTER_UNDONE_STYLE],
        [FOOTER_STEP3, FOOTER_DONE_STYLE] ]
    