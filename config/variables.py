import os
from dotenv import load_dotenv

load_dotenv()

# config/variables.py
BASE_URL = "https://testerbud.com/practice-login-form"
VALID_USERNAME = "user@premiumbank.com"
INVALID_USERNAME = "invalid@user.com"
TIMEOUT_MS = 5000

VALID_PASSWORD = os.getenv("VALID_PASS")
INVALID_PASSWORD = os.getenv("INVALID_PASS")
