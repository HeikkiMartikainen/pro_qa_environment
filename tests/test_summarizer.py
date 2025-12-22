import pytest
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from utils.summarizer import summarize_text

# Load environment variables at the start of the test session
load_dotenv()

# Configure the AI model once for the entire test file
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    # Skip all tests in this file if the key is not available
    pytest.skip("GOOGLE_API_KEY not found, skipping AI tests", allow_module_level=True)

@pytest.fixture(scope="module")
def ai_model():
    """A fixture to provide the initialized AI model to our tests."""
    return genai.GenerativeModel('gemini-2.5-flash')

def test_long_text_summary(ai_model):
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

    # Tell the model to specifically output JSON
    generation_config = {"response_mime_type": "application/json"}
    
    # Get the validation result from the AI
    response = ai_model.generate_content(validation_prompt, generation_config=generation_config)
    
    try:
        validation_result = json.loads(response.text)
        is_accurate = validation_result.get("is_accurate", False)
        reasoning = validation_result.get("reasoning", "No reason provided.")
        
        print(f"AI Validation Result: {is_accurate}, Reason: {reasoning}")
        
        assert is_accurate, f"The AI determined the summary was not accurate. Reason: {reasoning}"

    except (json.JSONDecodeError, AttributeError):
        pytest.fail(f"Failed to parse AI validation response. Raw response: {response.text}")