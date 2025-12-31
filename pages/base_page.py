from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigates to the specified URL."""
        self.page.goto(url)

    def get_title(self) -> str:
        """Returns the page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Returns the current URL."""
        return self.page.url
