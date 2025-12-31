from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# --- Test Functions ---

def test_successful_login(page: Page, base_url):
    """
    Tests that a standard user can successfully log in.
    """
    login_page = LoginPage(page)
    # Pass the base_url from fixture
    login_page.navigate(base_url)
    login_page.login("standard_user", "secret_sauce")

    # Assert that the login was successful by checking for a unique element
    inventory_list = page.locator(".inventory_list")
    expect(inventory_list).to_be_visible()
    expect(page).to_have_title("Swag Labs")

def test_invalid_logins(page: Page, invalid_login_data_from_ai, base_url):
    """
    Tests that the application handles various AI-generated invalid login attempts correctly.
    """
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    
    error_message_locator = page.locator('[data-test="error"]')

    # This loop runs the test for each set of credentials from the AI
    for creds in invalid_login_data_from_ai:
        username = creds.username
        password = creds.password
        expected_error = creds.expected_error
        
        print(f"\nTesting with invalid credentials: user='{username}', pass='{password}', expected='{expected_error}'")
        
        # Playwright's fill clears the input automatically
        login_page.login(username, password)

        # The application should show an error message.
        expect(error_message_locator).to_be_visible()

        # Verify the error message matches expected
        expect(error_message_locator).to_contain_text(expected_error)
