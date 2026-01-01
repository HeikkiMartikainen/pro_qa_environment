from pages.testerbud_login_page import TesterBudLoginPage

def test_testerbud_login(page):
    login_page = TesterBudLoginPage(page)

    # 1. Navigate to the page
    login_page.navigate()

    # 2. Verify page title
    title = login_page.get_title()
    assert login_page.EXPECTED_TITLE in title, f"Expected title to contain '{login_page.EXPECTED_TITLE}', but got '{title}'"

    # 3. Check if username input is visible
    assert login_page.username_input.is_visible(), "Username input field is not visible"

    # 4. Take screenshot
    login_page.take_screenshot("testerbud_login")
