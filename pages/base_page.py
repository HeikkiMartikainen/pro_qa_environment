from playwright.sync_api import Page
import os

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

    def take_screenshot(self, name: str, directory: str = "screenshots"):
        """Takes a screenshot and saves it to the specified directory."""
        if not os.path.exists(directory):
            os.makedirs(directory)

        if not name.endswith(".png"):
            name = f"{name}.png"

        self.page.screenshot(path=os.path.join(directory, name))
