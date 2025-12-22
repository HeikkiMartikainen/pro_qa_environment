from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Use the more robust data-test selectors
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def navigate(self):
        """Navigates to the login page."""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        """Fills the login form and clicks the login button."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()