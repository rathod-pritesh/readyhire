import json
import logging
import urllib.request
import urllib.error
from app.config.settings import settings
from app.models.response import ApplicationReadinessReport
from app.services.prompts import build_analysis_prompt
from app.services.providers.base_provider import AIProvider, GeminiResponseValidationError

logger = logging.getLogger("uvicorn.error")

class OpenRouterProvider(AIProvider):
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.primary_fallback = settings.FALLBACK_MODEL
        self.secondary_fallback = "google/gemini-2.5-flash-lite"

    def _call_openrouter(self, model: str, prompt: str) -> ApplicationReadinessReport:
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable is missing or empty.")

        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://readyhire.ai",
            "X-Title": "ReadyHire",
        }
        
        payload = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.1
        }
        
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST"
        )
        
        try:
            with urllib.request.urlopen(req, timeout=35) as response:
                status_code = response.getcode()
                if status_code != 200:
                    raise Exception(f"OpenRouter returned HTTP status code {status_code}")
                res_body = response.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            try:
                res_body = e.read().decode("utf-8")
                err_detail = json.loads(res_body)
                msg = err_detail.get("error", {}).get("message", str(e))
            except Exception:
                msg = str(e)
            raise Exception(f"OpenRouter HTTP {e.code} Error: {msg}")
        except Exception as e:
            raise Exception(f"OpenRouter Connection Error: {str(e)}")

        try:
            res_json = json.loads(res_body)
            content = res_json["choices"][0]["message"]["content"]
        except Exception as e:
            raise GeminiResponseValidationError(f"Invalid response structure from OpenRouter: {str(e)}")

        if not content:
            raise GeminiResponseValidationError("OpenRouter returned an empty response.")

        try:
            raw_json = content.strip()
            if raw_json.startswith("```json"):
                raw_json = raw_json[7:]
            if raw_json.endswith("```"):
                raw_json = raw_json[:-3]
            raw_json = raw_json.strip()

            data = json.loads(raw_json)
            return ApplicationReadinessReport(**data)
        except json.JSONDecodeError as e:
            raise GeminiResponseValidationError(f"Response content is not valid JSON: {str(e)}")
        except Exception as e:
            raise GeminiResponseValidationError(f"Response validation against schema failed: {str(e)}")

    def analyze_resume(self, resume_text: str, job_description: str) -> ApplicationReadinessReport:
        prompt = build_analysis_prompt(resume_text, job_description)
        
        # Try primary fallback model
        logger.info(f"Using OpenRouter model {self.primary_fallback}")
        try:
            return self._call_openrouter(self.primary_fallback, prompt)
        except Exception as primary_err:
            logger.warning(f"OpenRouter model {self.primary_fallback} failed: {str(primary_err)}")
            
            # Try secondary fallback model
            logger.info(f"Using OpenRouter model {self.secondary_fallback}")
            try:
                return self._call_openrouter(self.secondary_fallback, prompt)
            except Exception as secondary_err:
                logger.error(f"OpenRouter model {self.secondary_fallback} failed: {str(secondary_err)}")
                raise Exception(
                    f"OpenRouter analysis failed. "
                    f"Primary model ({self.primary_fallback}) error: {str(primary_err)}. "
                    f"Secondary model ({self.secondary_fallback}) error: {str(secondary_err)}."
                )
