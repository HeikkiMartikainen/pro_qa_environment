from playwright.sync_api import Page
from pages.base_page import BasePage

class TesterBudLoginPage(BasePage):
    EXPECTED_TITLE = "Login Automation Practice Page"
    URL = "https://testerbud.com/practice-login-form"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#formBasicEmail")
        self.password_input = page.locator("#formBasicPassword")
        self.login_button = page.locator("button[type='submit']")
        self.forget_password_link = page.locator("a[href='/forget-password']")
        self.register_link = page.locator("a[href='/register']")
        self.success_message = page.get_by_text("Login Successful")
        self.back_to_login_button = page.get_by_text("Back to Login")

    def navigate(self):
        """Navigates to the TesterBud login practice page."""
        super().navigate(self.URL)

    def login(self, username, password):
        """Fills in credentials and clicks login."""
        self.username_input.fill(username)
        if password is not None:
             self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """
        Retrieves the error message displayed on the page.
        """
        if self.page.locator(".alert-danger").is_visible():
             return self.page.locator(".alert-danger").first.inner_text()
        return ""

    def get_email_validation_message(self) -> str:
        """Returns the HTML5 validation message for the email input."""
        return self.page.evaluate("document.querySelector('#formBasicEmail').validationMessage")
