from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils import constants
import time

class EntrataPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        # Expected values from constants for validation
        self.expected_title = constants.HOME_PAGE_TITLE
        self.expected_homebody_RXP_Text = constants.HOMEBODY_RXP_TEXT
        self.expected_entrata_OS_Text = constants.ENTRATA_OS_TEXT
        self.cards_titles = constants.CARD_TITLES # as list
        self.cards_urls = constants.CARDS_URLS # as list
        self.homebody_title = constants.HOMEBODY_TITLE
        self.homebody_expected_url = constants.HOMEBODY_EXPECTED_URL
        # Locators for various elements on the page
        self.homebody_RXP_Link = (By.ID, "w-tabs-1-data-w-tab-0")
        self.entrata_OS_Link = (By.ID, "w-tabs-1-data-w-tab-1")
        self.homebody_RXP_Text = (By.XPATH, "//h1[@class='slider-hero_heading']")
        self.entrata_OS_Text = (By.XPATH, "//h2[@class='slider-hero_heading']")
        self.learnMore_button = (By.XPATH, "(//div[@class='button_text'][normalize-space()='Learn more'])[1]")
        self.book_demo = (By.XPATH,"//div[@class='text-btn hidden-mobile']")
        self.firstName_input = (By.ID, "FirstName")
        self.lastName_input = (By.ID, "LastName")
        self.email_input = (By.ID, "Email")
        self.company_input = (By.ID, "Company")
        self.phone_input = (By.ID, "Phone")
        self.unit_count_input = (By.ID, "Unit_Count__c")
        self.title_input = (By.ID, "Title")
        self.home_logo = (By.XPATH, "//a[@aria-label='home']")
        self.cards = (By.XPATH, "//div[@class='suite-cards_layout']")
        self.video_Link = (By.XPATH, "//div[@aria-label='Play']")
        self.video_play_button = (By.XPATH, "//button[@aria-label='Play Video: Homebody RXP Hype']")
        self.video_pause_button = (By.XPATH, "//button[@aria-label='Pause: Homebody RXP Hype']")

    def load_page(self, url):
        """Load the given URL in the browser."""
        self.driver.get(url)

    def is_title_correct(self):
        """Check if the current page title matches the expected title."""
        self.wait.until(EC.title_is(self.expected_title))
        return self.driver.title == self.expected_title
    
    def validate_homebody_RXP_text(self):
        """
        Click the Homebody RXP tab and validate the displayed text.
        Returns True if the text matches the expected value.
        """
        self.driver.execute_script("window.scrollBy(0, 300);")
        self.wait.until(EC.element_to_be_clickable(self.homebody_RXP_Link)).click()
        self.wait.until(EC.visibility_of_element_located(self.homebody_RXP_Text))
        element = self.wait.until(EC.visibility_of_element_located(self.homebody_RXP_Text))
        return element.text.strip() == self.expected_homebody_RXP_Text

    def validate_entrata_OS_text(self):
        """
        Click the Entrata OS tab and validate the displayed text.
        Returns True if the text matches the expected value.
        """
        self.wait.until(EC.element_to_be_clickable(self.entrata_OS_Link)).click()
        self.wait.until(EC.visibility_of_element_located(self.entrata_OS_Text))
        element = self.wait.until(EC.visibility_of_element_located(self.entrata_OS_Text))
        return element.text.strip() == self.expected_entrata_OS_Text

    def click_learn_more_button_and_validate_title_and_url(self):
        """
        Click the 'Learn More' button, switch to the new tab, and validate the title and URL.
        Returns True if both match the expected values.
        """
        self.wait.until(EC.element_to_be_clickable(self.homebody_RXP_Link)).click()
        self.wait.until(EC.element_to_be_clickable(self.learnMore_button)).click()
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.wait.until(EC.title_is(self.homebody_title))
        current_url = self.driver.current_url
        return self.driver.title == self.homebody_title and current_url == self.homebody_expected_url
    
    def click_book_demo_and_fill_details_without_submit_and_compare(self):
        """
        Click the 'Book Demo' button, fill out the form with constants, and compare entered values.
        Returns True if all values match the expected constants.
        """
        self.wait.until(EC.element_to_be_clickable(self.book_demo)).click()
        # Fill out the form fields
        self.wait.until(EC.visibility_of_element_located(self.firstName_input)).send_keys(constants.FIRST_NAME)
        self.wait.until(EC.visibility_of_element_located(self.lastName_input)).send_keys(constants.LAST_NAME)
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(constants.EMAIL)
        self.wait.until(EC.visibility_of_element_located(self.company_input)).send_keys(constants.COMPANY)
        self.wait.until(EC.visibility_of_element_located(self.phone_input)).send_keys(constants.PHONE)
        # Select unit count from dropdown
        unit_count_element = self.wait.until(EC.visibility_of_element_located(self.unit_count_input))
        select = Select(unit_count_element)
        select.select_by_value("1 - 100")  # or use select.select_by_visible_text("1 - 100")
        self.wait.until(EC.visibility_of_element_located(self.title_input)).send_keys(constants.TITLE)
        # Retrieve entered values for validation
        first_name_value = self.driver.find_element(*self.firstName_input).get_attribute("value")
        last_name_value = self.driver.find_element(*self.lastName_input).get_attribute("value")
        email_value = self.driver.find_element(*self.email_input).get_attribute("value")
        company_value = self.driver.find_element(*self.company_input).get_attribute("value")
        phone_value = self.driver.find_element(*self.phone_input).get_attribute("value")
        unit_count_value = Select(self.driver.find_element(*self.unit_count_input)).first_selected_option.text
        title_value = self.driver.find_element(*self.title_input).get_attribute("value")
        # If a new tab was opened, close it and switch back to the original
        if len(self.driver.window_handles) > 1:
            self.driver.close()  # Close current tab (tab 2)
            self.driver.switch_to.window(self.driver.window_handles[0])  # Switch to tab 1
        # Return True if all values match the expected constants
        return (
            first_name_value == constants.FIRST_NAME and
            last_name_value == constants.LAST_NAME and
            email_value == constants.EMAIL and
            company_value == constants.COMPANY and
            phone_value == constants.PHONE and
            unit_count_value == "1 - 100" and
            title_value == constants.TITLE
        )

    def navigate_Property_AI_Resident_Analytics_cards_and_verify_title_and_url(self):
        """
        Iterate through all Property AI Resident Analytics cards, click each, and verify the title and URL.
        Returns True if all cards have the expected title and URL.
        """
        all_passed = True
        # Collect all card relative hrefs at the start
        cards_container = self.wait.until(EC.visibility_of_element_located(self.cards))
        card_links = cards_container.find_elements(By.TAG_NAME, "a")
        card_hrefs = [card.get_attribute("href") for card in card_links]

        # Convert all hrefs to relative paths for searching
        from urllib.parse import urlparse
        card_relative_hrefs = [urlparse(href).path for href in card_hrefs]

        for idx, rel_href in enumerate(card_relative_hrefs):
            # After returning home, re-find the card by its relative href
            cards_container = self.wait.until(EC.visibility_of_element_located(self.cards))
            card = cards_container.find_element(By.XPATH, f".//a[@href='{rel_href}']")

            # Scroll to the card and click it
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
            self.driver.execute_script("window.scrollBy(0, 300);")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f".//a[@href='{rel_href}']")))
            card.click()

            # Validate the title and URL of the navigated page
            expected_title = self.cards_titles[idx]
            expected_url = self.cards_urls[idx]
            self.wait.until(EC.title_is(expected_title))
            actual_title = self.driver.title
            actual_url = self.driver.current_url

            if actual_title != expected_title or actual_url != expected_url:
                all_passed = False

            # Go back to home by clicking the home logo and wait for home page to load
            home_logo_elem = self.wait.until(EC.element_to_be_clickable(self.home_logo))
            home_logo_elem.click()
            self.wait.until(EC.title_is(self.expected_title))

        return all_passed

    def validate_video_is_playing(self):
        """
        Scroll to the video section, click the play button, and check if the video is playing.
        Returns True if the video is playing, otherwise False.
        """
        self.driver.execute_script("window.scrollBy(0, 2400);")
        # Click the video play button
        self.wait.until(EC.element_to_be_clickable(self.video_Link)).click()
        # Step 2: Wait and find the <video> element
        video = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
        # Step 3: Wait for video to load and start playing
        time.sleep(20)  # Optional wait if needed
        # Step 4: Check if video is playing (JS execution)
        is_playing = self.driver.execute_script("""
            const video = arguments[0];
            return !video.paused && !video.ended && video.readyState > 2;
        """, video)
        return is_playing