import logging
import pytest
import os
import json
from typing import cast
from google import genai
from google.genai import types
from dotenv import load_dotenv
from models import CredentialList
from config.variables import SAUCEDEMO_URL

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("google_genai").setLevel(logging.WARNING)

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return SAUCEDEMO_URL

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

    client = genai.Client(api_key=api_key)

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
    - Long strings (maximum 60 characters)
    - Special characters
    """

    safety_settings = [
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_NONE
        ),
    ]

    for attempt in range(3):
        try:
            response = client.models.generate_content(  # type: ignore
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type='application/json',
                    response_schema=CredentialList,
                    safety_settings=safety_settings
                )
            )
            # The new SDK parses the response into the schema object if provided
            if response.parsed:
                 parsed_creds = cast(CredentialList, response.parsed)
                 return parsed_creds.credentials

            # Fallback if parsed is somehow missing but text is present (unlikely with SDK)
            if response.text:
                data = json.loads(response.text)
                return CredentialList(**data).credentials

        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                pytest.skip(f"Skipping test due to API resource exhaustion: {e}")
            logging.error(f"Attempt {attempt + 1} failed. Error: {e}")

    pytest.fail("Failed to generate valid test data from AI.")
    return []
