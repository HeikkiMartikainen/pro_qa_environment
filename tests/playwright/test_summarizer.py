import pytest
import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
from utils.summarizer import summarize_text
from pydantic import BaseModel

# Load environment variables at the start of the test session
load_dotenv()

# Configure the AI model once for the entire test file
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    # Skip all tests in this file if the key is not available
    pytest.skip("GOOGLE_API_KEY not found, skipping AI tests", allow_module_level=True)

class ValidationResult(BaseModel):
    is_accurate: bool
    reasoning: str

@pytest.fixture(scope="module")
def ai_client():
    """A fixture to provide the initialized AI client to our tests."""
    return genai.Client(api_key=API_KEY)

def test_long_text_summary(ai_client):
    """
    Tests the summarization of a long text about the planet Jupiter.
    """
    long_text = (
        "Jupiter is the fifth planet from the Sun and the largest in the Solar System. "
        "It is a gas giant with a mass more than two and a half times that of all the "
        "other planets in the Solar System combined, but slightly less than one-thousandth "
        "the mass of the Sun. Jupiter is the third brightest natural object in the Earth's "
        "night sky after the Moon and Venus."
    )
    
    function_summary = summarize_text(long_text)
    assert function_summary, "The summarizer function returned an empty string."
    print(f"\nFunction's Summary: {function_summary}")

    # A more robust validation prompt asking for a JSON response
    validation_prompt = f"""
    Analyze the following text and summary.
    Original Text: "{long_text}"
    Proposed Summary: "{function_summary}"

    Based on the Original Text, is the Proposed Summary accurate and factually correct?
    Respond in JSON format with two keys:
    1. "is_accurate": a boolean (true or false).
    2. "reasoning": a brief explanation for your decision.
    """
    
    # Get the validation result from the AI
    response = ai_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=validation_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ValidationResult
        )
    )
    
    try:
        if response.parsed:
            validation_result = response.parsed
            is_accurate = validation_result.is_accurate
            reasoning = validation_result.reasoning
        else:
             data = json.loads(response.text)
             is_accurate = data.get("is_accurate", False)
             reasoning = data.get("reasoning", "No reason provided.")
        
        print(f"AI Validation Result: {is_accurate}, Reason: {reasoning}")
        
        assert is_accurate, f"The AI determined the summary was not accurate. Reason: {reasoning}"

    except (json.JSONDecodeError, AttributeError):
        pytest.fail(f"Failed to parse AI validation response. Raw response: {response.text}")
