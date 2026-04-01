from playwright.sync_api import Page
from pages.base_page import BasePage

class SauceDemoLoginPage(BasePage):
    EXPECTED_TITLE = "Swag Labs"
    URL = "https://www.saucedemo.com/"

    ERROR_INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
    ERROR_LOCKED_OUT_USER = "Epic sadface: Sorry, this user has been locked out."
    ERROR_USERNAME_REQUIRED = "Epic sadface: Username is required"
    ERROR_PASSWORD_REQUIRED = "Epic sadface: Password is required"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def navigate(self, url: str | None = None):
        """Navigates to the Sauce Demo login page."""
        super().navigate(url or self.URL)

    def login(self, username: str, password: str):
        """Fills in credentials and clicks login."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """
        Retrieves the error message displayed on the page.
        """
        if self.error_message.is_visible():
             return self.error_message.first.inner_text()
        return ""
