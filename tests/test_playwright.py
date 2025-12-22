from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    """
    Tests the standard user can successfully log in.
    
    Args:
        page (Page): The page fixture from pytest-playwright.
    """
    # 1. Create an instance of the LoginPage, passing the page fixture
    login_page = LoginPage(page)

    # 2. Navigate to the site
    login_page.navigate()

    # 3. Perform the login action
    login_page.login("standard_user", "secret_sauce")

    # 4. Assert that the login was successful
    # A good practice is to check for an element that only exists
    # after a successful login.
    inventory_list = page.locator(".inventory_list")
    expect(inventory_list).to_be_visible()

    # You can also check the page title or URL
    expect(page).to_have_title("Swag Labs")