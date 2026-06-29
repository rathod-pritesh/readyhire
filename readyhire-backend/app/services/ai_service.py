import time
import logging
from google.genai.errors import APIError
from app.models.response import ApplicationReadinessReport
from app.services.providers import (
    GeminiProvider,
    OpenRouterProvider,
    GeminiUnavailableError,
    GeminiResponseValidationError
)

logger = logging.getLogger("uvicorn.error")

def is_temporary_error(exc: Exception) -> bool:
    """
    Determines if an exception is a temporary service error that should trigger a retry.
    """
    if isinstance(exc, APIError):
        # 429: Too Many Requests, 5xx: Server Errors
        return exc.code in (429, 500, 502, 503, 504)
    if isinstance(exc, GeminiResponseValidationError):
        return False
    if isinstance(exc, ValueError):
        return False
    # Network, DNS, or socket connection timeouts are considered temporary
    return True

def analyze_resume_and_job(resume_text: str, job_description: str) -> ApplicationReadinessReport:
    """
    Analyzes the candidate's resume against the target job description.
    Tries Google Gemini first with 3 retries (exponential backoff),
    then falls back to OpenRouter.
    """
    gemini_provider = GeminiProvider()
    openrouter_provider = OpenRouterProvider()

    max_attempts = 4  # Initial attempt + 3 retries
    backoffs = [1, 2, 4]  # 1s, 2s, 4s wait times

    for attempt in range(max_attempts):
        try:
            logger.info("Using Google Gemini")
            return gemini_provider.analyze_resume(resume_text, job_description)
        except Exception as e:
            logger.warning(f"Gemini attempt {attempt + 1} failed: {str(e)}")
            
            # Switch immediately or if we ran out of attempts
            if attempt == max_attempts - 1 or not is_temporary_error(e):
                logger.info("Gemini unavailable")
                break
                
            wait_time = backoffs[attempt]
            logger.info(f"Retrying Gemini in {wait_time} seconds...")
            time.sleep(wait_time)

    # Fallback to OpenRouter
    logger.info("Switching to OpenRouter")
    try:
        return openrouter_provider.analyze_resume(resume_text, job_description)
    except Exception as or_err:
        logger.error(f"OpenRouter fallback failed: {str(or_err)}")
        raise GeminiUnavailableError(
            "Service temporarily unavailable. Both primary (Google Gemini) and fallback (OpenRouter) providers failed."
        )
