import google.generativeai as genai
import os

# Configure the library once when the module is imported
# This is a common pattern for library setup.
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    # Handle the missing key gracefully. You could also raise an error.
    print("Warning: GOOGLE_API_KEY not found. Summarizer will not work.")
else:
    genai.configure(api_key=api_key)


def summarize_text(text_to_summarize: str) -> str:
    """
    Summarizes a given piece of text using the Gemini model.
    """
    try:
        # Now that the library is configured, we can create the model.
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"Summarize the following text in one sentence: '{text_to_summarize}'"
        response = model.generate_content(prompt)
        
        return response.text.strip()
    except Exception as e:
        # This will catch errors if the API key was missing or invalid
        print(f"An error occurred during summarization: {e}")
        return ""