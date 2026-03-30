import pytest
from playwright.sync_api import Page, expect
from src.pages.saucedemo_login_page import SauceDemoLoginPage
from config.variables import SAUCEDEMO_URL, SAUCEDEMO_STANDARD_USER, SAUCEDEMO_LOCKED_OUT_USER, SAUCEDEMO_PASSWORD

@pytest.fixture
def login_page(page: Page):
    """Fixture to initialize the login page and navigate to it."""
    lp = SauceDemoLoginPage(page)
    lp.navigate()
    return lp

def test_verify_login_with_valid_credentials(login_page: SauceDemoLoginPage):
    """
    Verify login with valid credentials
    Expected: User should be redirected to the inventory page.
    """
    if not SAUCEDEMO_PASSWORD:
        pytest.skip("SAUCEDEMO_PASSWORD environment variable not set")
    login_page.login(SAUCEDEMO_STANDARD_USER, SAUCEDEMO_PASSWORD)
    expect(login_page.page).to_have_url(f"{SAUCEDEMO_URL}inventory.html")

def test_verify_login_with_invalid_credentials(login_page: SauceDemoLoginPage):
    """
    Verify login with invalid credentials
    Expected: Error message 'Epic sadface: Username and password do not match any user in this service' should be displayed
    """
    login_page.login("invalid_user", "invalid_password")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_verify_login_with_locked_out_user(login_page: SauceDemoLoginPage):
    """
    Verify login with locked out user
    Expected: Error message 'Epic sadface: Sorry, this user has been locked out.' should be displayed
    """
    if not SAUCEDEMO_PASSWORD:
        pytest.skip("SAUCEDEMO_PASSWORD environment variable not set")
    login_page.login(SAUCEDEMO_LOCKED_OUT_USER, SAUCEDEMO_PASSWORD)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")
