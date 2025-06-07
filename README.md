1. Install VS code
2. Install pyhton
3. Create Project folder and open in VS Code
	mkdir AutomateEntrata
	cd AutomateEntrata
3. Create Virtual Environment
	python -m venv venv
4. Activate Virtual Environment
	venv\Scripts\activate
5. Install dependencies
	pip install selenium pytest pytest-html webdriver-manager
6. Save to requirements.txt
	pip freeze > requirements.txt
7. To execute code 
	pytest

## Test Scenarios Covered

1. **Verify Entrata Home Page Title**
   - Loads the Entrata home page and asserts that the page title matches the expected value.

2. **Validate Homebody RXP Text (Verifying dynamic content.)**
   - Navigates to the Homebody RXP section and verifies that the displayed text matches the expected content.

3. **Validate Entrata OS Text (Verifying dynamic content.)**
   - Navigates to the Entrata OS section and verifies that the displayed text matches the expected content.

4. **Click 'Learn More' Button and Book Demo (without submit) (Interacting with forms (without submitting them).)**
   - Clicks the "Learn more" button, switches to the new tab, and validates the page title and URL.
   - Opens the Book Demo form, fills in all required fields (without submitting), and verifies that all entered values match the expected constants.

5. **Navigate to Property, AI, Resident, Analytics, Cards and Verify Title and URL (Navigating through different pages.)**
   - Iterates through all cards in the Property AI Resident Analytics section.
   - For each card: scrolls, clicks, validates the resulting page's title and URL, returns to the home page, and repeats for all cards.

6. **Validate Video is Playing (Testing other interesting features on the site.)**
   - Scrolls to the video section, clicks the play button, and verifies that the video starts playing by checking for the presence of the pause button.

---

**How to Run All Tests:**
pytest

All tests are located in the `tests/` directory and use the `pytest` framework.


**Step-by-Step: Clone & Run the Project**

1. Clone the Repository
   - git clone https://github.com/sudarshan692/EntrataAutomate.git
   - cd EntrataAutomate
3. Create and Activate a Virtual Environment
   - python -m venv venv
   - For Windows: venv\Scripts\activate
   - For mac/Linux: source venv/bin/activate
4. Install Dependencies
   - pip install -r requirements.txt
5. Run the Tests
   - pytest


