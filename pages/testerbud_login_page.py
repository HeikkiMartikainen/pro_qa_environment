from playwright.sync_api import Page
from pages.base_page import BasePage

class TesterBudLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Updated selector based on actual page HTML
        self.username_input = page.locator("#formBasicEmail")

    def navigate(self):
        """Navigates to the TesterBud login practice page."""
        super().navigate("https://testerbud.com/practice-login-form")
