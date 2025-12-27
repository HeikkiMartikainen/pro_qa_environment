from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Use the more robust data-test selectors
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def navigate(self, url: str = "https://www.saucedemo.com/"):
        """Navigates to the login page. Defaults to the standard URL if not provided."""
        super().navigate(url)

    def login(self, username: str, password: str):
        """Fills the login form and clicks the login button."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
