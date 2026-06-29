from abc import ABC, abstractmethod
from app.models.response import ApplicationReadinessReport

class GeminiUnavailableError(Exception):
    """Exception raised when the Gemini API or alternative providers are offline or failed."""
    pass

class GeminiResponseValidationError(Exception):
    """Exception raised when the response does not conform to the expected schema."""
    pass

class AIProvider(ABC):
    @abstractmethod
    def analyze_resume(self, resume_text: str, job_description: str) -> ApplicationReadinessReport:
        """
        Analyzes the candidate's resume against the target job description.
        
        Args:
            resume_text (str): The plain text content of the resume.
            job_description (str): The target job description.
            
        Returns:
            ApplicationReadinessReport: The structured validation report.
        """
        pass
