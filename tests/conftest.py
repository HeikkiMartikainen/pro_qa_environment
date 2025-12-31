import pytest
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import sys
from pathlib import Path

# Ensure root directory is in python path to import models
root_dir = Path(__file__).parent.parent
sys.path.append(str(root_dir))

from models import CredentialList  # noqa: E402

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def invalid_login_data_from_ai():
    """
    Fixture that runs once to generate a list of invalid
    login credentials using the Gemini AI, with retries.
    Returns a list of Credentials objects.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        pytest.skip("GOOGLE_API_KEY not found, skipping AI data generation.")

    genai.configure(api_key=api_key)

    # improved generation config with schema
    generation_config = {
        "response_mime_type": "application/json",
        "response_schema": CredentialList
    }

    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config=generation_config
    )

    prompt = """
    Generate a list of 5 invalid login credentials for testing the Sauce Demo website.

    Possible error messages on the site are:
    1. "Epic sadface: Username is required" (if username is empty)
    2. "Epic sadface: Password is required" (if password is empty)
    3. "Epic sadface: Username and password do not match any user in this service" (if credentials are invalid)

    For each test case, populate 'expected_error' with the exact error message from the list above that you expect to see.
    Include cases for:
    - Empty username
    - Empty password
    - Invalid username/password combination
    - Long strings
    - Special characters
    """

    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    for attempt in range(3):
        try:
            response = model.generate_content(prompt, safety_settings=safety_settings)
            data = json.loads(response.text)
            # The schema ensures it matches CredentialList, but we parse it to be sure
            return CredentialList(**data).credentials
        except (json.JSONDecodeError, ValueError, Exception) as e:
            print(f"\nAttempt {attempt + 1} failed. Error: {e}")

    pytest.fail("Failed to generate valid test data from AI.")
    return []
