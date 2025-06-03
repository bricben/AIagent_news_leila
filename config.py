
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT", "bbenaben@hotmail.com")

# Optional: Raise errors if not set
assert OPENAI_API_KEY, "OPENAI_API_KEY is missing"
assert SMTP_USER and SMTP_PASSWORD, "SMTP credentials are missing"