import os
from pathlib import Path
from dotenv import load_dotenv

# Locate and load the .env file from the project root
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
env_path = ROOT_DIR / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    PRIMARY_MODEL: str = os.getenv("PRIMARY_MODEL", "gemini-2.5-flash")
    FALLBACK_MODEL: str = os.getenv("FALLBACK_MODEL", "google/gemini-2.5-flash")
    ALLOWED_ORIGINS: list[str] = ["http://localhost:5173"]

    @property
    def GEMINI_MODEL(self) -> str:
        return self.PRIMARY_MODEL

settings = Settings()
