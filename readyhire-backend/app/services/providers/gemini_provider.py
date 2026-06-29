import json
from google import genai
from google.genai import types
from app.config.settings import settings
from app.models.response import ApplicationReadinessReport
from app.services.prompts import build_analysis_prompt
from app.services.providers.base_provider import AIProvider, GeminiResponseValidationError

class GeminiProvider(AIProvider):
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        self.model = settings.PRIMARY_MODEL
        self._client = None

    @property
    def client(self):
        if self._client is None:
            if not self.api_key:
                raise ValueError("GEMINI_API_KEY environment variable is missing or empty.")
            # Initialize GenAI Client using the configured API key
            self._client = genai.Client(api_key=self.api_key)
        return self._client

    def analyze_resume(self, resume_text: str, job_description: str) -> ApplicationReadinessReport:
        prompt = build_analysis_prompt(resume_text, job_description)

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ApplicationReadinessReport,
                temperature=0.1,  # Keep findings objective and aligned to inputs
            )
        )

        if not response.text:
            raise GeminiResponseValidationError("Gemini API returned an empty response.")

        try:
            # Check if the SDK successfully parsed the response directly
            if hasattr(response, "parsed") and response.parsed is not None:
                return response.parsed

            # Fallback to manual parsing and validation
            raw_json = response.text.strip()
            
            # Clean potential markdown block formatting
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
