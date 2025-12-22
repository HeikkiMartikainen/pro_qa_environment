import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Load environment variables from the .env file
load_dotenv()

# --- Fixtures ---

@pytest.fixture(scope="session")
def invalid_login_data_from_ai():
    """
    Fixture that runs once to generate a list of invalid
    login credentials using the Gemini AI, with retries.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        pytest.skip("GOOGLE_API_KEY not found, skipping AI data generation.")
    
    genai.configure(api_key=api_key)
    
    generation_config = {"response_mime_type": "application/json"}
    
    model = genai.GenerativeModel(
        'gemini-2.5-flash', # Use the stable model name
        generation_config=generation_config
    )

    prompt = """
    Generate a JSON array of 5 objects for testing a web login form.
    Each object must have a "username" and "password" key with invalid credential strings.
    Include examples like common input errors, formatting issues, and long strings (max 200 chars).
    Do not include any valid credentials.
    """
    
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    # Add a retry loop for resilience
    for attempt in range(3): # Try up to 3 times
        try:
            response = model.generate_content(prompt, safety_settings=safety_settings)
            return json.loads(response.text)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"\nAttempt {attempt + 1} failed to get valid JSON. Retrying... Error: {e}")
            
    pytest.fail("Failed to parse JSON response from AI after 3 attempts.")
    return []

# --- Test Functions ---

def test_successful_login(page: Page):
    """
    Tests that a standard user can successfully log in.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Assert that the login was successful by checking for a unique element
    inventory_list = page.locator(".inventory_list")
    expect(inventory_list).to_be_visible()
    expect(page).to_have_title("Swag Labs")

def test_invalid_logins(page: Page, invalid_login_data_from_ai):
    """
    Tests that the application handles various AI-generated invalid login attempts correctly.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    
    error_message_locator = page.locator('[data-test="error"]')

    # This loop runs the test for each set of credentials from the AI
    for creds in invalid_login_data_from_ai:
        username = creds.get("username", "")
        password = creds.get("password", "")
        
        print(f"\nTesting with invalid credentials: user='{username}', pass='{password}'")
        
        # We navigate again to ensure the form is clear for each attempt
        login_page.navigate()
        login_page.login(username, password)

        # The application should show an error message.
        # This assertion checks that *any* error appears. You could make it more specific
        # if you also had the AI generate the expected error message for each case.
        expect(error_message_locator).to_be_visible()
