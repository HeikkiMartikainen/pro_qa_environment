# Playwright & Robot Framework Dual-Testing Architecture

This project contains an automated end-to-end testing architecture demonstrating a side-by-side implementation of [Playwright](https://playwright.dev/python/) and [Robot Framework](https://robotframework.org/). It also leverages Google's Gemini AI for generating test data (invalid credentials) and verifying text summarization.

## 🚀 Features

- **Dual-Framework E2E Testing**: Automated UI tests implemented in both code-driven (Playwright/Pytest) and keyword-driven (Robot Framework) paradigms.
- **AI-Powered Testing**:
  - Generates dynamic invalid login credentials using Google's Gemini model.
  - Verifies text summarization capabilities using Gemini.
- **Resilient CI/CD**: Configured with GitHub Actions, featuring automatic retry mechanisms (`pytest-rerunfailures`) for external API stability and headless browser execution.
- **Secure Secret Management**: Strict separation of sensitive data using `.env` files and GitHub Secrets.
- **Standardized Dev Environment**: Includes Docker and fully configured VS Code Dev Container support for instant, reproducible local development.

## 🛠 Prerequisites

- Docker and VS Code (for Dev Container setup)
- Python 3.12+ (if running natively)
- [Google AI Studio API Key](https://aistudio.google.com/)

## 💻 Local Setup & Installation

### Option A: VS Code Dev Container (Recommended)
1. Clone the repository and open the folder in VS Code.
2. Press `F1` and select **"Dev Containers: Rebuild and Reopen in Container"**.
3. All dependencies, linting tools, and browser binaries are automatically installed.

### Option B: Native Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Install dependencies and browser binaries:**
   ```bash
   pip install -r requirements.txt
   playwright install --with-deps
   rfbrowser init
   ```

### 🔐 Environment Variables
Create a `.env` file in the root directory based on the provided `.env.example` file:
```
GOOGLE_API_KEY=your_gemini_api_key_here
VALID_USERNAME=your_test_user
VALID_PASSWORD=your_test_password
```
(Note: Tests will safely skip if passwords are not provided in the environment to prevent false-negative pipeline failures).

## 🧪 Running Tests
To run Pytest (Playwright + AI features):
```bash
pytest -v
```
To run Robot Framework tests:
```bash
robot -d results/ tests/robot/
```
To run tests with a visible browser (headed mode):
```bash
pytest --headed
```

## 📂 Project Structure
- `tests/playwright/`: Code-driven Playwright test files (test_login.py, etc.).
- `tests/robot/`: Keyword-driven Robot Framework tests and resources.
- `src/pages/`: Page Object Models (POM) for UI interaction.
- `config/`: Centralized test data (variables.py).
- `.devcontainer/` & `Dockerfile`: Standardized development environment configuration.

## 📊 Robot Framework vs. Playwright: A Comparative Study
This project demonstrates the ability to choose the right tool for the client's specific needs by implementing a side-by-side comparison.

| Feature | Robot Framework (Keyword-Driven) | Playwright (Code-Driven) |
| :--- | :--- | :--- |
| **Syntax** | High-level keywords (English-like). Accessible to non-programmers and business stakeholders. | Python code. Requires programming knowledge but offers full architectural flexibility. |
| **Execution Speed**| Slightly slower due to keyword parsing and Python abstraction layers. | Faster. Direct communication with browser via WebSocket protocols. |
| **Maintainability**| Excellent for simple flows and BDD. Complex logic requires strict keyword management. | Highly maintainable for complex logic using design patterns like POM. Strong typing helps. |
