from google import genai
import os

# Configure the library once when the module is imported
api_key = os.getenv("GOOGLE_API_KEY")
client = None

if not api_key:
    # Handle the missing key gracefully. You could also raise an error.
    print("Warning: GOOGLE_API_KEY not found. Summarizer will not work.")
else:
    # Initialize the client with the API key from the environment
    client = genai.Client(api_key=api_key)


def summarize_text(text_to_summarize: str) -> str:
    """
    Summarizes a given piece of text using the Gemini model.
    """
    try:
        if not client:
             raise ValueError("Client not initialized. Check GOOGLE_API_KEY.")

        # Use the client to generate content
        # model='gemini-1.5-flash' as requested to fix quotas
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Summarize the following text in one sentence: '{text_to_summarize}'"
        )
        
        return response.text.strip()
    except Exception as e:
        # This will catch errors if the API key was missing or invalid
        print(f"An error occurred during summarization: {e}")
        return ""
