import os
from dotenv import load_dotenv

load_dotenv()

# config/variables.py
TIMEOUT_MS = 5000

# Saucedemo credentials
SAUCEDEMO_URL = "https://www.saucedemo.com/"
SAUCEDEMO_STANDARD_USER = "standard_user"
SAUCEDEMO_LOCKED_OUT_USER = "locked_out_user"
SAUCEDEMO_PASSWORD = os.getenv("SAUCEDEMO_PASSWORD")
