import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "نور الاستخلاف"
APP_VERSION = "0.1.0"

ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:9000",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:9000",
    "*",
]

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

PROVIDER_MODELS = {
    "groq": "groq",
    "gemini": "gemini",
    "claude": "claude",
}

DEFAULT_MODEL = "groq"


def get_allowed_origins() -> list[str]:
    raw = os.getenv("ALLOWED_ORIGINS", "*")
    if raw == "*":
        return ["*"]
    return [origin.strip() for origin in raw.split(",") if origin.strip()]
