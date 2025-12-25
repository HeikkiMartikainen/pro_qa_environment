# Playwright with Gemini AI Testing Project

This project contains automated end-to-end tests for [Sauce Demo](https://www.saucedemo.com/) using [Playwright](https://playwright.dev/python/) and [Pytest](https://docs.pytest.org/). It also leverages Google's Gemini AI for generating test data (invalid credentials) and verifying text summarization.

## Features

- **E2E Testing**: Automated login tests using Playwright.
- **AI-Powered Testing**:
  - Generates invalid login credentials dynamically using Google's Gemini model.
  - Verifies text summarization capabilities using Gemini.
- **Docker Support**: Includes a Dockerfile for running tests in a containerized environment.

## Prerequisites

- Python 3.8+
- [Google AI Studio API Key](https://aistudio.google.com/) (for AI features)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

3. **Environment Setup:**
   Create a `.env` file in the root directory and add your Google API Key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running Tests

To run all tests:
```bash
pytest
```

To run specific tests:
```bash
pytest tests/test_login.py
pytest tests/test_summarizer.py
```

To run tests with a head (visible browser):
```bash
pytest --headed
```

## Docker

You can also run the tests using Docker.

1. **Build the image:**
   ```bash
   docker build -t playwright-tests .
   ```

2. **Run the container:**
   You need to pass the `GOOGLE_API_KEY` as an environment variable.
   ```bash
   docker run -e GOOGLE_API_KEY=your_api_key_here playwright-tests pytest
   ```

## Project Structure

- `pages/`: Contains Page Object Models (e.g., `login_page.py`).
- `tests/`: Contains test files (`test_login.py`, `test_summarizer.py`, etc.).
- `utils/`: Utility scripts (e.g., `summarizer.py`).
- `models.py`: Pydantic models for data validation.
- `Dockerfile`: Configuration for Docker environment.
- `requirements.txt`: Python dependencies.
