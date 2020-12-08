import os
from dotenv import load_dotenv

# Loads .env file
load_dotenv()

# Config
TOKEN = os.getenv("TOKEN")

CONFIRMATION_CODE = os.getenv("CONFIRMATION_CODE")

SECRET_KEY = os.getenv("SECRET_KEY")
