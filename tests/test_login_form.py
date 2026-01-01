import os
from pages.testerbud_login_page import TesterBudLoginPage

def test_testerbud_login(page):
    login_page = TesterBudLoginPage(page)

    # 1. Navigate to the page
    login_page.navigate()

    # 2. Verify page title
    # The practice page title is different from the main page.
    title = login_page.get_title()
    assert "Login Automation Practice Page" in title, f"Expected title to contain 'Login Automation Practice Page', but got '{title}'"

    # 3. Check if username input is visible
    assert login_page.username_input.is_visible(), "Username input field is not visible"

    # 4. Take screenshot
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    page.screenshot(path=os.path.join(screenshot_dir, "testerbud_login.png"))
