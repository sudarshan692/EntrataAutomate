from utils import constants

def test_load_page_and_verify_entrata_title(entrata_page):
    """
    Test Scenario:
    - Loads the Entrata home page and verifies that the page title matches the expected value.
    """
    entrata_page.load_page(constants.BASE_URL)
    assert entrata_page.is_title_correct(), "Page title did not match expected title"

def test_validate_homebody_RXP_text(entrata_page):
    """
    Test Scenario:
    - Navigates to the Homebody RXP section and verifies that the displayed text matches the expected content.
    """
    assert entrata_page.validate_homebody_RXP_text(), "Homebody RXP text is not displayed correctly"

def test_validate_entrata_OS_text(entrata_page):
    """
    Test Scenario:
    - Navigates to the Entrata OS section and verifies that the displayed text matches the expected content.
    """
    assert entrata_page.validate_entrata_OS_text(), "Entrata OS text is not displayed correctly"

def test_click_learn_more_button_And_Book_Demo_without_submit(entrata_page):
    """
    Test Scenario:
    - Clicks the 'Learn more' button, switches to the new tab, and validates the page title and URL.
    - Opens the Book Demo form, fills in all required fields (without submitting), and verifies that all entered values match the expected constants.
    """
    assert entrata_page.click_learn_more_button_and_validate_title_and_url(), "Learn more button did not navigate to the expected page"
    assert entrata_page.click_book_demo_and_fill_details_without_submit_and_compare(), "Book demo form did not submit correctly"

def test_navigate_to_Property_AI_Resident_Analytics_cards_and_verify_title_and_url(entrata_page):
    """
    Test Scenario:
    - Iterates through all Property AI Resident Analytics cards.
    - For each card: scrolls, clicks, validates the resulting page's title and URL, returns to the home page, and repeats for all cards.
    """
    assert entrata_page.navigate_Property_AI_Resident_Analytics_cards_and_verify_title_and_url(), "One or more cards did not have the expected title or URL"

def test_validate_video_is_playing(entrata_page):
    """
    Test Scenario:
    - Scrolls to the video section, clicks the play button, and verifies that the video starts playing by checking for the presence of the pause button or video playback state.
    """
    assert entrata_page.validate_video_is_playing(), "Video did not start playing after clicking the play button"