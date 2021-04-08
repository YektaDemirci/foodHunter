from selenium.webdriver.common.by import By

class MainPageLocators(object):
    # ingredient
    SEARCH_BAR = (By.ID, "search-bar-id")
    SUBMIT = (By.ID, "submit_one")
    SUBMIT_MESSAGE = (By.ID, "message_submit")
    RESULTS = (By.ID, "results")
    RESULT_DIV = (By.CLASS_NAME, "result-div")

    # location
    LOCATION_INPUT = (By.ID, "location-input")
    LOCATION_IFRAME = (By.ID, "location-map")
    LOCATION_STATUS_DIV = (By.ID, "location-status")
    LOCATION_MODAL_CLOSE = (By.ID, "location-modal-close")
    # class name assigned by Google API
    LOCATION_DROPDOWN = (By.CLASS_NAME, "pac-container")
    LOCATION_DROPDOWN_ITEM = (By.CLASS_NAME, "pac-item")
    LOCATION_DROPDOWN_ITEM_PLACE_INFO = (By.CLASS_NAME, "pac-item-query")
    LOCATION_IFRAME_PLACE_NAME = (By.CLASS_NAME, "place-name")
    LOCATION_IFRAME_PLACE_ADDRESS = (By.CLASS_NAME, "address")

    REVIEW_SUMMARY = (By.ID, "order_modal")
    REVIEW_SUMMARY_CLOSE = (By.CLASS_NAME, "close")


class FrontendLocators(object):

    # footer prefixes because step# by className returned panel divs instead of footer
    FOOTER_STEP1 = (By.ID, "footer-step1")
    FOOTER_STEP2 = (By.ID, "footer-step2")
    FOOTER_STEP3 = (By.ID, "footer-step3")

    # added box to run test over
    BOX_STEP1 = (By.ID, "box-step1")
    BOX_STEP2 = (By.ID, "box-step2")
    BOX_STEP3 = (By.ID, "box-step3")

    SUBMIT_BUTTON = (By.CLASS_NAME, "submitLeftNext")
    MID_NEXT_BUTTON = (By.CLASS_NAME, "submitMidNext")
    MID_BACK_BUTTON = (By.CLASS_NAME, "submitMidBack")
    RIGHT_BACK_BUTTON = (By.CLASS_NAME, "submitRightBack")

    MID_ARROW_RIGHT = (By.ID, "step2-right-arrow-button")

    #Bar states
    BOX_ACTIVE_STYLE = "activeBox"
    BOX_DONE_STYLE = "doneBox"
    BOX_UNDONE_STYLE = "undoneBox"

    # Should constants be in the 'locators.py' file or another file?
    FOOTER_ACTIVE_STYLE = "current-step"
    FOOTER_DONE_STYLE = "done-step"
    FOOTER_UNDONE_STYLE = "undone-step"

    SAMPLE_INGREDIENT = "chicken"

    # Step 3 options
    REVIEW_BUTTON = (By.ID, "review")
    CLEAR_BUTTON = (By.ID, "clear")

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
        [FOOTER_STEP1, FOOTER_DONE_STYLE],
        [FOOTER_STEP2, FOOTER_DONE_STYLE],
        [FOOTER_STEP3, FOOTER_ACTIVE_STYLE] ]


    # Checking if CSS properties are correct in boxes
    STEP_1_BOX = [ 
        [BOX_STEP1, BOX_ACTIVE_STYLE],
        [BOX_STEP2, BOX_UNDONE_STYLE],
        [BOX_STEP3, BOX_UNDONE_STYLE] ]

    STEP_2_BOX = [ 
        [BOX_STEP1, BOX_DONE_STYLE],
        [BOX_STEP2, BOX_ACTIVE_STYLE],
        [BOX_STEP3, BOX_UNDONE_STYLE] ]

    STEP_3_BOX = [ 
        [BOX_STEP1, BOX_DONE_STYLE],
        [BOX_STEP2, BOX_DONE_STYLE],
        [BOX_STEP3, BOX_ACTIVE_STYLE] ]
    
