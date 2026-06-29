import json
from google import genai
from google.genai import types
from google.genai.errors import APIError
from app.config.settings import settings
from app.models.response import ApplicationReadinessReport
from app.services.prompts import build_analysis_prompt

class GeminiUnavailableError(Exception):
    """Exception raised when the Gemini API is offline, unauthorized, or rate-limited."""
    pass

class GeminiResponseValidationError(Exception):
    """Exception raised when the response from Gemini does not conform to the expected schema."""
    pass

def analyze_resume_and_job(resume_text: str, job_description: str) -> ApplicationReadinessReport:
    """
    Sends the resume text and job description to the Gemini API, requesting
    a structured response matching the ApplicationReadinessReport schema.
    """
    if not settings.GEMINI_API_KEY:
        raise GeminiUnavailableError("GEMINI_API_KEY environment variable is missing or empty.")

    try:
        # Initialize GenAI Client using the configured API key
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
    except Exception as e:
        raise GeminiUnavailableError(f"Failed to initialize Gemini client: {str(e)}")

    prompt = build_analysis_prompt(resume_text, job_description)

    try:
        # Request content generation with schema validation configuration
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ApplicationReadinessReport,
                temperature=0.1,  # Keep findings objective and aligned to inputs
            )
        )
    except APIError as e:
        raise GeminiUnavailableError(f"Gemini API Error: {e.message} (Code: {e.code})")
    except Exception as e:
        raise GeminiUnavailableError(f"Network error or request timeout with Gemini API: {str(e)}")

    if not response.text:
        raise GeminiResponseValidationError("Gemini API returned an empty response.")

    try:
        # Check if the SDK successfully parsed the response directly
        if hasattr(response, "parsed") and response.parsed is not None:
            return response.parsed

        # Fallback to manual parsing and validation
        raw_json = response.text.strip()
        
        # Clean any potential markdown wrapping, just in case (though response_mime_type prevents it)
        if raw_json.startswith("```json"):
            raw_json = raw_json[7:]
        if raw_json.endswith("```"):
            raw_json = raw_json[:-3]
        raw_json = raw_json.strip()

        data = json.loads(raw_json)
        return ApplicationReadinessReport(**data)
    except json.JSONDecodeError as e:
        raise GeminiResponseValidationError(f"Response text is not valid JSON: {str(e)}")
    except Exception as e:
        raise GeminiResponseValidationError(f"Response validation against schema failed: {str(e)}")
